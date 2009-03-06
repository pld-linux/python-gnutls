%define 	module	gnutls
Summary:	Python wrapper for the GNUTLS library
Name:		python-%{module}
Version:	1.1.8
Release:	1
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/p/python-gnutls/%{name}-%{version}.tar.gz
# Source0-md5:	a9032d65b338573291ef3a9be664c887
URL:		http://pypi.python.org/pypi/python-gnutls/
BuildRequires:	gnutls-devel >= 2.4.1
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a high level object oriented wrapper around libgnutls, as
well as low level bindings to the GNUTLS types and functions via ctypes. The
high level wrapper hides the details of accessing the GNUTLS library via ctypes
behind a set of classes that encapsulate GNUTLS sessions, certificates and
credentials and expose them to python applications using a simple API.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%dir %{py_sitedir}/%{module}/interfaces
%{py_sitedir}/%{module}/interfaces/*.py[co]
%dir %{py_sitedir}/%{module}/interfaces/twisted
%{py_sitedir}/%{module}/interfaces/twisted/*.py[co]
%dir %{py_sitedir}/%{module}/library
%{py_sitedir}/%{module}/library/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/library/*.so
%{py_sitedir}/*-*.egg-info
