Name:           dwm          
Version:        6.0       
Release:        2%{?dist}
Summary:        Dynamic Window Manager

Packager:       Arild Jensen <ajensen@counter-attack.com>

Group:          User Interface/Desktops
License:        MIT
URL:            http://dwm.suckless.org/ 
Source0:        http://git.suckless.org/dwm/snapshot/dwm-6.0.tar.gz
Patch0:         dwm-6.0-ca.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libX11-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libXinerama-devel
Requires:       xorg-x11-xinit
Requires:       st
Requires:       terminus-fonts

%description
A dynamic window manager for X with tiled, monocle and floating layouts.

%prep
%setup -q
%patch0 -p1


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

# Thu Feb 21 2013  Arild Jensen <ajensen@counter-attack.com> 6.0-2
--Patched to use 'st' instead of uxterm and added dependency on Terminus font.
