Summary:     X interface to the GDB, DBX and XDB debuggers
Name:        ddd
Version:     3.1
Release:     1
Source0:     ftp://ftp.ips.cs.tu-bs.de/pub/local/softech/ddd/src/%{name}-%{version}.tar.gz
Copyright:   GPL
Group:       Development/Debuggers
Icon:        ddd.xpm
URL:         http://www.cs.tu-bs.de/softech/ddd/
Buildroot:   /tmp/%{name}-%{version}-root

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

%package python
Summary:     X interface to the GDB, DBX and XDB debuggers - The python debugger
Group:       Development/Debuggers
Requires:    %{name} = %{version}

%description python
Data Display Debugger - python debugger.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--with-motif \
	--prefix=/usr/X11R6
make CXXOPT="-DNDEBUG $RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/{lib/python-1.5,X11R6/lib/X11/app-defaults}}

make install prefix=$RPM_BUILD_ROOT/usr/X11R6

install pydb/pydb.py $RPM_BUILD_ROOT/usr/X11R6/bin
install pydb/{pydbcmd,pydbsupt}.py $RPM_BUILD_ROOT/usr/lib/python-1.5

install ddd/Ddd $RPM_BUILD_ROOT/usr/X11R6/lib/X11/app-defaults
gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/*

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/ddd <<EOF
ddd name "DDD"
ddd description "Data Display Debuger"
ddd exec "/usr/X11R6/bin/ddd"
ddd group "Development"
EOF

cat > $RPM_BUILD_ROOT/etc/X11/wmconfig/ddd-python <<EOF
ddd name "DDD for python"
ddd description "Data Display Debuger - python"
ddd exec "/usr/X11R6/bin/ddd --pydb"
ddd group "Development"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc DOCS ANNOUNCE BUGS ChangeLog* NEWS* OPENBUGS PROBLEMS README TIPS TODO doc/sample.dddinit
/etc/X11/wmconfig/ddd
%attr(755, root, root) /usr/X11R6/bin/*
%attr(644, root,  man) /usr/X11R6/man/man1/*
/usr/X11R6/lib/X11/app-defaults/Ddd

%files python
%defattr(644, root, root, 755)
/etc/X11/wmconfig/ddd-python
%attr(755, root, root) /usr/X11R6/bin/pydb.py
/usr/lib/python-1.5/*

%changelog
* Wed Dec  2 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [3.1-1]
- based on spec written by Alec Habig <habig@budoe.bu.edu>,
- only one package is now generated,
- added -q %setup parameter,
- added gziping man pages,
- changed Buildroot to /tmp/%%{name}-%%{version}-root,
- added using %%{name} and %%{version} in Source,
- removeda all %post{un} scripts,
- added package Icon,
- added python subpackage,
- removed Packager field (this must be placed in private ~/.rpmrc),
- added %attr and %defattr macros in %files (allow build package from
  non-root account).
