%define up_name	ulex
%define name	ocaml-%{up_name}
%define version	1.1
%define release	%mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A lexer generator for Unicode and OCaml
Source0:	http://www.cduce.org/download/%{up_name}-%{version}.tar.bz2
Patch0:		ocaml-ulex-1.0.install_flags.patch
URL:		http://www.cduce.org/
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:	mysql-devel
BuildRequires:  ocaml-findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
ulex is a lexer generator for Unicode and OCaml written by Alain Frisch.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}
%patch0 -p1 -b .install_flags

%build
make all all.opt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install OCAMLFIND_DESTDIR="%{buildroot}/%{_libdir}/ocaml"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README LICENSE
%dir %{_libdir}/ocaml/ulex
%{_libdir}/ocaml/ulex/*.cmi
%{_libdir}/ocaml/ulex/*.cma
%{_libdir}/ocaml/ulex/META

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/ulex/*.a
%{_libdir}/ocaml/ulex/*.cmx
%{_libdir}/ocaml/ulex/*.cmxa
%{_libdir}/ocaml/ulex/*.mli
