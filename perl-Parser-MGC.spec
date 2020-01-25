#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Parser
%define		pnam	MGC
Summary:	Parser::MGC - build simple recursive-descent parsers
Name:		perl-Parser-MGC
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Parser/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c31a129ae1e322930c64e435f32e6fcc
URL:		http://search.cpan.org/dist/Parser-MGC/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-File-Slurp-Tiny
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This base class provides a low-level framework for building
recursive-descent parsers that consume a given input string from left
to right, returning a parse structure. It takes its name from the
m//gc regexps used to implement the token parsing behaviour.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

mv lib/Parser/MGC/Examples/EvaluateExpression.pm examples

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

# already as man
rm $RPM_BUILD_ROOT%{perl_vendorlib}/Parser/MGC/Tutorial.pod

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Parser/MGC.pm
%{_mandir}/man3/Parser::MGC.3pm*
%{_mandir}/man3/Parser::MGC::Tutorial.3pm*
%{_examplesdir}/%{name}-%{version}
