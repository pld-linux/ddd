Summary:	X interface to the GDB, DBX and XDB debuggers
Summary(pl):	Interfejs X do debugerów GDB, DBX i XDB
Name:		ddd
Version:	3.1.6
Release:	1
Copyright:	GPL
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Source0:	ftp://ftp.ips.cs.tu-bs.de/pub/local/softech/ddd/src/%{name}-%{version}.tar.gz
Source1:	ddd.desktop
Source2:	ddd-python.desktop
Icon:		ddd.xpm
URL:		http://www.cs.tu-bs.de/softech/ddd/
Buildroot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
The Data Display Debugger (DDD) is a common graphical user interface for
GDB, DBX, and XDB, the popular UNIX debuggers.  Besides ``classical''
front-end features such as viewing source texts, DDD provides a graphical
data display, where data structures are displayed as graphs.  A simple mouse
click dereferences pointers or views structure contents, updated each time
the program stops.  Using DDD, you can reason about your application by
viewing its data, not just by viewing it execute lines of source code. 
Other DDD features include: debugging of programs written in C, C++, Ada,
Fortran, Java, Pascal, Modula-2, or Modula-3; machine-level debugging;
hypertext source navigation and lookup; breakpoint, backtrace, and history
editors; preferences and settings editors; program execution in terminal
emulator window; debugging on remote host; on-line manual; interactive help
on the Motif user interface; GDB/DBX/XDB command-line interface with full
editing, history, search, and completion capabilities.  DDD has been
designed to compete with well-known commercial debuggers

%description -l pl
Data Display Debugger (DDD) jest typowm graficznym interfejsem do
GDB, DBX, i XDB - popularnych UNIXowych debuggerów. Poza ``klasycznymi''
mo¿liwo¶ciami interfejsów graficznych takich jak przegl±danie kodów
¼ród³owych DDD dostarcza graficznych narzêdzi, gdzie struktury wy¶wietlane
s± w postaci graficznej. Proste klikniêcie mysz± pozwala na przegl±danie
zawarto¶ci struktur (aktualizowane za ka¿dym razem gdy program siê zatrzyma).
Inne mo¿liwo¶ci DDD to: mo¿liwo¶æ debugowania programów napisanych w C, C++,
Ada, Fortran, Java, Pascal, Modula-2, or Modula-2; debugowanie na poziomie
maszyny; hypertekstowa nawigacja po ¼ród³ach; brekpoin, backtrace i emulator
okna historii; mo¿liwo¶æ ustawiania preferencji; uruchamianie programów w oknie
terminala; debugowanie na zdalnych serwerach; podrêcznik on-line; interaktywna
pomoc; linia poleceñ GDB/DBX/XDB z pe³n± edycj±, histori± i wyszukiwaniem.

%package python
Summary:	X interface to the GDB, DBX and XDB debuggers - The python debugger
Summary(pl):	Interfejs X do debugerów GDB, DBX i XDB - debuger pythona
Group:		Development/Debuggers
Group(pl):	Programowanie/Odpluskwiacze
Requires:	%{name} = %{version}

%description python
Data Display Debugger - python debugger.

%description -l pl
Data Display Debugger - debugger pythona.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure \
	--with-motif
make CXXOPT="-DNDEBUG $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/applnk/Development,usr/lib/python1.5,%{_libdir}/X11/app-defaults}

make install prefix=$RPM_BUILD_ROOT%{_prefix} \
	mandir=$RPM_BUILD_ROOT%{_mandir} \
	bindir=$RPM_BUILD_ROOT%{_bindir} \
	libdir=$RPM_BUILD_ROOT%{_libdir}

install pydb/pydb.py $RPM_BUILD_ROOT%{_bindir}/pydb
install pydb/{pydbcmd,pydbsupt}.py $RPM_BUILD_ROOT/usr/lib/python1.5

install ddd/Ddd $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT/etc/X11/applnk/Development

gzip -9nf ANNOUNCE BUGS ChangeLog NEWS* OPENBUGS PROBLEMS README TIPS \
	TODO $RPM_BUILD_ROOT%{_mandir}/man1/*
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {ANNOUNCE,BUGS,ChangeLog,NEWS*,OPENBUGS,PROBLEMS,README,TIPS,TODO}.gz
%doc doc/sample.dddinit
/etc/X11/applnk/Development/ddd.desktop
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/Ddd
%{_mandir}/man1/*

%files python
%defattr(644,root,root,755)
/etc/X11/applnk/Development/ddd-python.desktop
%attr(755,root,root) %{_bindir}/pydb
/usr/lib/python*/*
