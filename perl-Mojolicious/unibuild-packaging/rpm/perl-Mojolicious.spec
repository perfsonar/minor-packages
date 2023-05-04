%{!?perl_vendorlib: %define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)}

Name:           perl-Mojolicious
Version:        7.48
Release:        1%{?dist}
Summary:        Real-time web framework
License:        Artistic 2.0
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mojolicious/
Source0:        Mojolicious-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl-macros
BuildRequires:  perl >= 0:5.010001
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket::IP)
BuildRequires:  perl(JSON::PP) >= 2.27103
BuildRequires:  perl(Pod::Simple) >= 3.09
BuildRequires:  perl(Time::Local) >= 1.2
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(IO::Compress::Gzip)
Requires:       perl(IO::Socket::IP)
Requires:       perl(JSON::PP) >= 2.27103
Requires:       perl(Pod::Simple) >= 3.09
Requires:       perl(Time::Local) >= 1.2
Requires:       libev-devel 

%description
An amazing real-time web framework built on top of the powerful Mojo web
development toolkit. With support for RESTful routes, plugins, commands,
Perl-ish templates, content negotiation, session management, form
validation, testing framework, static file server, CGI/PSGI detection,
first class Unicode support and much more for you to discover.

%prep
%setup -q -n Mojolicious-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*


# TODO: This was disabled because something in it causes Unibuild's
# 'make' loop to hit EOF after this package is built and nothing
# afterward is built.  Fixing this is not a high priority to fix since
# the plan is for a Perl purge at some point in the not-too-distant
# future.  --MAF 2022-06-01
#
# %check || :
#  make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE META.json README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*
#Leaving out binaries because perfSONAR does not use them
%exclude %{_bindir}/*
%exclude %{_mandir}/man1/*


%changelog
* Mon Oct 30 2017 Andy Lake 7.48-1
- Specfile autogenerated by cpanspec 1.78.