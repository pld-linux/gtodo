Summary:	A todo list application
Summary(pl):	Program zarz±dzaj±cy list± spraw do zrobienia
Name:		gtodo
Version:	0.13.2
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	http://qball.no-ip.com/%{name}-%{version}.tar.gz
# Source0-md5:	6b19f297b3e21372ab1c999a3dfb8fac
URL:		http://qball.no-ip.com/test/index.php?s=44
BuildRequires:	gtk+2-devel
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gToDo is as the name suggests a todo list application.

%description -l pl
gToDo, jak sama nazwa wskazuje, jest programem zarz±dzaj±cym list±
spraw do zrobienia.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
