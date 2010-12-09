%define	major	2
%define	libname	%mklibname %name %major
%define oldlibname %mklibname %name 1
%define	develname %mklibname %name -d

Name:          clthreads
Summary:       Clthreads C++ libraries
Version:       2.4.0
Release:       %mkrel 2
License:       LGPLv2+
Group:	       System/Libraries 
Source0:       http://www.kokkinizita.net/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Patch0:        clthreads-2.2.1-fix-install.patch
Patch1:        clthreads-2.4.0-linkage.patch
URL: 	       http://www.kokkinizita.net/linuxaudio/aeolus/index.html
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Clthreads C++ libraries

#--------------------------------------------------------------------

%package -n	%{libname}
Group: 		System/Libraries
Summary: 	Libraries for %name
Obsoletes:      %{oldlibname} < 2.2.1-2

%description 
Clthreads C++ libraries

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%_libdir/libclthreads.so.%{major}*

#--------------------------------------------------------------------

%description -n	%{libname}
The libraries from %name package

%package -n	%{develname}
Group: 		Development/Other
Summary: 	Libraries for %name
Requires:	%{libname} = %version-%release
Provides:	lib%name-devel = %version-%release
Provides: 	%{name}-devel = %{version}-%{release}
Obsoletes:      %{oldlibname}-devel < 2.2.1-2Obsoletes:     
Obsoletes:      %{libname}-devel

%description -n	%{develname}
Development libraries from %name

%files -n %{develname}
%defattr (-,root,root)
%_includedir/clthreads.h
%_libdir/libclthreads.so

#--------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch1 -p0

%build
%make LDFLAGS="%{ldflags}" CPPFLAGS="%{optflags} -fPIC"

%install
rm -fr %buildroot
mkdir -p %{buildroot}%{_includedir}
make install PREFIX=%{buildroot}%{_prefix}

%clean
rm -fr %buildroot
