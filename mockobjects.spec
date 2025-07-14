%define j2ee12  %{?_with_j2ee12:1}%{!?_without_j2ee12:0}
%define j2ee13  %{?_with_j2ee13:1}%{!?_without_j2ee13:0}
Summary:	Java MockObjects package
Summary(pl.UTF-8):	Pakiet Java MockObjects
Name:		mockobjects
Version:	0.09
Release:	0.1
License:	BSD Style
Group:		Development
Source0:	http://www.mockobjects.com/dist/%{name}-%{version}.tar.gz
# Source0-md5:	-
Patch0:		%{name}-buildjdk.patch
Patch1:		%{name}-ext-httpmethod-abstract.patch
Patch2:		%{name}-junit.patch
URL:		http://www.mockobjects.com/
BuildRequires:	ant
BuildRequires:	ant >= 1.6.1
BuildRequires:	java-commons-httpclient
BuildRequires:	jdk
BuildRequires:	jdk < 1.5
BuildRequires:	jdk >= 1.4.0
BuildRequires:	junit
#Requires:	/usr/sbin/update-alternatives
Requires:	junit
Provides:	%{name}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Mock Objects project is a generic unit testing framework whose
goal is to facilitate developing unit tests in the mock object style.
The goal of this project is to provide, a core mock objects framework.
This is a library of code that supports the implementation of mock
objects. It is based around a set of expectation classes for values
and collections. There are also various other classes to make mock
objects easier to write or to use.

%description -l pl.UTF-8
Projekt Mock Objects to ogólny szkielet testów jednostkowych, którego
celem jest ułatwienie tworzenia testów jednostkowych w stylu pozornych
obiektów. Celem projektu jest dostarczenie szkieletu głównych obiektów
pozornych. Jest to biblioteka kodu wspierającego implementowanie
takich obiektów. Jest oparta na zbiorze klas oczekujących dla wartości
i kolekcji. Zawiera także różne inne klasy ułatwiające pisanie i
używanie obiektów pozornych.

%package jdk1.4
Summary:	MockObjects for 1.4 JDK
Summary(pl.UTF-8):	MockObjects dla JDK 1.4
Group:		Development
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/sbin/update-alternatives
Requires:	jdk < 1.5
Requires:	jdk >= 1.4

%description jdk1.4
MockObjects specific to JDK 1.4.x.

%description jdk1.4 -l pl.UTF-8
MockObjects specyficzne dla JDK 1.4.x.

%package httpclient
Summary:	MockObjects for Commons HttpClient
Summary(pl.UTF-8):	MockObjects dla Commons HttpClient
Group:		Development
Requires:	%{name} = %{version}-%{release}
Requires:	/usr/sbin/update-alternatives
Requires:	java-commons-httpclient

%description httpclient
MockObjects for Jakarta Commons HttpClient.

%description httpclient -l pl.UTF-8
MockObjects dla Jakarta Commons HttpClient.

%package alt-httpclient
Summary:	Mockable API for Commons HttpClient
Summary(pl.UTF-8):	Mockable API dla Commons HttpClient
Group:		Development
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-httpclient = %{version}-%{release}
Requires:	/usr/sbin/update-alternatives
Requires:	java-commons-httpclient

%description alt-httpclient
Alternative API for Jakarta Commons HttpClient to allow for testing.

%description alt-httpclient -l pl.UTF-8
Alternatywne API dla Jakarta Commons HttpClient do testowania.

%package alt-jdk1.4
Summary:	Mockable API for JDK 1.4
Summary(pl.UTF-8):	Mockable API dla JDK 1.4
Group:		Development
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-jdk1.4 = %%{version}-%{release}
Requires:	jdk < 1.5
Requires:	jdk >= 1.4

%description alt-jdk1.4
Alternative API for JDK 1.4 to allow for testing.

%description alt-jdk1.4 -l pl.UTF-8
Alternatywne API dla JDK 1.4 do testowania.

%package jdk1.4-j2ee1.2
Summary:	Mockable J2EE API for JDK 1.4 and J2EE 1.2
Summary(pl.UTF-8):	Mockable J2EE API dla JDK 1.4 i J2EE 1.2
Group:		Development
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-jdk1.4 = %{version}-%{release}
Requires:	jdk < 1.5
Requires:	jdk >= 1.4

%description jdk1.4-j2ee1.2
API for JDK 1.4 to allow testing with J2EE 1.2 mocks.

%description jdk1.4-j2ee1.2 -l pl.UTF-8
API dla JDK 1.4 do testowania z obiektami J2EE 1.2.

%package jdk1.4-j2ee1.3
Summary:	Mockable J2EE API for JDK 1.4 and J2EE 1.3
Summary(pl.UTF-8):	Mockable J2EE API dla JDK 1.4 i J2EE 1.3
Group:		Development
Requires:	%{name} = %{version}-%{release}
Requires:	%{name}-jdk1.4 = %{version}-%{release}
Requires:	jdk < 1.5
Requires:	jdk >= 1.4

%description jdk1.4-j2ee1.3
API for JDK 1.4 to allow testing with J2EE 1.3 mocks.

%description jdk1.4-j2ee1.3 -l pl.UTF-8
API dla JDK 1.4 do testowania z obiektami J2EE 1.3.

%prep
%setup -q
%patch -P0
%patch -P1 -p1
%patch -P2 -p1

%build
# build with (almost) empty CLASSPATH
CLASSPATH=`build-classpath junit` ant -buildfile build.xml -Dbuild.compiler=modern jar-core

#JVM extensions

[ -z "$JAVA_HOME" ] && export JAVA_HOME="/usr/lib/java"

CLASSPATH=`build-classpath junit` ant -buildfile build.xml -Dbuild.compiler=modern jar-jdk

#Httpclient extensions
CLASSPATH=`build-classpath jakarta-commons-httpclient junit` ant jar-ext-httpclient

%if %{j2ee12}
rm -rf out/j2ee/classes/*
CLASSPATH=`build-classpath j2ee-1.2 junit` ant -buildfile build.xml -Dbuild.compiler=modern -Djdk.version=1.4 -Dj2ee.version=1.2 compile-j2ee jar-j2ee
%endif

%if %{j2ee13}
rm -rf out/j2ee/classes/*
CLASSPATH=`build-classpath j2ee-1.3 junit` ant -buildfile build.xml -Dbuild.compiler=modern -Djdk.version=1.4 -Dj2ee.version=1.3 compile-j2ee jar-j2ee
%endif

%install
rm -rf $RPM_BUILD_ROOT
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

# jars
install -d $RPM_BUILD_ROOT%{_javadir}
install -d $RPM_BUILD_ROOT%{_javadir}{-1.4.0,-1.4.1,-1.4.2}
install -d $RPM_BUILD_ROOT%{_javadir}-ext/%{name}-{,alt-}jdk1.4

cd out
install %{name}-core-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-core-%{version}.jar
install %{name}-httpclient.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-httpclient-%{version}.jar
install alt-httpclient.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-alt-httpclient-%{version}.jar

# Install JDK Mocks and alternatives
install %{name}-jdk1.4-%{version}.jar $RPM_BUILD_ROOT%{_javadir}-ext/%{name}-jdk1.4/%{name}-%{version}.jar
install %{name}-alt-jdk1.4-%{version}.jar $RPM_BUILD_ROOT%{_javadir}-ext/%{name}-alt-jdk1.4/%{name}-alt-%{version}.jar

# Install J2EE Mocks
%if %{j2ee12}
install %{name}-jdk1.4-j2ee1.2-%{version}.jar $RPM_BUILD_ROOT%{_javadir}-ext/%{name}-jdk1.4/%{name}-j2ee1.2-%{version}.jar
%endif

%if %{j2ee13}
install %{name}-jdk1.4-j2ee1.3-%{version}.jar $RPM_BUILD_ROOT%{_javadir}-ext/%{name}-jdk1.4/%{name}-j2ee1.3-%{version}.jar
%endif

cd -

cd $RPM_BUILD_ROOT%{_javadir}
for jar in *-%{version}.jar; do
	ln -sf ${jar} $(echo $jar| sed "s|-%{version}||g")
done
cd -

cd $RPM_BUILD_ROOT%{_javadir}-ext/%{name}-jdk1.4
for jar in *-%{version}.jar; do
	ln -sf ${jar} $(echo $jar| sed "s|-%{version}||g")
done
cd -

cd $RPM_BUILD_ROOT%{_javadir}-ext/%{name}-alt-jdk1.4
for jar in *-%{version}.jar; do
	ln -sf ${jar} $(echo $jar| sed "s|-%{version}||g")
done
cd -

for EXTENSION_VM in 1.4.0 1.4.1 1.4.2; do
	EXTENSION_PREFIX=$(echo $EXTENSION_VM | sed -e 's/1\.\([4]\)\.[0-9]/1.\1/')
	cd $RPM_BUILD_ROOT%{_javadir}-${EXTENSION_VM}
	ln -sf %{_javadir}-ext/%{name}-jdk${EXTENSION_PREFIX}/%{name}-%{version}.jar  .
	ln -sf %{_javadir}-ext/%{name}-alt-jdk${EXTENSION_PREFIX}/%{name}-alt-%{version}.jar .
%if %{j2ee12}
	ln -sf %{_javadir}-ext/%{name}-jdk${EXTENSION_PREFIX}/%{name}-j2ee1.2-%{version}.jar  .
%endif
%if %{j2ee13}
	ln -sf %{_javadir}-ext/%{name}-jdk${EXTENSION_PREFIX}/%{name}-j2ee1.3-%{version}.jar  .
%endif
	for jar in *-%{version}.jar; do
		ln -sf ${jar} $(echo $jar| sed "s|-%{version}||g")
	done
	cd -
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/README
%{_javadir}/%{name}-core*

%files jdk1.4
%defattr(644,root,root,755)
%{_javadir}-ext/%{name}-jdk1.4/%{name}-%{version}.jar
%{_javadir}-ext/%{name}-jdk1.4/%{name}.jar
%{_javadir}-1.4.0/%{name}-%{version}.jar
%{_javadir}-1.4.0/%{name}.jar
%{_javadir}-1.4.1/%{name}-%{version}.jar
%{_javadir}-1.4.1/%{name}.jar
%{_javadir}-1.4.2/%{name}-%{version}.jar
%{_javadir}-1.4.2/%{name}.jar

%files httpclient
%defattr(644,root,root,755)
%{_javadir}/%{name}-httpclient*

%files alt-jdk1.4
%defattr(644,root,root,755)
%{_javadir}-ext/%{name}-alt-jdk1.4/*
%{_javadir}-1.4.0/%{name}-alt-%{version}.jar
%{_javadir}-1.4.0/%{name}-alt.jar
%{_javadir}-1.4.1/%{name}-alt-%{version}.jar
%{_javadir}-1.4.1/%{name}-alt.jar
%{_javadir}-1.4.2/%{name}-alt-%{version}.jar
%{_javadir}-1.4.2/%{name}-alt.jar

%files alt-httpclient
%defattr(644,root,root,755)
%{_javadir}/%{name}-alt-httpclient*

%if %{j2ee12}
%files jdk1.4-j2ee1.2
%defattr(644,root,root,755)
%{_javadir}-ext/%{name}-jdk1.4/%{name}-j2ee1.2-%{version}.jar
%{_javadir}-ext/%{name}-jdk1.4/%{name}-j2ee1.2.jar
%{_javadir}-1.4.0/%{name}-j2ee1.2-%{version}.jar
%{_javadir}-1.4.0/%{name}-j2ee1.2.jar
%{_javadir}-1.4.1/%{name}-j2ee1.2-%{version}.jar
%{_javadir}-1.4.1/%{name}-j2ee1.2.jar
%{_javadir}-1.4.2/%{name}-j2ee1.2-%{version}.jar
%{_javadir}-1.4.2/%{name}-j2ee1.2.jar
%endif

%if %{j2ee13}
%files jdk1.4-j2ee1.3
%defattr(644,root,root,755)
%{_javadir}-ext/%{name}-jdk1.4/%{name}-j2ee1.3-%{version}.jar
%{_javadir}-ext/%{name}-jdk1.4/%{name}-j2ee1.3.jar
%{_javadir}-1.4.0/%{name}-j2ee1.3-%{version}.jar
%{_javadir}-1.4.0/%{name}-j2ee1.3.jar
%{_javadir}-1.4.1/%{name}-j2ee1.3-%{version}.jar
%{_javadir}-1.4.1/%{name}-j2ee1.3.jar
%{_javadir}-1.4.2/%{name}-j2ee1.3-%{version}.jar
%{_javadir}-1.4.2/%{name}-j2ee1.3.jar
%endif
