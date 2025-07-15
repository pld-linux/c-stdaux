Summary:	Auxiliary macros and functions for the C standard library
Name:		c-stdaux
Version:	1.5.0
Release:	1
License:	Apache 2.0 or LGPL v2.1+
Group:		Libraries
Source0:	https://github.com/c-util/c-stdaux/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c2694ec5ecf3097facbf7be734bea519
URL:		https://c-util.github.io/c-stdaux/
BuildRequires:	meson >= 0.60.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The c-stdaux project contains support macros and auxiliary functions
around the functionality of common C standard libraries. This includes
helpers for the ISO C Standard Library, but also other common
specifications like POSIX or common extended features of widespread
compilers like gcc and clang.

%package devel
Summary:	Auxiliary macros and functions for the C standard library
Group:		Development/Libraries

%description devel
The c-stdaux project contains support macros and auxiliary functions
around the functionality of common C standard libraries. This includes
helpers for the ISO C Standard Library, but also other common
specifications like POSIX or common extended features of widespread
compilers like gcc and clang.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_npkgconfigdir}

%meson_install

%{__mv} $RPM_BUILD_ROOT%{_pkgconfigdir}/*.pc $RPM_BUILD_ROOT%{_npkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc AUTHORS NEWS.md README.md
%{_includedir}/c-stdaux*.h
%{_npkgconfigdir}/libcstdaux-1.pc
