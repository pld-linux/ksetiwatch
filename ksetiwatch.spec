Summary:	SETI@home client statistics monitor for KDE
Summary(pl):	Monitor statystyk klienta SETI@home dla KDE
Name:		ksetiwatch
Version:	2.2.2
Release:	1
Group:		X11/Window Managers/Tools
License:	GPL
Source0:	http://prdownloads.sourceforge.net/ksetiwatch/%{name}-%{version}.tar.gz
URL:		http://ksetiwatch.sourceforge.net/
BuildRequires:	qt-devel >= 2.2
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog TODO AUTHORS %{name}/docs/en/{*.html,*.png}
%{_applnkdir}/Applications/*
%{_datadir}/apps/%{name}/pics/*
%{_datadir}/apps/%{name}/sounds/*
%{_datadir}/icons/locolor
%{_datadir}/locale
%attr(755,root,root) %{_bindir}/*
