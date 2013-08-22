Name:		   jboss-eap
Version:	 6.1.0
Release:	 1
Summary: 	 JBoss Enterprise Application Platform
License:   Proprietary
Source:    http://redhat.com
BuildArch: noarch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
Prefix:    /opt
Packager:  Arild Jensen <ajensen@counter-attack.com>


%description
JBoss Enterprise Application Platform repackaged with no modification from redhat.com standard download. Suggest using a Configuration Manager (such as Puppet) to handle file permissions and ownership and CLI files to implement custom JBoss configuration.

%prep
%setup -n jboss-eap-6.1

%files
%defattr(-,root,root,-)
/opt/*

%build 

%install
mkdir -p                                $RPM_BUILD_ROOT/opt/jboss-eap
cp -R    $RPM_BUILD_DIR/jboss-eap-6.1/* $RPM_BUILD_ROOT/opt/jboss-eap

%post

%clean
rm -rf %{buildroot}
