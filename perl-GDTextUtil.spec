%define	upstream_name	 GDTextUtil
%define upstream_version 0.86

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Text utilities for use with GD 
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl-GD >= 1.20
BuildArch:	noarch
Provides:	perl-GD-TextUtil = %{version}-%{release}

%description
This module provides a font-independent way of dealing with text in GD, for use
with the GD::Text::* modules and GD::Graph.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/GD
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.860.0-4mdv2012.0
+ Revision: 765282
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.860.0-3
+ Revision: 763775
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.860.0-2
+ Revision: 667169
- mass rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.860.0-1mdv2010.1
+ Revision: 403187
- rebuild using %%perl_convert_version

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.86-4mdv2009.0
+ Revision: 223767
- rebuild

* Thu Mar 06 2008 Oden Eriksson <oeriksson@mandriva.com> 0.86-3mdv2008.1
+ Revision: 180403
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Jan 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.86-2mdv2007.0
+ Revision: 107910
- rebuild
- Import perl-GDTextUtil

* Wed Nov 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.86-1mdk
- new version
- spec cleanup
- %%mkrel
- fix directory ownership
- rpmbuilupdate aware
- better summary
- better description
- fixed name

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.83-10mdk
- fix deps

