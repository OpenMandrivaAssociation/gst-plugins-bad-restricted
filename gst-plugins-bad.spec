%define build_experimental	0
%{?_with_experimental: %{expand: %%global build_experimental 1}}
%define build_amrwb	0
%define build_faac	0
%define build_faad	0
%define build_xvid	0
%define build_dts	0
%define build_dirac	0
%define build_gme	1
%define build_celt	1

##########################
# Hardcode PLF build
%define build_plf	0
##########################

%if %{build_plf}
%define distsuffix plf
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%define build_amrwb	0
%define build_faac	1
%define build_faad	1
%define build_xvid	0
%define build_dts	1
%endif

%define bname	gstreamer%{api}
%define api	1.0
%define major	0
%define	libbasecamerabinsrc	%mklibname gstbasecamerabinsrc %{api} %{major}
%define	libbasevideo		%mklibname gstbasevideo %{api} %{major}
%define	libphotography		%mklibname gstphotography %{api} %{major}
%define	libsignalprocessor	%mklibname gstsignalprocessor %{api} %{major}
%define	libcodecparsers		%mklibname gstcodecparsers %{api} %{major}
%define devname	%mklibname -d 	%{name} %{api}

Summary:	GStreamer Streaming-media framework plug-ins
Name:		gst-plugins-bad
Version:	1.0.5
Release:	2%{?extrarelsuffix}
License:	LGPLv2+ and GPLv2+
Group:		Sound
Url:		http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{name}-%{version}.tar.xz
Patch0:		gst-plugins-bad-0.10.7-wildmidi-timidity.cfg.patch
# gw: fix for bug #36437 (paths to realplayer codecs)
# prefer codecs from the RealPlayer package in restricted
Patch10:	gst-plugins-bad-0.10.6-real-codecs-path.patch

%ifarch %ix86
BuildRequires:	nasm => 0.90
%endif
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api}) >= %{version}
BuildRequires:	pkgconfig(gstreamer-%{api}) >= %{version}
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libcdaudio)
BuildRequires:	pkgconfig(libmimic)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libmusicbrainz)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(orc-0.4) >= 0.4.5
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(valgrind)
BuildRequires:	pkgconfig(wayland-client)
%if %{build_plf}
BuildRequires:	pkgconfig(vo-aacenc)
BuildRequires:	pkgconfig(vo-amrwbenc)
%endif

%description
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that aren't up to par compared
to the rest. They might be close to being good quality, but they're
missing something - be it a good code review, some documentation, a
set of tests, a real live maintainer, or some actual wide use. If the
blanks are filled in they might be upgraded to become part of either
gstreamer-plugins-good or gstreamer-plugins-ugly, depending on the
other factors. If the plug-ins break, you can't complain - instead,
you can fix the problem and send us a patch, or bribe someone into
fixing them for you.  New contributors can start here for things to
work on.

%if %{build_plf}
This package is in restricted repository as it violates some patents.
%endif

%package -n %{bname}-plugins-bad
Summary:	Sound
Group:		System/Libraries
Requires:	%{bname}-voip >= %{version}-%{release}

%description -n %{bname}-plugins-bad
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plug-ins.

This package contains a set of plug-ins that aren't up to par compared
to the rest. They might be close to being good quality, but they're
missing something - be it a good code review, some documentation, a
set of tests, a real live maintainer, or some actual wide use. If the
blanks are filled in they might be upgraded to become part of either
gstreamer-plugins-good or gstreamer-plugins-ugly, depending on the
other factors. If the plug-ins break, you can't complain - instead,
you can fix the problem and send us a patch, or bribe someone into
fixing them for you.  New contributors can start here for things to
work on.

%if %{build_plf}
This package is in restricted repository as it violates some patents.
%endif

%package -n %{libbasecamerabinsrc}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries
Conflicts:	%{libbasevideo} < 1.0.5

%description -n %{libbasecamerabinsrc}
This package contains the libraries for %{name}%{api}.

%package -n %{libbasevideo}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries
Conflicts:	%{libbasecamerabinsrc} < 1.0.5

%description -n %{libbasevideo}
This package contains the libraries for %{name}%{api}.

%package -n %{libphotography}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libphotography}
This package contains the libraries for %{name}%{api}.

%package -n %{libsignalprocessor}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libsignalprocessor}
This package contains the libraries for %{name}%{api}.

%package -n %{libcodecparsers}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libcodecparsers}
This package contains the libraries for %{name}%{api}.

%package -n %{devname}
Summary:	Libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libbasecamerabinsrc} = %{version}-%{release}
Requires:	%{libbasevideo} = %{version}-%{release}
Requires:	%{libphotography} = %{version}-%{release}
Requires:	%{libsignalprocessor} = %{version}-%{release}
Requires:	%{libcodecparsers} = %{version}-%{release}
Provides:	%{name}%{api}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development libraries and includes files necessary to 
develop applications and plugins for GStreamer.

%package -n %{bname}-curl
Summary:	GStreamer Curl plugin
Group:		Networking/Other
BuildRequires:	pkgconfig(libcurl)

%description -n %{bname}-curl
This is a HTTP plugin for GStreamer based on the curl library.

%files -n %{bname}-curl
%{_libdir}/gstreamer-%{api}/libgstcurl.so

%package -n %{bname}-mpeg2enc
Summary:	GStreamer mjpegtools plug-in
Group:		Video
BuildRequires:	pkgconfig(mjpegtools)

%description -n %{bname}-mpeg2enc
mjpegtools-based encoding and decoding plug-in.

%files -n %{bname}-mpeg2enc
%{_libdir}/gstreamer-%{api}/libgstmpeg2enc.so
%{_libdir}/gstreamer-%{api}/libgstmplex.so

%if %{build_gme}
%package -n %{bname}-gme
Summary:	GStreamer Game Music plug-in
Group:		Sound
BuildRequires:	libgme-devel

%description -n %{bname}-gme
Game Music decoding plug-in.

%files -n %{bname}-gme
%{_libdir}/gstreamer-%{api}/libgstgme.so
%endif

%if %{build_dirac}
%package -n %{bname}-dirac
Summary:	GStreamer dirac plug-in
Group:		Video
BuildRequires:	pkgconfig(dirac) >= 0.9

%description -n %{bname}-dirac
Dirac encoding and decoding plug-in.

%files -n %{bname}-dirac
%{_libdir}/gstreamer-%{api}/libgstdirac.so
%endif

%package -n %{bname}-schroedinger
Summary:	GStreamer dirac plug-in based on Schroedinger
Group:		Video
BuildRequires:	pkgconfig(schroedinger-1.0)
Epoch:		1

%description -n %{bname}-schroedinger
Dirac encoding and decoding plug-in based on Schroedinger.

%files -n %{bname}-schroedinger
%{_libdir}/gstreamer-%{api}/libgstschro.so

%package -n %{bname}-rtpvp8
Summary:	GStreamer VP8 plug-in
Group:		Video
BuildRequires:	pkgconfig(vpx)
Conflicts:	%{bname}-vp8 < 1.0.3-2

%description -n %{bname}-rtpvp8
VP8 encoding and decoding plug-in.

%files -n %{bname}-rtpvp8
%{_libdir}/gstreamer-%{api}/libgstrtpvp8.so

%if %{build_dts}
%package -n %{bname}-dts
Summary:	GStreamer plug-ins for DTS audio playback
Group:		Sound
BuildRequires:	dtsdec-devel

%description -n %{bname}-dts
Plug-ins for decoding DTS audio.

%files -n %{bname}-dts
%{_libdir}/gstreamer-%{api}/libgstdtsdec.so
%endif

%if %{build_xvid}
%package -n %{bname}-xvid
Summary:	GStreamer plug-ins for XVID video encoding and decoding
Group:		Video
BuildRequires:	xvid-devel >= 1.1

%description -n %{bname}-xvid
Plug-ins for encoding and decoding XVID video.

This package is in restricted repository as it violates some patents.

%files -n %{bname}-xvid
%{_libdir}/gstreamer-%{api}/libgstxvid.so
%endif

%package -n %{bname}-mms
Summary:	GStreamer plug-in for mms streams
Group:		System/Libraries
Requires:	%{bname}-plugins-base = %{version}
BuildRequires:	pkgconfig(libmms)

%description -n %{bname}-mms
Plug-in supporting the mms protocol based on the libmms library.

%files -n %{bname}-mms
%{_libdir}/gstreamer-%{api}/libgstmms.so

%package -n %{bname}-rtmp
Summary:	GStreamer plug-in for rtmp streams
Group:		System/Libraries
Requires:	%{bname}-plugins-base = %{version}
BuildRequires:	pkgconfig(librtmp)

%description -n %{bname}-rtmp
Plug-in supporting the rtmp protocol based on the librtmp library.

%files -n %{bname}-rtmp
%{_libdir}/gstreamer-%{api}/libgstrtmp.so

%package -n %{bname}-soundtouch
Summary:	GStreamer plug-in for SoundTouch support
Group:		Sound
Requires:	%{bname}-plugins-base = %{version}
BuildRequires:	pkgconfig(soundtouch)

%description -n %{bname}-soundtouch
Plug-in supporting the SoundTouch audio manipulation support.

%files -n %{bname}-soundtouch
%{_libdir}/gstreamer-%{api}/libgstsoundtouch.so

%package -n %{bname}-libass
Summary:	GStreamer subtitles plugin
Group:		Video
BuildRequires:	pkgconfig(libass)

%description -n %{bname}-libass
This is a subtitle plugin for GStreamer based on libass.

%files -n %{bname}-libass
%{_libdir}/gstreamer-%{api}/libgstassrender.so

%package -n %{bname}-voip
Summary:	GStreamer voip plugins
Group:		Sound

%description -n %{bname}-voip
This is a collection of VoIP plugins for GStreamer.

%files -n %{bname}-voip
%{_libdir}/gstreamer-%{api}/libgstrtpmux.so
%{_libdir}/gstreamer-%{api}/libgstdtmf.so

%if %{build_faad}
%package -n %{bname}-faad
Summary:	GStreamer plug-in for AAC audio playback
Group:		Sound
Requires:	%{bname}-plugins-base >= %{version}
BuildRequires:	libfaad2-devel

%description -n %{bname}-faad
Plug-ins for playing AAC audio

This package is in restricted repository as it violates some patents.
%endif

%if %{build_faac}
%package -n %{bname}-faac
Summary:	GStreamer plug-ins for AAC audio encoding
Group:		Sound
Requires:	%{bname}-plugins-base >= %{version}
BuildRequires:	libfaac-devel

%description -n %{bname}-faac
Plug-ins for encoding AAC audio

This package is in restricted repository as it violates some patents.
%endif

%package -n %{bname}-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Group:		Sound
Requires:	%{bname}-plugins-base >= %{version}
BuildRequires:	gsm-devel >= 1.0.10

%description -n %{bname}-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%if 0
### SWFDEC FLASH PLUGIN ###
%package -n %{bname}-swfdec
Summary:	GStreamer Flash rendering plug-in
Group:		System/Libraries
Requires:	%{bname}-plugins-base = %{version}
BuildRequires:	libswfdec-devel => 0.3.0

%description -n %{bname}-swfdec
Plug-in for rendering Flash animations using swfdec library
%endif

%if %{build_amrwb}
%package -n %{bname}-amrwb
Summary:	GStreamer plug-in for AMR-WB support
Group:		Sound
Requires:	%{bname}-plugins-base >= %{version}
BuildRequires:	libamrwb-devel

%description -n %{bname}-amrwb
Plug-in for decoding AMR-WB under GStreamer.

This package is in restricted repository as it violates some patents.
%endif

%if %{build_celt}
%package -n %{bname}-celt
Summary:	GStreamer plug-in for CELT support
Group:		Video
Requires:	%{bname}-plugins-base >= %{version}
BuildRequires:	pkgconfig(celt) >= 0.7.0

%description -n %{bname}-celt
Plug-in for CELT support under GStreamer.
%endif

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--with-package-name='OpenMandriva %{name} package' \
	--with-package-origin='http://www.rosalinux.com/' \
%if ! %{build_celt}
	--disable-celt \
%endif
%if ! %{build_faac}
	--disable-faac \
%endif
%if ! %{build_faad}
	--disable-faad \
%endif
%if ! %{build_dirac}
	--disable-dirac \
%endif
%if ! %{build_xvid}
	--disable-xvid \
%endif
%if ! %{build_dts}
	--disable-dts \
%endif
%if ! %{build_plf}
	--disable-voamrwbenc \
	--disable-voaacenc \
%endif
%if %{build_experimental}
	--enable-experimental
%endif

%make

%install
%makeinstall_std

%find_lang %{name}-%{api}

%files -n %{bname}-plugins-bad -f %{name}-%{api}.lang
%doc AUTHORS COPYING README NEWS
%{_libdir}/gstreamer-%{api}/libgstadpcmdec.so
%{_libdir}/gstreamer-%{api}/libgstadpcmenc.so
%{_libdir}/gstreamer-%{api}/libgstasfmux.so
%{_libdir}/gstreamer-%{api}/libgstaudiovisualizers.so
%{_libdir}/gstreamer-%{api}/libgstautoconvert.so
%{_libdir}/gstreamer-%{api}/libgstbayer.so
%{_libdir}/gstreamer-%{api}/libgstcamerabin2.so
%{_libdir}/gstreamer-%{api}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{api}/libgstdataurisrc.so
%{_libdir}/gstreamer-%{api}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{api}/libgstdvb.so
%{_libdir}/gstreamer-%{api}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{api}/libgstdvdspu.so
%{_libdir}/gstreamer-%{api}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{api}/libgstfestival.so
%{_libdir}/gstreamer-%{api}/libgstfrei0r.so
%{_libdir}/gstreamer-%{api}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{api}/libgstgdp.so
%{_libdir}/gstreamer-%{api}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{api}/libgstid3tag.so
%{_libdir}/gstreamer-%{api}/libgstinter.so
%{_libdir}/gstreamer-%{api}/libgstinterlace.so
%{_libdir}/gstreamer-%{api}/libgstjpegformat.so
%{_libdir}/gstreamer-%{api}/libgstliveadder.so
%{_libdir}/gstreamer-%{api}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{api}/libgstmpg123.so
%{_libdir}/gstreamer-%{api}/libgstmimic.so
%{_libdir}/gstreamer-%{api}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{api}/libgstopus.so
%{_libdir}/gstreamer-%{api}/libgstpcapparse.so
%{_libdir}/gstreamer-%{api}/libgstpnm.so
%{_libdir}/gstreamer-%{api}/libgstscaletempoplugin.so
%{_libdir}/gstreamer-%{api}/libgstrawparse.so
%{_libdir}/gstreamer-%{api}/libgstremovesilence.so
%{_libdir}/gstreamer-%{api}/libgstsdpelem.so
%{_libdir}/gstreamer-%{api}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{api}/libgstshm.so
%{_libdir}/gstreamer-%{api}/libgstsiren.so
%{_libdir}/gstreamer-%{api}/libgstsmooth.so
%{_libdir}/gstreamer-%{api}/libgstspeed.so
%{_libdir}/gstreamer-%{api}/libgstsubenc.so
%{_libdir}/gstreamer-%{api}/libgstbz2.so
%{_libdir}/gstreamer-%{api}/libgstfragmented.so
%{_libdir}/gstreamer-%{api}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{api}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{api}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{api}/libgstwaylandsink.so
%if %{build_plf}
%{_libdir}/gstreamer-%{api}/libgstvoaacenc.so
%{_libdir}/gstreamer-%{api}/libgstvoamrwbenc.so
%{_datadir}/gstreamer-%{api}/presets/GstVoAmrwbEnc.prs
%endif
%if %{build_experimental}
#%{_libdir}/gstreamer-%{api}/libgstdeinterlace2.so
%endif
%{_libdir}/gstreamer-%{api}/libgstmodplug.so
%{_libdir}/gstreamer-%{api}/libgsty4mdec.so

%if %{build_faad}
%files -n %{bname}-faad
%{_libdir}/gstreamer-%{api}/libgstfaad.so
%endif

%if %{build_faac}
%files -n %{bname}-faac
%{_libdir}/gstreamer-%{api}/libgstfaac.so
%endif

%files -n %{bname}-gsm
%{_libdir}/gstreamer-%{api}/libgstgsm.so

%if 0
### SWFDEC FLASH PLUGIN ###
%files -n %{bname}-swfdec
%{_libdir}/gstreamer-%{api}/libgstswfdec.so
%endif

%if %{build_amrwb}
%files -n %{bname}-amrwb
%{_datadir}/gstreamer-%{api}/presets/GstAmrwbEnc.prs
%{_libdir}/gstreamer-%{api}/libgstamrwbenc.so
%endif

%if %{build_celt}
%files -n %{bname}-celt
%{_libdir}/gstreamer-%{api}/libgstcelt.so
%endif

%files -n %{libbasecamerabinsrc}
%{_libdir}/libgstbasecamerabinsrc-%{api}.so.%{major}*

%files -n %{libbasevideo}
%{_libdir}/libgstbasevideo-%{api}.so.%{major}*

%files -n %{libphotography}
%{_libdir}/libgstphotography-%{api}.so.%{major}*

%files -n %{libsignalprocessor}
%{_libdir}/libgstsignalprocessor-%{api}.so.%{major}*

%files -n %{libcodecparsers}
%{_libdir}/libgstcodecparsers-%{api}.so.%{major}*

%files -n %{devname}
%doc docs/plugins/html
%doc %{_datadir}/gtk-doc/html/
%{_libdir}/libgstbasevideo-%{api}.so
%{_libdir}/libgstcodecparsers-%{api}.so
%{_libdir}/libgstphotography-%{api}.so
%{_libdir}/libgstsignalprocessor-%{api}.so
%{_includedir}/gstreamer-%{api}/gst/basecamerabinsrc/*
%{_includedir}/gstreamer-%{api}/gst/codecparsers/
%{_includedir}/gstreamer-%{api}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{api}/gst/signalprocessor/gstsignalprocessor.h
%{_includedir}/gstreamer-%{api}/gst/video/
%{_libdir}/pkgconfig/gstreamer-basevideo-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{api}.pc
%{_libdir}/libgstbasecamerabinsrc-%{api}.so

