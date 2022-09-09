#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		libkleo
Summary:	Kleo library
Summary(pl.UTF-8):	Biblioteka kleo
Name:		ka5-%{kaname}
Version:	22.08.1
Release:	2
License:	GPL v2+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	11fecddfe91496fa16e356bb77154fd3
URL:		http://www.kde.org/
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	boost-devel >= 1.34.0
BuildRequires:	gettext-devel
BuildRequires:	gpgme-qt5-devel >= 1.8.0
BuildRequires:	ka5-kpimtextedit-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kitemmodels-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kleo library.

%description -l pl.UTF-8
Biblioteka kleo.

%package devel
Summary:	Header files for libkipi development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kaname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libkipi development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kaname}.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/libkleopatrarc
%ghost %{_libdir}/libKF5Libkleo.so.5
%attr(755,root,root) %{_libdir}/libKF5Libkleo.so.5.*.*
%dir %{_datadir}/libkleopatra
%dir %{_datadir}/libkleopatra/pics
%{_datadir}/libkleopatra/pics/chiasmus_chi.png
%{_datadir}/libkleopatra/pics/hi16-app-gpg.png
%{_datadir}/libkleopatra/pics/hi16-app-gpgsm.png
%{_datadir}/libkleopatra/pics/hi22-app-gpg.png
%{_datadir}/libkleopatra/pics/hi22-app-gpgsm.png
%{_datadir}/libkleopatra/pics/hi32-app-gpg.png
%{_datadir}/libkleopatra/pics/hi32-app-gpgsm.png
%{_datadir}/libkleopatra/pics/key.png
%{_datadir}/libkleopatra/pics/key_bad.png
%{_datadir}/libkleopatra/pics/key_ok.png
%{_datadir}/libkleopatra/pics/key_unknown.png
%{_datadir}/libkleopatra/pics/smartcard.xpm
%{_datadir}/qlogging-categories5/libkleo.categories
%{_datadir}/qlogging-categories5/libkleo.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/Libkleo
%{_libdir}/cmake/KF5Libkleo
%{_libdir}/libKF5Libkleo.so
%{_libdir}/qt5/mkspecs/modules/qt_Libkleo.pri
