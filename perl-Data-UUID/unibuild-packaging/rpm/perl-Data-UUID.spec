Name:           perl-Data-UUID
Version:        1.226
Release:        1%{?dist}
Summary:        Globally/Universally Unique Identifiers (GUIDs/UUIDs)
License:        BSD
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Data-UUID/
Source0:        Data-UUID-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(Digest::MD5)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module provides a framework for generating v3 UUIDs (Universally
Unique Identifiers, also known as GUIDs (Globally Unique Identifiers). A
UUID is 128 bits long, and is guaranteed to be different from all other
UUIDs/GUIDs generated until 3400 CE.

%prep
%setup -q -n Data-UUID-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE META.json README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Data*
%{_mandir}/man3/*

%changelog
* Tue May 16 2023 Andy Lake 1.226-1
- Specfile autogenerated by cpanspec 1.78.