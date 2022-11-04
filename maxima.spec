%define debug_package  %{nil}

# maxima doesnt like the info pages compressed
%define dont_compress 1

%define emacs_sitelisp	%{_datadir}/emacs/site-lisp/
%define texmf			%{_datadir}/texmf

%bcond_with	_pdfdoc
%bcond_with	_tests

# FIXME: most of lips compiler are actually broken
# so I disabled them and I used clisp as default
%bcond_with		clisp
%bcond_with		gcl
%bcond_with		sbcl
%bcond_without	ecl
%define defaultlisp	ecl
#define defaultlisp	clisp

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
Version:	5.46.0
Release:	1
License:	GPLv2
Group:		Sciences/Mathematics
URL:		https://maxima.sourceforge.net
Source0:	https://downloads.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
Source6:	maxima-modes.el
## Other maxima reference docs
Source10:	http://starship.python.net/crew/mike/TixMaxima/macref.pdf
Source11:	https://maxima.sourceforge.net/docs/maximabook/maximabook-19-Sept-2004.pdf
## upstreamable patches
# https://bugzilla.redhat.com/show_bug.cgi?id=837142
# https://sourceforge.net/tracker/?func=detail&aid=3539587&group_id=4933&atid=104933
Patch50: maxima-5.37.1-clisp-noreadline.patch
# Build the fasl while building the executable to avoid double initialization
Patch51: maxima-5.46.0-build-fasl.patch

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
%doc macref.pdf maximabook-19-Sept-2004.pdf
%{_bindir}/%{name}
%{_bindir}/r%{name}
%{_libexecdir}/%{name}/%{version}/mgnuplot
%{_datadir}/bash-completion/completions/*%{name}
%{_datadir}/mime/packages/x-mac.xml
%{_datadir}/mime/packages/x-%{name}-out.xml
%{_datadir}/%{name}/%{version}/*
%exclude %doc %{_datadir}/%{name}/%{version}/doc/html/{de,es,ja,pt,pt_BR,ru}
#doc %lang(en) %{_datadir}/%{name}/%{version}/doc/html/*.h*
#doc %lang(en) %{_datadir}/%{name}/%{version}/doc/share/
%doc %{_docdir}/%{name}/EMaximaIntro.ps
%exclude %{_infodir}/{de,es,ja,pt,pt_BR,ru}
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
Requires:	%{name} = %{version}-%{release}
Requires:	tk
Provides:	x%{name} = %{version}-%{release}

%description gui
Tcl/Tk GUI interface to Maxima.

%files gui
%{_bindir}/x%{name}
%{_metainfodir}/*.appdata.xml
%{_datadir}/applications/*%{name}.desktop
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

%define lang_subpkg(c:l:) \
%define countrycode %{-c:%{-c*}}%{!-c:%{error:Country code not defined}} \
%define languageame %{-l:%{-l*}}%{!-l:%{error:Language name not defined}} \
\
%package lang-%{countrycode}\
Summary:	Maxima %{languageame} language pack\
BuildArch:	noarch\
Requires:	%{name} = %{version} \
Supplements:  %{name}\
\
%description lang-%{countrycode}\
Maxima %{languageame} language support.\
\
%files lang-%{countrycode}\
%doc %lang(%{countrycode}) %{_datadir}/%{name}/%{version}/doc/html/%{countrycode}/\
%lang(%{countrycode}) %{_infodir}/%{countrycode}

%lang_subpkg -c de		-l German
%lang_subpkg -c ja		-l Japanese
%lang_subpkg -c es		-l Spanish
%lang_subpkg -c pt		-l Portugese
%lang_subpkg -c pt_BR	-l Brazilian
%lang_subpkg -c ru		-l Russian

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
#export CFLAGS="%{optflags} -fno-fast-math"
#export CXXFLAGS="%{optflags} -fno-fast-math"

%configure \
	%{clisp_flags} \
	%{gcl_flags} \
	%{sbcl_flags} \
	%{ecl_flags} \
	%{?defaultlisp:--with-default-lisp=%{defaultlisp} } \
	--enable-lang-de \
	--enable-lang-ja \
	--enable-lang-es \
	--enable-lang-pt \
	--enable-lang-pt_BR \
	--enable-lang-ru \
	--with-emacs-prefix=%{_datadir}/%{name}/%{version}/emacs \
	%{nil}

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

%if %{with ecl}
install -Dpm 0755 src/binary-ecl/maxima.fas %{buildroot}%{ecllib}/maxima.fas
%endif

# icons
for d in 16 32 48 64 72 128 256
do
	install -dpm 0755 %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/
	rsvg-convert -f png -h ${d} -w ${d} interfaces/xmaxima/net.sourceforge.maxima.svg \
			-o %{buildroot}%{_iconsdir}/hicolor/${d}x${d}/apps/%{name}.png
done
install -dpm 0755 %{buildroot}%{_datadir}/pixmaps/
convert -size 32x32 interfaces/xmaxima/net.sourceforge.maxima.svg \
	%{buildroot}%{_datadir}/pixmaps/%{name}.xpm

# emacs
install -dpm 0755 %{buildroot}%{emacs_sitelisp}/site-start.d
ln -s %{_datadir}/%{name}/%{version}/emacs %{buildroot}%{emacs_sitelisp}/%{name}
for file in %{buildroot}%{_datadir}/%{name}/%{version}/emacs/*.el
do
	touch `dirname $file`/`basename $file .el`.elc
done
install -dpm 0755 %{buildroot}%{emacs_sitelisp}/site-start.d
install -pm 0644 %{SOURCE6} %{buildroot}%{emacs_sitelisp}/site-start.d/
touch %{buildroot}%{emacs_sitelisp}/site-start.d/maxima-modes.elc

# emaxima LaTeX style (%ghost)
install -dpm 0755 %{buildroot}%{texmf}/tex/latex/
ln -sf %{_datadir}/%{name}/%{version}/emacs %{buildroot}%{texmf}/tex/latex/e%{name}

# docs
install -dpm 0755 %{buildroot}%{_docdir}/%{name}/
install -pm 0644 %{SOURCE10} %{buildroot}%{_docdir}/%{name}
install -pm 0644 %{SOURCE11} %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/%{name}/%{version}/doc/EMaximaIntro.ps %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_datadir}/%{name}/%{version}/doc/{contributors,implementation}

# locales
%find_lang %{name} --with-man

%if %{with _tests}
%check
make -k check ||:
%endif

