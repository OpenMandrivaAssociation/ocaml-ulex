%define up_name	ulex
%define name	ocaml-%{up_name}
%define version	1.1
%define release	%mkrel 3

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


%changelog
* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-3mdv2010.0
+ Revision: 389930
- rebuild

* Mon Dec 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-2mdv2009.1
+ Revision: 320721
- move non-devel files into main package
- site-lib hierarchy doesn't exist anymore

* Thu Aug 14 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-1mdv2009.0
+ Revision: 272043
- update to new version 1.1

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2009.0
+ Revision: 254376
- rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-3mdv2008.1
+ Revision: 178370
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-2mdv2008.0
+ Revision: 77681
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage

* Thu Jun 07 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.0-1mdv2008.0
+ Revision: 36883
- new release: 1.0
- regenerate P0


* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-2mdv2007.0
+ Revision: 122748
- also build native version

* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-1mdv2007.1
+ Revision: 122718
- fix build dependencies

* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.9-1mdv2007.1
- first mdv release

