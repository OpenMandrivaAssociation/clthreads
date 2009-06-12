%define	major	2
%define	libname	%mklibname %name %major
%define oldlibname %mklibname %name 1
%define	develname %mklibname %name -d

Name:          clthreads
Summary:       Clthreads C++ libraries
Version:       2.2.1
Release:       %mkrel 6
License:       LGPLv2+
Group:	       System/Libraries 
Source0:       %{name}-%{version}.tar.bz2
Patch0:        clthreads-2.2.1-fix-install.patch
URL: 	       http://users.skynet.be/solaris/linuxaudio/getit.html
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
%patch0 -p0

%build

%make

%install
make DESTDIR=%buildroot  install

%clean

