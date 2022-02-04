# SPDX-License-Identifqier: MIT
%global forgeurl https://github.com/mitradranirban/fbf-ani-fonts
Version:   1.0.2

Release:   1

URL: %{forgeurl}

%global foundry fbf

%global fontfamily    ani

%global fontlicense       GPlv3+ with exception

%global fontlicenses      LICENCE

%global fontdocs          changelog copyright

%global fontdocsex        %{fontlicenses}

%global fontsummary       Script like Bengali Font

%global fonts            *.ttf

%global fontconfs        67-0-%{fontpkgname}.conf

BuildRequires: fontforge

%global fontdescription  %{expand:
Ani font shows Bengali characters like hand written one with unique latin 
characters. It was developed in 2002 and is corrently updated to Unicode
 14.0 standard.
}

Source0:  https://raw.githubusercontent.com/mitradranirban/fbf-ani-fonts/main/fbf-ani-fonts-1.0.1.tar.gz

%fontpkg

%prep

%setup -q -n %{foundry}-%{fontfamily}-fonts-%{version}
 chmod 755 generate.pe
./generate.pe *.sfd

%build

%fontbuild

%install

%fontinstall

%check

%fontcheck

%fontfiles

%changelog

* Fri Feb 04 2022 20:36:29 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.2-1
- Updated font to add character to be compliant with Unicode 14.0
- removed typos in lookups
- support for Assamese language
 
