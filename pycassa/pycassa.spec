#
# RPM Spec for Pycassa
#

Name:		pycassa
Version:	1.11.2
Release:	1%{?dist}
Summary:	Thrift-based python client library for Apache Cassandra
BuildArch:	noarch
License:    ASL 2.0	
Group:		Development/Libraries

Source0:	%{name}-%{version}.tar.gz

Requires:   python3
Requires:   python3-thrift

BuildRequires:	python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-thrift

%description
Thrift-based python client library for Apache Cassandra

%package -n	python3-%{name}
Summary:	Thrift-based python3 client library for Apache Cassandra

%description -n python3-%{name}
Thrift-based python client library for Apache Cassandra

%prep
%setup -q -n %{name}-%{version}

%build
python3 setup.py build

%install
%{_builddir}/%{name}-%{version}/rpm-install-script.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{name} -f INSTALLED_FILES
%defattr(-,root,root)
%license LICENSE

%changelog
* Wed Jul 1 2020 Antoine Delvaux <antoine.delvaux@man.poznan.pl> - 1.12.2-1
- Python 3 port

