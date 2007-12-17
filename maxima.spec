%define enable_clisp	1
%define enable_cmucl	0
%define enable_gcl	1
%define defaultlisp	gcl

%ifarch x86_64
%define enable_clisp	0
%endif

%if %enable_clisp
%define clisp_flags	--enable-clisp
%else
%define clisp_flags	--disable-clisp
%endif

%if %enable_cmucl
%define cmucl_flags	--enable-cmucl
%else
%define cmucl_flags	--disable-cmucl
%endif

%if %enable_gcl
%define gcl_flags	--enable-gcl
%else
%define gcl_flags	--disable-gcl
%endif

Summary:	Maxima Symbolic Computation Program
Name: 		maxima
Version: 	5.13.0
Release: 	%mkrel 4
License: 	GPL+
Group: 		Sciences/Mathematics
URL: 		http://maxima.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/maxima/%{name}-%{version}.tar.gz
Source1:	icons-%{name}.tar.bz2
Patch0:		maxima-5.13.0-xdg-utils.patch
BuildRequires:	texinfo
BuildRequires:	tetex
Requires: 	tk
Requires:       tcl
Requires:	maxima-runtime
Requires:	gnuplot
%if %{enable_clisp}
BuildRequires:	clisp
%endif
%if %{enable_cmucl}
BuildRequires:	cmucl
%endif
%if %{enable_gcl}
BuildRequires:	gcl >= 2.5.3
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
%{_libdir}/maxima/%{version}/binary-clisp/*
%endif

#--------------------------------------------------------------------

%if %{enable_cmucl}
%package runtime-cmucl
Summary: Maxima compiled with CMUCL
Group: Sciences/Mathematics
Requires:	cmucl
Requires:	maxima = %{version}-%{release}
Provides:	maxima-runtime = %{version}-%{release}
%description runtime-cmucl
Maxima compiled with CMUCL.


%files runtime-cmucl
%defattr(-,root,root)
%{_libdir}/maxima/%{version}/binary-cmucl/*
%endif

#--------------------------------------------------------------------

%if %{enable_gcl}
%package runtime-gcl
Summary: Maxima compiled with GCL
Group: 		Sciences/Mathematics
Requires:	maxima = %{version}-%{release}
Provides:	maxima-runtime = %{version}-%{release}
%description runtime-gcl
Maxima compiled with Gnu Common Lisp.

%files runtime-gcl
%defattr(-,root,root)
%{_bindir}/rmaxima
%{_libdir}/maxima/%{version}/binary-gcl/*
%endif

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1 -b .xdg

%build
export GCL_ANSI=y
CFLAGS="%optflags -fno-fast-math" \
CXXFLAGS="%optflags -fno-fast-math" \
%configure2_5x \
	%{clisp_flags} \
	%{gcl_flags} \
	%{cmucl_flags} \
	--with-default-lisp=%{defaultlisp}

make
make check

(cd doc/info
texi2dvi -p -t @afourpaper -t @finalout maxima.texi
)

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

# menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
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
mkdir -p $RPM_BUILD_ROOT%{_iconsdir}
tar xjf %{SOURCE1} -C $RPM_BUILD_ROOT%{_iconsdir}

# don't compress info pages
export EXCLUDE_FROM_COMPRESS=info

%post
%_install_info maxima.info
%update_icon_cache hicolor

%postun
%_remove_install_info maxima.info
%clean_icon_cache hicolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README README.lisps
#%doc doc/info/maxima.pdf
%{_bindir}/maxima
%{_libdir}/maxima/%{version}/mgnuplot
%{_datadir}/maxima/%{version}/*
%{_infodir}/*.info*
%{_infodir}/maxima-index.lisp
%{_mandir}/man1/maxima.*

