# SPDX-License-Identifqier: MIT
%global forgeurl https://github.com/mitradranirban/fonts-fbf-beng
Version:   1.0.2
Release:   1%{?dist}
%forgemeta
URL: %{forgeurl}

%global foundry fbf
%global fontfamily    ani
%global fontlicense       GPLv3+ with exceptions
%global fontlicenses      LICENCE
%global fontdocs          Ani-*
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
Source0:  %forgesource

%fontpkg

%prep

%forgesetup
chmod 755 generate.pe
./generate.pe Ani.sfd

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog

* Tue Feb 08 2022 14:36:29 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.2-1
- corrected pstf lookup to render ya_phala glyph rendering bug 
- Updated font to add character to be compliant with Unicode 14.0
- removed typos in lookups
- support for Assamese language
 
