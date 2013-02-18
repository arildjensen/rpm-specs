Name:           st
Version:        0.3
Release:        1%{?dist}
Summary:        Simple Terminal

Packager:       Arild Jensen <ajensen@counter-attack.com>

Group:          User Interface/Desktops
License:        MIT
URL:            http://st.suckless.org/ 
Source0:        http://git.suckless.org/st/snapshot/st-0.3.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libX11-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libXext-devel
BuildRequires:  libXft-devel
Requires:       xorg-x11-xinit

%description
A simple terminal emulator for X.

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
%doc FAQ
%doc TODO
%doc LEGACY
%{_mandir}/man1/st.1.gz
%{_bindir}/st



%changelog
* Wed Feb 18 2013  Arild Jensen <ajensen@counter-attack.com> 0.3-1
--Initial build.
