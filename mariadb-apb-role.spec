%if 0%{?copr}
%define build_timestamp .%(date +"%Y%m%d%H%M%%S")
%else
%define build_timestamp %{nil}
%endif

Name:		mariadb-apb-role
Version:	1.0.2
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
* Wed Oct 04 2017 Jason Montleon <jmontleo@redhat.com> 1.0.2-1
- Bug 1498185 - Move version label onto APB spec (dymurray@redhat.com)

* Fri Sep 29 2017 Jason Montleon <jmontleo@redhat.com> 1.0.1-1
- new package built with tito

* Thu Sep 28 2017 David Zager <dzager@redhat.com> 1.0.0-1
- new package built with tito

