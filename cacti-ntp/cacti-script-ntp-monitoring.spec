Name:       cacti-script-ntp-monitoring
Summary:    A script and graph template for cacti to monitor NTP status
Version:    0.1
Release:    1
License:    distributable, see http://www.internet2.edu/membership/ip.html
Group:      BSD
URL:        http://software.internet2.edu
Source0:    query-ntpd.pl
Source1:    cacti_graph_template_ntp_quality_query-ntpd_pl.xml
Source2:    setup_cacti_ntp_graph.pl
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:  noarch
Requires:   cacti
Requires:   perl

%description
A script for cacti that collects NTP statistics, along with a graph template that sets up cacti to create graphs of the statistics.

%prep

%build

%install
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/cacti/scripts
%{__cp} %{SOURCE0} $RPM_BUILD_ROOT/usr/share/cacti/scripts
%{__mkdir} -p $RPM_BUILD_ROOT/usr/share/%{name}
%{__cp} %{SOURCE1} $RPM_BUILD_ROOT/usr/share/%{name}
%{__cp} %{SOURCE2} $RPM_BUILD_ROOT/usr/share/%{name}

%clean

%files
%defattr(-, root, root, -)
%attr(0755, root, root) /usr/share/cacti/scripts/query-ntpd.pl
/usr/share/%{name}/*

%changelog
* Wed Apr 23 2014 Aaron Brown <aaron@internet2.edu> - 0.1-1
- Initial package.
