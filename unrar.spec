Summary:     unRAR - extract, test and view RAR archives.
Summary(pl): unRAR - rozpakowuje, testuje i przegl±da archiwa RAR.
Name:        unrar
Version:     2.01
Release:     1d
Copyright:   Freeware
Group:       Utilities/Archiving
Source:      ftp://tsx-11.mit.edu/pub/linux/sources/usr.bin/Archivers/%{name}-%{version}.tar.gz
BuildRoot:   /tmp/%{name}-%{version}-root

%description
The unRAR utility is a freeware program, distributed with source code and
developed for extracting, testing and viewing the contents of archives created
with the RAR archiver version 1.50 and above.

%description -l pl
UnRAR jest programem freeware, rozpowszechnianym wraz z kodem ¼ród³owym, 
przeznaczonym do rozpakowywania, testowania oraz przegl±dania zawarto¶ci
archiwów stworzonych przez program RAR w wersji 1.50 i wy¿szej.

%prep
%setup -q

%build
cd src
make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin

install -s src/unrar $RPM_BUILD_ROOT/usr/bin

%files
%attr(755,root,root) /usr/bin/*

%changelog
* Sun Oct 4 1998 Piotr Grochowski <pager@dione.ids.pl>
  [2.01]
- First relase as a PLD package.
