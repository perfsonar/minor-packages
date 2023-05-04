Name:           perl-Mo
Version:        0.40
Release:        1%{?dist}
Summary:        Mo Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Mo/
Source0:        Mo-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl-macros
BuildRequires:  perl >= 1:v5.6.0
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::All)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Class::XSAccessor)
Requires:       perl(IO::All)
Requires:       perl(Moose)
Requires:       perl(Mouse)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
package Less; use Mo; extends 'Nothing';

has something => ();

%prep
%setup -q -n Mo-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE META.json README dist.ini xt
%{perl_vendorlib}/*
%{_mandir}/man3/*
%{_bindir}/*

%changelog
* Fri Aug 05 2022 Andy Lake <andy@es.net> 0.40-1
- Specfile autogenerated by cpanspec 1.78.