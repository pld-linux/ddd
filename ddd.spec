%include	/usr/lib/rpm/macros.python
Summary:	X interface to the GDB, DBX and XDB debuggers
Summary(ja):	GDB,DBX,Ladebug,JDB,Perl,Python¤Î¥°¥é¥Õ¥£¥«¥ë¥Ç¥Ð¥Ã¥¬¤Î¥Õ¥í¥ó¥È¥¨¥ó¥É
Summary(pl):	Interfejs X do debugerów GDB, DBX i XDB
Summary(zh_CN):	Í¼ÐÎ»¯µÄ³ÌÐòµ÷ÊÔÆ÷Ç°¶Ë;ÈçGDB,DBX,Ladebug,JDB,Perl,Python
Name:		ddd
Version:	3.3.1
Release:	16
License:	GPL
Group:		Development/Debuggers
Source0:	ftp://ftp.gnu.org/gnu/ddd/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}-python.desktop
Source3:	http://art.gnome.org/images/icons/other/Debugger.png
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-ptrace.patch
Patch2:		%{name}-info.patch
Patch3:		%{name}-gcc3.patch
URL:		http://www.gnu.org/software/ddd/
BuildRequires:	XFree86-devel
BuildRequires:	motif-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	libstdc++-devel
BuildRequires:	python >= 2.2
BuildRequires:	texinfo
BuildRequires:	automake
BuildRequires:	rpm-pythonprov
Requires:	gdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The Data Display Debugger (DDD) is a common graphical user interface
for GDB, DBX, and XDB, the popular UNIX debuggers. Besides
``classical'' front-end features such as viewing source texts, DDD
provides a graphical data display, where data structures are displayed
as graphs. A simple mouse click dereferences pointers or views
structure contents, updated each time the program stops. Using DDD,
you can reason about your application by viewing its data, not just by
viewing it execute lines of source code. Other DDD features include:
debugging of programs written in C, C++, Ada, Fortran, Java, Pascal,
Modula-2, or Modula-3; machine-level debugging; hypertext source
navigation and lookup; breakpoint, backtrace, and history editors;
preferences and settings editors; program execution in terminal
emulator window; debugging on remote host; on-line manual; interactive
help on the Motif user interface; GDB/DBX/XDB command-line interface
with full editing, history, search, and completion capabilities. DDD
has been designed to compete with well-known commercial debuggers

%description -l ja
DDD¤Ï¡¢GDB,DBX,WDB,Ladebug,JDB,XDB,Perl¥Ç¥Ð¥Ã¥¬¡¢¤Þ¤¿¤ÏPython¥Ç¥Ð¥Ã¥¬
¤Î¤è¤¦¤Ê¥³¥Þ¥ó¥É¥é¥¤¥ó·¿¥Ç¥Ð¥Ã¥¬¤ò¥°¥é¥Õ¥£¥«¥ë·¿¤Î¥Ç¥Ð¥Ã¥¬¤ËÊÑ¿È¤µ¤»¤ë
¥Õ¥í¥ó¥È¥¨¥ó¥É¤Ç¤¹¡£¥½¡¼¥¹¥³¡¼¥É¤Î»²¾ÈÅù¤Î¤è¤¦¤Ê"ÄÌ¾ï"¤Î¥Õ¥í¥ó¥È¥¨¥ó¥É
¤Îµ¡Ç½¤Î¤ß¤Ê¤é¤º¡¢DDD¤Ï¥Ç¡¼¥¿¹½Â¤¤ò¥°¥é¥Õ¤È¤·¤ÆÉ½¼¨¤¹¤ë¡¢²ñÏÃ¼°¥°¥é¥Õ
¥£¥«¥ë¥Ç¡¼¥¿É½¼¨¤¹¤ë¤³¤È¤ÇÍ­Ì¾¤Ë¤Ê¤ê¤Þ¤·¤¿¡£
 
%description -l pl
Data Display Debugger (DDD) jest typowym graficznym interfejsem do
GDB, DBX, i XDB - popularnych UNIXowych debuggerów. Poza
``klasycznymi'' mo¿liwo¶ciami interfejsów graficznych takich jak
przegl±danie kodów ¼ród³owych DDD dostarcza graficznych narzêdzi,
gdzie struktury wy¶wietlane s± w postaci graficznej. Proste klikniêcie
mysz± pozwala na przegl±danie zawarto¶ci struktur (aktualizowane za
ka¿dym razem gdy program siê zatrzyma). Inne mo¿liwo¶ci DDD to:
mo¿liwo¶æ debugowania programów napisanych w C, C++, Ada, Fortran,
Java, Pascal, Modula-2, or Modula-2; debugowanie na poziomie maszyny;
hypertekstowa nawigacja po ¼ród³ach; breakpoint, backtrace i emulator
okna historii; mo¿liwo¶æ ustawiania preferencji; uruchamianie
programów w oknie terminala; debugowanie na zdalnych serwerach;
podrêcznik on-line; interaktywna pomoc; linia poleceñ GDB/DBX/XDB z
pe³n± edycj±, histori± i wyszukiwaniem.

%package python
Summary:	X interface to the GDB, DBX and XDB debuggers - The python debugger
Summary(pl):	Interfejs X do debugerów GDB, DBX i XDB - debugger pythona
Group:		Development/Debuggers
Requires:	%{name} = %{version}
%pyrequires_eq	python

%description python
Data Display Debugger - python debugger.

%description python -l pl
Data Display Debugger - debugger pythona.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__aclocal}
%{__automake}
%configure2_13 \
	--with-motif \
	--with-readline-libraries=%{_libdir}

%{__make} CXXOPT="-DNDEBUG %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir} \
	$RPM_BUILD_ROOT%{_libdir}/X11/app-defaults \
	$RPM_BUILD_ROOT{%{_applnkdir}/Development,%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install pydb/pydb.py $RPM_BUILD_ROOT%{_bindir}/pydb
install pydb/{pydbcmd,pydbsupt}.py $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

install ddd/Ddd $RPM_BUILD_ROOT%{_libdir}/X11/app-defaults

install %{SOURCE1} %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Development
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/ddd.png

mv doc/README README.doc

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc ANNOUNCE AUTHORS *BUGS INSTALL NEWS* PROBLEMS README* TIPS TODO doc/ddd.pdf
%doc doc/sample.dddinit
%{_applnkdir}/Development/ddd.desktop
%{_pixmapsdir}/*
%attr(755,root,root) %{_bindir}/ddd
%{_libdir}/X11/app-defaults/Ddd
%{_mandir}/man1/*
%{_datadir}/ddd*
%{_infodir}/ddd*

%files python
%defattr(644,root,root,755)
%{_applnkdir}/Development/ddd-python.desktop
%attr(755,root,root) %{_bindir}/pydb
%{py_sitedir}/*.py?
