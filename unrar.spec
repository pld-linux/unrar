Summary:	unRAR - extract, test and view RAR archives
Summary(pl):	unRAR - rozpakowuje, testuje i przegl±da archiwa RAR
Name:		unrar
Version:	2.50.1
Release:	3
License:	Freeware
Group:		Utilities/Archiving
Group(pl):	Narzêdzia/Archiwizacja
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unRAR utility is a freeware program, distributed with source code
and developed for extracting, testing and viewing the contents of
archives created with the RAR archiver version 1.50 and above.

%description -l pl
UnRAR jest programem freeware, rozpowszechnianym wraz z kodem
¼ród³owym, przeznaczonym do rozpakowywania, testowania oraz
przegl±dania zawarto¶ci archiwów stworzonych przez program RAR w
wersji 1.50 i wy¿szej.

%prep
%setup -q

%build
%{__make} clean
%{__make} CFLAGS="-D_UNIX $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install -s unrar $RPM_BUILD_ROOT%{_bindir}
gzip -9nf *.txt *.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt.gz *.lsm.gz
%attr(755,root,root) %{_bindir}/*
