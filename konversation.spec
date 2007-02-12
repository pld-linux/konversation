%define		_snap	050106
Summary:	A user friendly IRC Client for KDE
Summary(pl.UTF-8):   Przyjazny dla użytkownika klient IRC dla KDE
Name:		konversation
Version:	0.16
Release:	0.%{_snap}.1
License:	GPL
Group:		Applications/Communications
%if ! %{with cvs}
Source0:	%{name}-%{_snap}.tar.bz2
# Source0-md5:	462c51a6f3c38a3c49642e47a6527131	
%else
Source0:	kdesource.tar.gz
%endif
URL:		http://konversation.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	unsermake >= 040511
Requires:	kdelibs
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
%setup -q -n %{name} %{?with_cvs:-D}

%build
cp %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make} -C konversation

%install
rm -rf $RPM_BUILD_ROOT
%{__make}  -C konversation \
	install DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

%{__sed} -i -e "s,Network,Network;X-Communication,g" \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/konversation.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/konversation
%{_datadir}/config.kcfg/konversation.kcfg
%{_datadir}/apps/kconf_update/*
%{_datadir}/services/konvirc*.protocol
%{_desktopdir}/kde/konversation.desktop
%{_iconsdir}/*/*/*/*.*
