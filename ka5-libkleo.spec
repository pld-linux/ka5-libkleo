%define		kdeappsver	18.12.0
%define		qtver		5.9.0
%define		kaname		libkleo
Summary:	Kleo library
Summary(pl.UTF-8):	Biblioteka kleo
Name:		ka5-%{kaname}
Version:	18.12.0
Release:	1
License:	GPL v2+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2e2d1039424b91d7b0da4413b778c996
URL:		http://www.kde.org/
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	boost-devel >= 1.34.0
BuildRequires:	gettext-devel
BuildRequires:	gpgme-qt5-devel >= 1.8.0
BuildRequires:	kf5-extra-cmake-modules >= 5.51.0
BuildRequires:	kf5-kcodecs-devel >= 5.51.0
BuildRequires:	kf5-kcompletion-devel >= 5.51.0
BuildRequires:	kf5-kconfig-devel >= 5.51.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.51.0
BuildRequires:	kf5-ki18n-devel >= 5.51.0
BuildRequires:	kf5-kitemmodels-devel >= 5.51.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.51.0
BuildRequires:	kf5-kwindowsystem-devel >= 5.51.0
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
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/libkleo.categories
/etc/xdg/libkleo.renamecategories
/etc/xdg/libkleopatrarc
%attr(755,root,root) %ghost %{_libdir}/libKF5Libkleo.so.5
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

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF5/Libkleo
%{_includedir}/KF5/libkleo
%{_includedir}/KF5/libkleo_version.h
%{_libdir}/cmake/KF5Libkleo
%attr(755,root,root) %{_libdir}/libKF5Libkleo.so
%{_libdir}/qt5/mkspecs/modules/qt_Libkleo.pri
