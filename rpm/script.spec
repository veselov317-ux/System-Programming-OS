Name:           script
Version:        1.0
Release:        1%{?dist}
Summary:        Simple script

License:        GPL
Source0:        script.tar.gz
BuildArch:      noarch

%description
Simple script package.

%prep
%setup -q

%build


%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 task1 %{buildroot}/usr/bin/task1

%files
/usr/bin/task1

%changelog
* Thu Dec 01 2025 veselov317-ux <veselov317@gmail.com> - 1.0-1
- Initial package
