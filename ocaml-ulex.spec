%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define up_name ulex

Summary:	A lexer generator for Unicode and OCaml
Name:		ocaml-%{up_name}
Version:	1.1
Release:	6
License:	MIT
Group:		Development/Other
Url:		http://www.cduce.org/
Source0:	http://www.cduce.org/download/%{up_name}-%{version}.tar.bz2
Patch0:		ocaml-ulex-1.0.install_flags.patch
BuildRequires:	camlp4
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	mysql-devel

%description
ulex is a lexer generator for Unicode and OCaml written by Alain Frisch.

%files
%doc CHANGES README LICENSE
%dir %{_libdir}/ocaml/ulex
%{_libdir}/ocaml/ulex/*.cmi
%{_libdir}/ocaml/ulex/*.cma
%{_libdir}/ocaml/ulex/META

#----------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{EVRD}

%description devel
This package contains the development files needed to build applications
using %{name}.

%files devel
%{_libdir}/ocaml/ulex/*.a
%{_libdir}/ocaml/ulex/*.cmx
%{_libdir}/ocaml/ulex/*.cmxa
%{_libdir}/ocaml/ulex/*.mli

#----------------------------------------------------------------------------

%prep
%setup -q -n %{up_name}-%{version}
%patch0 -p1 -b .install_flags

%build
make all all.opt

%install
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install OCAMLFIND_DESTDIR="%{buildroot}/%{_libdir}/ocaml"

