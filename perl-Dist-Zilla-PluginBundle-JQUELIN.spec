%define upstream_name    Dist-Zilla-PluginBundle-JQUELIN
%define upstream_version 1.111710

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Build & release a distribution like jquelin
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Dist::Zilla::PluginBundle::Git)
BuildRequires:	perl(Dist::Zilla::Plugin::Repository)
BuildRequires:	perl(Dist::Zilla::Plugin::TaskWeaver)
BuildRequires:	perl(Dist::Zilla::Role::PluginBundle)
BuildRequires:	perl(Dist::Zilla::Plugin::Bugtracker)
BuildRequires:	perl(Dist::Zilla::Plugin::CheckChangeLog)
BuildRequires:	perl(Dist::Zilla::Plugin::CompileTests)
BuildRequires:	perl(Dist::Zilla::Plugin::CriticTests)
BuildRequires:	perl(Dist::Zilla::Plugin::HasVersionTests)
BuildRequires:	perl(Dist::Zilla::Plugin::Homepage)
BuildRequires:	perl(Dist::Zilla::Plugin::KwaliteeTests)
BuildRequires:	perl(Dist::Zilla::Plugin::MetaProvides::Package)
BuildRequires:	perl(Dist::Zilla::Plugin::MinimumVersionTests)
BuildRequires:	perl(Dist::Zilla::Plugin::PodWeaver)
BuildRequires:	perl(Dist::Zilla::Plugin::PortabilityTests)
BuildRequires:	perl(Dist::Zilla::Plugin::Prepender)
BuildRequires:	perl(Dist::Zilla::Plugin::ReportVersions)
BuildRequires:	perl(Dist::Zilla::Plugin::UnusedVarsTests)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Autobox)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build)

BuildArch:	noarch

%description
This is a plugin bundle to load all dist-zilla plugins that jq is using.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*


