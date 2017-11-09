%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name:		mariadb-apb-role
Version:	1.0.10
Release:	1%{build_timestamp}%{?dist}
Summary:	Ansible Playbook for MariaDB APB

License:	ASL 2.0
URL:		https://github.com/ansibleplaybookbundle/RHSCL-MariaDB-APB
Source0:	https://github.com/ansibleplaybookbundle/RHSCL-MariaDB-APB/archive/%{name}-%{version}.tar.gz
BuildArch:  	noarch


%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%install
mkdir -p %{buildroot}/opt/apb/ %{buildroot}/opt/ansible/
mv playbooks %{buildroot}/opt/apb/actions
mv roles %{buildroot}/opt/ansible/roles

%files
%doc
/opt/apb/actions
/opt/ansible/roles

%changelog
* Wed Nov 08 2017 jesus m. rodriguez <jesusr@redhat.com> 1.0.10-1
- Bug 1511258 - Properly delete mariadb service. (#13) (cchase@redhat.com)

* Wed Nov 08 2017 Jason Montleon <jmontleo@redhat.com> 1.0.9-1
- Bug 1511077 - user password was incorrectly using root_password
  (cchase@redhat.com)

* Tue Nov 07 2017 Jason Montleon <jmontleo@redhat.com> 1.0.8-1
- Bug 1510599 - use service name for binding DB_HOST instead of cluster IP
  (cchase@redhat.com)

* Tue Nov 07 2017 Jason Montleon <jmontleo@redhat.com> 1.0.7-1
- Bug 1508278 - Use include_tasks instead of include for updated Ansible
  version. (cchase@redhat.com)

* Fri Nov 03 2017 Jason Montleon <jmontleo@redhat.com> 1.0.6-1
- Bug 1509476 - Generate password broken when left blank. (cchase@redhat.com)

* Fri Nov 03 2017 Jason Montleon <jmontleo@redhat.com> 1.0.5-1
- Bug 1508278 - Revert to using include for now for Ansible 2.3.2
  compatibility. (cchase@redhat.com)

* Fri Nov 03 2017 Jason Montleon <jmontleo@redhat.com> 1.0.4-1
- Bug 1509018 - Added tags to show up under the right tab in the UI
  (cchase@redhat.com)
- Bug 1508994 - Hide password with display_type: password (cchase@redhat.com)
- Bug 1508278 - Use include_tasks instead of include (cchase@redhat.com)

* Tue Oct 10 2017 Jason Montleon <jmontleo@redhat.com> 1.0.3-1
- Update dockerfiles (david.j.zager@gmail.com)
- Bug 1500364 - Update apb.yml with all dependent images
  (david.j.zager@gmail.com)
- Bug 1498571 - Remove image from APB (david.j.zager@gmail.com)

* Wed Oct 04 2017 Jason Montleon <jmontleo@redhat.com> 1.0.2-1
- Bug 1498185 - Move version label onto APB spec (dymurray@redhat.com)

* Fri Sep 29 2017 Jason Montleon <jmontleo@redhat.com> 1.0.1-1
- new package built with tito

* Thu Sep 28 2017 David Zager <dzager@redhat.com> 1.0.0-1
- new package built with tito

