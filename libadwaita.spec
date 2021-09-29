%define tag     alpha.3

Name:       libadwaita
Version:    1.0.0
Release:    %{tag}%{?dist}
Summary:    Building blocks for modern GNOME applications
License:        GPLv2+
URL:            https://gitlab.gnome.org/GNOME/libadwaita.git
Requires:       gtk4
Requires:       libva
BuildRequires:  sassc
BuildRequires:  meson
BuildRequires:  ninja-build
Buildrequires:  gtk4-devel
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection-devel
Buildrequires:  vala

Source0:        https://download.gnome.org/sources/%{name}/1.0/%{name}-%{version}.%{tag}.tar.xz

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for developing addons for %{name}.

%description
Building blocks for modern GNOME applications

%prep
%autosetup -n %{name}-%{version}.%{tag} -p1

%build
%meson -Dgtk_doc=false -Dexamples=false -Dtests=true
%meson_build

%install
%meson_install

%files
%{_libdir}/libadwaita-1.so.0
%{_libdir}/girepository-1.0/

%{_datadir}/locale/

%files devel
%{_includedir}/libadwaita-1/
%{_libdir}/libadwaita-1.so
%{_libdir}/pkgconfig/libadwaita-1.pc
%{_libdir}/gtk-4.0/inspector/libadwaita-inspector-module1.so
%{_libdir}/gtk-4.0/inspector/libadwaita-inspector-module1.so.0

%{_datadir}/gir-1.0/Adw-1.gir
%{_datadir}/vala/

%changelog
