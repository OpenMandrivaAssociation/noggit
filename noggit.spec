Name:		noggit
Version:	0.8
Release:	1
Summary:	Streaming JSON parser
Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/yonik/noggit
Source0:	https://github.com/yonik/noggit/archive/refs/tags/noggit-%{version}.tar.gz#/noggit-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	mvn(org.sonatype.oss:oss-parent:pom::)
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

%description
Noggit is a small streaming JSON parser. 0.8 is the current release
and has no compile dependencies.

%prep
%autosetup -n noggit-noggit-%{version}

%files -f .mfiles
%doc LICENSE.txt README.md
