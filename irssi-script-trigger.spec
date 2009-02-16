%include	/usr/lib/rpm/macros.perl
Summary:	Execute a command or replace text, triggered by an event in irssi
Summary(hu.UTF-8):	Parancs végrehajtása vagy szöveg cseréje irssi események bekövetkeztekor
Name:		irssi-script-trigger
Version:	1.0
Release:	1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://scripts.irssi.org/scripts/trigger.pl
# Source0-md5:	4d4f472281a5a27b2daa9fdcfb0a7d1f
URL:		http://scripts.irssi.org/
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	irssi >= 0.8.12-7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_scriptdir	%{_prefix}/share/irssi/scripts

%description
Execute a command or replace text, triggered by an event in irssi.

%description -l hu.UTF-8
Parancs végrehajtása vagy szöveg cseréje irssi események
bekövetkeztekor.

%prep
%setup -qcT
install %{SOURCE0} .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_scriptdir}
install *.pl $RPM_BUILD_ROOT%{_scriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_scriptdir}/trigger.pl
