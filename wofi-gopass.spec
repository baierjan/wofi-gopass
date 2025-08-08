#
# spec file for package wofi-gopass
#
# Copyright (c) 2025 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           wofi-gopass
Version:        0.0
Release:        0
Summary:        Simple wofi frontend for gopass
License:        MIT
URL:            https://github.com/baierjan/wofi-gopass
Source:         wofi-gopass-%{version}.tar.gz
BuildRequires:  /bin/bash
Requires:       gopass
Requires:       wl-clipboard
Requires:       wofi
Supplements:    (wofi and gopass)
BuildArch:      noarch

%description
A simplified version of wofi-pass specifically tailored to gopass. The script uses wofi and wl-copy to provide a Wayland-native way to interact with gopass. It provides search dialog that lets the user choose the appropriate password entry and which field to copy.

%prep
%autosetup -p1

%build
:

%install
install -Dm0775 wofi-gopass %{buildroot}%{_bindir}/wofi-gopass

%files
%license LICENSE
%doc README.md
%{_bindir}/wofi-gopass

%changelog
