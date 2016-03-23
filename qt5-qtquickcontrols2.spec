%define api %(echo %{version} |cut -d. -f1)
%define major %api
%define beta %nil

%define _qt5_prefix %{_libdir}/qt%{api}

Name:		qt5-qtquickcontrols2
Version:	5.6.0
%if "%{beta}" != ""
Release:	0.%{beta}.1
%define qttarballdir qtquickcontrols2-opensource-src-%{version}-%{beta}
Source0:	http://download.qt.io/development_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}-%{beta}/submodules/%{qttarballdir}.tar.xz
%else
Release:	1
%define qttarballdir qtquickcontrols2-opensource-src-%{version}
Source0:	http://download.qt.io/official_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}/submodules/%{qttarballdir}.tar.xz
%endif
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

%description
Qt Quick Controls.

%files
%{_qt5_prefix}/qml/Qt/labs
%{_qt5_prefix}/examples/qtlabscontrols

%libpackage Qt5LabsTemplates 5

%define devname %mklibname -d Qt5LabsTemplates

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files for %{name}

%files -n %{devname}
%{_includedir}/qt5/QtLabsControls
%{_includedir}/qt5/QtLabsTemplates
%{_libdir}/libQt5LabsTemplates.so
%{_libdir}/libQt5LabsTemplates.prl
%{_libdir}/libQt5LabsControls.a
%{_libdir}/libQt5LabsControls.prl
%{_qt5_prefix}/mkspecs/modules/qt_lib_*_private.pri

#------------------------------------------------------------------------------

%prep
%setup -q -n %qttarballdir

%build
%qmake_qt5
%make

#------------------------------------------------------------------------------

%install
%makeinstall_std INSTALL_ROOT=%{buildroot}
