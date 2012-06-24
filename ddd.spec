#%include	/usr/lib/rpm/macros.python
Summary:	X interface to the GDB, DBX and XDB debuggers
Summary(ja):	GDB,DBX,Ladebug,JDB,Perl,Python�Υ���ե�����ǥХå��Υե��ȥ����
Summary(pl):	Interfejs X do debuger�w GDB, DBX i XDB
Summary(zh_CN):	ͼ�λ��ĳ��������ǰ��;��GDB,DBX,Ladebug,JDB,Perl,Python
Name:		ddd
Version:	3.3.9
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Debuggers
Source0:	ftp://ftp.gnu.org/gnu/ddd/%{name}-%{version}.tar.gz
# Source0-md5:	acfca53c62507795f4ceb355cb34e2a2
Source1:	%{name}.desktop
Source2:	%{name}-python.desktop
Source3:	http://art.gnome.org/images/icons/other/Debugger.png
# Source3-md5:	c046d9b0a04abdbb4a2be08a374ac2cd
Patch0:		%{name}-ptrace.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-home_etc.patch
URL:		http://www.gnu.org/software/ddd/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	elfutils-devel
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	motif-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	python >= 2.2
BuildRequires:	readline-devel
#BuildRequires:	rpm-pythonprov
BuildRequires:	texinfo
Requires:	gdb
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

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
DDD�ϡ�GDB,DBX,WDB,Ladebug,JDB,XDB,Perl�ǥХå����ޤ���Python�ǥХå�
�Τ褦�ʥ��ޥ�ɥ饤�󷿥ǥХå��򥰥�ե����뷿�ΥǥХå����ѿȤ�����
�ե��ȥ���ɤǤ��������������ɤλ������Τ褦��"�̾�"�Υե��ȥ����
�ε�ǽ�Τߤʤ餺��DDD�ϥǡ�����¤�򥰥�դȤ���ɽ�����롢���ü������
������ǡ���ɽ�����뤳�Ȥ�ͭ̾�ˤʤ�ޤ�����

%description -l pl
Data Display Debugger (DDD) jest typowym graficznym interfejsem do
GDB, DBX, i XDB - popularnych UNIXowych debugger�w. Poza
``klasycznymi'' mo�liwo�ciami interfejs�w graficznych takich jak
przegl�danie kod�w �r�d�owych DDD dostarcza graficznych narz�dzi,
gdzie struktury wy�wietlane s� w postaci graficznej. Proste klikni�cie
mysz� pozwala na przegl�danie zawarto�ci struktur (aktualizowane za
ka�dym razem gdy program si� zatrzyma). Inne mo�liwo�ci DDD to:
mo�liwo�� debugowania program�w napisanych w C, C++, Ada, Fortran,
Java, Pascal, Modula-2, or Modula-2; debugowanie na poziomie maszyny;
hypertekstowa nawigacja po �r�d�ach; breakpoint, backtrace i emulator
okna historii; mo�liwo�� ustawiania preferencji; uruchamianie
program�w w oknie terminala; debugowanie na zdalnych serwerach;
podr�cznik on-line; interaktywna pomoc; linia polece� GDB/DBX/XDB z
pe�n� edycj�, histori� i wyszukiwaniem.

%package python
Summary:	X interface to the GDB, DBX and XDB debuggers - The python debugger
Summary(pl):	Interfejs X do debuger�w GDB, DBX i XDB - debugger pythona
Group:		Development/Debuggers
Requires:	%{name} = %{version}-%{release}
#%pyrequires_eq	python

%description python
Data Display Debugger - python debugger.

%description python -l pl
Data Display Debugger - debugger pythona.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-motif \
	--with-readline-libraries=%{_libdir}

%{__make} \
	CXXOPT="-DNDEBUG %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdefsdir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install pydb/pydb.py $RPM_BUILD_ROOT%{_bindir}/pydb
#install pydb/{pydbcmd,pydbsupt}.py $RPM_BUILD_ROOT%{py_sitedir}
#%py_comp $RPM_BUILD_ROOT%{py_sitedir}
#%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}

install ddd/Ddd $RPM_BUILD_ROOT%{_appdefsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
#install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/ddd.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TIPS TODO doc/*.pdf
%attr(755,root,root) %{_bindir}/ddd
%{_datadir}/ddd*
%{_appdefsdir}/Ddd
%{_desktopdir}/ddd.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/*
%{_infodir}/ddd*

#%files python
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_bindir}/pydb
#%{py_sitedir}/*.py?
#%{_desktopdir}/ddd-python.desktop
