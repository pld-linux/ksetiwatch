Summary:	SETI@home client statistics monitor for KDE
Summary(pl):	Monitor statystyk klienta SETI@home dla KDE
Name:		ksetiwatch
Version:	2.5.0pre2
Release:	1
Group:		X11/Window Managers/Tools
License:	GPL
Source0:	http://unc.dl.sourceforge.net/sourceforge/ksetiwatch/%{name}-%{version}.tar.gz
URL:		http://ksetiwatch.sourceforge.net
BuildRequires:	qt-devel >= 3.0.3
BuildRequires:	kdelibs-devel >= 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Ksetiwatch is a KDE aplication which allows you to see how many units
have you done. There is nice map of the sky inside.

%description -l pl
Ksetiwatch jest programem pod KDE, kt�ry pozwala ogl�da� swoje post�py
w liczeniu jednostek SETI@home. Wartym zobaczenia elementem jest mapa
nieba.

%define         _prefix         /usr/X11R6
%define         _htmldir        /usr/share/doc/kde/HTML

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install-strip DESTDIR=$RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Utilities
mv $RPM_BUILD_ROOT%{_applnkdir}/{Applications,Utilities}/ksetiwatch.desktop

%find_lang ksetiwatch --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f ksetiwatch.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksetiwatch
%{_datadir}/apps/ksetiwatch
%{_pixmapsdir}/*/*/*/*
%{_applnkdir}/Utilities/ksetiwatch.desktop
