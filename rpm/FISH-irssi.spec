Name:          irssi-fish
Version:       1.6
Release:       1
License:       MIT 
Group:         Productivity/Networking/IRC
Summary:       FiSH for Irssi
Distribution:  SailfishOS
Source:        %{name}-%{version}.tar.gz
URL:           https://github.com/falsovsky/FiSH-irssi
Packager:        szopin

Provides:      libfish.so()
Requires:      irssi  
BuildRequires:   irssi-devel

%description
FiSH encryption module for Irssi

%prep
ls -la %{name}-%{version}
%setup -q -n %{name}-%{version}/irssi-fish

%build
cmake .
%{__make} %{?_smp_mflags}

%install
%make_install

%files
%attr(0755, root, root) "/usr/local/lib/irssi/modules/libfish.so"

%changelog

