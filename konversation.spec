%define		_snap	040602
Summary:	A user friendly IRC Client for KDE
Summary(pl):	Przyjazny dla u¿ytkownika klient IRC dla KDE
Name:		konversation
Version:	0.13
Release:	0.%{_snap}.3
License:	GPL
Group:		Applications/Communications
%if ! %{with cvs}
Source0:	http://ep09.pld-linux.org/~djurban/kde/snap/%{name}-%{_snap}.tar.bz2
# Source0-md5:	d4fe0d2929a1564c084ba3176dfccef6
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

%description -l pl
Prosty i ³atwy w u¿yciu klient IRC dla KDE wyró¿niaj±cy siê m.in:
- wsparciem dla przekre¶lania tekstu oraz ró¿nych kodowañ
- wchodzeniem na wiele kana³ów na raz
- obs³ug± wiadomo¶ci away oraz teraz odtwarzanego utworu
- i wieloma innymi mo¿liwo¶ciami

%prep
%setup -q -n %{name} %{?with_cvs:-D}

%build
cp %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}
%{__sed} -i -e "s,Network,Network;X-Communication,g" \
	$RPM_BUILD_ROOT%{_desktopdir}/kde/konversation.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/konversation
%{_datadir}/apps/kconf_update/*
%{_desktopdir}/kde/konversation.desktop
%{_iconsdir}/hicolor/*/*/konversation.png
