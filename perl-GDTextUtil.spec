%define	modname	GDTextUtil
%define modver	0.86

Summary:	Text utilities for use with GD 
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	8
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:	http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/%{modname}-%{modver}.tar.bz2
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl-GD >= 1.20
Provides:	perl-GD-TextUtil = %{version}-%{release}

%description
This module provides a font-independent way of dealing with text in GD, for use
with the GD::Text::* modules and GD::Graph.

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*

