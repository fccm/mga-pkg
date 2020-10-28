Name:           excellent-bifurcation
Version:        0.0.20071015
Release:        %mkrel 1
Summary:        Vertical arcade shooter
License:        GPL
Group:          Games/Shooter
URL:            https://packages.debian.org/en/sid/excellent-bifurcation
Source0:        excellent-bifurcation_0.0.20071015.orig.tar.gz
Source1:        excellent-bifurcation.6
Source2:        excellent-bifurcation.desktop
Source3:        excellent-bifurcation.png
Source4:        copyright
Source5:        changelog

Patch0:         excellent-bifurcation_mageia.patch
Patch1:         windowed.patch

BuildRequires:  pkgconfig(allegro)

%description
Excellent Bifurcation is a vertical shooter in which you have two sides
available to play on. Its graphics try to mimic the colours, sounds and
feeling of the 8-bit games.

In the game, you drive two ships at the same time, on two sides of the
screen. The game play is very unique and fun. It might be quite a brain
bender anyway.

Excellent Bifurcation was Linley Henzel's entry in the AutoFire 2007
Shooter Competition, and finished in 2nd place.

Screenshot:
https://screenshots.debian.net/package/excellent-bifurcation

%global debug_package %{nil}

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} .
cp %{SOURCE2} .
cp %{SOURCE3} .
cp %{SOURCE4} .
cp %{SOURCE5} .

%build
dos2unix Readme.txt
fold -w 80 -s Readme.txt > README.txt

cd src && make

%install
install -d %{buildroot}/%{_gamesbindir}/
install -m 0755 src/excellent-bifurcation %{buildroot}/%{_gamesbindir}/

install -d %{buildroot}/%{_datadir}/games/excellent-bifurcation/gfx
install -d %{buildroot}/%{_datadir}/games/excellent-bifurcation/wavs
install -d %{buildroot}/%{_datadir}/games/excellent-bifurcation/wavs/ambi
install -m 0644 gfx/*  %{buildroot}/%{_datadir}/games/excellent-bifurcation/gfx/
install -m 0644 wavs/*.* %{buildroot}/%{_datadir}/games/excellent-bifurcation/wavs/
install -m 0644 wavs/ambi/* %{buildroot}/%{_datadir}/games/excellent-bifurcation/wavs/ambi/

install -d %{buildroot}%{_mandir}/man6/
install -m 0644 excellent-bifurcation.6 %{buildroot}%{_mandir}/man6/

install -d %{buildroot}%{_datadir}/excellent-bifurcation/
install -m 0644 excellent-bifurcation.png %{buildroot}%{_datadir}/excellent-bifurcation/

install -d %{buildroot}%{_datadir}/applications/
install -m 0644 excellent-bifurcation.desktop %{buildroot}%{_datadir}/applications/

%files
%doc copyright changelog README.txt
%{_gamesbindir}/excellent-bifurcation
%{_datadir}/games/excellent-bifurcation/
%{_mandir}/man6/excellent-bifurcation.6*
%{_datadir}/applications/excellent-bifurcation.desktop
%{_datadir}/excellent-bifurcation/excellent-bifurcation.png
