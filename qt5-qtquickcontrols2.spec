%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta beta3
%define devname %mklibname -d Qt5QuickControls2

%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qtquickcontrols2
Version:	5.15.0
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtquickcontrols2-everywhere-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtquickcontrols2-everywhere-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
Source100:	%{name}.rpmlintrc
Patch0:		qtquickcontrols2-beta3-compile.patch
Summary:	Qt GUI toolkit
Group:		Development/KDE and Qt
License:	LGPLv2 with exceptions or GPLv3 with exceptions and GFDL
URL:		http://www.qt.io
BuildRequires:	qmake5 = %{version}
BuildRequires:	pkgconfig(Qt5Gui) = %{version}
BuildRequires:	pkgconfig(Qt5Quick) = %{version}
BuildRequires:	pkgconfig(Qt5Widgets) = %{version}
BuildRequires:	pkgconfig(Qt5Sql) = %{version}
BuildRequires:	qt5-qtquick-private-devel = %{version}
BuildRequires:	qt5-qtqmlmodels-private-devel
# FIXME if there's an installed version, some tools in the
# qtquickcontrols2 tree try to link against it, causing
# symbol mismatches when internal APIs or ABIs changed.
BuildConflicts:	%{name}
BuildConflicts:	%{devname}
# For the Provides: generator
BuildRequires:	cmake >= 3.11.0-1

%description
Qt Quick Controls.

%files
%{_qt5_prefix}/qml/QtQuick/*
%{_qt5_prefix}/qml/Qt/labs/calendar
%{_qt5_prefix}/qml/Qt/labs/platform

%libpackage Qt5QuickControls2 5
%libpackage Qt5QuickTemplates2 5

#------------------------------------------------------------------------------
%package examples
Summary: Examples for %{name}
Group: Development/KDE and Qt

%description examples
Examples for %{name}.

%files examples
%{_qt5_prefix}/examples/*

#------------------------------------------------------------------------------
%package -n %{devname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}
Obsoletes: %{mklibname -d Qt5LabTemplates} < %{EVRD}

%description -n %{devname}
Development files for %{name}.

%files -n %{devname}
%{_includedir}/qt5/QtQuickControls2
%{_includedir}/qt5/QtQuickTemplates2
%{_libdir}/libQt5QuickTemplates2.so
%{_libdir}/libQt5QuickTemplates2.prl
%{_libdir}/libQt5QuickControls2.so
%{_libdir}/libQt5QuickControls2.prl
%{_qt5_prefix}/mkspecs/modules/qt_lib_quickcontrols2.pri
%{_qt5_prefix}/mkspecs/modules/qt_lib_quicktemplates2.pri
%{_qt5_prefix}/mkspecs/modules/qt_lib_*_private.pri
%{_libdir}/pkgconfig/Qt5QuickControls2.pc
%{_libdir}/pkgconfig/Qt5QuickTemplates2.pc
%{_libdir}/cmake/Qt5QuickControls2
%{_libdir}/cmake/Qt5QuickTemplates2

#------------------------------------------------------------------------------

%prep
%autosetup -n %qttarballdir -p1

%build
%qmake_qt5
%make_build

#------------------------------------------------------------------------------

%install
%make_install INSTALL_ROOT=%{buildroot}
