#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-scatterplot3d
Version  : 0.3.41
Release  : 36
URL      : https://cran.r-project.org/src/contrib/scatterplot3d_0.3-41.tar.gz
Source0  : https://cran.r-project.org/src/contrib/scatterplot3d_0.3-41.tar.gz
Summary  : 3D Scatter Plot
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : buildreq-R

%description
No detailed description available

%prep
%setup -q -c -n scatterplot3d
cd %{_builddir}/scatterplot3d

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589530283

%install
export SOURCE_DATE_EPOCH=1589530283
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library scatterplot3d
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library scatterplot3d
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library scatterplot3d
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc scatterplot3d || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/scatterplot3d/CITATION
/usr/lib64/R/library/scatterplot3d/DESCRIPTION
/usr/lib64/R/library/scatterplot3d/INDEX
/usr/lib64/R/library/scatterplot3d/Meta/Rd.rds
/usr/lib64/R/library/scatterplot3d/Meta/features.rds
/usr/lib64/R/library/scatterplot3d/Meta/hsearch.rds
/usr/lib64/R/library/scatterplot3d/Meta/links.rds
/usr/lib64/R/library/scatterplot3d/Meta/nsInfo.rds
/usr/lib64/R/library/scatterplot3d/Meta/package.rds
/usr/lib64/R/library/scatterplot3d/Meta/vignette.rds
/usr/lib64/R/library/scatterplot3d/NAMESPACE
/usr/lib64/R/library/scatterplot3d/R/scatterplot3d
/usr/lib64/R/library/scatterplot3d/R/scatterplot3d.rdb
/usr/lib64/R/library/scatterplot3d/R/scatterplot3d.rdx
/usr/lib64/R/library/scatterplot3d/doc/index.html
/usr/lib64/R/library/scatterplot3d/doc/s3d.Rnw
/usr/lib64/R/library/scatterplot3d/doc/s3d.pdf
/usr/lib64/R/library/scatterplot3d/help/AnIndex
/usr/lib64/R/library/scatterplot3d/help/aliases.rds
/usr/lib64/R/library/scatterplot3d/help/paths.rds
/usr/lib64/R/library/scatterplot3d/help/scatterplot3d.rdb
/usr/lib64/R/library/scatterplot3d/help/scatterplot3d.rdx
/usr/lib64/R/library/scatterplot3d/html/00Index.html
/usr/lib64/R/library/scatterplot3d/html/R.css
/usr/lib64/R/library/scatterplot3d/po/de/LC_MESSAGES/R-scatterplot3d.mo
/usr/lib64/R/library/scatterplot3d/po/en/LC_MESSAGES/R-scatterplot3d.mo
