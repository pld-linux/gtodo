Summary:	A todo list application
Summary(pl):	Program zarz±dzaj±cy list± spraw do zrobienia
Name:		gtodo
Version:	0.14
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	51f5d71c51374931a24cce1839402457
URL:		http://qballcow.nl/gtodo/
BuildRequires:	GConf2-devel
BuildRequires:	gnome-vfs2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
Requires(post):	GConf2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gToDo is as the name suggests a todo list application.

%description -l pl
gToDo, jak sama nazwa wskazuje, jest programem zarz±dzaj±cym list±
spraw do zrobienia.

%prep
%setup -q

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
%gconf_schema_install

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
