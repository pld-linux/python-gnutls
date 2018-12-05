%define 	module	gnutls
Summary:	Python wrapper for the GNUTLS library
Summary(pl.UTF-8):	Pythonowy interfejs do biblioteki GNUTLS
Name:		python-%{module}
Version:	3.1.2
Release:	1
License:	LGPL v2+
Group:		Development/Languages/Python
#Source0Download: https://pypi.python.org/simple/python-gnutls/
Source0:	https://files.pythonhosted.org/packages/source/p/python-gnutls/%{name}-%{version}.tar.gz
# Source0-md5:	ee71ddd04b2c01fbe99ae3b02739cddf
URL:		https://pypi.python.org/pypi/python-gnutls/
BuildRequires:	gnutls-devel >= 3.2.0
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	gnutls >= 3.2.0
Requires:	python-modules >= 1:2.7
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
