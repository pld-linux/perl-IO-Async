#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	IO
%define	pnam	Async
Summary:	IO::Async - perform asynchronous filehandle IO and other operations
#Summary(pl.UTF-8):
Name:		perl-IO-Async
Version:	0.26
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/P/PE/PEVANS/IO-Async-%{version}.tar.gz
# Source0-md5:	7f9a04354483166640c94500651e291d
URL:		http://search.cpan.org/dist/IO-Async/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Async::MergePoint)
BuildRequires:	perl(Socket::GetAddrInfo) >= 0.08
BuildRequires:	perl(Test::Refcount)
BuildRequires:	perl-Heap >= 0.8
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This collection of modules allows programs to be written that perform
asynchronous filehandle IO operations. A typical program using them
would consist of a single subclass of IO::Async::Loop to act as a
container o other objects, which perform the actual IO work required
by the program. As as IO handles, the loop also supports timers and
signal handlers, and includes more higher-level functionallity built
on top of these basic parts.

Because there are a lot of classes in this collection, the following
overview gives a brief description of each.

The base class of all the event handling subclasses is
IO::Async::Notifier. It does not perform any IO operations itself, but
instead acts as a base class to build the specific IO functionallity
upon. It can also coordinate a collection of other Notifiers contained
within it, forming a tree structure.

The following sections describe particular types of Notifier.

# %description -l pl.UTF-8 # TODO

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
%{perl_vendorlib}/IO/*.pm
%{perl_vendorlib}/IO/Async
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
