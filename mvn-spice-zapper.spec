#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-spice-zapper
Version  : 1.2
Release  : 2
URL      : https://repo1.maven.org/maven2/org/sonatype/spice/zapper/spice-zapper/1.2/spice-zapper-1.2.jar
Source0  : https://repo1.maven.org/maven2/org/sonatype/spice/zapper/spice-zapper/1.2/spice-zapper-1.2.jar
Source1  : https://repo1.maven.org/maven2/org/sonatype/spice/zapper/spice-zapper/1.2/spice-zapper-1.2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-spice-zapper-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-spice-zapper package.
Group: Data

%description data
data components for the mvn-spice-zapper package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/zapper/spice-zapper/1.2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/zapper/spice-zapper/1.2

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/zapper/spice-zapper/1.2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/sonatype/spice/zapper/spice-zapper/1.2


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/sonatype/spice/zapper/spice-zapper/1.2/spice-zapper-1.2.jar
/usr/share/java/.m2/repository/org/sonatype/spice/zapper/spice-zapper/1.2/spice-zapper-1.2.pom
