%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name:		mariadb-apb-role
Version:	1.2.0
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
* Fri Mar 02 2018 Jason Montleon <jmontleo@redhat.com> 1.1.10-1
- Bug 1544606 - Ensure subsequent updates do not fail because dir exists
  (jmontleo@redhat.com)

* Thu Mar 01 2018 Jason Montleon <jmontleo@redhat.com> 1.1.9-1
- Bug 1544606 - Use rsync to work around cp hanging (BZ1550644)
  (jmontleo@redhat.com)

* Wed Feb 28 2018 Jason Montleon <jmontleo@redhat.com> 1.1.8-1
- Revert "Bug 1549019 - Work around connection upgrade issues with oc cp"
  (jmontleo@redhat.com)

* Tue Feb 27 2018 Jason Montleon <jmontleo@redhat.com> 1.1.7-1
- Bug 1549019 - Work around connection upgrade issues with oc cp
  (jmontleo@redhat.com)
- Bug 1549019 - Partially work around connection upgrade issues
  (jmontleo@redhat.com)

* Thu Feb 22 2018 David Zager <david.j.zager@gmail.com> 1.1.6-1
- Bug 1510294 Remove repetitive/false descriptions, set consistent titles
  (jmontleo@redhat.com)

* Fri Jan 26 2018 Jason Montleon <jmontleo@redhat.com> 1.1.5-1
- Bug 1535931 - Save all databases (jmontleo@redhat.com)

* Tue Jan 16 2018 David Zager <david.j.zager@gmail.com> 1.1.4-1
- Bug 1510294 Update APB params to use mariadb prefix instead of mysql
  (jmontleo@redhat.com)

* Mon Jan 08 2018 David Zager <david.j.zager@gmail.com> 1.1.3-1
- Update tito releasers (david.j.zager@gmail.com)
- Bug 1472226 - Add pattern regex for UI validation (cchase@redhat.com)

* Thu Dec 21 2017 Jason Montleon <jmontleo@redhat.com> 1.1.2-1
- add update functionality, add version 10.2 (jmontleo@redhat.com)
- Bug 1510804 - change tag to database. (cchase@redhat.com)

* Mon Dec 04 2017 Jason Montleon <jmontleo@redhat.com> 1.1.1-1
- updates for repo and container name change (jmontleo@redhat.com)
- specify tags in Dockerfiles (jmontleo@redhat.com)
- bump release (#14) (jmrodri@gmail.com)

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

