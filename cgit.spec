Name:           cgit
Version:        0.9.1
Release:        1%{?dist}
Summary:        cgit

Packager:       Arild Jensen <ajensen@counter-attack.com>

License:        GPL
URL:            http://hjemli.net/git/
Source0:        http://hjemli.net/git/snapshot/cgit-0.9.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  libzip-devel
BuildRequires:  openssl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  make
BuildRequires:  curl
BuildRequires:  tar
BuildRequires:  asciidoc
Requires:       httpd

%description
A web frontend for git repositories.

%prep
%setup -q


%build
make get-git
make %{?_smp_mflags}


%install
make install     DESTDIR=%{buildroot} CGIT_SCRIPT_PATH=/var/www/html/cgit
make install-man DESTDIR=%{buildroot}
mkdir -p "%{buildroot}"/var/www/cgi-bin
mv       "%{buildroot}"/var/www/html/cgit/cgit.cgi "%{buildroot}"/var/www/cgi-bin/cgit.cgi


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README
%doc COPYING
%{_mandir}/man5/cgitrc.5.gz
%dir /var/www/html/cgit
/var/www/html/cgit/cgit.css
/var/www/cgi-bin/cgit.cgi
/var/www/html/cgit/cgit.png
/usr/lib/cgit



%changelog
* Mon Mar 18 2013 Arild Jensen <ajensen@counter-attack.com> 0.9.1-1
--Initial build.
