Summary: Bloonix plugins for mysql.
Name: bloonix-plugins-mysql
Version: 0.12
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
Requires: bloonix-core
Requires: perl(DBI)
Requires: perl(DBD::mysql)
AutoReqProv: no

%description
bloonix-plugins-mysql provides plugins to check mysql.

%define blxdir /usr/lib/bloonix
%define docdir %{_docdir}/%{name}-%{version}

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Configure.PL --prefix /usr
%{__make}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{docdir}
install -c -m 0444 LICENSE ${RPM_BUILD_ROOT}%{docdir}/
install -c -m 0444 ChangeLog ${RPM_BUILD_ROOT}%{docdir}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{blxdir}
%dir %{blxdir}/plugins
%{blxdir}/plugins/check-*
%{blxdir}/etc/plugins/plugin-*

%dir %attr(0755, root, root) %{docdir}
%doc %attr(0444, root, root) %{docdir}/ChangeLog
%doc %attr(0444, root, root) %{docdir}/LICENSE

%changelog
* Mon Nov 03 2014 Jonny Schulz <js@bloonix.de> - 0.12-1
- Updated the license information.
* Tue Aug 26 2014 Jonny Schulz <js@bloonix.de> - 0.11-1
- Licence added and old releases deleted.
* Sat Mar 23 2014 Jonny Schulz <js@bloonix.de> - 0.10-1
- Complete rewrite of all plugins.
* Sun Sep 16 2012 Jonny Schulz <js@bloonix.de> - 0.8-1
- Added environment variable CONFIG_PATH for more
  security.
- Improved the yaml file handling.
- Updated the plugin-* files.
* Fri Jul 01 2011 Jonny Schulz <js@bloonix.de> - 0.5-1
- Renamed environment variable YAML_FILE_BASEDIR to
  PLUGIN_LIBDIR.
- Renamed environment variables BLOONIX_MYSQL_USERNAME
  and BLOONIX_MYSQL_PASSWORD to MYSQL_USERNAME and
  MYSQL_PASSWORD.
- Kicked unused option o_stat.
* Tue Jun 21 2011 Jonny Schulz <js@bloonix.de> - 0.4-1
- Added check-mysql-slave to check mysql replications.
* Mon Dec 27 2010 Jonny Schulz <js@bloonix.de> - 0.3-1
- Renamed all plugin files from *.plugin to plugin-*.
* Wed Nov 17 2010 Jonny Schulz <js@bloonix.de> - 0.2-1
- Kicked option --stat from all plugins, because
  statistics will be printed by default on stdout.
* Mon Aug 02 2010 Jonny Schulz <js@bloonix.de> - 0.1-1
- Initial release.
