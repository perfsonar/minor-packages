%global py_version 3.6

%{?perl_default_filter}
%global __provides_exclude_from ^%{python_sitearch}/.*\\.so$

%global have_mongrel 0
%global have_jsx 0

# We only want the Python3 bindings
%global ruby_configure --without-ruby
%global erlang_configure --without-erlang
%global php_configure --without-php --without-php_extension
%global golang_configure --without-go
%global python_configure --without-python --with-py3

Name:		thrift
Version:	0.13.0
Release:	1%{?dist}
Summary:	Software framework for cross-language services development

# Parts of the source are used under the BSD and zlib licenses, but
# these are OK for inclusion in an Apache 2.0-licensed whole:
# https://www.apache.org/legal/3party.html

# Here's the breakdown:
# thrift-0.9.1/lib/py/compat/win32/stdint.h is 2-clause BSD
# thrift-0.9.1/compiler/cpp/src/md5.[ch] are zlib
License:	ASL 2.0 and BSD and zlib
URL:		https://thrift.apache.org/

Source0:	https://archive.apache.org/dist/%{name}/%{version}/%{name}-%{version}.tar.gz
Source2:	https://raw.github.com/apache/%{name}/%{version}/bootstrap.sh

# From Debian patches
Patch1:     disable_failing_tests.patch
Patch2:     disable_TLSv1_0_and_TLSv1_1.patch
Patch3:     link_tests_atomic.patch
Patch4:     no_gradlew.patch
Patch5:     no_shmem.patch

Group:		Development/Libraries

# BuildRequires for language-specific bindings are listed under these
# subpackages, to facilitate enabling or disabling individual language
# bindings in the future

BuildRequires:	libstdc++-devel
BuildRequires:	boost169-devel
BuildRequires:	boost169-static
BuildRequires:	libevent-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	openssl-devel
BuildRequires:	zlib-devel
BuildRequires:	bison-devel
BuildRequires:	flex-devel
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	bison
BuildRequires:	flex

%description

The Apache Thrift software framework for cross-language services
development combines a software stack with a code generation engine to
build services that work efficiently and seamlessly between C++, Java,
Python and other languages.

%package	 devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
Requires:	boost169-devel

%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        glib
Summary:        GLib support for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    glib
The %{name}-qt package contains GLib bindings for %{name}.


%package -n	python3-%{name}
Summary:	Python support for %{name}
BuildRequires:	python3-devel
BuildRequires:  python3-setuptools
BuildRequires:	python36-six        >=  1.7.2
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	python3

%description -n python3-%{name}
The python-%{name} package contains Python bindings for %{name}.

#%global _default_patch_fuzz 2
%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%{?!el5:sed -i -e 's/^AC_PROG_LIBTOOL/LT_INIT/g' configure.ac}

# avoid spurious executable permissions in debuginfo package
find . -name \*.cpp -or -name \*.cc -or -name \*.h | xargs -r chmod 644

cp -p %{SOURCE2} bootstrap.sh

# work around linking issues
echo 'libthrift_c_glib_la_LIBADD = $(GLIB_LIBS) $(GOBJECT_LIBS) -L../cpp ' >> lib/c_glib/Makefile.am
echo 'libthriftqt_la_LIBADD = $(QT_LIBS) -lthrift' >> lib/cpp/Makefile.am
echo 'libthriftz_la_LIBADD = $(ZLIB_LIBS) -lthrift' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftqt_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am
echo 'EXTRA_libthriftz_la_DEPENDENCIES = libthrift.la' >> lib/cpp/Makefile.am

%build
export PY_PREFIX=%{_prefix}
export GLIB_LIBS=$(pkg-config --libs glib-2.0)
export GLIB_CFLAGS=$(pkg-config --cflags glib-2.0)
export GOBJECT_LIBS=$(pkg-config --libs gobject-2.0)
export GOBJECT_CFLAGS=$(pkg-config --cflags gobject-2.0)

find %{_builddir} -name rebar -exec rm -f '{}' \;
find . -name Makefile\* -exec sed -i -e 's/[.][/]rebar/rebar/g' {} \;

sh ./bootstrap.sh

# use unversioned doc dirs where appropriate (via _pkgdocdir macro)
%configure --disable-maintainer-mode --disable-dependency-tracking --disable-static --without-cpp --without-c_glib --without-perl --without-java --without-nodejs --with-qt4=no --with-qt5=no --without-rust --disable-tutorial --with-boost=/usr %{python_configure} %{ruby_configure} %{erlang_configure} %{golang_configure} %{php_configure} --docdir=%{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}

# eliminate unused direct shlib dependencies
sed -i -e 's/ -shared / -Wl,--as-needed\0/g' libtool

make %{?_smp_mflags}
cd lib/py
python3 setup.py build

%install
%make_install
cd lib/py
python3 setup.py install --root=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name fastbinary.so | xargs -r chmod 755

# Ensure all python scripts are executable
find %{buildroot} -name \*.py -exec grep -q /usr/bin/env {} \; -print | xargs -r chmod 755

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc LICENSE NOTICE
%{_bindir}/thrift

%files -n python3-%{name}
%{python3_sitearch}/%{name}
%{python3_sitearch}/%{name}-%{version}-py%{py_version}.egg-info
%doc LICENSE NOTICE

%changelog
* Mon Jun 22 2020 Antoine Delvaux <antoine.delvaux@man.poznan.pl> - 0.13.0-1
- Python 3 port

* Tue Mar 14 2017 Christopher Tubbs <ctubbsii@fedoraproject.org> - 0.9.1-15
- Build TNonblockingServer, remove useless man page, and use java-headless

* Tue Dec 27 2016 William Benton <willb@redhat.com> - 0.9.1-14
- Backport QT/Glib separation from master
- fix BZ 1390992

* Wed Oct 21 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 0.9.1-13
- Backport THRIFT-2214 fix to get package built on aarch64.

* Mon May 05 2014 Lubomir Rintel <lkundrak@v3.sk> - 0.9.1-12
- Fix EPEL build

* Fri Feb 21 2014 willb <willb@redhat> - 0.9.1-11
- fix BZ 1068561

* Fri Dec 20 2013 willb <willb@redhat> - 0.9.1-10
- fix BZ 1045544

* Wed Oct 16 2013 willb <willb@redhat> - 0.9.1-9
- Remove spurious dependencies
- Move some versioned shared libraries from -devel

* Wed Oct 16 2013 Dan Horák <dan[at]danny.cz> - 0.9.1-8
- Mono available only on selected arches

* Sun Oct 13 2013 willb <willb@redhat> - 0.9.1-7
- minor specfile cleanups

* Fri Oct 11 2013 willb <willb@redhat> - 0.9.1-6
- added thrift man page
- integrated fb303
- fixed many fb303 library dependency problems

* Tue Oct 1 2013 willb <willb@redhat> - 0.9.1-5
- fixed extension library linking when an older thrift package is not
  already installed
- fixed extension library dependencies in Makefile

* Tue Oct 1 2013 willb <willb@redhat> - 0.9.1-4
- addresses rpmlint warnings and errors
- properly links glib, qt, and z extension libraries

* Mon Sep 30 2013 willb <willb@redhat> - 0.9.1-3
- adds QT support
- clarified multiple licensing
- uses parallel make
- removes obsolete M4 macros
- specifies canonical location for source archive

* Tue Sep 24 2013 willb <willb@redhat> - 0.9.1-2
- fixes for i686
- fixes bogus requires for Java package

* Fri Sep 20 2013 willb <willb@redhat> - 0.9.1-1
- updated to upstream version 0.9.1
- disables PHP support, which FTBFS in this version

* Fri Sep 20 2013 willb <willb@redhat> - 0.9.0-5
- patch build xml to generate unversioned jars instead of moving after the fact
- unversioned doc dirs on Fedora versions where this is appropriate
- replaced some stray hardcoded paths with macros
- thanks to Gil for the above observations and suggestions for fixes

* Thu Aug 22 2013 willb <willb@redhat> - 0.9.0-4
- removed version number from jar name (obs pmackinn)

* Thu Aug 22 2013 willb <willb@redhat> - 0.9.0-3
- Fixes for F19 and Erlang support

* Thu Aug 15 2013 willb <willb@redhat> - 0.9.0-2
- Incorporates feedback from comments on review request

* Mon Jul 1 2013 willb <willb@redhat> - 0.9.0-1
- Initial package
