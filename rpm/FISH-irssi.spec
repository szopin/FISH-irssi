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
BuildRequires:   irssi-devel cmake
BuildRequires:  openssl-devel
BuildRequires:	gcc
BuildRequires:	glib2-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig

%description
FiSH encryption module for Irssi

%prep
%setup -q -n %{name}-%{version}/FiSH-irssi

%build
%cmake .
%{__make} %{?_smp_mflags}

%install
%make_install

%files
%attr(0755, root, root) "/usr/%{_lib}/irssi/modules/libfish.so"
%exclude /usr/local/share/doc/FiSH-irssi/README
%changelog

