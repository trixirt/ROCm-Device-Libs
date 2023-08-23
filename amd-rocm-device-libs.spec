%global commit0 2b9acb09a3808d80c61ab89235a7cf487f52e955
%global debug_package %{nil}
%global _name amd-rocm-device-libs
%global rocm_path /opt/rocm
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global toolchain clang
%global up_name ROCm-Device-Libs

%define patch_level 1

%bcond_with debug
%bcond_with static

%if %{without debug}
  %if %{without static}
    %global suf %{nil}
  %else
    %global suf -static
  %endif
%else
  %if %{without static}
    %global suf -debug
  %else
    %global suf -static-debug
  %endif
%endif

Name: %{_name}%{suf}

Version:        5.6
Release:        %{patch_level}.git%{?shortcommit0}%{?dist}
Summary:        TBD
License:        NCSA

URL:            https://github.com/trixirt/%{up_name}
Source0:        %{url}/archive/%{commit0}/%{up_name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  zlib-devel

%if %{without debug}
%global debug_package %{nil}
%endif

%description
TBD

%package devel
Summary:        TBD

%description devel
%{summary}

%prep
%autosetup -p1 -n %{up_name}-%{commit0}

%build
%cmake	-G Ninja \
%if %{with static}
         -DBUILD_SHARED_LIBS=OFF \
%endif
%if %{without debug}
        -DCMAKE_BUILD_TYPE=RELEASE \
%else
	-DCMAKE_BUILD_TYPE=DEBUG \
%endif
	-DCMAKE_INSTALL_PREFIX=%{rocm_path}

%cmake_build

%install
%cmake_install

%files devel
%{rocm_path}

%changelog
* Sat Aug 05 2023 Tom Rix <trix@redhat.com>
- Stub something together
