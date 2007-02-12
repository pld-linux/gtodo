Summary:	A todo list application
Summary(pl.UTF-8):   Program zarządzający listą spraw do zrobienia
Name:		gtodo
Version:	0.14
Release:	3
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/gtodo/%{name}-%{version}.tar.gz
# Source0-md5:	51f5d71c51374931a24cce1839402457
Patch0:		%{name}-desktop.patch
URL:		http://qballcow.nl/index.php?name=gtodo
BuildRequires:	GConf2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gToDo is as the name suggests a todo list application.

%description -l pl.UTF-8
gToDo, jak sama nazwa wskazuje, jest programem zarządzającym listą
spraw do zrobienia.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install gtodo.schemas

%preun
%gconf_schema_uninstall gtodo.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
