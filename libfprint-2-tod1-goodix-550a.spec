%global debug_package       %{nil}

Name:           libfprint-2-tod1-goodix-550a

Version:        0.0.9
Release:        %autorelease
Summary:        Repackaged driver module binary from Lenovo for Goodix 27C6:550A fingerprint reader

License:        GPL-3.0
URL:            https://support.lenovo.com/ca/en/downloads/ds560884-goodix-fingerprint-driver-for-linux-thinkpad-e14-gen-4-e15-gen-4
Source0:        https://github.com/QuanTrinhCA/libfprint-2-tod1-goodix-550a/archive/refs/tags/%{version}.tar.gz

Requires:       libfprint-tod
#For installing udev rules
BuildRequires:  systemd

%description
Repackaged Goodix driver module from Lenovo for fingerprint reader to support 27C6:550A.

%prep
%setup -q -n libfprint-2-tod1-goodix-550a-%{version}

%install
mv libfprint-2-tod1-goodix-550a-%{version}/* %{_builddir}/libfprint-2-tod1-goodix-550a-%{version}/
install -p -d -m 0755 %{buildroot}%{_libdir}/libfprint-2/tod-1/
install -m 0644 usr/lib/x86_64-linux-gnu/libfprint-2/tod-1/libfprint-tod-goodix-550a-%{version}.so %{buildroot}%{_libdir}/libfprint-2/tod-1/libfprint-tod-goodix-550a-%{version}.so
install -p -d -m 0755 %{buildroot}%{_udevrulesdir}
install -m 0644 lib/udev/rules.d/60-libfprint-2-tod1-goodix.rules %{buildroot}%{_udevrulesdir}/60-libfprint-2-tod1-goodix.rules

%files
%defattr(-,root,root,-)
%{_libdir}/libfprint-2/tod-1/libfprint-tod-goodix-550a-%{version}.so
%{_udevrulesdir}/60-libfprint-2-tod1-goodix.rules
