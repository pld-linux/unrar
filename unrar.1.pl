.\" 
.\" Translation (c) Wojciech Aleksander <walx@polbox.com>
.\" 
.TH UNRAR 1 "11 lutego 1999" 
.SH NAZWA
unrar \- rozpakowuje pliki z archiw�w rar
.SH SK�ADNIA
.B unrar
.I "<polecenie> [-<prze��cznik 1> -<prze��cznik N>] archiwum [pliki...] [�cie�ka\...]"
.SH "OPIS
Ten podr�cznik po kr�tce opisuje polecenie
.BR unrar
.br
Podr�cznik ten zosta� napisany dla dystrubucji Debian GNU/Linux 
poniewa� oryginalny program nie posiada stron podr�cznika systemowego.
.br

Polecenia i opcje opisane tutaj dotycz� wersji unrar 2.02.
.SH OPCJE
Po nazwie programu nale�y poda� polecenie i dodatkowe prze��czniki 
poprzedzone uko�nikiem.
Podstawowe komendy zosta�y przedstawione poni�ej.
Aby uzyska� pe�ny opis nale�y uruchomi� program
.BR unrar
bez opcji.
.TP
.B e
Rozpakowuje pliki do katalogu bie��cego.
.TP
.B l
Wy�wietla zawarto�� archiwum.
.TP
.B p
Wy�wietla plik na wyj�cie standardowe (stdout).
.TP
.B t
Testuje pliki zawarte w archiwum.
.TP
.B v
Wy�wietla zawarto�� archiwum w trybie "gadatliwym".
.TP
.B x
Rozpakowuje pliki wraz ze �cie�k�.
.SH PRZE��CZNIKI
.BR UWAGA:
Ka�dy prze��cznik musi by� poprzedzony bia�� spacj�. 
Nie mo�na podawa� ich razem.
.TP
.B -av-
Wy��cza sprawdzanie AV.
.TP
.B -c-
Nie wy�wietla komentarzy.
.TP
.B -f
Od�wie�a pliki.
.TP
.B -kb
Nie kasuje rozpakowanych uszkodzonych plik�w.
.TP
.B -ierr
Wysy�a wszystkie komunikaty na stderr.
.TP
.B -inul
Wy��cza wszystkie komunikaty.
.TP
.B -o+
Nadpisuje istniej�ce pliki.
.TP
.B -o-
Nie nadpisuje istniej�cych plik�w.
.TP
.B -p<has�o>
Ustawia has�o.
.TP
.B -p-
Nie pyta o has�o.
.TP
.B -r
Do��cza podkatalogi.
.TP
.B -u
Uaktualnia pliki.
.TP
.B -v
Wy�wietla wszystkie cz�ci archiwum.
.TP
.B -x<plik>
Wyklucza podany plik.
.TP
.B -x@<lista>
Wyklucza pliki w podanym pliku z list�.
.TP
.B -x@
Wczytuje nazwy plik�w do wykluczenia ze stdin.
.TP
.B -y
Przyjmuje odpowied� tak na wszystkie zapytania.
.SH "ZOBACZ TAK�E"
Pe�na dokumentacja tego programu znajduje si� w pliku
.IR Rar.Txt ,
kt�ry znajduje si� w katalogu /usr/share/doc/rar. Opcje tu opisane s� 
takie same dla
.BR rar
oraz
.BR unrar .
.SH AUTOR
T� stron� podr�cznika systemowego napisa� Peter Cech <cech@debian.org>
na podstawie polecenia "unrar -h" wykonanego w systemie Debian GNU/Linux
(mo�e by� tak�e u�ywana w innych dystrybucjach).
