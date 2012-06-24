Summary:	unRAR - extract, test and view RAR archives
Summary(pl):	unRAR - rozpakowuje, testuje i przegl�da archiwa RAR
Summary(pt_BR):	Descompressor de arquivos no formato .rar
Summary(ru):	����������� ������ .zip
Summary(uk):	������������ ���̦� .zip
Name:		unrar
Version:	3.1.3
Release:	1
License:	Freeware
Group:		Applications/Archiving
Source0:	http://www.rarlab.com/rar/%{name}src-%{version}.tar.gz
Source1:	%{name}.1
Source2:	%{name}.1.pl
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The unRAR utility is a freeware program, distributed with source code
and developed for extracting, testing and viewing the contents of
archives created with the RAR archiver version 1.50 and above.

%description -l pl
UnRAR jest programem freeware, rozpowszechnianym wraz z kodem
�r�d�owym, przeznaczonym do rozpakowywania, testowania oraz
przegl�dania zawarto�ci archiw�w stworzonych przez program RAR w
wersji 1.50 i wy�szej.

%description -l pt_BR
O programa unrar � utilizado para descompactar arquivos no formato
".rar".

%description -l ru
Unzip ������ ������, ��������� ����������� � ��������� ����� ��
������� ZIP, �������� ������ ���������������� � ���� DOS.
������������� ���������, zip, ������� ������ ZIP. ��� ���������
���������� � �������� ���������� PKZIP � PKUNZIP �� PKWARE ��� MS-DOS,
�� �� ������ ������� ����� ��� ��������� ����������.

%description -l uk
Unzip ����� ����̦�, ����צ�Ѥ æ̦�Φ��� �� ��������� ����� � ��Ȧצ�
ZIP, ������ ������ �������������� � �צԦ DOS. �����צ��� ��������,
zip, ������� ��Ȧ�� ZIP. ����צ �������� ��ͦ�Φ � ��Ȧ���� ����������
PKZIP �� PKUNZIP צ� PKWARE ��� MS-DOS, ��� � �������� �������� ��æ�
��� ��������� צ�Ҧ��������.

%prep
%setup -q -n unrar

%build
%{__make} -f makefile.unix CC=%{__cc} CXX=%{__cxx} CXXFLAGS="%{rpmcflags}"

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
