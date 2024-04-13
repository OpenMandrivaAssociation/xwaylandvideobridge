Name:           xwaylandvideobridge
Version:        0.4.0
Release:        2
Summary:        Utility to allow streaming Wayland windows to X applications
 
License:        (GPL-2.0-only or GPL-3.0-only) and LGPL-2.0-or-later and BSD-3-Clause
URL:            https://invent.kde.org/system/xwaylandvideobridge
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  appstream
BuildRequires:  appstream-util
BuildRequires:  cmake >= 3.16
BuildRequires:  ninja
BuildRequires:  cmake(Qt6)
BuildRequires:  extra-cmake-modules
BuildRequires:	 cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  cmake(KPipeWire) >= 5.27.80
BuildRequires:  pkgconfig(libpipewire-0.3)
 
Requires:       hicolor-icon-theme
 
# Requires at least KPipeWire 5.27.5
Requires:      %{_lib}KPipeWire-plasma6 >= 5.27.80

%description
By design, X11 applications can't access window or screen contents
for wayland clients. This is fine in principle, but it breaks screen
sharing in tools like Discord, MS Teams, Skype, etc and more.
 
This tool allows us to share specific windows to X11 clients,
but within the control of the user at all times.
 
 
%prep
%autosetup -n %{name}-%{version}
 
%build
%cmake  \
        -DBUILD_WITH_QT6:BOOL=ON \
        -GNinja
%ninja_build
 
%install
%ninja_install -C build
%find_lang %{name} --all-name
 
%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_bindir}/xwaylandvideobridge
%{_datadir}/applications/org.kde.xwaylandvideobridge.desktop
%{_datadir}/metainfo/org.kde.xwaylandvideobridge.appdata.xml
%{_datadir}/qlogging-categories6/xwaylandvideobridge.categories
%{_sysconfdir}/xdg/autostart/org.kde.%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/xwaylandvideobridge.svg
