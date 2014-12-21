Name:		freecol
Version:	0.11.1
Release:	1
Summary:	Open version of the game Colonization
License:	GPLv2+
Group:		Games/Strategy
URL:		http://www.freecol.org/
Source0:	http://prdownloads.sourceforge.net/freecol/%{name}-%{version}-src.zip
BuildRequires:	ant
BuildRequires:	ant
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
export JAVA_HOME=%_prefix/lib/jvm/java-openjdk
export ANT_OPTS=-Dfile.encoding=UTF8
ant

%install

%__mkdir_p %{buildroot}%{_datadir}/games/%{name}
cp FreeCol.jar %{buildroot}%{_datadir}/games/%{name}
cp -a {data,jars} %{buildroot}%{_datadir}/games/%{name}

%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh

java -Xmx256M -jar %{_datadir}/games/freecol/FreeCol.jar \\
	--freecol-data %{_datadir}/games/%{name}/data
EOF

%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__cp packaging/common/%{name}.xpm %{buildroot}%{_datadir}/pixmaps

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=FreeCol
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

%files
%defattr(0644,root,root,0755)
%doc packaging/common/{COPYING,README}
%attr(0755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/*
%{_datadir}/pixmaps/%{name}.xpm
