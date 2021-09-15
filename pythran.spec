#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7B24DA8C9551659F (sguelton@redhat.com)
#
Name     : pythran
Version  : 0.10.0
Release  : 5
URL      : https://files.pythonhosted.org/packages/c4/92/94b344b88bb010186caa65e5730509b4a6d2b1ab59e512ea11a2cbbb36fc/pythran-0.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c4/92/94b344b88bb010186caa65e5730509b4a6d2b1ab59e512ea11a2cbbb36fc/pythran-0.10.0.tar.gz
Source1  : https://files.pythonhosted.org/packages/c4/92/94b344b88bb010186caa65e5730509b4a6d2b1ab59e512ea11a2cbbb36fc/pythran-0.10.0.tar.gz.asc
Summary  : Ahead of Time compiler for numeric kernels
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pythran-bin = %{version}-%{release}
Requires: pythran-license = %{version}-%{release}
Requires: pythran-python = %{version}-%{release}
Requires: pythran-python3 = %{version}-%{release}
Requires: numpy
Requires: ply
BuildRequires : buildreq-distutils3
BuildRequires : numpy
BuildRequires : ply

%description
Pythran is an ahead of time compiler for a subset of the Python language, with a
        focus on scientific computing. It takes a Python module annotated with a few
        interface descriptions and turns it into a native Python module with the same
        interface, but (hopefully) faster.
        
        It is meant to efficiently compile **scientific programs**, and takes advantage
        of multi-cores and SIMD instruction units.
        
        Until 0.9.5 (included), Pythran was supporting Python 3 and Python 2.7.
        It now only supports Python **3**.

%package bin
Summary: bin components for the pythran package.
Group: Binaries
Requires: pythran-license = %{version}-%{release}

%description bin
bin components for the pythran package.


%package license
Summary: license components for the pythran package.
Group: Default

%description license
license components for the pythran package.


%package python
Summary: python components for the pythran package.
Group: Default
Requires: pythran-python3 = %{version}-%{release}

%description python
python components for the pythran package.


%package python3
Summary: python3 components for the pythran package.
Group: Default
Requires: python3-core
Provides: pypi(pythran)
Requires: pypi(beniget)
Requires: pypi(gast)
Requires: pypi(numpy)
Requires: pypi(ply)

%description python3
python3 components for the pythran package.


%prep
%setup -q -n pythran-0.10.0
cd %{_builddir}/pythran-0.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631726593
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pythran
cp %{_builddir}/pythran-0.10.0/LICENSE %{buildroot}/usr/share/package-licenses/pythran/6a7b1189c16283fa7f28dbdadda64777c82412a2
cp %{_builddir}/pythran-0.10.0/docs/LICENSE.rst %{buildroot}/usr/share/package-licenses/pythran/0fcc278a4a3d0341c919d405ce4a80f9c20f7c0c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pythran
/usr/bin/pythran-config

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pythran/0fcc278a4a3d0341c919d405ce4a80f9c20f7c0c
/usr/share/package-licenses/pythran/6a7b1189c16283fa7f28dbdadda64777c82412a2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
