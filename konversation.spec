Summary:	A user friendly IRC Client for KDE
Summary(pl.UTF-8):	Przyjazny dla użytkownika klient IRC dla KDE
Name:		konversation
Version:	1.0.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://download.berlios.de/konversation/%{name}-%{version}.tar.bz2
# Source0-md5:	60c2c5f94d4a916055db09728304b19f
Patch0:		%{name}-am110.patch
URL:		http://konversation.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel >= 3.3.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A simple and easy to use IRC client for KDE with support for:
- strikeout
- multi-channel joins
- away / unaway messages
- ignore list functionality
- support for foreign language characters
- configurable background colors and much more.

%description -l pl.UTF-8
Prosty i łatwy w użyciu klient IRC dla KDE wyróżniający się m.in:
- wsparciem dla przekreślania tekstu oraz różnych kodowań
- wchodzeniem na wiele kanałów na raz
- obsługą wiadomości away oraz teraz odtwarzanego utworu
- i wieloma innymi możliwościami

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%{__sed} -i -e "s,Network.*,Network;IRCClient;," \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/konversation.desktop

%find_lang %{name} --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/konversation
%{_datadir}/apps/kconf_update/*
%{_datadir}/config.kcfg/*
%{_datadir}/services/konvirc*.protocol
%{_desktopdir}/kde/konversation.desktop
%{_iconsdir}/hicolor/*/*/*
%{_iconsdir}/crystalsvg/*/*/*
