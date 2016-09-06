#
# Conditional build:
%bcond_with	tests	# do not perform "make test"

%define 	module		wlc
%define 	egg_name	wlc
%define		pypi_name	wlc
Summary:	Weblate commandline client using Weblate's REST API
Name:		wlc
Version:	0.5
Release:	1
License:	GPL v3+
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/w/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	15a3a221938aa4ef75698aed72ffd0be
URL:		https://weblate.org/
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A command line utility for Weblate, translation tool with tight
version control integration

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
%{__rm} -r %{module}.egg-info

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT
%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/%{module}/test_*
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/%{module}/__pycache__/test_*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/wlc
%{py3_sitescriptdir}/%{pypi_name}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
