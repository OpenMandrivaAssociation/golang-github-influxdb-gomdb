# http://github.com/influxdb/gomdb

%global commit		29fe330c5ab33c4e48470bd4b980bf522471190a
%global goipath         github.com/influxdb/gomdb


%gometa -i

Name:           %{goname}
Version:	0
Release:	0.11.git%{?dist}
Summary:	Go wrapper for LMDB
License:	BSD
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml
BuildArch:	noarch

%description
Go wrapper for LMDB - OpenLDAP Lightning Memory-Mapped Database

%package devel
Summary:	Go wrapper for LMDB

%description devel
Go wrapper for LMDB - OpenLDAP Lightning Memory-Mapped Database

This package contains library source intended for
building other packages which use %{goipath}.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .

%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d .

%files devel -f devel.file-list
%doc LICENSE README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.10.git%{shortcommit}.git29fe330.git29fe330
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git29fe330
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.8.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git29fe330
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git29fe330
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.2.git29fe330
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Sep 25 2014 Jan Chaloupka <jchaloup@redhat.com> - 0-0.1.git29fe330
- First package for Fedora

