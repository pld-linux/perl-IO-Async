#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Async
Summary:	IO::Async - perform asynchronous filehandle IO and other operations
Summary(pl.UTF-8):	IO::Async - asynchroniczne operacje we/wy na plikach i inne
Name:		perl-IO-Async
Version:	0.74
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/PEVANS/IO-Async-%{version}.tar.gz
# Source0-md5:	cf5f6a54c07f1d6f0ca484cac057bb6b
URL:		http://search.cpan.org/dist/IO-Async/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Async-MergePoint
BuildRequires:	perl-CPS
BuildRequires:	perl-Heap >= 0.80
BuildRequires:	perl-Socket-GetAddrInfo >= 0.18
BuildRequires:	perl-Storable
BuildRequires:	perl-Time-HiRes
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Identity
BuildRequires:	perl-Test-Refcount
BuildRequires:	perl-Test-Warn
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This collection of modules allows programs to be written that perform
asynchronous filehandle IO operations. A typical program using them
would consist of a single subclass of IO::Async::Loop to act as a
container of other objects, which perform the actual IO work required
by the program. As well as IO handles, the loop also supports timers
and signal handlers, and includes more higher-level functionallity
built on top of these basic parts.

%description -l pl.UTF-8
Zestaw modułów umożliwiających pisanie programów wykonywanie
asynchroncznych operacji we/wy na uchwytach plików. Typowy program
wykonujący je składa się z pojedynczej podklasy IO::Async::Loop
pełniącej rolę kontenera innych obiektów, wykonujących właściwe
operacje we/wy wymagane przez program. Oprócz obsługi we/wy pętla
obsługuje także stopery i sygnały, a także zawiera nieco funkcji
wyższego poziomu stworzonych w oparciu o te podstawowe elementy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/Async.pm
%{perl_vendorlib}/IO/Async
%{_mandir}/man3/IO::Async*.3pm*
%{_examplesdir}/%{name}-%{version}
