Name:           freerdp
Version:        1.0.2
Release:        15%{?dist}.1
Summary:        Remote Desktop Protocol client

Group:          Applications/Communications
License:        ASL 2.0
URL:            http://www.freerdp.com/
Source0:        http://pub.freerdp.com/releases/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  cmake
BuildRequires:  xmlto
BuildRequires:  openssl-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXv-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  cups-devel
BuildRequires:  pcsc-lite-devel
BuildRequires:  desktop-file-utils

Provides:       xfreerdp = %{version}-%{release}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-plugins%{?_isa} = %{version}-%{release}

Patch0: 0001-xfreerdp.1.xml-Don-t-claim-to-support-multiple-conne.patch
Patch1: 0002-Replace-itemizedlist-s-with-variablelist-s.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1186916
Patch3: libfreerdp-core-fix-issue-436.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1296654
Patch4: fix-crashes-in-pulseaudio.patch

# Fix crash if pulseaudio device isn't specified
# https://bugzilla.redhat.com/show_bug.cgi?id=1067543
Patch5: rdpsnd-pulse-Fix-crash-if-device-isn-t-specified.patch

# Fix crash if requested bitmap isn't in cache
# https://bugzilla.redhat.com/show_bug.cgi?id=1311164
Patch6: cover-the-case-of-servers-asking-for-cached-bitmaps-.patch

# Add support for wildcard certificates
# https://bugzilla.redhat.com/show_bug.cgi?id=1275241
Patch7: libfreerdp-core-verify-TLS-certificate-with-both-TLS.patch
Patch8: fix-issue-530-NLA-password-asked-after-certificate-r.patch
Patch9: 1-Add-support-for-Wildcard-Certificates-2-For-Gatewa.patch
Patch10: Using-the-more-efficient-code-for-comparing-host-nam.patch
Patch11: Fixed-a-possible-buffer-overflow-issue.patch

# Prevent stucked keys on focus out and unmap events
# https://bugzilla.redhat.com/show_bug.cgi?id=1415069
Patch12: x11-release-all-pressed-keys-when-window-is-unmapped.patch
Patch13: release-keys-when-xfreerdp-is-unfocused-to-prevent-s.patch

# Fix crashes when copying images
# https://bugzilla.redhat.com/show_bug.cgi?id=1417536
Patch14: remove-unncessary-NULL-ptr-check.patch

# Enable TLS 1.1 connections and later
# https://bugzilla.redhat.com/show_bug.cgi?id=1312967
Patch15: tls-enable-tls-1.patch

# Add description for available plugins
# https://bugzilla.redhat.com/show_bug.cgi?id=1428041
Patch16: Add-description-for-available-plugins.patch
Patch20: Fix-smartcard-usage-in-manpage.patch

# Fix NTLM on big endian
# https://bugzilla.redhat.com/show_bug.cgi?id=1204742
Patch17: Fix-NTLM-on-big-endian.patch

# Fix colors on big endian
# https://bugzilla.redhat.com/show_bug.cgi?id=1308810
Patch18: Fix-colors-on-big-endian.patch

# Add FIPS mode support
# https://bugzilla.redhat.com/show_bug.cgi?id=1363811
Patch19: FIPS-mode-support.patch

# Fix CVE-2018-8786
# https://bugzilla.redhat.com/show_bug.cgi?id=1684152
Patch21: CVE-2018-8786.patch

# Fix CVE-2018-8787
# https://bugzilla.redhat.com/show_bug.cgi?id=1684156
Patch22: CVE-2018-8787.patch

# Fix CVE-2018-8788
# https://bugzilla.redhat.com/show_bug.cgi?id=1684163
Patch23: CVE-2018-8788.patch

%description
The xfreerdp Remote Desktop Protocol (RDP) client from the FreeRDP
project.

xfreerdp can connect to RDP servers such as Microsoft Windows
machines, xrdp and VirtualBox.


%package        libs
Summary:        Core libraries implementing the RDP protocol
Group:          Applications/Communications
%description    libs
libfreerdp-core can be embedded in applications.

libfreerdp-channels and libfreerdp-kbd might be convenient to use in X
applications together with libfreerdp-core.

libfreerdp-core can be extended with plugins handling RDP channels.


%package        plugins
Summary:        Plugins for handling the standard RDP channels
Group:          Applications/Communications
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    plugins
A set of plugins to the channel manager implementing the standard virtual
channels extending RDP core functionality. For instance, sounds, clipboard
sync, disk/printer redirection, etc.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}-libs.


%prep

%setup -q

%patch0 -p1
%patch1 -p1
%patch3 -p1 -b .fix-invalid-dereference
%patch4 -p1 -b .fix-crashes-in-pulseaudio
%patch5 -p1 -b .rdpsnd-pulse-fix-crash-if-device-isn-t-specified
%patch6 -p1 -b .cover-the-case-of-servers-asking-for-cached-bitmaps-.patch
%patch7 -p1 -b .libfreerdp-core-verify-TLS-certificate-with-both-TLS
%patch8 -p1 -b .fix-issue-530-NLA-password-asked-after-certificate-r
%patch9 -p1 -b .1-Add-support-for-Wildcard-Certificates-2-For-Gatewa
%patch10 -p1 -b .Using-the-more-efficient-code-for-comparing-host-nam
%patch11 -p1 -b .Fixed-a-possible-buffer-overflow-issue
%patch12 -p1 -b .x11-release-all-pressed-keys-when-window-is-unmapped
%patch13 -p1 -b .release-keys-when-xfreerdp-is-unfocused-to-prevent-s
%patch14 -p1 -b .remove-unncessary-NULL-ptr-check
%patch15 -p1 -b .tls-enable-tls-1
%patch16 -p1 -b .Add-description-for-available-plugins
%patch17 -p1 -b .Fix-NTLM-on-big-endian
%patch18 -p1 -b .Fix-colors-on-big-endian
%patch19 -p1 -b .FIPS-mode-support
%patch20 -p1 -b .Fix-smartcard-usage-in-manpage
%patch21 -p1 -b .CVE-2018-8786
%patch22 -p1 -b .CVE-2018-8787
%patch23 -p1 -b .CVE-2018-8788

cat << EOF > xfreerdp.desktop 
[Desktop Entry]
Type=Application
Name=X FreeRDP
NoDisplay=true
Comment=Connect to RDP server and display remote desktop
Icon=%{name}
Exec=/usr/bin/xfreerdp
Terminal=false
Categories=Network;RemoteAccess;
EOF


%build

%cmake \
        -DWITH_CUPS=ON \
        -DWITH_PCSC=ON \
        -DWITH_PULSEAUDIO=ON \
        -DWITH_X11=ON \
        -DWITH_XCURSOR=ON \
        -DWITH_XEXT=ON \
        -DWITH_XINERAMA=ON \
        -DWITH_XKBFILE=ON \
        -DWITH_XV=ON \
        -DWITH_ALSA=OFF \
        -DWITH_CUNIT=OFF \
        -DWITH_DIRECTFB=OFF \
        -DWITH_FFMPEG=OFF \
        -DWITH_SSE2=OFF \
        -DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
        .

make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

# No need for keymap files when using xkbfile
rm -rf $RPM_BUILD_ROOT/usr/share/freerdp

desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications xfreerdp.desktop
install -p -D resources/FreeRDP_Icon_256px.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps/%{name}.png


%clean
rm -rf $RPM_BUILD_ROOT


%post
# This is no gtk application, but try to integrate nicely with GNOME if it is available
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%post libs -p /sbin/ldconfig


%postun libs -p /sbin/ldconfig


%files
%defattr(-,root,root,-)
%{_bindir}/xfreerdp
%{_mandir}/man1/xfreerdp.*
%{_datadir}/applications/xfreerdp.desktop
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png

%files libs
%defattr(-,root,root,-)
%doc LICENSE README ChangeLog
%{_libdir}/lib%{name}-*.so.*
%dir %{_libdir}/%{name}/

%files plugins
%defattr(-,root,root,-)
%{_libdir}/%{name}/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}/
%{_libdir}/lib%{name}-*.so
%{_libdir}/pkgconfig/%{name}.pc


%changelog
* Fri Mar 8 2019 Ondrej Holy <oholy@redhat.com> - 1.0.2-15.1
- Fix CVE-2018-8786 (#1684152)
- Fix CVE-2018-8787 (#1684156)
- Fix CVE-2018-8788 (#1684163)

* Wed Jan 31 2018 Ondrej Holy <oholy@redhat.com> - 1.0.2-15
- Fix smartcard usage in manpage (#1428041)

* Thu Nov 23 2017 Ondrej Holy <oholy@redhat.com> - 1.0.2-14
- Add FIPS mode support (#1363811)

* Thu Oct 5 2017 Ondrej Holy <oholy@redhat.com> - 1.0.2-13
- Fix NTLM on big endian (#1204742)
- Fix colors on big endian (#1308810)

* Thu Sep 21 2017 Ondrej Holy <oholy@redhat.com> - 1.0.2-12
- Add description for available plugins (#1428041)

* Thu Sep 7 2017 Ondrej Holy <oholy@redhat.com> - 1.0.2-11
- Use boolean types defined stdbool.h (#1404575)
- Prevent stucked keys on focus out and unmap events (#1415069)
- Fix crashes when copying images (#1417536)
- Enable TLS 1.1 connections and later (#1312967)

* Mon Apr 18 2016 Ondrej Holy <oholy@redhat.com> - 1.0.2-10
- Add support for wildcard certificates (#1275241)

* Wed Apr 6 2016 Ondrej Holy <oholy@redhat.com> - 1.0.2-9
- Fix crash if requested bitmap isn't in cache (#1311164)

* Wed Apr 6 2016 Ondrej Holy <oholy@redhat.com> - 1.0.2-8
- Fix crash if pulseaudio device isn't specified (#1067543)

* Fri Jan 15 2016 Ondrej Holy <oholy@redhat.com> - 1.0.2-7
- Fix crashes in pulseaudio
- Resolves: #1210049

* Thu Mar 19 2015 Ondrej Holy <oholy@redhat.com> - 1.0.2-6
- Fix crash during CA verification caused by invalid pointer dereference
- Resolves: #1186916

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.0.2-5
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.0.2-4
- Mass rebuild 2013-12-27

* Thu Dec 19 2013 Soren Sandmann <ssp@redhat.com> - 1.0.2-3
- Man page fixes
  - Document that multiple connections don't work (988294)
  - Document the list of plugins (988307, 988308)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 02 2013 Mads Kiilerich <mads@kiilerich.com> - 1.0.2-1
- freerdp-1.0.2

* Sun Sep 30 2012 Mads Kiilerich <mads@kiilerich.com> - 1.0.1-7
- merge f17 1.0.1-6 - Backport fix for bug 816692

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Feb 29 2012 Mads Kiilerich <mads@kiilerich.com> - 1.0.1-5
- Use new upstream tar with standard naming
- Use _isa for subpackage dependencies

* Tue Feb 28 2012 Mads Kiilerich <mads@kiilerich.com> - 1.0.1-4
- Include patch for sending invalid extra data

* Tue Feb 28 2012 Mads Kiilerich <mads@kiilerich.com> - 1.0.1-3
- Install a freedesktop .desktop file and a high-res icon instead of relying on
  _NET_WM_ICON

* Sat Feb 25 2012 Mads Kiilerich <mads@kiilerich.com> - 1.0.1-2
- Explicit build requirement for xmlto - needed for EL6

* Wed Feb 22 2012 Mads Kiilerich <mads@kiilerich.com> - 1.0.1-1
- FreeRDP-1.0.1 - major upstream rewrite and relicensing under Apache license

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 28 2011 Mads Kiilerich <mads@kiilerich.com> - 0.8.2-2
- rebuild on rawhide because of broken dependencies

* Tue Nov 16 2010 Mads Kiilerich <mads@kiilerich.com> - 0.8.2-1
- freerdp-0.8.2

* Mon Nov 08 2010 Mads Kiilerich <mads@kiilerich.com> - 0.8.1-2
- make -devel require pkgconfig
- first official Fedora package

* Sun Nov 07 2010 Mads Kiilerich <mads@kiilerich.com> - 0.8.1-1
- freerdp-0.8.1

* Sat Sep 25 2010 Mads Kiilerich <mads@kiilerich.com> - 0.7.4-2
- hack the generated libtool to not set rpath on x86_64
- configure with alsa explicitly

* Tue Aug 24 2010 Mads Kiilerich <mads@kiilerich.com> - 0.7.4-1
- freerdp-0.7.4
- cleanup of packaging structure

* Wed Jul 28 2010 Mads Kiilerich <mads@kiilerich.com> - 0.7.3-1
- 0.7.3
- fix some minor pylint warnings

* Fri Jul 23 2010 Mads Kiilerich <mads@kiilerich.com> - 0.7.2-2
- 0.7.2
- Address many comments from cwickert:
- - cleanup of old formatting, alignment with spectemplate-lib.spec and
    cwickert spec from #616193
- - add alsa as build requirement
- - remove superfluous configure options and disable static libs
- - add missing rpm groups

* Sun Jun 13 2010 Mads Kiilerich <mads@kiilerich.com> - 0.7.0-1
- First official release, first review request
