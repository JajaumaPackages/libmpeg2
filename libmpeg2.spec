Name:           libmpeg2
Version:        0.5.1
Release:        1%{?dist}
Summary:        A free MPEG-2 video stream decoder

License:        GPLv2
URL:            http://libmpeg2.sourceforge.net
Source0:        http://libmpeg2.sourceforge.net/files/libmpeg2-%{version}.tar.gz

%description
libmpeg2 is a free library for decoding mpeg-2 and mpeg-1 video streams. It is
released under the terms of the GPL license.  The main goals in libmpeg2
development are conformance, speed portability and reuseability.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package        -n mpeg2dec
Summary:        A test program for libmpeg2

%description    -n mpeg2dec
mpeg2dec is a test program for libmpeg2. It decodes mpeg-1 and mpeg-2 video
streams, and also includes a demultiplexer for mpeg-1 and mpeg-2 program
streams. It is purposely kept simple : it does not include features like
reading files from a DVD, CSS, fullscreen output, navigation, etc... The main
purpose of mpeg2dec is to have a simple test bed for libmpeg2.


%prep
%setup -q


%build
%configure --disable-static

sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/*.so.*

%files devel
%doc doc/libmpeg2.txt doc/*.c
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n mpeg2dec
%{_bindir}/*
%{_mandir}/man1/*.1*


%changelog
* Mon May 16 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.5.1-1
- Public release
