Name:          irssi-fish
Version:       1.6
Release:       1
License:       MIT 
Group:         Productivity/Networking/IRC
Summary:       FiSH for Irssi
Distribution:  SailfishOS

URL:           https://github.com/falsovsky/FiSH-irssi
Packager:        szopin

Provides:      libfish.so()
Requires:      irssi  
BildRequires:   irssi-devel

%description
FiSH encryption module for Irssi
  
%files
%attr(0755, root, root) "/usr/local/lib/irssi/modules/libfish.so"

%changelog
