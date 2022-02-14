%define _enable_debug_packages	%{nil}
%define debug_package	%{nil}
# maxima doesnt like the info pages compressed
%define dont_compress 1

%define emacs_sitelisp	%{_datadir}/emacs/site-lisp/
%define texmf			%{_datadir}/texmf

%bcond_with	_pdfdoc
%bcond_with	_tests

# FIXME: most of lips compiler are actually broken
# so I disabled them and I used clist as default
%bcond_without	clisp
%bcond_with	gcl
%bcond_with	sbcl
%bcond_with	ecl
#define defaultlisp	ecl
%define defaultlisp	clisp

%define clisp_flags	--%{?with_clisp:en}%{!?with_clisp:dis}able-clisp
%define gcl_flags	--%{?with_gcl:en}%{!?with_gcl:dis}able-gcl
%define sbcl_flags	--%{?with_sbcl:en}%{!?with_sbcl:dis}able-sbcl
%define ecl_flags	--%{?with_ecl:en}%{!?with_ecl:dis}able-ecl

# build module required by sagemath runtime?
%define sagemath	%{?with_ecl:1}%{!?with_ecl:0}
%if %{with ecl}
%define ecllib		%(ecl -eval "(princ (SI:GET-LIBRARY-PATHNAME))" -eval "(quit)")
%endif

Summary:	Maxima Symbolic Computation Program
Name:		maxima
Version:	5.45.1
Release:	1
License:	GPLv2
Group:		Sciences/Mathematics
URL:		http://maxima.sourceforge.net
Source0:	http://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
#Source1:	maxima.png
#Source2:	xmaxima.desktop
Source6:	maxima-modes.el
## Other maxima reference docs
#Source10:	http://starship.python.net/crew/mike/TixMaxima/macref.pdf
Source11:	http://maxima.sourceforge.net/docs/maximabook/maximabook-19-Sept-2004.pdf
## upstreamable patches
# https://bugzilla.redhat.com/show_bug.cgi?id=837142
# https://sourceforge.net/tracker/?func=detail&aid=3539587&group_id=4933&atid=104933
Patch50: maxima-5.37.1-clisp-noreadline.patch
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
%if %{with clisp}
BuildRequires:	clisp
%endif
%if %{with gcl}
BuildRequires:	gcl > 2.5.3
%endif
%if %{with sbcl}
BuildRequires:	sbcl = %{sbcl_version}
%endif
%if %{with ecl}
BuildRequires:	ecl
BuildRequires:	ffi-devel
%endif
Requires:	gnuplot
Requires:	%{name}-runtime
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

%files
%doc AUTHORS COPYING README README-lisps.md
%{_bindir}/%{name}
%{_bindir}/r%{name}
%{_libexecdir}/%{name}/%{version}/mgnuplot
%{_datadir}/bash-completion/completions/*%{name}
%{_datadir}/mime/packages/x-mac.xml
%{_datadir}/mime/packages/x-%{name}-out.xml
%{_datadir}/%{name}/%{version}/*
%exclude %doc %{_datadir}/%{name}/%{version}/doc/html/{es,de,pt,pt_BR}.utf8
%exclude %{_infodir}/{es,de,pt,pt_BR}.utf8
%{_infodir}/*.info*
%{_infodir}/%{name}-index.lisp*
%{_mandir}/man1/%{name}.*
%{_mandir}/{de,ru}/man1/%{name}.*
%{texmf}/tex/latex/e%{name}
%{emacs_sitelisp}/%{name}
%{emacs_sitelisp}/site-start.d/*

#--------------------------------------------------------------------

%package gui
Summary: Tcl/Tk GUI interface to Maxima
Group:		Sciences/Mathematics
Requires:	%{name}
Requires:	tk
Provides:	%{name} = %{version}-%{release}
%description gui
Tcl/Tk GUI interface to Maxima.

%files gui
%{_bindir}/x%{name}
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*%{name}*
%{_iconsdir}/hicolor/*/apps/*.png

#--------------------------------------------------------------------

%if %{with clisp}
%package runtime-clisp
Summary: Maxima compiled with clisp
Group: Sciences/Mathematics
Requires:	clisp
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-runtime = %{version}-%{release}
%description runtime-clisp
Maxima compiled with clisp.

%files runtime-clisp
%dir %{_libdir}/%{name}/%{version}/binary-clisp
%{_libdir}/maxima/%{version}/binary-clisp/*
%endif

#--------------------------------------------------------------------

%if %{with gcl}
%package runtime-gcl
Summary: Maxima compiled with GCL
Group:		Sciences/Mathematics
Requires:	%{name} = %{version}-%{release}
Suggests:	rlwrap
Provides:	%{name}-runtime = %{version}-%{release}
%description runtime-gcl
Maxima compiled with Gnu Common Lisp.

%files runtime-gcl
%dir %{_libdir}/%{name}/%{version}/binary-gcl
%{_libdir}/%{name}/%{version}/binary-gcl/*
%endif

#--------------------------------------------------------------------

%if %{with sbcl}
%package runtime-sbcl
Summary: Maxima compiled with SBCL
Group: Sciences/Mathematics
Requires:	sbcl = %{sbcl_version}
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-runtime = %{version}-%{release}

%description runtime-sbcl
Maxima compiled with SBCL.

%files runtime-sbcl
%dir %{_libdir}/%{name}/%{version}/binary-sbcl
%{_libdir}/%{name}/%{version}/binary-sbcl/*
%endif

#--------------------------------------------------------------------

%if %{with ecl}
%package runtime-ecl
Summary: Maxima compiled with ECL
Group: Sciences/Mathematics
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-runtime = %{version}-%{release}

%description runtime-ecl
Maxima compiled with ECL.

%files runtime-ecl
%dir %{_libdir}/%{name}/%{version}/binary-ecl
%{_libdir}/%{name}/%{version}/binary-ecl/*
%{ecllib}/%{name}.fas
%endif

#--------------------------------------------------------------------

%package lang-de-utf8
Summary:	Maxima German UTF-8 language pack
Group:		Sciences/Mathematics
Requires:	%{name} = %{version}

%description lang-de-utf8
Maxima German language support (UTF-8).

%files lang-de-utf8
%doc %{_datadir}/%{name}/%{version}/doc/html/de.utf8
%{_infodir}/de.utf8

#--------------------------------------------------------------------

%package lang-es-utf8
Summary:	Maxima Spanish UTF-8 language pack
Group:		Sciences/Mathematics
Requires:	%{name} = %{version}

%description lang-es-utf8
Maxima Spanish language support (UTF-8).

%files lang-es-utf8
%doc %{_datadir}/%{name}/%{version}/doc/html/es.utf8
%{_infodir}/es.utf8

#--------------------------------------------------------------------

%package lang-pt-utf8
Summary:	Maxima Portuguese UTF-8 language pack
Group:		Sciences/Mathematics
Requires:	%{name} = %{version}

%description lang-pt-utf8
Maxima Portuguese language support (UTF-8).

%files lang-pt-utf8
%doc %{_datadir}/%{name}/%{version}/doc/html/pt.utf8
%{_infodir}/pt.utf8

#--------------------------------------------------------------------

%package lang-pt_BR-utf8
Summary:	Maxima Brazilian Portuguese UTF-8 language pack
Group:		Sciences/Mathematics
Requires:	%{name} = %{version}

%description lang-pt_BR-utf8
Maxima Brazilian Portuguese language support (UTF-8).

%files lang-pt_BR-utf8
%doc %{_datadir}/%{name}/%{version}/doc/html/pt_BR.utf8
%{_infodir}/pt_BR.utf8

#--------------------------------------------------------------------

%prep
%autosetup -p1

%build
#export PYTHON=%{__python3}
%if %{with gcl}
export GCL_ANSI=y
%endif
%if %{with sbcl}
export SBCL_HOME=%{_libdir}/sbcl
%endif
export CFLAGS="%{optflags} -fno-fast-math"
export CXXFLAGS="%{optflags} -fno-fast-math"

%configure \
	--with-emacs-prefix=%{_datadir}/%{name}/%{version}/emacs \
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

# makes tests run
touch tests/test.sh.in

%make_build

%if %{with _pdfdoc}
make -C doc/info pdf
%endif

%install
%make_install
# DESTDIR=%{buildroot}

%if %{with ecl}
install -D -m755 src/binary-ecl/maxima.fas %{buildroot}%{ecllib}/maxima.fas
%endif

# icons
for d in 16 32 48 64 72 128 256
do
	install -dm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	rsvg-convert -f png -h ${d} -w ${d} interfaces/xmaxima/net.sourceforge.maxima.svg \
			-o %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -size 32x32 interfaces/xmaxima/net.sourceforge.maxima.svg \
	%{buildroot}%{_datadir}/pixmaps/%{name}.xpm
#install -p -D -m644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.png

# .desktop
install -dm 0755 %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/openmandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Maxima
Comment=Tcl/Tk interface to Maxima
Exec=%{_bindir}/x%{name}
Icon=%{name}
#MimeType=
Type=Application
StartupNotify=false
Categories=Education;Science;Math;
EOF

# emacs
install -d -m 0755 %{buildroot}%{emacs_sitelisp}/{,site-start.d}
ln -s %{_datadir}/%{name}/%{version}/emacs %{buildroot}%{emacs_sitelisp}/%{name}
for file in %{buildroot}%{_datadir}/%{name}/%{version}/emacs/*.el
do
	touch `dirname $file`/`basename $file .el`.elc
done
install -D -m644 -p %{SOURCE6} %{buildroot}%{emacs_sitelisp}/site-start.d/
touch %{buildroot}%{emacs_sitelisp}/site-start.d/maxima-modes.elc

# emaxima LaTeX style (%ghost)
install -d %{buildroot}%{texmf}/tex/latex/
ln -sf  %{_datadir}/%{name}/%{version}/emacs %{buildroot}%{texmf}/tex/latex/e%{name}

# docs
#install -dm 0755 %{buildroot}%{_docdir}	
#rm -rf %{buildroot}%{_datadir}/%{name}/%{version}/doc/{contributors,implementation,misc,maximabook,EMaximaIntro.ps}
install -pm 0644 %{SOURCE10} %{buildroot}%{_docdir}%{buildroot}%{_docdir}/%{name}
install -pm 0644 %{SOURCE11} %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/%{version}/doc/EMaximaIntro.ps %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_datadir}/%{name}/%{version}/doc/{contributors,implementation}

# locales
%find_lang %{name} --with-man

%if %{with _tests}
%check
make -k check ||:
%endif

