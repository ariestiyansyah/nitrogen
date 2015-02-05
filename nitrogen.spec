%define __debug_package %{nil}
Name:           nitrogen
Version:        1.0.0
Release:        1%{?dist}
Summary:        Depedency manager for Go 
Group:		Applications/Internet
License:        MIT License
URL:            https://github.com/lucachr/nitrogen
Source0:        nitrogen-%{version}.tar.gz
BuildArch:	noarch
Requires:	bash
BuildRoot:	%{tmppath}/%{name}-root
  

%description
A simple dependency manager for Go

%prep
%setup -q


%build


%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}/usr/bin
install -m 755 nitrogen ${RPM_BUILD_ROOT}%{_bindir}

%files
%attr(755,root,root) %{_bindir}/nitrogen

%clean
rm -rf ${RPM_BUILD_ROOT}


%changelog
* Thu Feb  5 2015 Rizky Ariestiyansyah
- 
