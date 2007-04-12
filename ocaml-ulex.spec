%define up_name	ulex
%define name	ocaml-%{up_name}
%define version	0.9
%define release	%mkrel 2
%define ocaml_sitelib %(if [ -x /usr/bin/ocamlc ]; then ocamlc -where;fi)/site-lib

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A lexer generator for Unicode and OCaml
Source: 	http://www.cduce.org/download/%{up_name}-%{version}.tar.bz2
Patch:      %{name}-0.9.install_flags.patch
URL:		http://www.cduce.org/
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:	mysql-devel
BuildRequires:  findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
ulex is a lexer generator for Unicode and OCaml written by Alain Frisch.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q -n %{up_name}-%{version}
%patch -p 1

%build
%make all all.opt

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"

%clean
rm -rf %{buildroot}

%files devel
%defattr(-,root,root)
%doc CHANGES README LICENSE
%{ocaml_sitelib}/ulex


