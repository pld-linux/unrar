Summary:	unRAR - extract, test and view RAR archives
Summary(pl):	unRAR - rozpakowuje, testuje i przegl±da archiwa RAR
Name:		unrar
Version:	2.71
Release:	2
License:	Freeware
Group:		Applications/Archiving
Source0:	ftp://sunsite.unc.edu/pub/Linux/utils/compress/%{name}-%{version}.tar.gz
Source1:	%{name}.1
Source2:	%{name}.1.pl
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
%{__make} CFLAGS="-D_UNIX %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,pl/man1}}

install unrar $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1
gzip -9nf *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt.gz
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%attr(755,root,root) %{_bindir}/*
