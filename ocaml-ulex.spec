%define up_name	ulex
%define name	ocaml-%{up_name}
%define version	1.1
%define release	%mkrel 1

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
BuildRequires:  findlib
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
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README LICENSE
%dir %{ocaml_sitelib}/ulex
%{ocaml_sitelib}/ulex/*.cmi

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/ulex/*
%exclude %{ocaml_sitelib}/ulex/*.cmi
