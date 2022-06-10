Name:           perl-Hash-Merge
Version:        0.12
Release:        1%{?dist}
Summary:        Merges arbitrary deep hashes into a single hash
Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Hash-Merge/
Source0:        Hash-Merge-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(Test::More), perl(Clone), perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:  perl(Hash::Merge)

%{?perl_default_filter}

%description
%{summary}.

%prep
%setup -q -n Hash-Merge-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -x %{buildroot}%{perl_vendorlib}/Hash/Merge.pm
%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/Hash/
%{_mandir}/man3/*.3*


%changelog
* Wed Mar 17 2010 Chris Weyl <cweyl@alumni.drew.edu> - 0.12-1
- PERL_INSTALL_ROOT => DESTDIR, add perl_default_filter
- auto-update to 0.12 (by cpan-spec-update 0.01) (for DBIx::Class)
- added a new br on perl(ExtUtils::MakeMaker) (version 0)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.11-4
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Jun 26 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.11-2
- fix permissions (silence rpmlint too)
- own Hash/ directory

* Fri Jun 26 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.11-1
- initial package for Fedora
