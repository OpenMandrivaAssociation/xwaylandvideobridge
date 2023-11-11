%global qt5_minver 5.15.0
%global kf5_minver 5.83.0
%global kp5_minver 5.27.5
 
Name:           xwaylandvideobridge
Version:        0.3.0
Release:        1
Summary:        Utility to allow streaming Wayland windows to X applications
 
License:        (GPL-2.0-only or GPL-3.0-only) and LGPL-2.0-or-later and BSD-3-Clause
URL:            https://invent.kde.org/system/xwaylandvideobridge
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz
 
BuildRequires:  appstream-util
BuildRequires:  cmake >= 3.16
BuildRequires:  ninja
BuildRequires:  extra-cmake-modules >= %{kf5_minver}
BuildRequires:  cmake(Qt5Quick) >= %{qt5_minver}
BuildRequires:  cmake(Qt5DBus) >= %{qt5_minver}
BuildRequires:  cmake(Qt5X11Extras) >= %{qt5_minver}
BuildRequires:  cmake(KF5CoreAddons) >= %{kf5_minver}
BuildRequires:  cmake(KF5I18n) >= %{kf5_minver}
BuildRequires:  cmake(KF5WindowSystem) >= %{kf5_minver}
BuildRequires:  cmake(KF5Notifications) >= %{kf5_minver}
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-event)
BuildRequires:  pkgconfig(xcb-record)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  cmake(KPipeWire) >= %{kp5_minver}
 
Requires:       hicolor-icon-theme
 
# Requires at least KPipeWire 5.27.5
Requires:       kpipewire%{?_isa} >= %{kp5_minver}
 
%description
By design, X11 applications can't access window or screen contents
for wayland clients. This is fine in principle, but it breaks screen
sharing in tools like Discord, MS Teams, Skype, etc and more.
 
This tool allows us to share specific windows to X11 clients,
but within the control of the user at all times.
 
 
%prep
%autosetup -n %{name}-%{version}
 
%build
%cmake -GNinja
%make_build
 
%install
%make_install -C build
%find_lang %{name} --all-name
 
%files -f %{name}.lang
%license LICENSES/*
%doc README.md
#{_kf5_bindir}/%{name}
#{_kf5_datadir}/applications/org.kde.%{name}.desktop
#{_kf5_datadir}/icons/hicolor/*/apps/%{name}.*
#{_kf5_metainfodir}/org.kde.%{name}.appdata.xml
#{_kf5_datadir}/qlogging-categories5/%{name}.categories
%{_sysconfdir}/xdg/autostart/org.kde.%{name}.desktop
