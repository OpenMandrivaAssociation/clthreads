%define	major	2
%define	libname	%mklibname %{name} %{major}
%define oldlibname %mklibname %{name} 1
%define	develname %mklibname %{name} -d

Summary:	POSIX threads C++ access library
Name:	clthreads
Version:	2.4.2
Release:	1
License:	LGPLv2+
Group:	System/Libraries 
Url:	https://kokkinizita.linuxaudio.org/linuxaudio/
Source0:	https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2
Patch0:		clthreads-2.4.2-fix-makefile.patch

%description
C++ wrapper library around the POSIX threads API.

#--------------------------------------------------------------------

%package -n %{libname}
Summary:	Libraries for %{name}
Group:	System/Libraries
%rename	%{oldlibname}

%description -n %{libname}
C++ wrapper library around the POSIX threads API. This package contains
the main %{name} library.

%files -n %{libname}
%_libdir/libclthreads.so.%{major}*

#--------------------------------------------------------------------

%package -n	%{develname}
Summary:	Libraries for %{name}
Group:	Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
%rename	%{oldlibname}-devel

%description -n	%{develname}
C++ wrapper library around the POSIX threads API. This package contains
the development files from %{name}.

%files -n %{develname}
%{_includedir}/%{name}.h
%{_libdir}/libclthreads.so

#--------------------------------------------------------------------

%prep
%autosetup -p1


%build
cd source
%make_build LDFLAGS="%{ldflags}" CPPFLAGS="%{optflags} -fPIC" PREFIX=%{_prefix} LIBDIR=%{_libdir}


%install
cd source
mkdir -p %{buildroot}%{_includedir}
%make_install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIR=%{_libdir} 
