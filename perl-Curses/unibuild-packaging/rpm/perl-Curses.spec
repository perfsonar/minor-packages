Name:           perl-Curses
Version:        1.45
Release:        2%{?dist}
Summary:        Perl bindings for ncurses

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Curses
Source0:        Curses-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  sed
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Perl bindings for ncurses, bringing terminal-independent character
handling capabilities to Perl.


%prep
%setup -q -n Curses-%{version}
test -f hints/c-linux.ncursesw.h || cp hints/c-linux.ncurses.h hints/c-linux.ncursesw.h
sed -i -e 's|<form.h>|"/usr/include/ncursesw/form.h"|g' hints/*.h
sed -i -e 's|/usr/local/bin/perl|%{__perl}|' demo*
sed -i -e 's|/usr//bin/perl|%{__perl}|' demo*

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" \
 PANELS MENUS FORMS

sed -i -e 's|<form.h>|"/usr/include/ncursesw/form.h"|g' hints/*.h
make %{?_smp_mflags}

# A note about the following alarming output...
#
#  WARNING: Your Curses form.h file appears to be in the default
#  system search path, which will not work for us because of
#  the conflicting Perl form.h file.  This means your 'make' will
#  probably fail unless you fix this, as described in the INSTALL
#  file.
#
#... can be ignored because /usr/include/form.h is a symlink to
#/usr/include/ncurses/form.h, which the Makefile.PL finds and
#uses quite happily.


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

#Remove exec perm for file aimed to be bundled as %%doc
chmod -x demo*

%check
make test



%files
%doc Copying Artistic README demo*
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Curses.pm
%{_mandir}/man3/*.3*


%changelog
* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.38-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 20 2021 Steve Traylen <steve.traylen@cern.ch> - 1.38-1
- 1.38 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri May 21 2021 Jitka Plesnikova <jplesnik@redhat.com> - 1.37-3
- Perl 5.34 rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 29 2020 Steve Traylen <steve.traylen@cern.ch> - 1.37-1
- 1.37 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-13
- Perl 5.32 rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-10
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-7
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-3
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.36-1
- 1.36 bump

* Tue May 24 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.34-1
- 1.34 bump

* Sun May 15 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.33-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 3 2015 Steve Traylen <steve.traylen@cern.ch> - 1.33-1
- New upstream 1.33.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.32-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.32-2
- Perl 5.22 rebuild

* Mon Jun 1 2015 Steve Traylen <steve.traylen@cern.ch> - 1.32-1
- New upstream 1.32.

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.28-10
- Perl 5.18 rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Aug 10 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1.28-8
- fix license field to correct value

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jun 11 2012 Petr Pisar <ppisar@redhat.com> - 1.28-6
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.28-4
- Perl mass rebuild

* Tue Jun 14 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.28-3
- Perl mass rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Feb 6 2011 Steve Traylen <steve.traylen@cern.ch> - 1.28-1
- Upstream to 1.28

* Thu Dec 16 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.27-5
- 661697 rebuild for fixing problems with vendorach/lib

* Fri Apr 30 2010 Marcela Maslanova <mmaslano@redhat.com> - 1.27-4
- Mass rebuild with perl-5.12.0

* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 1.27-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 16 2009 kwizart < kwizart at gmail.com > - 1.27-1
- Update to 1.27
- Remove exec perm for demo* provided as %%doc - Fix #510186

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Mar  4 2008 Tom "spot" Callaway <tcallawa@redhat.com> 1.20-3
- rebuild for new perl

* Thu Feb 14 2008 Garrick Staples <garrick@usc.edu> 1.20-2
- forgot to update tarball, building

* Thu Feb 14 2008 Garrick Staples <garrick@usc.edu> 1.20-1
- bump to 1.20

* Fri Aug 17 2007 Garrick Staples <garrick@usc.edu> 1.16-4
- fix /usr//bin/perl, bz#253336

* Thu Aug 16 2007 Garrick Staples <garrick@usc.edu> 1.16-3
- need BR: perl(Test::More)

* Thu Aug 16 2007 Garrick Staples <garrick@usc.edu> 1.16-2
- rebuild

* Thu Aug 16 2007 Garrick Staples <garrick@usc.edu> 1.16-1
- bump to 1.16
- correct License: tag
- need BR: perl-devel

* Sun Aug 27 2006 Garrick Staples <garrick@usc.edu> 1.15-1
- bump to 1.15

* Sun Aug 27 2006 Garrick Staples <garrick@usc.edu> 1.14-2
- rebuild

* Sun Aug 27 2006 Garrick Staples <garrick@usc.edu> 1.14-1
- bump to 1.14
- FC6 mass rebuild

* Fri Apr 21 2006 Garrick Staples <garrick@usc.edu> 1.13-3
- add a note about the falsely alarming warning
- don't remove execute bit from demos

* Thu Apr 20 2006 Garrick Staples <garrick@usc.edu> 1.13-2
- spec cleanups
- add doc files

* Wed Apr 19 2006 Garrick Staples <garrick@usc.edu> 1.13-1
- Initial spec file
