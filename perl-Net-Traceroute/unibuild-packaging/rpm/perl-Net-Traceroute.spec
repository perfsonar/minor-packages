Name:			perl-Net-Traceroute
Version:		1.15
Release:		1%{?dist}
Summary:		Traceroute(1) functionality in perl
License:		CHECK(Distributable)
Group:			Development/Libraries
URL:			http://search.cpan.org/dist/Net-Traceroute/
Source0:		Net-Traceroute-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:		noarch
BuildRequires:  perl-macros
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Time::HiRes)
Requires:		perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:		perl(Net::Traceroute)
%description
This module implements a parser for various traceroute implementations.
At present, it can parse most LBL traceroute derivatives used on typical
unixes, and the traceroute of cisco IOS. Traceroutes known not to be
supported include that of Microsoft Windows and HP-UX.

This module has two basic modes of operation, one, where it will run
traceroute for you, and the other where you provide text from previously
running traceroute to parse.

%prep
%setup -q -n Net-Traceroute-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Wed Apr 8 2015 andy@es.net 1.15-1
- Updating to 1.15

* Thu Jun 21 2012 asides@lbl.gov 1.13-1
- Specfile autogenerated by cpanspec 1.77.