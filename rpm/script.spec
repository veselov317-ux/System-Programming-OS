Name: script
Version: 1.0
Release: 1%{?dist}
Summary: Script package
License: GPL
Source0: script.tar.gz
BuildArch: noarch
%description
Packed automatically script.
%prep
%setup -q 
%build
%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 task1 %{buildroot}/usr/bin/task1
%file

