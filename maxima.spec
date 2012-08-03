%define enable_clisp	1
%define enable_gcl	1
%define enable_sbcl	1
%define enable_ecl	1
%define defaultlisp	clisp

%if %enable_clisp
%define clisp_flags	--enable-clisp
%else
%define clisp_flags	--disable-clisp
%endif

%if %enable_gcl
%define gcl_flags	--enable-gcl
%else
%define gcl_flags	--disable-gcl
%endif

%if %enable_sbcl
%define sbcl_flags	--enable-sbcl
%define sbcl_version	1.0.47
%else
%define sbcl_flags	--disable-sbcl
%endif

%if %enable_ecl
%define ecl_flags	--enable-ecl
# build module required by sagemath runtime?
%define sagemath	1
%define ecllib		%(ecl -eval "(princ (SI:GET-LIBRARY-PATHNAME))" -eval "(quit)")
%else
%define sagemath	0
%define ecl_flags	--disable-ecl
%endif

Summary:	Maxima Symbolic Computation Program
Name:		maxima
Version:	5.27.0
Release:	%mkrel 1
License:	GPLv2
Group:		Sciences/Mathematics
URL:		http://maxima.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/maxima/%{name}-%{version}.tar.gz
Source1:	icons-%{name}.tar.bz2
Patch0:		maxima-5.22.0-xdg-utils.patch
Patch1:		maxima-5.14.0-missed-extract-categories.patch
Patch2:		maxima-fix-contrib-docs.patch
Patch3:		maxima-5.23.0-clisp-noreadline.patch
Patch4:		maxima-5.22.0-ecl-ldflags.patch
BuildRequires:	texinfo
BuildRequires:	texlive
BuildRequires:	python
Suggests:	tk
Suggests:	tcl
Requires:	maxima-runtime
Requires:	gnuplot
%if %{enable_clisp}
BuildRequires:	clisp
%endif
%if %{enable_gcl}
BuildRequires:	gcl > 2.5.3
%endif
%if %{enable_sbcl}
BuildRequires:	sbcl = %{sbcl_version}
%endif
%if %{enable_ecl}
BuildRequires:	ecl 
%endif

%description
Maxima is a full symbolic computation program.  It is full featured
doing symbolic manipulation of polynomials, matrices, rational
functions, integration, Todd-coxeter, graphing, bigfloats.  It has a
symbolic debugger source level debugger for maxima code.  Maxima is
based on the original Macsyma developed at MIT in the 1970's.  It is
quite reliable, and has good garbage collection, and no memory leaks.
It comes with hundreds of self tests.

#--------------------------------------------------------------------

%package gui
Summary: Tcl/Tk GUI interface to Maxima
Group:		Sciences/Mathematics
Requires:	maxima
Requires:	tk
Provides:	xmaxima = %{version}-%{release}
%description gui
Tcl/Tk GUI interface to Maxima.

%files gui
%defattr(-,root,root)
%{_bindir}/xmaxima
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/*.png

#--------------------------------------------------------------------

%if %{enable_clisp}
%package runtime-clisp
Summary: Maxima compiled with clisp
Group: Sciences/Mathematics
Requires:	clisp
Requires:	maxima = %{version}-%{release}
Provides:	maxima-runtime = %{version}-%{release}
%description runtime-clisp
Maxima compiled with clisp.

%files runtime-clisp
%defattr(-,root,root)
%dir %{_libdir}/maxima/%{version}/binary-clisp
%{_libdir}/maxima/%{version}/binary-clisp/*
%endif

#--------------------------------------------------------------------

%if %{enable_gcl}
%package runtime-gcl
Summary: Maxima compiled with GCL
Group:		Sciences/Mathematics
Requires:	maxima = %{version}-%{release}
Suggests:	rlwrap
Provides:	maxima-runtime = %{version}-%{release}
%description runtime-gcl
Maxima compiled with Gnu Common Lisp.

%files runtime-gcl
%defattr(-,root,root)
%{_bindir}/rmaxima
%dir %{_libdir}/maxima/%{version}/binary-gcl
%{_libdir}/maxima/%{version}/binary-gcl/*
%endif

#--------------------------------------------------------------------
%if %{enable_sbcl}
%package runtime-sbcl
Summary: Maxima compiled with SBCL
Group: Sciences/Mathematics
Requires:	sbcl = %{sbcl_version}
Requires:	maxima = %{version}-%{release}
Provides:	maxima-runtime = %{version}-%{release}

%description runtime-sbcl
Maxima compiled with SBCL.

%files runtime-sbcl
%defattr(-,root,root)
%dir %{_libdir}/maxima/%{version}/binary-sbcl
%{_libdir}/maxima/%{version}/binary-sbcl/*
%endif

#--------------------------------------------------------------------
%if %{enable_ecl}
%package runtime-ecl
Summary: Maxima compiled with ECL
Group: Sciences/Mathematics
Requires:	maxima = %{version}-%{release}
Provides:	maxima-runtime = %{version}-%{release}

%description runtime-ecl
Maxima compiled with ECL.

%files runtime-ecl
%defattr(-,root,root)
%dir %{_libdir}/maxima/%{version}/binary-ecl
%{_libdir}/maxima/%{version}/binary-ecl/*
  %if %{sagemath}
%{ecllib}/maxima.fas
  %endif
%endif

#--------------------------------------------------------------------
%package lang-de-utf8
Summary:	Maxima German UTF-8 language pack
Group:		Sciences/Mathematics
Requires:	maxima = %{version}

%description lang-de-utf8
Maxima German language support (UTF-8).

%files lang-de-utf8
%defattr(-,root,root)
%doc %{_datadir}/maxima/%{version}/doc/html/de.utf8
%{_infodir}/de.utf8

#--------------------------------------------------------------------
%package lang-es-utf8
Summary:	Maxima Spanish UTF-8 language pack
Group:		Sciences/Mathematics
Requires:	maxima = %{version}

%description lang-es-utf8
Maxima Spanish language support (UTF-8).

%files lang-es-utf8
%defattr(-,root,root)
%doc %{_datadir}/maxima/%{version}/doc/html/es.utf8
%{_infodir}/es.utf8

#--------------------------------------------------------------------
%package lang-pt-utf8
Summary:	Maxima Portuguese UTF-8 language pack
Group:		Sciences/Mathematics
Requires:	maxima = %{version}

%description lang-pt-utf8
Maxima Portuguese language support (UTF-8).

%files lang-pt-utf8
%defattr(-,root,root)
%doc %{_datadir}/maxima/%{version}/doc/html/pt.utf8
%{_infodir}/pt.utf8

#--------------------------------------------------------------------
%package lang-pt_BR-utf8
Summary:	Maxima Brazilian Portuguese UTF-8 language pack
Group:		Sciences/Mathematics
Requires:	maxima = %{version}

%description lang-pt_BR-utf8
Maxima Brazilian Portuguese language support (UTF-8).

%files lang-pt_BR-utf8
%defattr(-,root,root)
%doc %{_datadir}/maxima/%{version}/doc/html/pt_BR.utf8
%{_infodir}/pt_BR.utf8

#--------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export GCL_ANSI=y
%if %{enable_sbcl}
export SBCL_HOME=%{_libdir}/sbcl
%endif
export CFLAGS="%{optflags} -fno-fast-math"
export CXXFLAGS="%{optflags} -fno-fast-math"
%configure2_5x \
	%{clisp_flags} \
	%{gcl_flags} \
	%{sbcl_flags} \
	%{ecl_flags} \
	--with-default-lisp=%{defaultlisp} \
  	--enable-lang-de-utf8 \
  	--enable-lang-es-utf8 \
	--enable-lang-pt-utf8 \
	--enable-lang-pt_BR-utf8

make

(cd doc/info
texi2dvi -p -t @afourpaper -t @finalout maxima.texi
)

%if %{sagemath}
# from sagemath ecl spkg
pushd src
    mkdir ./lisp-cache
    ecl  \
	-eval '(require `asdf)' \
	-eval '(setf asdf::*user-cache* (truename "./lisp-cache"))' \
	-eval '(load "maxima-build.lisp")' \
	-eval '(asdf:make-build :maxima :type :fasl :move-here ".")' \
	-eval '(quit)' 
popd
%endif

%check
make check

%install
rm -rf %{buildroot}
%makeinstall install-info
rm -f %{buildroot}%{_infodir}/dir

# set executable rights for example scripts
chmod +x %{buildroot}%{_datadir}/%{name}/%{version}/doc/misc/grepforvariables.sh
chmod +x %{buildroot}%{_datadir}/%{name}/%{version}/doc/misc/processlisfiles.sh
chmod +x %{buildroot}%{_datadir}/%{name}/%{version}/share/contrib/lurkmathml/mathmltest

%if %{sagemath}
mkdir -p %{buildroot}%{ecllib}
install -m755 src/maxima.fasb %{buildroot}%{ecllib}/maxima.fas
%endif

# menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Maxima
Comment=Tcl/Tk interface to Maxima
Exec=%{_bindir}/xmaxima
Icon=%{name}
Terminal=false
Type=Application
Categories=Science;Math;
EOF

# icons
mkdir -p %{buildroot}%{_iconsdir}
tar xjf %{SOURCE1} -C %{buildroot}%{_iconsdir}

# don't compress info pages
export EXCLUDE_FROM_COMPRESS=info

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README README.lisps
%doc doc/info/maxima.pdf
%{_bindir}/maxima
%{_libdir}/maxima/%{version}/mgnuplot
%{_datadir}/maxima/%{version}/*
%{_infodir}/*.info*
%{_infodir}/maxima-index.lisp*
%{_mandir}/man1/maxima.*
%exclude %doc %{_datadir}/maxima/%{version}/doc/html/es.utf8
%exclude %{_infodir}/es.utf8
%exclude %doc %{_datadir}/maxima/%{version}/doc/html/pt.utf8
%exclude %{_infodir}/pt.utf8
%exclude %doc %{_datadir}/maxima/%{version}/doc/html/pt_BR.utf8
%exclude %{_infodir}/pt_BR.utf8
