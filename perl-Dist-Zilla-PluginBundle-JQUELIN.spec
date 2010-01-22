%define upstream_name    Dist-Zilla-PluginBundle-JQUELIN
%define upstream_version 1.100220

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Build & release a distribution like jquelin
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Dist::Zilla::PluginBundle::Git)
BuildRequires: perl(Dist::Zilla::Plugin::TaskWeaver)
BuildRequires: perl(Dist::Zilla::Role::PluginBundle)
BuildRequires: perl(English)
BuildRequires: perl(File::Find)
BuildRequires: perl(Module::Build)
BuildRequires: perl(Moose)
BuildRequires: perl(Moose::Autobox)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This is a plugin bundle to load all dist-zilla plugins that jq is using.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*
