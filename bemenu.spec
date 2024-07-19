#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v16
# autospec commit: 1bec16f
#
# Source0 file verified with key 0x29317348D687B86B
#
Name     : bemenu
Version  : 0.6.23
Release  : 19
URL      : https://github.com/Cloudef/bemenu/releases/download/0.6.23/bemenu-0.6.23.tar.gz
Source0  : https://github.com/Cloudef/bemenu/releases/download/0.6.23/bemenu-0.6.23.tar.gz
Source1  : https://github.com/Cloudef/bemenu/releases/download/0.6.23/bemenu-0.6.23.tar.gz.asc
Source2  : 29317348D687B86B.pkey
Summary  : Dynamic menu library
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: bemenu-bin = %{version}-%{release}
Requires: bemenu-lib = %{version}-%{release}
Requires: bemenu-license = %{version}-%{release}
Requires: bemenu-man = %{version}-%{release}
BuildRequires : git
BuildRequires : gnupg
BuildRequires : libX11-dev
BuildRequires : libxkbcommon-dev
BuildRequires : ncurses-dev
BuildRequires : pango-dev
BuildRequires : scdoc
BuildRequires : wayland
BuildRequires : wayland-dev
BuildRequires : wayland-protocols
BuildRequires : wayland-protocols-dev
BuildRequires : wlroots-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
bemenu
======
Dynamic menu library and client program inspired by dmenu
![preview](.github/preview.svg)

%package bin
Summary: bin components for the bemenu package.
Group: Binaries
Requires: bemenu-license = %{version}-%{release}

%description bin
bin components for the bemenu package.


%package dev
Summary: dev components for the bemenu package.
Group: Development
Requires: bemenu-lib = %{version}-%{release}
Requires: bemenu-bin = %{version}-%{release}
Provides: bemenu-devel = %{version}-%{release}
Requires: bemenu = %{version}-%{release}

%description dev
dev components for the bemenu package.


%package lib
Summary: lib components for the bemenu package.
Group: Libraries
Requires: bemenu-license = %{version}-%{release}

%description lib
lib components for the bemenu package.


%package license
Summary: license components for the bemenu package.
Group: Default

%description license
license components for the bemenu package.


%package man
Summary: man components for the bemenu package.
Group: Default

%description man
man components for the bemenu package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 29317348D687B86B' gpg.status
%setup -q -n bemenu-0.6.23
cd %{_builddir}/bemenu-0.6.23

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1721407300
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  PREFIX=/usr


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1721407300
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/bemenu
cp %{_builddir}/bemenu-%{version}/LICENSE-CLIENT %{buildroot}/usr/share/package-licenses/bemenu/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
cp %{_builddir}/bemenu-%{version}/LICENSE-LIB %{buildroot}/usr/share/package-licenses/bemenu/f45ee1c765646813b442ca58de72e20a64a7ddba || :
export GOAMD64=v2
GOAMD64=v2
%make_install PREFIX=/usr DESTDIR=%{buildroot}
## install_append content
mkdir -p %{buildroot}/usr/lib64
mv %{buildroot}/usr/lib/* %{buildroot}/usr/lib64
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bemenu
/usr/bin/bemenu-run

%files dev
%defattr(-,root,root,-)
/usr/include/bemenu.h
/usr/lib64/libbemenu.so
/usr/lib64/pkgconfig/bemenu.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/bemenu/bemenu-renderer-curses.so
/usr/lib64/bemenu/bemenu-renderer-wayland.so
/usr/lib64/bemenu/bemenu-renderer-x11.so
/usr/lib64/libbemenu.so.0
/usr/lib64/libbemenu.so.0.6.23

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/bemenu/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/bemenu/f45ee1c765646813b442ca58de72e20a64a7ddba

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/bemenu.1
