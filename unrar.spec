Summary:     unRAR - extract, test and view RAR archives.
Summary(pl): unRAR - rozpakowuje, testuje i przegl�da archiwa RAR.
Name:        unrar
Version:     2.03.1
Release:     1
Copyright:   Freeware
Group:       Utilities/Archiving
Source:      ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
BuildRoot:   /tmp/%{name}-%{version}-root

%description
The unRAR utility is a freeware program, distributed with source code and
developed for extracting, testing and viewing the contents of archives created
with the RAR archiver version 1.50 and above.

%description -l pl
UnRAR jest programem freeware, rozpowszechnianym wraz z kodem �r�d�owym, 
przeznaczonym do rozpakowywania, testowania oraz przegl�dania zawarto�ci
archiw�w stworzonych przez program RAR w wersji 1.50 i wy�szej.

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
* Sat Nov 21 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.03.1-1]
- changed base Source url.

* Sun Oct 4 1998 Piotr Grochowski <pager@dione.ids.pl>
  [2.01-1]
- First relase as a PLD package.
