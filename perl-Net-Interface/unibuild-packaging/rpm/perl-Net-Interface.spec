Name:			perl-Net-Interface
Version:		1.012
Release:		1%{?dist}
Summary:		Perl extension to access network interfaces
License:		Distributable, see Copying
Group:			Development/Libraries
URL:			http://search.cpan.org/dist/Net-Interface/
Source0:		Net-Interface-%{version}.tar.gz
Patch0:		simplesets.t.patch
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc
BuildRequires:  perl-generators
BuildRequires:  perl-macros
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::Simple)
Requires:		perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:		perl(Net::Interface)

%description
Net::Interface is a module that allows access to the host network interfaces
in a manner similar to ifconfig(8). Version 1.00 is a complete re-write and
includes support for IPV6 as well as the traditional IPV4.

Both read and write access to network device attributes including the
creation of new logical and physical interfaces is available where supported
by the OS and this module.

NOTE: if your OS is not supported, please feel free to contribute new
capabilities, patches, etc.... see: Net::Interface::Developer

ANOTHER NOTE: Many of the operations of Net::Interface, particularly those
that set interface values require privileged access to OS resources. Wherever
possible, Net::Interface will simply fail softly when there are not adequate
privileges to perform the requested operation or where the operation is not
supported.

%prep
%setup -q -n Net-Interface-%{version}
%patch0 -p0

%build
./configure
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Artistic Changes Copying README test.pl.developer
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Net*
%{_mandir}/man3/*

%changelog
* Wed Jun 20 2012 asides@lbl.gov 1.012-1
- Specfile autogenerated by cpanspec 1.77.
