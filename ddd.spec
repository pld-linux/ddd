Summary:	X interface to the GDB, DBX and XDB debuggers
Summary(ja.UTF-8):	GDB,DBX,Ladebug,JDB,Perl,Pythonのグラフィカルデバッガのフロントエンド
Summary(pl.UTF-8):	Interfejs X do debugerów GDB, DBX i XDB
Summary(zh_CN.UTF-8):	图形化的程序调试器前端;如GDB,DBX,Ladebug,JDB,Perl,Python
Name:		ddd
Version:	3.4.1
Release:	1
Epoch:		1
License:	GPL v3+
Group:		Development/Debuggers
Source0:	https://ftp.gnu.org/gnu/ddd/%{name}-%{version}.tar.gz
# Source0-md5:	99ebcd5ad29d25e198e89209e8d7104e
Source1:	%{name}.desktop
# originally http://art.gnome.org/images/icons/other/Debugger.png
Source2:	Debugger.png
# Source2-md5:	c046d9b0a04abdbb4a2be08a374ac2cd
Patch0:		%{name}-ptrace.patch
Patch1:		%{name}-info.patch
Patch2:		%{name}-home_etc.patch
URL:		http://www.gnu.org/software/ddd/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison >= 1.28
BuildRequires:	elfutils-devel
BuildRequires:	flex
BuildRequires:	freetype-devel >= 2.0
BuildRequires:	gnulib
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	motif-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	texinfo
Requires:	gdb
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

ln -sf %{_datadir}/gnulib/doc/fdl-1.3.texi ddd/fdl-1.3.texi

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
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
cp -p %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/ddd.png

%{__mv} $RPM_BUILD_ROOT%{_datadir}/ddd-%{version}/info $RPM_BUILD_ROOT%{_infodir}
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/ddd-%{version}/doc

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README doc/{ANNOUNCE,AUTHORS,CREDITS,FONTS,NEWS,NEWS-OLD,NICKNAMES,TIPS,*.pdf}
%attr(755,root,root) %{_bindir}/ddd
%{_datadir}/ddd-%{version}
%{_desktopdir}/ddd.desktop
%{_pixmapsdir}/ddd.png
%{_mandir}/man1/ddd.1*
%{_infodir}/ddd.info*
%{_infodir}/ddd-themes.info*
