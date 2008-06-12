%define Summary FreeCol is an open version of the game Colonization

Name:       	freecol
Version:    	0.7.3
Release:    	%mkrel 1
Summary:    	%Summary
License:    	GPLv2+
Group:      	Games/Strategy
URL:        	http://www.freecol.org/
Source:     	http://prdownloads.sourceforge.net/freecol/freecol-%version-src.tar.gz
BuildRoot:  	%_tmppath/%name-buildroot
BuildRequires:	ant
BuildRequires:	ant-nodeps
BuildRequires:	xerces-j2
Requires:   	java >= 1.4
Requires(post,postun): desktop-common-data

%description
FreeCol is an open version of Colonization. It is a Civilization-like game in
which the player has to conquer the new world.

%prep
%setup -q -n %name

%build
ant

%install
rm -rf %buildroot

mkdir -p %buildroot/%_datadir/games/freecol
cp FreeCol.jar %buildroot/%_datadir/games/freecol
cp -a {data,jars} %buildroot/%_datadir/games/freecol

mkdir -p %buildroot/%_bindir
cat > %buildroot/%_bindir/freecol << EOF
#!/bin/sh

java -Xmx256M -jar %_datadir/games/freecol/FreeCol.jar \\
	--freecol-data %_datadir/games/freecol/data
EOF

mkdir -p %buildroot/%_datadir/pixmaps
cp packaging/common/freecol.xpm %buildroot/%_datadir/pixmaps

mkdir -p %buildroot/%_datadir/applications
cat > %buildroot/%_datadir/applications/mandriva-%name.desktop << EOF
[Desktop Entry]
Name=FreeCol
Comment=%Summary
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/freecol
%defattr(0644,root,root,0755)
%doc packaging/common/{COPYING,README}
%_datadir/applications/mandriva-%name.desktop
%_datadir/games/freecol
%_datadir/pixmaps/freecol.xpm
