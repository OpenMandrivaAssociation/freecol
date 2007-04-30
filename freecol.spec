%define Summary FreeCol is an open version of the game Colonization

Name:       	freecol
Version:    	0.6.0
Release:    	%mkrel 1
Summary:    	%Summary
License:    	GPL
Group:      	Games/Strategy
URL:        	http://www.freecol.org/
Source:     	http://prdownloads.sourceforge.net/freecol/freecol-%version-src.tar.gz
BuildRoot:  	%_tmppath/%name-buildroot
BuildRequires:	j2sdk-ant
BuildRequires:	java-devel
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

mkdir -p %buildroot/%_menudir
cat > %buildroot/%_menudir/%name << EOF
?package(%name): needs="x11" \
	section="Games/Strategy" \
	title="FreeCol" \
	longtitle="%{Summary}" \
	command="%_bindir/%name" \
	icon="%name.xpm" \
	xdg="true"
EOF

mkdir -p %buildroot/%_datadir/applications
cat > %buildroot/%_datadir/applications/mandriva-%name.desktop << EOF
[Desktop Entry]
Name=FreeCol
Comment=%Summary
Exec=%_bindir/%name
Icon=%name
Terminal=false
Type=Application
Categories=X-MandrivaLinux-MoreApplications-Games-Strategy;Game;StrategyGame;
Encoding=UTF-8
EOF

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %buildroot

%files
%defattr(0755,root,root,0755)
%_bindir/freecol
%defattr(0644,root,root,0755)
%doc FreeCol.pdf packaging/common/{COPYING,README}
%_datadir/applications/mandriva-%name.desktop
%_datadir/games/freecol
%_datadir/pixmaps/freecol.xpm
%_menudir/%name
