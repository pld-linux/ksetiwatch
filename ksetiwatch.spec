Summary:	SETI@home client statistics monitor for KDE
Summary(pl):	Monitor statystyk klienta SETI@home dla KDE
Name:		ksetiwatch
Version:	3.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sourceforge/ksetiwatch/%{name}-%{version}.tar.bz2
# Source0-md5:	fa9bb1997e1bbf946302c27803b1ac71
Source1:	%{name}.png
Patch0:		%{name}-desktop.patch
URL:		http://ksetiwatch.sourceforge.net/
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.0
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	setiathome
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ksetiwatch is a KDE aplication which allows you to see how many units
have you done. There is nice map of the sky inside.

%description -l pl
Ksetiwatch jest programem pod KDE, który pozwala ogl±daæ swoje postêpy
w liczeniu jednostek SETI@home. Wartym zobaczenia elementem jest mapa
nieba.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_appsdir=%{_desktopdir}

mv $RPM_BUILD_ROOT%{_desktopdir}/{Applications,}/ksetiwatch.desktop
install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog TODO AUTHORS
%attr(755,root,root) %{_bindir}/ksetiwatch
%{_datadir}/apps/ksetiwatch
%{_pixmapsdir}/ksetiwatch.png
%{_iconsdir}/hicolor/*/apps/*.png
%{_desktopdir}/ksetiwatch.desktop
