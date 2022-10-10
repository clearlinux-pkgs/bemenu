#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x29317348D687B86B
#
Name     : bemenu
Version  : 0.6.12
Release  : 6
URL      : https://github.com/Cloudef/bemenu/releases/download/0.6.12/bemenu-0.6.12.tar.gz
Source0  : https://github.com/Cloudef/bemenu/releases/download/0.6.12/bemenu-0.6.12.tar.gz
Source1  : https://github.com/Cloudef/bemenu/releases/download/0.6.12/bemenu-0.6.12.tar.gz.asc
Summary  : Dynamic menu library
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: bemenu-license = %{version}-%{release}
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(ncurses)
BuildRequires : pkgconfig(ncursesw)
BuildRequires : pkgconfig(pango)
BuildRequires : pkgconfig(pangocairo)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : scdoc
BuildRequires : wayland

%description
bemenu
======
Dynamic menu library and client program inspired by dmenu
![preview](.github/preview.svg)

%package license
Summary: license components for the bemenu package.
Group: Default

%description license
license components for the bemenu package.


%prep
%setup -q -n bemenu-0.6.12
cd %{_builddir}/bemenu-0.6.12

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665411351
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1665411351
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bemenu
cp %{_builddir}/bemenu-%{version}/LICENSE-CLIENT %{buildroot}/usr/share/package-licenses/bemenu/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/bemenu-%{version}/LICENSE-LIB %{buildroot}/usr/share/package-licenses/bemenu/f45ee1c765646813b442ca58de72e20a64a7ddba || :
%make_install

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bemenu/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/bemenu/f45ee1c765646813b442ca58de72e20a64a7ddba
