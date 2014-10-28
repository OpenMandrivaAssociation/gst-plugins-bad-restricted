%define build_experimental	0
%{?_with_experimental: %{expand: %%global build_experimental 1}}
%define build_amrwb	0
%define build_faac	0
%define build_faad	0
%define build_xvid	0
%define build_dts	0
%define build_dirac	0
%define build_gme	1

##########################
# Hardcode PLF build
%define build_plf	1
##########################
%if "%{disttag}" == "mdk"
%define	build_plf	1
%endif

%if %{build_plf}
%define distsuffix plf
# make EVR of plf build higher than regular to allow update, needed with rpm5 mkrel
%define extrarelsuffix plf
%define build_amrwb	0
%define build_faac	1
%define build_faad	1
%define build_xvid	0
%define build_dirac	0
%define build_dts	1
%endif

%define bname	gstreamer%{api}
%define api	1.0
%define major	0
%define	libbasecamerabinsrc	%mklibname gstbasecamerabinsrc %{api} %{major}
%define	libphotography		%mklibname gstphotography %{api} %{major}
%define	libcodecparsers		%mklibname gstcodecparsers %{api} %{major}
%define libmpegts		%mklibname gstmpegts %{api} %{major}
%define libgl			%mklibname gstgl %{api} %{major}
%define liburidownloader	%mklibname gsturidownloader %{api} %{major}
%define libinsertbin		%mklibname gstinsertbin %{api} %{major}
%define girname			%mklibname gstreamer-plugins-bad-gir %{api}
%define libbadbase		%mklibname gstbadbase %{api} %{major}
%define libbadvideo		%mklibname gstbadvideo %{api} %{major}
%define libgstwayland		%mklibname gstwayland %{api} %{major}
%define devname			%mklibname -d %{name} %{api}

Summary:	GStreamer Streaming-media framework plug-ins
Name:		gst-plugins-bad
Version:	1.4.3
Release:	1%{?extrarelsuffix}
License:	LGPLv2+ and GPLv2+
Group:		Sound
Url:		http://gstreamer.freedesktop.org/
Source0:	http://gstreamer.freedesktop.org/src/gst-plugins-bad/%{name}-%{version}.tar.xz
Patch0:		gst-plugins-bad-0.10.7-wildmidi-timidity.cfg.patch
# gw: fix for bug #36437 (paths to realplayer codecs)
# prefer codecs from the RealPlayer package in restricted
Patch10:	gst-plugins-bad-0.10.6-real-codecs-path.patch

%ifarch %{ix86} x86_64
BuildRequires:	nasm => 0.90
%endif
BuildRequires:	bzip2-devel
BuildRequires:	gettext-devel
BuildRequires:	fonts-ttf-dejavu
BuildRequires:	gobject-introspection-devel
BuildRequires:	kernel-headers
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(check)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dvdnav) >= 4.1.2
BuildRequires:	pkgconfig(dvdread) >= 4.1.2
BuildRequires:	pkgconfig(egl)
BuildRequires:	pkgconfig(exempi-2.0)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(gio-2.0) >= 2.25.0
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(glesv2)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gmodule-export-2.0)
BuildRequires:	pkgconfig(gmodule-no-export-2.0)
BuildRequires:	pkgconfig(gnutls) >= 2.11.3
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{api}) >= %{version}
BuildRequires:	pkgconfig(gstreamer-%{api}) >= %{version}
BuildRequires:	pkgconfig(gstreamer-video-%{api}) >= %{version}
BuildRequires:	pkgconfig(gudev-1.0)
BuildRequires:	pkgconfig(kate)
BuildRequires:	pkgconfig(libass)
BuildRequires:	pkgconfig(libcdaudio)
BuildRequires:	pkgconfig(libchromaprint)
BuildRequires:	pkgconfig(libcrypto)
BuildRequires:	pkgconfig(libdc1394-2) >= 2.0.0
BuildRequires:	pkgconfig(libexif) >= 0.6.16
BuildRequires:	pkgconfig(libmimic)
BuildRequires:	pkgconfig(libmodplug)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(libmusicbrainz)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libofa) >= 0.9.3
BuildRequires:	pkgconfig(libopenjpeg1)
BuildRequires:	pkgconfig(libusb-1.0)
BuildRequires:	pkgconfig(libwebp)
BuildRequires:	pkgconfig(neon)
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(opencv)
BuildRequires:	pkgconfig(opus)
BuildRequires:	pkgconfig(orc-0.4) >= 0.4.5
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.36
BuildRequires:	pkgconfig(librtmp)
BuildRequires:	pkgconfig(sbc) >= 1.0
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(slv2) >= 0.6.6
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	pkgconfig(soundtouch)
BuildRequires:	pkgconfig(spandsp) >= 0.0.6
BuildRequires:	pkgconfig(libusb-1.0)
%ifnarch %{mipsx}
BuildRequires:	pkgconfig(valgrind)
%endif
BuildRequires:	pkgconfig(vdpau)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zvbi-0.2)
%if %{build_plf}
BuildRequires:	pkgconfig(vo-aacenc)
BuildRequires:	pkgconfig(vo-amrwbenc)
%endif
BuildRequires:	wildmidi-devel

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

%description -n %{libbasecamerabinsrc}
This package contains the libraries for %{name}%{api}.

%package -n %{libphotography}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libphotography}
This package contains the libraries for %{name}%{api}.

%package -n %{libcodecparsers}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libcodecparsers}
This package contains the libraries for %{name}%{api}.

%package -n %{libbadbase}
Summary:        Libraries for GStreamer streaming-media framework
Group:          System/Libraries

%description -n %{libbadbase}
This package contains the libraries for %{name}%{api}.

%package -n %{libbadvideo}
Summary:        Libraries for GStreamer streaming-media framework
Group:          System/Libraries

%description -n %{libbadvideo}
This package contains the libraries for %{name}%{api}.

%package -n %{libgstwayland}
Summary:        Libraries for GStreamer streaming-media framework
Group:          System/Libraries

%description -n %{libgstwayland}
This package contains the libraries for %{name}%{api}.


%package -n %{libgl}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libgl}
GStreamer is a streaming-media framework, based on graphs of filters which
operate on media data. Applications using this library can do anything
from real-time sound processing to playing videos, and just about anything
else media-related.  Its plugin-based architecture means that new data
types or processing capabilities can be added simply by installing new
plugins.

This package contains the libraries.

%package -n %{libinsertbin}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libinsertbin}
This package contains the libraries for %{name}%{api}.

%package -n %{libmpegts}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{libmpegts}
This package contains the libraries for %{name}%{api}.

%package -n %{liburidownloader}
Summary:	Libraries for GStreamer streaming-media framework
Group:		System/Libraries

%description -n %{liburidownloader}
This package contains the libraries for %{name}%{api}.

%package -n %{devname}
Summary:	Libraries and include files for GStreamer streaming-media framework
Group:		Development/C
Requires:	%{libbasecamerabinsrc} = %{version}-%{release}
Requires:	%{libphotography} = %{version}-%{release}
Requires:	%{libcodecparsers} = %{version}-%{release}
Requires:	%{libgl} = %{EVRD}
Requires:	%{libinsertbin} = %{version}-%{release}
Requires:	%{libbadbase} = %{version}-%{release}
Requires:	%{libbadvideo} = %{version}-%{release}
Requires:	%{libgstwayland} = %{version}-%{release}
Requires:	%{libmpegts} = %{version}-%{release}
Requires:	%{liburidownloader} = %{version}-%{release}
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
Requires:	%{bname}-plugins-base
BuildRequires:	pkgconfig(libmms)

%description -n %{bname}-mms
Plug-in supporting the mms protocol based on the libmms library.

%files -n %{bname}-mms
%{_libdir}/gstreamer-%{api}/libgstmms.so

%package -n %{bname}-rtmp
Summary:	GStreamer plug-in for rtmp streams
Group:		System/Libraries
Requires:	%{bname}-plugins-base
BuildRequires:	pkgconfig(librtmp)

%description -n %{bname}-rtmp
Plug-in supporting the rtmp protocol based on the librtmp library.

%files -n %{bname}-rtmp
%{_libdir}/gstreamer-%{api}/libgstrtmp.so

%package -n %{bname}-soundtouch
Summary:	GStreamer plug-in for SoundTouch support
Group:		Sound
Requires:	%{bname}-plugins-base
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

%package -n %{bname}-opencv
Summary:	GStreamer OpenCV Plugins
Group:		Video

%description -n %{bname}-opencv
GStreamer OpenCV Plugins.

%files -n %{bname}-opencv
%{_libdir}/gstreamer-%{api}/libgstopencv.so
%{_datadir}/gst-plugins-bad/%{api}/opencv_haarcascades/*.xml

%if %{build_faad}
%package -n %{bname}-faad
Summary:	GStreamer plug-in for AAC audio playback
Group:		Sound
Requires:	%{bname}-plugins-base
BuildRequires:	faad2-devel

%description -n %{bname}-faad
Plug-ins for playing AAC audio

This package is in restricted repository as it violates some patents.
%endif

%if %{build_faac}
%package -n %{bname}-faac
Summary:	GStreamer plug-ins for AAC audio encoding
Group:		Sound
Requires:	%{bname}-plugins-base
BuildRequires:	faac-devel

%description -n %{bname}-faac
Plug-ins for encoding AAC audio

This package is in restricted repository as it violates some patents.
%endif

%package -n %{bname}-gsm
Summary:	GStreamer plugin for GSM lossy audio format
Group:		Sound
Requires:	%{bname}-plugins-base
BuildRequires:	gsm-devel >= 1.0.10

%description -n %{bname}-gsm
Output plugin for GStreamer to convert to GSM lossy audio format.

%if 0
### SWFDEC FLASH PLUGIN ###
%package -n %{bname}-swfdec
Summary:	GStreamer Flash rendering plug-in
Group:		System/Libraries
Requires:	%{bname}-plugins-base
BuildRequires:	libswfdec-devel => 0.3.0

%description -n %{bname}-swfdec
Plug-in for rendering Flash animations using swfdec library
%endif

%if %{build_amrwb}
%package -n %{bname}-amrwb
Summary:	GStreamer plug-in for AMR-WB support
Group:		Sound
Requires:	%{bname}-plugins-base
BuildRequires:	pkgconfig(opencore-amrwb)

%description -n %{bname}-amrwb
Plug-in for decoding AMR-WB under GStreamer.

This package is in restricted repository as it violates some patents.
%endif

%package -n %{girname}
Group:		System/Libraries
Summary:	Object Introspection interface description for %{name}
Requires:	%{libgl} = %{version}
Requires:	%{libinsertbin} = %{version}
Requires:	%{libmpegts} = %{version}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q
%apply_patches

%build
export CC=gcc
export CXX=g++
%configure \
	--disable-static \
	--disable-directfb \
	--with-package-name='OpenMandriva %{name} package' \
	--with-package-origin='http://www.openmandriva.org/' \
	--with-gtk=3.0 \
%if ! %{build_faac}
	--disable-faac \
%endif
%if ! %{build_faad}
	--disable-faad \
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
%{_libdir}/gstreamer-%{api}/libgstchromaprint.so
%{_libdir}/gstreamer-%{api}/libgstcoloreffects.so
%{_libdir}/gstreamer-%{api}/libgstdataurisrc.so
%{_libdir}/gstreamer-%{api}/libgstdebugutilsbad.so
%{_libdir}/gstreamer-%{api}/libgstdvb.so
%{_libdir}/gstreamer-%{api}/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-%{api}/libgstdvdspu.so
%{_libdir}/gstreamer-%{api}/libgstfieldanalysis.so
%{_libdir}/gstreamer-%{api}/libgstfestival.so
%{_libdir}/gstreamer-%{api}/libgstfluidsynthmidi.so
%{_libdir}/gstreamer-%{api}/libgstfragmented.so
%{_libdir}/gstreamer-%{api}/libgstfrei0r.so
%{_libdir}/gstreamer-%{api}/libgstgaudieffects.so
%{_libdir}/gstreamer-%{api}/libgstgdp.so
%{_libdir}/gstreamer-%{api}/libgstgeometrictransform.so
%{_libdir}/gstreamer-%{api}/libgstid3tag.so
%{_libdir}/gstreamer-%{api}/libgstinter.so
%{_libdir}/gstreamer-%{api}/libgstinterlace.so
%{_libdir}/gstreamer-%{api}/libgstjpegformat.so
%{_libdir}/gstreamer-%{api}/libgstkate.so
%{_libdir}/gstreamer-%{api}/libgstladspa.so
%{_libdir}/gstreamer-%{api}/libgstliveadder.so
%{_libdir}/gstreamer-%{api}/libgstmpegtsmux.so
%{_libdir}/gstreamer-%{api}/libgstmpg123.so
%{_libdir}/gstreamer-%{api}/libgstmimic.so
%{_libdir}/gstreamer-%{api}/libgstmpegpsdemux.so
%{_libdir}/gstreamer-%{api}/libgstneonhttpsrc.so
%{_libdir}/gstreamer-%{api}/libgstofa.so
%{_libdir}/gstreamer-%{api}/libgstopenjpeg.so
%{_libdir}/gstreamer-%{api}/libgstopus.so
%{_libdir}/gstreamer-%{api}/libgstpcapparse.so
%{_libdir}/gstreamer-%{api}/libgstpnm.so
%{_libdir}/gstreamer-%{api}/libgstrawparse.so
%{_libdir}/gstreamer-%{api}/libgstremovesilence.so
%{_libdir}/gstreamer-%{api}/libgstresindvd.so
%{_libdir}/gstreamer-%{api}/libgstrsvg.so
%{_libdir}/gstreamer-%{api}/libgstsbc.so
%{_libdir}/gstreamer-%{api}/libgstsdpelem.so
%{_libdir}/gstreamer-%{api}/libgstsegmentclip.so
%{_libdir}/gstreamer-%{api}/libgstshm.so
%{_libdir}/gstreamer-%{api}/libgstsiren.so
%{_libdir}/gstreamer-%{api}/libgstsmooth.so
%{_libdir}/gstreamer-%{api}/libgstspeed.so
%{_libdir}/gstreamer-%{api}/libgstsubenc.so
%{_libdir}/gstreamer-%{api}/libgstbz2.so
%{_libdir}/gstreamer-%{api}/libgstmpegpsmux.so
%{_libdir}/gstreamer-%{api}/libgstmpegtsdemux.so
%{_libdir}/gstreamer-%{api}/libgstuvch264.so
%{_libdir}/gstreamer-%{api}/libgstvdpau.so
%{_libdir}/gstreamer-%{api}/libgstvideoparsersbad.so
%{_libdir}/gstreamer-%{api}/libgstwaylandsink.so
%{_libdir}/gstreamer-%{api}/libgstwebp.so
%{_libdir}/gstreamer-%{api}/libgstwildmidi.so
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
%{_libdir}/gstreamer-%{api}/libgstaccurip.so
%{_libdir}/gstreamer-%{api}/libgstaiff.so
%{_libdir}/gstreamer-%{api}/libgstaudiofxbad.so
%{_libdir}/gstreamer-%{api}/libgstdashdemux.so
%{_libdir}/gstreamer-%{api}/libgstdecklink.so
%{_libdir}/gstreamer-%{api}/libgstaudiomixer.so
%{_libdir}/gstreamer-%{api}/libgstfbdevsink.so
%{_libdir}/gstreamer-%{api}/libgstfreeverb.so
%{_libdir}/gstreamer-%{api}/libgstivtc.so
%{_libdir}/gstreamer-%{api}/libgstmidi.so
%{_libdir}/gstreamer-%{api}/libgstmxf.so
%{_libdir}/gstreamer-%{api}/libgstopenal.so
%{_libdir}/gstreamer-%{api}/libgstrfbsrc.so
%{_libdir}/gstreamer-%{api}/libgstsmoothstreaming.so
%{_libdir}/gstreamer-%{api}/libgstspandsp.so
%{_libdir}/gstreamer-%{api}/libgstvideofiltersbad.so
%{_libdir}/gstreamer-%{api}/libgstyadif.so
%{_libdir}/gstreamer-%{api}/libgstcompositor.so
%{_libdir}/gstreamer-%{api}/libgstivfparse.so
%{_libdir}/gstreamer-%{api}/libgstjp2kdecimator.so
%{_libdir}/gstreamer-%{api}/libgstopenexr.so
%{_libdir}/gstreamer-%{api}/libgstopengl.so
%{_libdir}/gstreamer-%{api}/libgstsndfile.so
%{_libdir}/gstreamer-%{api}/libgststereo.so
%{_libdir}/gstreamer-%{api}/libgstvideosignal.so
%{_libdir}/gstreamer-%{api}/libgstvmnc.so
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

%files -n %{libbasecamerabinsrc}
%{_libdir}/libgstbasecamerabinsrc-%{api}.so.%{major}*

%files -n %{libphotography}
%{_libdir}/libgstphotography-%{api}.so.%{major}*

%files -n %{libcodecparsers}
%{_libdir}/libgstcodecparsers-%{api}.so.%{major}*

%files -n %{libgl}
%{_libdir}/libgstgl-%{api}.so.%{major}*

%files -n %{libinsertbin}
%{_libdir}/libgstinsertbin-%{api}.so.%{major}*

%files -n %{libmpegts}
%{_libdir}/libgstmpegts-%{api}.so.%{major}*

%files -n %{liburidownloader}
%{_libdir}/libgsturidownloader-%{api}.so.%{major}*

%files -n %{libbadbase}
%{_libdir}/libgstbadbase-%{api}.so.%{major}*

%files -n %{libbadvideo}
%{_libdir}/libgstbadvideo-%{api}.so.%{major}*

%files -n %{libgstwayland}
%{_libdir}/libgstwayland-%{api}.so.%{major}*

%files -n %{devname}
%doc docs/plugins/html
%doc %{_datadir}/gtk-doc/html/
%{_libdir}/libgstbasecamerabinsrc-%{api}.so
%{_libdir}/libgstcodecparsers-%{api}.so
%{_libdir}/libgstphotography-%{api}.so
%{_libdir}/libgstinsertbin-%{api}.so
%{_libdir}/libgstmpegts-%{api}.so
%{_libdir}/libgsturidownloader-%{api}.so
%{_libdir}/libgstbadbase-%{api}.so
%{_libdir}/libgstbadvideo-%{api}.so
%{_libdir}/libgstwayland-%{api}.so
%{_libdir}/libgstgl-%{api}.so
%{_includedir}/gstreamer-%{api}/gst/basecamerabinsrc/
%{_includedir}/gstreamer-%{api}/gst/codecparsers/
%{_includedir}/gstreamer-%{api}/gst/gl/
%{_includedir}/gstreamer-%{api}/gst/interfaces/photography*
%{_includedir}/gstreamer-%{api}/gst/insertbin
%{_includedir}/gstreamer-%{api}/gst/mpegts
%{_includedir}/gstreamer-%{api}/gst/uridownloader
%{_datadir}/gir-1.0/GstInsertBin-%{api}.gir
%{_datadir}/gir-1.0/GstMpegts-%{api}.gir
%{_libdir}/pkgconfig/gstreamer-plugins-bad-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-codecparsers-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-gl-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-insertbin-%{api}.pc
%{_libdir}/pkgconfig/gstreamer-mpegts-%{api}.pc

%files -n %{girname}
%{_libdir}/girepository-1.0/GstInsertBin-%{api}.typelib
%{_libdir}/girepository-1.0/GstMpegts-%{api}.typelib

