Summary:	unRAR - extract, test and view RAR archives
Summary(pl.UTF-8):	unRAR - rozpakowuje, testuje i przegląda archiwa RAR
Summary(pt_BR.UTF-8):	Descompressor de arquivos no formato .rar
Summary(ru.UTF-8):	Распаковщик файлов .zip
Summary(uk.UTF-8):	Розпаковувач файлів .zip
Name:		unrar
Version:	3.7.5
Release:	1
License:	Freeware
Group:		Applications/Archiving
#Source0Download: http://www.rarlab.com/rar_add.htm
Source0:	http://www.rarlab.com/rar/%{name}src-%{version}.tar.gz
# Source0-md5:	10b142866c656e40273434aae6747f96
Source1:	%{name}.1
Source2:	%{name}.1.pl
URL:		http://www.rarlab.com/
BuildRequires:	libstdc++-devel
BuildRequires:	rpmbuild(macros) >= 1.167
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unRAR utility is a freeware program, distributed with source code
and developed for extracting, testing and viewing the contents of
archives created with the RAR archiver version 1.50 and above.

%description -l pl.UTF-8
UnRAR jest programem freeware, rozpowszechnianym wraz z kodem
źródłowym, przeznaczonym do rozpakowywania, testowania oraz
przeglądania zawartości archiwów stworzonych przez program RAR w
wersji 1.50 i wyższej.

%description -l pt_BR.UTF-8
O programa unrar é utilizado para descompactar arquivos no formato
".rar".

%description -l ru.UTF-8
Unzip выдает список, проверяет целостность и извлекает файлы из
архивов ZIP, довольно широко распространенных в мире DOS.
Сопутствующая программа, zip, создает архивы ZIP. Обе программы
совместимы с архивами созданными PKZIP и PKUNZIP от PKWARE для MS-DOS,
но во многих случаях опции или умолчания отличаются.

%description -l uk.UTF-8
Unzip видає перелік, перевіряє цілісність та видобуває файли з архівів
ZIP, досить широко розповсюджених у світі DOS. Відповідна програма,
zip, створює архіви ZIP. Обидві програми сумісні з архівами створеними
PKZIP та PKUNZIP від PKWARE для MS-DOS, але в багатьох випадках опції
або умовчання відрізняються.

%prep
%setup -q -n unrar

%build
%{__make} -f makefile.unix \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,pl/man1}}

install unrar $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE2} $RPM_BUILD_ROOT%{_mandir}/pl/man1/unrar.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%{_mandir}/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%attr(755,root,root) %{_bindir}/*
