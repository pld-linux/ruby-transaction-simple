Summary:	Simple transactions module for Ruby
Summary(pl.UTF-8):   Prosty moduł transakcji dla języka Ruby
Name:		ruby-transaction-simple
Version:	1.3.0
Release:	2
License:	Ruby License
Group:		Development/Languages
Source0:	http://rubyforge.org/frs/download.php/4332/transaction-simple-%{version}.tar.gz
# Source0-md5:	c10b1f4d320cf8cb8bb6fdf10531141e
Source1:	setup.rb
URL:		http://halostatue.ca/
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Transaction::Simple provides a generic way to add active transactional
support to objects. The transaction methods added by this module will
work with most objects, excluding those that cannot be Marshaled
(bindings, procedure objects, IO instances, or singleton objects).

%description -l pl.UTF-8
Transaction::Simple udostępnia ogólną metodę dodającą obsługę
transakcji aktywnych do obiektu. Metody transakcyjne dodane przez ten
moduł będą działać z większością obiektów z wyjątkiem tych, na których
nie można wykonać operacji Marshal (dowiązań, obiektów procedur,
instancji IO czy obiektów singleton).

%prep
%setup -q -n transaction-simple-%{version}
cp %{SOURCE1} .

%build
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
