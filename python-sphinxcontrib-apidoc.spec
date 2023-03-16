#
# Conditional build:
%bcond_without	tests	# unit tests (requires package already installed)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Sphinx extension for running 'sphinx-apidoc' on each build
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do uruchamiania 'sphinx-apidoc' przy każdym budowaniu
Name:		python-sphinxcontrib-apidoc
Version:	0.3.0
Release:	4
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinxcontrib-apidoc/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinxcontrib-apidoc/sphinxcontrib-apidoc-%{version}.tar.gz
# Source0-md5:	baf2ad8a88918b04b54d0655aa273a82
URL:		https://pypi.org/project/sphinxcontrib-apidoc/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 4.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-Sphinx >= 1.6.0
BuildRequires:	python-pytest >= 3.0
BuildRequires:	python-sphinxcontrib-apidoc
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-pbr >= 4.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 1.6.0
BuildRequires:	python3-pytest >= 3.0
BuildRequires:	python3-sphinxcontrib-apidoc
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
Requires:	python-sphinxcontrib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinx-apidoc is a tool for automatic generation of Sphinx sources
that, using the autodoc extension, documents a whole package in the
style of other automatic API documentation tools.

%description -l pl.UTF-8
sphinx-apidoc to narzędzie do automatycznego generowania źródeł
sphinksowych, które, przy użyciu rozszerzenia autodoc, dokumentują
cały pakiet w stylu innych narzędzi do automatycznego dokumentowania
API.

%package -n python3-sphinxcontrib-apidoc
Summary:	Sphinx extension for running 'sphinx-apidoc' on each build
Summary(pl.UTF-8):	Rozszerzenie Sphinksa do uruchamiania 'sphinx-apidoc' przy każdym budowaniu
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4
Requires:	python3-sphinxcontrib

%description -n python3-sphinxcontrib-apidoc
sphinx-apidoc is a tool for automatic generation of Sphinx sources
that, using the autodoc extension, documents a whole package in the
style of other automatic API documentation tools.

%description -n python3-sphinxcontrib-apidoc -l pl.UTF-8
sphinx-apidoc to narzędzie do automatycznego generowania źródeł
sphinksowych, które, przy użyciu rozszerzenia autodoc, dokumentują
cały pakiet w stylu innych narzędzi do automatycznego dokumentowania
API.

%prep
%setup -q -n sphinxcontrib-apidoc-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python} -m pytest tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.rst
%{py_sitescriptdir}/sphinxcontrib/apidoc
%{py_sitescriptdir}/sphinxcontrib_apidoc-%{version}-py*.egg-info
%{py_sitescriptdir}/sphinxcontrib_apidoc-%{version}-py*-nspkg.pth
%endif

%if %{with python3}
%files -n python3-sphinxcontrib-apidoc
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog LICENSE README.rst
%{py3_sitescriptdir}/sphinxcontrib/apidoc
%{py3_sitescriptdir}/sphinxcontrib_apidoc-%{version}-py*.egg-info
%{py3_sitescriptdir}/sphinxcontrib_apidoc-%{version}-py*-nspkg.pth
%endif
