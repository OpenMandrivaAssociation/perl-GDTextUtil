%define	module	GDTextUtil
%define name	perl-%{module}
%define version 0.86
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Text utilities for use with GD 
License:	GPL or Artistic
Group:		Development/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/MV/MVERB/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl-GD >= 1.20
Obsoletes:	perl-GD-TextUtil
Provides:	perl-GD-TextUtil
BuildArch:	noarch

%description
This module provides a font-independent way of dealing with text in GD, for use
with the GD::Text::* modules and GD::Graph.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot} 
%makeinstall_std

%clean 
rm -rf %{buildroot} 

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/GD
%{_mandir}/*/*


