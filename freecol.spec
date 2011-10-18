Name:		freecol
Version:	0.10.3
Release:	%mkrel 1
Summary:	FreeCol is an open version of the game Colonization
License:	GPLv2+
Group:		Games/Strategy
URL:		http://www.freecol.org/
Source:		http://prdownloads.sourceforge.net/freecol/freecol-%version-src.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:	ant
BuildRequires:	ant-nodeps
BuildRequires:	xerces-j2
BuildRequires:	unzip
Requires:	java >= 1.6
Requires:	desktop-common-data
BuildArch:	noarch

%description
FreeCol is an open version of Colonization. It is a Civilization-like game in
which the player has to conquer the new world.

%prep
%setup -q -n %{name}

%build
ant

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/games/%{name}
cp FreeCol.jar %{buildroot}%{_datadir}/games/%{name}
cp -a {data,jars} %{buildroot}%{_datadir}/games/%{name}

mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh

java -Xmx256M -jar %{_datadir}/games/freecol/FreeCol.jar \\
	--freecol-data %{_datadir}/games/%{name}/data
EOF

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp packaging/common/%{name}.xpm %{buildroot}%{_datadir}/pixmaps

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=FreeCol
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%defattr(0644,root,root,0755)
%doc packaging/common/{COPYING,README}
%{_datadir}/applications/mandriva-%{name}.desktop
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/*
%{_datadir}/pixmaps/%{name}.xpm
