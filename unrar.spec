Summary:	unRAR - extract, test and view RAR archives
Summary(pl):	unRAR - rozpakowuje, testuje i przegl±da archiwa RAR
Name:		unrar
Version:	3.00
Release:	1
License:	Freeware
Group:		Applications/Archiving
Source0:	http://www.rarlab.com/rar/%{name}src.tar.gz
Source1:	%{name}.1
Source2:	%{name}.1.pl
Patch0:		%{name}-makefile.patch
BuildRequires:	gcc-c++
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
%setup -q -c
%patch0 -p1

%build
%{__make} -f makefile.gcc CC=%{__cc} CXX=%{__cxx} OPT="%{rpmcflags}"

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
