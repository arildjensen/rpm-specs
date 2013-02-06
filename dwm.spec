Name:           dwm          
Version:        6.0       
Release:        1%{?dist}
Summary:        Dynamic Window Manager

Packager:       Arild Jensen <ajensen@counter-attack.com>

Group:          User Interface/Desktops
License:        MIT
URL:            http://dwm.suckless.org/ 
Source0:        http://git.suckless.org/dwm/snapshot/dwm-6.0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libX11-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libXinerama-devel
Requires:       xorg-x11-xinit

%description
A dynamic window manager for X with tiled, monocle and floating layouts.

%prep
%setup -q


%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=/usr DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc LICENSE
%doc README
%doc BUGS
%doc TODO
%{_mandir}/man1/dwm.1.gz
%{_bindir}/dwm



%changelog
* Wed Feb 06 2013  Arild Jensen <ajensen@counter-attack.com> 6.0-1
--Initial build.
