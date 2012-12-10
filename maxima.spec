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
%define sbcl_version	1.1.2
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
Release:	3
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
BuildRequires:	texlive-epsf
BuildRequires:	texlive-ec
BuildRequires:	texlive-cm-super
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
#%{_bindir}/rmaxima
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
autoreconf -fi

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
%{_bindir}/rmaxima
%{_libdir}/maxima/%{version}/mgnuplot
%{_datadir}/maxima/%{version}/*
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


%changelog
* Fri Aug 03 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 5.27.0-1mdv2012.0
+ Revision: 811666
- update to 5.27.0

* Sat Jan 28 2012 Paulo Andrade <pcpa@mandriva.com.br> 5.24.0-4
+ Revision: 769489
- Remove maxima and maxima-runtime-gcl conflict.

* Fri Aug 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.24.0-3
+ Revision: 697243
- Add extra logic to build maxima as an ecl module for sagemath
- Correct wrong install/remove info macros
- Do not list localized documentation in multiple packages
- Rebuild with correct sbcl version requirement
- Add new localization packages
- Update to maxima 5.24.0

* Wed Feb 02 2011 Paulo Andrade <pcpa@mandriva.com.br> 5.23.0-1
+ Revision: 635334
- Require explicit sbcl version
- Remove cmucl backend conditional generation
- Enable all lisp backends
- Add back the clisp-noreadline patch to disable readline when running under sagemath

  + Александр Казанцев <kazancas@mandriva.org>
    - new release 5.23.0

* Fri Dec 17 2010 Александр Казанцев <kazancas@mandriva.org> 5.22.1-3mdv2011.0
+ Revision: 622594
- set clisp default due non-latin enviroment error

* Sun Aug 22 2010 Paulo Andrade <pcpa@mandriva.com.br> 5.22.1-2mdv2011.0
+ Revision: 572046
- Update to version 5.22.1
- Update to version 5.22.0

* Mon Apr 19 2010 Frederik Himpe <fhimpe@mandriva.org> 5.20.1-8mdv2010.1
+ Revision: 536862
- Rebuild for new sbcl

* Wed Mar 03 2010 Frederik Himpe <fhimpe@mandriva.org> 5.20.1-7mdv2010.1
+ Revision: 514006
- Rebuild for new sbcl

* Tue Mar 02 2010 Paulo Andrade <pcpa@mandriva.com.br> 5.20.1-6mdv2010.1
+ Revision: 513704
- Enable ecl as a maxima lisp backend
- Add ecl to list of maxima runtime lisps
- Make runtimes owners of it's directories

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 5.20.1-5mdv2010.1
+ Revision: 503752
- rebuild

* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 5.20.1-4mdv2010.1
+ Revision: 503636
- rebuild for new gmp

* Fri Feb 05 2010 Frederik Himpe <fhimpe@mandriva.org> 5.20.1-3mdv2010.1
+ Revision: 501269
- Rebuild for new SBCL

* Fri Jan 01 2010 Frederik Himpe <fhimpe@mandriva.org> 5.20.1-2mdv2010.1
+ Revision: 484902
- Rebuild for new sbcl

* Wed Dec 16 2009 Frederik Himpe <fhimpe@mandriva.org> 5.20.1-1mdv2010.1
+ Revision: 479588
- update to new version 5.20.1

* Wed Nov 25 2009 Frederik Himpe <fhimpe@mandriva.org> 5.19.2-3mdv2010.1
+ Revision: 470125
- Fix summary of sbcl subpackage
- Rebuild for new gcl and binutils (libfd)

* Wed Nov 11 2009 Frederik Himpe <fhimpe@mandriva.org> 5.19.2-2mdv2010.1
+ Revision: 464397
- Rebuild for new sbcl and gcl

* Sun Sep 13 2009 Frederik Himpe <fhimpe@mandriva.org> 5.19.2-1mdv2010.0
+ Revision: 439030
- update to new version 5.19.2

* Sun Aug 30 2009 Frederik Himpe <fhimpe@mandriva.org> 5.19.1-2mdv2010.0
+ Revision: 422449
- Rebuild for new sbcl

* Thu Aug 27 2009 Frederik Himpe <fhimpe@mandriva.org> 5.19.1-1mdv2010.0
+ Revision: 421784
- Update to new version 5.19.1
- Rediff noreadline patch

* Wed Aug 19 2009 Paulo Andrade <pcpa@mandriva.com.br> 5.18.1-3mdv2010.0
+ Revision: 418334
- Pass -I option to clisp if --disable-readline option is used
- Rebuild with newer clisp and gcl

* Wed Jul 29 2009 Frederik Himpe <fhimpe@mandriva.org> 5.18.1-2mdv2010.0
+ Revision: 404436
- Rebuild for new sbcl and clisp

* Thu Jun 04 2009 Frederik Himpe <fhimpe@mandriva.org> 5.18.1-1mdv2010.0
+ Revision: 382883
- Update to new version 5.18.1

* Wed Mar 11 2009 Frederik Himpe <fhimpe@mandriva.org> 5.17.1-4mdv2009.1
+ Revision: 353928
- Rebuild for new sbcl

* Thu Mar 05 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.17.1-3mdv2009.1
+ Revision: 349355
- rebuild again to really link against new readline

* Sat Feb 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 5.17.1-2mdv2009.1
+ Revision: 346035
- rebuild against new readline

* Fri Feb 06 2009 Frederik Himpe <fhimpe@mandriva.org> 5.17.1-1mdv2009.1
+ Revision: 338272
- update to new version 5.17.1

* Thu Feb 05 2009 Frederik Himpe <fhimpe@mandriva.org> 5.17.0-3mdv2009.1
+ Revision: 337978
- Rebuild for new sbcl

* Mon Jan 05 2009 Frederik Himpe <fhimpe@mandriva.org> 5.17.0-2mdv2009.1
+ Revision: 325124
- Rebuild for new sbcl

* Sat Dec 06 2008 Frederik Himpe <fhimpe@mandriva.org> 5.17.0-1mdv2009.1
+ Revision: 310920
- Update to new version 5.17.0

* Fri Oct 31 2008 Frederik Himpe <fhimpe@mandriva.org> 5.16.3-4mdv2009.1
+ Revision: 299064
- Rebuild for new sbcl

* Mon Oct 13 2008 Funda Wang <fwang@mandriva.org> 5.16.3-2mdv2009.1
+ Revision: 293066
- hardcode sbcl version (bug#44840)

* Mon Sep 01 2008 Frederik Himpe <fhimpe@mandriva.org> 5.16.3-2mdv2009.0
+ Revision: 278719
- Build SBCL runtime and set it as default, like upstream recommends
  (http://maxima.sourceforge.net/wiki/index.php/Lisp)
- Build clisp runtime on x86_64 again, it works now
- Don't package ChangeLog (outdated) and INSTALL

* Sat Aug 30 2008 Frederik Himpe <fhimpe@mandriva.org> 5.16.3-1mdv2009.0
+ Revision: 277600
- Update to new version 5.16.3
- Fix license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Adam Williamson <awilliamson@mandriva.org>
    - reduce tk and tcl to suggests rather than requires (#39518, Michael Koren)

* Sat May 03 2008 Funda Wang <fwang@mandriva.org> 5.15.0-1mdv2009.0
+ Revision: 200604
- drop unused patch
- New version 5.15.0

  + Giuseppe Ghibò <ghibo@mandriva.com>
    - Fix docs for grobner contrib.

* Fri Apr 25 2008 Giuseppe Ghibò <ghibo@mandriva.com> 5.14.0-2mdv2009.0
+ Revision: 197362
- Added tetex-latex, tetex-dvips and python to BuildRequires.
- Added Patch1, Patch2 to fix documentation.
- Fixed docs.

* Sat Apr 19 2008 Giuseppe Ghibò <ghibo@mandriva.com> 5.14.0-1mdv2009.0
+ Revision: 195775
- Release 5.14.0.

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Mon Jan 28 2008 Adam Williamson <awilliamson@mandriva.org> 5.13.0-5mdv2008.1
+ Revision: 158937
- runtime-gcl suggests rlwrap (Fred Himpe, #36035)

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Sep 24 2007 Adam Williamson <awilliamson@mandriva.org> 5.13.0-4mdv2008.0
+ Revision: 92661
- correct binary name in menu entry (launch xmaxima, the graphical front end, not maxima, the console one: bug #33930)

* Fri Sep 21 2007 Adam Williamson <awilliamson@mandriva.org> 5.13.0-3mdv2008.0
+ Revision: 92040
- no longer requires gv due to patch
- add maxima-5.13.0-xdg-utils.patch to use xdg-open instead of specific binaries (from Gentoo, MDV bug #33867)

* Wed Sep 05 2007 Adam Williamson <awilliamson@mandriva.org> 5.13.0-2mdv2008.0
+ Revision: 80500
- reduce menu categories as per frederik

* Tue Sep 04 2007 Adam Williamson <awilliamson@mandriva.org> 5.13.0-1mdv2008.0
+ Revision: 79401
- add more menu categories
- slightly rearrange spec
- regenerate icons-maxima.tar.bz2 to use fd.o icon naming scheme
- use Fedora license policy (GPL+)
- new release 5.13.0

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Sun May 27 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 5.12.0-2mdv2008.0
+ Revision: 31828
- Rebuild against new Maxima

* Tue May 08 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 5.12.0-1mdv2008.0
+ Revision: 25348
- New version


* Fri Jan 05 2007 Nicolas Lécureuil <neoclust@mandriva.org> 5.11.0-2mdv2007.0
+ Revision: 104538
- Rediff Patch0

* Fri Jan 05 2007 Nicolas Lécureuil <neoclust@mandriva.org> 5.11.0-1mdv2007.1
+ Revision: 104408
- New version  5.11.0
- Add Menu entry
- Import maxima

* Wed Apr 12 2006 Giuseppe Ghib� <ghibo@mandriva.com> 5.9.3-1mdk
- Release 5.9.3.

* Mon Nov 07 2005 Giuseppe Ghib� <ghibo@mandriva.com> 5.9.2-1mdk
- Release 5.9.2.
- Rebuilt Patch0.

* Thu Aug 04 2005 Giuseppe Ghib� <ghibo@mandriva.com> 5.9.1-5mdk
- Rebuilt against gcl 2.6.7-0.cvs20050803 and gcc 4.0.1.

* Mon Apr 18 2005 Giuseppe Ghib� <ghibo@mandriva.com> 5.9.1-4mdk
- Don't use clisp for X86-64 for now (clisp failed to build
  under X86-64).

* Thu Feb 17 2005 Giuseppe Ghib� <ghibo@mandrakesoft.com> 5.9.1-3mdk
- Added gv in Requires.

* Wed Feb 16 2005 Giuseppe Ghib� <ghibo@mandrakesoft.com> 5.9.1-2mdk
- Added Patch0 (use gv instead of ghostview).

* Wed Feb 16 2005 Giuseppe Ghib� <ghibo@mandrakesoft.com> 5.9.1-1mdk
- Release: 5.9.1.

* Wed Mar 24 2004 Giuseppe Ghib� <ghibo@mandrakesoft.com> 5.9.0-6mdk
- Fixed typo in menu entry.

