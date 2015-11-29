%define 	module	gnutls
Summary:	Python wrapper for the GNUTLS library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki GNUTLS
Name:		python-%{module}
Version:	2.0.1
Release:	2
License:	LGPL v2+
Group:		Development/Languages/Python
Source0:	https://pypi.python.org/packages/source/p/python-gnutls/%{name}-%{version}.tar.gz
# Source0-md5:	adba310851a15d19ff29355385c6f74f
URL:		https://pypi.python.org/pypi/python-gnutls/
BuildRequires:	gnutls-devel >= 3.1.4
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	gnutls >= 3.1.4
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a high level object oriented wrapper around
libgnutls, as well as low level bindings to the GNUTLS types and
functions via ctypes. The high level wrapper hides the details of
accessing the GNUTLS library via ctypes behind a set of classes that
encapsulate GNUTLS sessions, certificates and credentials and expose
them to Python applications using a simple API.

%description -l pl.UTF-8
Ten pakiet udostępnia wysokopoziomowe, zorientowane obiektowo
obudowanie libgnutls, a także niskopoziomowe wiązania do typów i
funkcji GNUTLS poprzez ctypes. Wysokopoziomowe obudowanie skrywa
szczegóły dostępu do biblioteki GNUTLS poprzez ctypes za zbiorem klas
przechowujących sesje, certyfikaty oraz dane uwierzytelniające GNUTLS
i udostępnia je aplikacjom Pythona poprzez proste API.

%prep
%setup -q

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog LICENSE README
%dir %{py_sitescriptdir}/gnutls
%{py_sitescriptdir}/gnutls/*.py[co]
%dir %{py_sitescriptdir}/gnutls/interfaces
%{py_sitescriptdir}/gnutls/interfaces/*.py[co]
%dir %{py_sitescriptdir}/gnutls/interfaces/twisted
%{py_sitescriptdir}/gnutls/interfaces/twisted/*.py[co]
%dir %{py_sitescriptdir}/gnutls/library
%{py_sitescriptdir}/gnutls/library/*.py[co]
%{py_sitescriptdir}/python_gnutls-%{version}-py*.egg-info
