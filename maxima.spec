%define _enable_debug_packages	%{nil}
%define debug_package	%{nil}
# maxima doesnt like the info pages compressed
%define dont_compress 1

%define enable_clisp	1
%define enable_gcl	1
%define enable_sbcl	1
%define enable_ecl	1
%define defaultlisp	sbcl

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
%define sbcl_version	1.1.3
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

%define emacs_sitelisp	%{_datadir}/emacs/site-lisp/
%define xemacs_sitelisp	%{_datadir}/xemacs/site-packages/lisp/
%define texmf		%{_datadir}/texmf

Summary:	Maxima Symbolic Computation Program
Name:		maxima
Version:	5.30.0
Release:	4
License:	GPLv2
Group:		Sciences/Mathematics
URL:		http://maxima.sourceforge.net
Source0:	http://downloads.sourceforge.net/sourceforge/maxima/maxima-%{version}.tar.gz
Source1:	maxima.png
Source2:	xmaxima.desktop
Source6:	maxima-modes.el

## Other maxima reference docs
Source10:	http://starship.python.net/crew/mike/TixMaxima/macref.pdf
Source11:	http://maxima.sourceforge.net/docs/maximabook/maximabook-19-Sept-2004.pdf

## upstreamable patches
# https://bugzilla.redhat.com/show_bug.cgi?id=837142
# https://sourceforge.net/tracker/?func=detail&aid=3539587&group_id=4933&atid=104933
Patch50: maxima-5.28.0-clisp-noreadline.patch

# Build the fasl while building the executable to avoid double initialization
Patch51: maxima-5.30.0-build-fasl.patch

BuildRequires:	desktop-file-utils
BuildRequires:	texinfo
BuildRequires:	texlive-epsf
BuildRequires:	texlive-ec
BuildRequires:	texlive-cm-super
BuildRequires:	texlive
BuildRequires:	python
BuildRequires:	time
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
BuildRequires:	ffi-devel
%endif
Requires:	gnuplot
Requires:	maxima-runtime
Suggests:	tcl
Suggests:	tk

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
%{_bindir}/xmaxima
%{_datadir}/applications/*.desktop
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
%dir %{_libdir}/maxima/%{version}/binary-ecl
%{_libdir}/maxima/%{version}/binary-ecl/*
%{ecllib}/maxima.fas
%endif

#--------------------------------------------------------------------
%package lang-de-utf8
Summary:	Maxima German UTF-8 language pack
Group:		Sciences/Mathematics
Requires:	maxima = %{version}

%description lang-de-utf8
Maxima German language support (UTF-8).

%files lang-de-utf8
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
%doc %{_datadir}/maxima/%{version}/doc/html/pt_BR.utf8
%{_infodir}/pt_BR.utf8

#--------------------------------------------------------------------

%prep
%setup -q

%patch50 -p1 -b .clisp-noreadline
%patch51 -p1 -b .build-fasl

# Extra docs
install -p -m644 %{SOURCE10} .
install -D -p -m644 %{SOURCE11} doc/maximabook/maxima.pdf

sed -i -e 's|@ARCH@|%{_target_cpu}|' src/maxima.in

sed -i -e 's:/usr/local/info:/usr/share/info:' \
  interfaces/emacs/emaxima/maxima.el
sed -i -e \
  's/(defcustom\s+maxima-info-index-file\s+)(\S+)/$1\"maxima.info-16\"/' \
  interfaces/emacs/emaxima/maxima.el

# remove CVS crud
find -name CVS -type d | xargs --no-run-if-empty rm -rv

%build
autoreconf -fi

%if %{enable_gcl}
export GCL_ANSI=y
%endif
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
	--enable-lang-pt_BR-utf8 LDFLAGS=

# help avoid (re)running makeinfo/tex
touch doc/info/maxima.info

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%if %{?enable_ecl}
install -D -m755 src/binary-ecl/maxima.fas $RPM_BUILD_ROOT%{ecllib}/maxima.fas
%endif

# app icon
install -p -D -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/maxima.png

desktop-file-install \
  --dir="$RPM_BUILD_ROOT%{_datadir}/applications" \
  %{SOURCE2} 

# (x)emacs
install -D -m644 -p %{SOURCE6} $RPM_BUILD_ROOT%{_datadir}/maxima/%{version}/emacs/site_start.d/maxima-modes.el

for dir in %{emacs_sitelisp} %{xemacs_sitelisp} ; do
  install -d -m755 $RPM_BUILD_ROOT$dir/{,site-start.d}
  ln -s %{_datadir}/maxima/%{version}/emacs $RPM_BUILD_ROOT$dir/maxima
  for file in $RPM_BUILD_ROOT%{_datadir}/maxima/%{version}/emacs/*.el ; do
    touch `dirname $file`/`basename $file .el`.elc
  done
  ln -s %{_datadir}/maxima/%{version}/emacs/site_start.d/maxima-modes.el $RPM_BUILD_ROOT$dir/site-start.d/
  touch $RPM_BUILD_ROOT$dir/site-start.d/maxima-modes.elc
done

# emaxima LaTeX style (%ghost)
install -d $RPM_BUILD_ROOT%{texmf}/tex/latex/
ln -sf  %{_datadir}/maxima/%{version}/emacs \
        $RPM_BUILD_ROOT%{texmf}/tex/latex/emaxima

## unwanted/unpackaged files
rm -f $RPM_BUILD_ROOT%{_infodir}/dir
# docs
rm -rf $RPM_BUILD_ROOT%{_datadir}/maxima/%{version}/doc/{contributors,implementation,misc,maximabook,EMaximaIntro.ps}

%check
make -k check

%files
%doc AUTHORS COPYING README README.lisps
%{_bindir}/maxima
%{_bindir}/rmaxima
%{_datadir}/maxima/%{version}/*
/usr/libexec/maxima/5.30.0/mgnuplot
%{_infodir}/*.info*
%{_infodir}/maxima-index.lisp*
%{_mandir}/man1/maxima.*
%exclude %doc %{_datadir}/maxima/%{version}/doc/html/es.utf8
%exclude %{_infodir}/es.utf8
%exclude %doc %{_datadir}/maxima/%{version}/doc/html/de.utf8
%exclude %{_infodir}/de.utf8
%exclude %doc %{_datadir}/maxima/%{version}/doc/html/pt.utf8
%exclude %{_infodir}/pt.utf8
%exclude %doc %{_datadir}/maxima/%{version}/doc/html/pt_BR.utf8
%exclude %{_infodir}/pt_BR.utf8
%{texmf}/tex/latex/emaxima
%{emacs_sitelisp}/maxima
%{emacs_sitelisp}/site-start.d/*
%{xemacs_sitelisp}/maxima
%{xemacs_sitelisp}/site-start.d/*
