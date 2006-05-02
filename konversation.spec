Summary:	A user friendly IRC Client for KDE
Summary(pl):	Przyjazny dla u¿ytkownika klient IRC dla KDE
Name:		konversation
Version:	0.19
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://download.berlios.de/konversation/%{name}-%{version}.tar.bz2
# Source0-md5:	2194967b21276315a29258ccc557c429
URL:		http://konversation.berlios.de/
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

%description -l pl
Prosty i ³atwy w u¿yciu klient IRC dla KDE wyró¿niaj±cy siê m.in:
- wsparciem dla przekre¶lania tekstu oraz ró¿nych kodowañ
- wchodzeniem na wiele kana³ów na raz
- obs³ug± wiadomo¶ci away oraz teraz odtwarzanego utworu
- i wieloma innymi mo¿liwo¶ciami

%prep
%setup -q

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

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/konversation
%{_datadir}/apps/kconf_update/*
%{_datadir}/config.kcfg/*
%{_datadir}/services/konvirc*.protocol
%{_desktopdir}/kde/konversation.desktop
%{_iconsdir}/hicolor/*/*/*
%{_iconsdir}/crystalsvg/*/*/*
