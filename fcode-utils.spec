Name:		fcode-utils
Version:	1.0.2
Release:	3%{?dist}
Summary:	Utilities for dealing with FCode
Group:		Development/Languages
# The entire source code is GPLv2 except localvalues/ and documentation/ which are CPL-licensed
License:	GPLv2 and CPL
URL:		http://www.openfirmware.info/FCODE_suite
# wget "http://tracker.coreboot.org/trac/openbios/changeset/197/fcode-utils?old_path=%2F&old=197&format=zip" -O fcode-utils-1.0.2.zip
Source0:	%{name}-%{version}.zip
# Fedora-specific patch
Patch0:		fcode-utils-optflags.diff
# patch from Debian folks
Patch1:		fcode-utils-types.h.diff
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
Utilities for dealing with FCode, a Forth programming language dialect
compliant with ANS Forth.


%prep
%setup -q -n %{name}
%patch0 -p0 -b .optflags
%patch1 -p1 -b .types
install -p -m 0644 detok/README README.detok
install -p -m 0644 toke/README README.toke


%build
CFLAGS="%{optflags}" make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -p -m 0755 detok/detok $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 romheaders/romheaders $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 toke/toke $RPM_BUILD_ROOT%{_bindir}
cp -a localvalues $RPM_BUILD_ROOT%{_datadir}/%{name}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING README README.detok README.toke documentation
%{_bindir}/detok
%{_bindir}/romheaders
%{_bindir}/toke
%{_datadir}/%{name}


%changelog
* Fri Mar 13 2009 Peter Lemenkov <lemenkov@gmail.com> 1.0.2-3
- Added comment about licensing

* Sat Feb 28 2009 Peter Lemenkov <lemenkov@gmail.com> 1.0.2-2
- Added localvalues (and added license CPL to spec header)
- Added patch from Debian

* Sat Feb 28 2009 Peter Lemenkov <lemenkov@gmail.com> 1.0.2-1
- Initial build
