Name:           perl-Statistics-Descriptive
Version:        3.0200
Release:        1%{?dist}
Summary:        Perl module of basic descriptive statistical functions
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Statistics-Descriptive/
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/Statistics-Descriptive-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
This module provides basic functions used in descriptive statistics. It has
an object oriented design and supports two different types of data storage
and calculation objects: sparse and full. With the sparse method, none of
the data is stored and only a few statistical measures are available. Using
the full method, the entire data set is retained and additional functions
are available.

%prep
%setup -q -n Statistics-Descriptive-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes examples README UserSurvey.txt
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Jul 03 2010 Iain Arnell <iarnell@gmail.com> 3.0200-1
- update to latest upstream version.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb  8 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6-3
- rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.6-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Tue Aug 29 2006 Patrice Dumas <pertusus at free.fr> - 2.6-2
- Rebuild for FC6

* Fri Jul 14 2006 Patrice Dumas <pertusus at free.fr> - 2.6-1
- Submit to Fedora Extras.

* Mon Mar 27 2006 Ville Skyttä <ville.skytta at iki.fi> - 2.6-0.2
- Rebuild.

* Fri Jun  3 2005 Ville Skyttä <ville.skytta at iki.fi> - 2.6-0.1
- Rebuild for FC4.

* Sat Jun 12 2004 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6-0.fdr.2
- Bring up to date with current fedora.us Perl spec template.

* Mon Oct 13 2003 Ville Skyttä <ville.skytta at iki.fi> - 0:2.6-0.fdr.1
- First build.
