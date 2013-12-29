Summary:	X.org input driver for joysticks
Name:		xorg-driver-input-joystick
Version:	1.6.2
Release:	3
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-joystick-%{version}.tar.bz2
# Source0-md5:	49a98669508abca1b58c4a52628767ea
Source1:	%{name}.conf
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-xserver-server-devel
Requires:	xorg-xserver-server
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for joysticks.

%package devel
Summary:	X.org joystick input driver - properties definition
Group:		Development/Libraries
Requires:	xorg-xserver-server-devel

%description devel
X.org joystick input driver - properties definition.

%prep
%setup -qn xf86-input-joystick-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d/50-joystick.conf

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/joystick_drv.so
%{_datadir}/X11/xorg.conf.d/50-joystick.conf
%{_mandir}/man4/joystick.4*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg/joystick-properties.h
%{_pkgconfigdir}/xorg-joystick.pc

