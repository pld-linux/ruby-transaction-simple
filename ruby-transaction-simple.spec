%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define	ruby_version	%(ruby -r rbconfig -e 'print Config::CONFIG["ruby_version"]')
Summary:	Simple transactions module for Ruby
Summary(pl):	Prosty modu³ transakcji dla jêzyka Ruby
Name:		ruby-transaction-simple
Version:	1.3.0
Release:	1
License:	Ruby License
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/4332/transaction-simple-%{version}.tar.gz
# Source0-md5:	c10b1f4d320cf8cb8bb6fdf10531141e
Source1:	setup.rb
URL:		http://halostatue.ca/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Transaction::Simple provides a generic way to add active transactional
support to objects. The transaction methods added by this module will
work with most objects, excluding those that cannot be Marshaled
(bindings, procedure objects, IO instances, or singleton objects).

%description -l pl
Transaction::Simple udostêpnia ogóln± metodê dodaj±c± obs³ugê
transakcji aktywnych do obiektu. Metody transakcyjne dodane przez ten
modu³ bêd± dzia³aæ z wiêkszo¶ci± obiektów z wyj±tkiem tych, na których
nie mo¿na wykonaæ operacji Marshal (dowi±zañ, obiektów procedur,
instancji IO czy obiektów singleton).

%prep
%setup -q -n transaction-simple-%{version}

%build
cp %{SOURCE1} .
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir}
ruby setup.rb setup

rdoc --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc
%{ruby_rubylibdir}/transaction
%{ruby_ridir}/Transaction
