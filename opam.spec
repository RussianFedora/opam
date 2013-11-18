Name:           opam
Version:        1.1.0
Release:        1%{?dist}
Summary:        A package manager for OCaml

License:        LGPLv3
URL:            http://opam.ocamlpro.com/
Source0:        http://www.ocamlpro.com/pub/%{name}-full-%{version}.tar.gz

BuildRequires:  ocaml-camlp4-devel


%description
OPAM is a source-based package manager for OCaml. It supports multiple
simultaneous compiler installations, flexible package constraints, and
a Git-friendly development workflow.

%prep
%setup -q -n %{name}-full-%{version}


%build
%configure
make


%install
%make_install


%files
%doc AUTHORS CHANGES README.md CHANGES CONTRIBUTING LICENSE
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*

%changelog
* Mon Nov 18 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.1.0-1
- Update to 1.1.0

* Tue Oct 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.0.0-2
- Correct files section

* Tue Oct 01 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.0.0-1
- Initial release