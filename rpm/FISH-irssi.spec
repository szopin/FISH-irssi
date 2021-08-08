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

%setup -q -n %{name}-%{version}/FISH-irssi

%build
cmake .

%files
%attr(0755, root, root) "/usr/local/lib/irssi/modules/libfish.so"

%changelog

