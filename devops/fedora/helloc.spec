%define _unpackaged_files_terminate_build 0
%define debug_package %{nil}
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

Name:           helloc
Version:        1.0 
Release:        1%{?dist}
Summary:        hello c program

License:        MIT 
URL:            http://local.host
Source0:        helloc-1.0.tar.gz 

BuildRequires:  gcc,cmake
Requires:       glibc 

%description


%prep
%autosetup


%build
%cmake
%cmake_build


%install
%cmake_install


%files



%changelog
* Fri Mar 07 2025 slackman cn <slackman@disroot.com>
- 
