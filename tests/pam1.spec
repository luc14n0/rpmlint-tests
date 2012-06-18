Name:		pam1
Version:	0
Release:	0
Group:          Development/Tools/Building
Summary:	Lorem ipsum
License:	GPL-2.0+
BuildRoot:	%_tmppath/%name-%version-build
Url:            http://www.opensuse.org/
BuildArch:      noarch

%description
Lorem ipsum dolor sit amet, consectetur adipisici elit, sed
eiusmod tempor incidunt ut labore et dolore magna aliqua. Ut enim
ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
aliquid ex ea commodi consequat. Quis aute iure reprehenderit in
voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint obcaecat cupiditat non proident, sunt in culpa qui
officia deserunt mollit anim id est laborum.

%prep
%build

%install
install -d -m 755 %buildroot/lib/security
install -d -m 755 %buildroot/usr/lib/security
echo 4711 > %buildroot/lib/security/pam_foobar.so
echo 4711 > %buildroot/usr/lib/security/pam_nologin.so

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
/usr/lib/security
/lib/security

%changelog
* Mon Apr 18 2011 lnussel@suse.de
- dummy