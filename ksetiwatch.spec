Summary:	SETI@home client statistics monitor for KDE
Summary(pl):	Monitor statystyk klienta SETI@home dla KDE
Name:		ksetiwatch
Version:	2.2.2
Release:	1
Group:		X11/Window Managers/Tools
License:	GPL
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/ksetiwatch/%{name}-%{version}.tar.gz
URL:		http://ksetiwatch.sourceforge.net/
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRequires:	qt-devel >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

%description
Ksetiwatch is a KDE aplication which allows you to see how many units
have you done. There is nice map of the sky inside.

%description -l pl
Ksetiwatch jest programem pod KDE, który pozwala ogl±daæ swoje postêpy
w liczeniu jednostek SETI@home. Wartym zobaczenia elementem jest mapa
nieba.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO AUTHORS
%{_applnkdir}/Applications/*
%{_datadir}/apps/ksetiwatch
%{_pixmapsdir}/*/*/apps/*
%attr(755,root,root) %{_bindir}/*
