%define tarball xf86-video-s3virge
%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir	%{moduledir}/drivers

Summary:   Xorg X11 s3virge video driver
Name:      xorg-x11-drv-s3virge
Version:   1.10.4
Release:   1.1%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2
Source1:   s3virge.xinf

ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.3.0.0-6

Requires:  hwdata
Requires:  xorg-x11-server-Xorg >= 1.3.0.0-6

%description 
X.Org X11 s3virge video driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases
install -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/hwdata/videoaliases/

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{driverdir}/s3virge_drv.so
%{_datadir}/hwdata/videoaliases/s3virge.xinf
%{_mandir}/man4/s3virge.4*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.10.4-1.1
- Rebuilt for RHEL 6

* Tue Aug 04 2009 Dave Airlie <airlied@redhat.com> 1.10.4-1
- s3virge 1.10.4

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.3-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 15 2009 Adam Jackson <ajax@redhat.com> - 1.10.3-1.1
- ABI bump

* Thu Jul 02 2009 Adam Jackson <ajax@redhat.com> 1.10.3-1
- s3virge 1.10.3

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 22 2008 Dave Airlie <airlied@redhat.com> 1.10.2-1
- Latest upstream release

* Thu Mar 20 2008 Dave Airlie <airlied@redhat.com> 1.10.0-1
- Latest upstream release

* Mon Mar 17 2008 Dave Airlie <airlied@redhat.com> 1.9.1-8
- fixup pciaccess conversion

* Mon Mar 10 2008 Dave Airlie <airlied@redhat.com> 1.9.1-7
- pciaccess conversion

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.9.1-6
- Autorebuild for GCC 4.3

* Wed Aug 22 2007 Adam Jackson <ajax@redhat.com> - 1.9.1-5
- Rebuild for PPC toolchain bug

* Mon Jun 18 2007 Adam Jackson <ajax@redhat.com> 1.9.1-4
- Update Requires and BuildRequires.  Disown the module directories.  Add
  Requires: hwdata.

* Fri Feb 16 2007 Adam Jackson <ajax@redhat.com> 1.9.1-3
- ExclusiveArch -> ExcludeArch

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - sh: line 0: fg: no job control
- rebuild

* Tue May 23 2006 Adam Jackson <ajackson@redhat.com> 1.9.1-2
- Rebuild for 7.1 ABI fix.

* Sun Apr  9 2006 Adam Jackson <ajackson@redhat.com> 1.9.1-1
- Update to 1.9.1 from 7.1RC1.

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1.8.6.5-1.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1.8.6.5-1.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Wed Jan 18 2006 Mike A. Harris <mharris@redhat.com> 1.8.6.5-1
- Updated xorg-x11-drv-s3virge to version 1.8.6.5 from X11R7.0

* Tue Dec 20 2005 Mike A. Harris <mharris@redhat.com> 1.8.6.4-1
- Updated xorg-x11-drv-s3virge to version 1.8.6.4 from X11R7 RC4
- Removed 'x' suffix from manpage dirs to match RC4 upstream.

* Wed Nov 16 2005 Mike A. Harris <mharris@redhat.com> 1.8.6.2-1
- Updated xorg-x11-drv-s3virge to version 1.8.6.2 from X11R7 RC2

* Fri Nov 4 2005 Mike A. Harris <mharris@redhat.com> 1.8.6.1-1
- Updated xorg-x11-drv-s3virge to version 1.8.6.1 from X11R7 RC1
- Fix *.la file removal.

* Tue Oct 4 2005 Mike A. Harris <mharris@redhat.com> 1.8.6-1
- Update BuildRoot to use Fedora Packaging Guidelines.
- Deglob file manifest.
- Limit "ExclusiveArch" to x86, x86_64, ppc

* Fri Sep 2 2005 Mike A. Harris <mharris@redhat.com> 1.8.6-0
- Initial spec file for s3virge video driver generated automatically
  by my xorg-driverspecgen script.
