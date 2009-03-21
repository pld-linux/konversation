%define		snap	942538
Summary:	A user friendly IRC Client for KDE
Summary(pl.UTF-8):	Przyjazny dla użytkownika klient IRC dla KDE
Name:		konversation
Version:	1.1.75
Release:	0.%{snap}.1
License:	GPL
Group:		Applications/Communications
Source0:	http://team.pld-linux.org/~vip/%{name}-%{version}-rev%{snap}.tar.bz2
# Source0-md5:	dc437d65107e31858e42b4c21f4850cf
URL:		http://konversation.kde.org/
BuildRequires:	automoc4
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	kde4-kdepimlibs-devel
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

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:release}%{?debug:debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	.

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir} \
        kde_libs_htmldir=%{_kdedocdir}

%find_lang %{name}  --with-kde --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/konversation
%{_datadir}/apps/kconf_update/*
%{_iconsdir}/*/*/*/*.*
%{_desktopdir}/kde4/konversation.desktop
%{_datadir}/kde4/services/konvirc.protocol
%{_datadir}/kde4/services/konvirc6.protocol
