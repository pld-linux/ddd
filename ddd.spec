Summary:	X interface to the GDB, DBX and XDB debuggers
Summary(ja.UTF-8):	GDB,DBX,Ladebug,JDB,Perl,Pythonのグラフィカルデバッガのフロントエンド
Summary(pl.UTF-8):	Interfejs X do debugerów GDB, DBX i XDB
Summary(zh_CN.UTF-8):	图形化的程序调试器前端;如GDB,DBX,Ladebug,JDB,Perl,Python
Name:		ddd
Version:	3.3.12
Release:	14
Epoch:		1
License:	GPL
Group:		Development/Debuggers
Source0:	http://ftp.gnu.org/gnu/ddd/%{name}-%{version}.tar.gz
# Source0-md5:	c50396db7bac3862a6d2555b3b22c34e
Source1:	%{name}.desktop
Source2:	http://art.gnome.org/images/icons/other/Debugger.png
# Source2-md5:	c046d9b0a04abdbb4a2be08a374ac2cd
Patch0:		%{name}-ptrace.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-home_etc.patch
Patch3:		%{name}-am185.patch
Patch4:		%{name}-gcc.4.4-build.patch
URL:		http://www.gnu.org/software/ddd/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison
BuildRequires:	elfutils-devel
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	motif-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	texinfo
Requires:	gdb
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	%{_datadir}/X11/app-defaults

%define		specflags	-fno-strict-aliasing

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

%description -l ja.UTF-8
DDDは、GDB,DBX,WDB,Ladebug,JDB,XDB,Perlデバッガ、またはPythonデバッガ
のようなコマンドライン型デバッガをグラフィカル型のデバッガに変身させる
フロントエンドです。ソースコードの参照等のような"通常"のフロントエンド
の機能のみならず、DDDはデータ構造をグラフとして表示する、会話式グラフ
ィカルデータ表示することで有名になりました。

%description -l pl.UTF-8
Data Display Debugger (DDD) jest typowym graficznym interfejsem do
GDB, DBX, i XDB - popularnych UNIXowych debuggerów. Poza
``klasycznymi'' możliwościami interfejsów graficznych takich jak
przeglądanie kodów źródłowych DDD dostarcza graficznych narzędzi,
gdzie struktury wyświetlane są w postaci graficznej. Proste kliknięcie
myszą pozwala na przeglądanie zawartości struktur (aktualizowane za
każdym razem gdy program się zatrzyma). Inne możliwości DDD to:
możliwość debugowania programów napisanych w C, C++, Ada, Fortran,
Java, Pascal, Modula-2, or Modula-2; debugowanie na poziomie maszyny;
hypertekstowa nawigacja po źródłach; breakpoint, backtrace i emulator
okna historii; możliwość ustawiania preferencji; uruchamianie
programów w oknie terminala; debugowanie na zdalnych serwerach;
podręcznik on-line; interaktywna pomoc; linia poleceń GDB/DBX/XDB z
pełną edycją, historią i wyszukiwaniem.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-motif \
	--with-readline \
	--with-termlib=tinfo

%{__make} \
	CXXOPT="-DNDEBUG %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_appdefsdir},%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install ddd/Ddd $RPM_BUILD_ROOT%{_appdefsdir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/ddd.png

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

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
