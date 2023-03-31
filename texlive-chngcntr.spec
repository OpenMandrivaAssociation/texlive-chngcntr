Name:		texlive-chngcntr
Version:	47577
Release:	2
Summary:	Change the resetting of counters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chngcntr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chngcntr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chngcntr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines commands \counterwithin (which sets up a counter to be
reset when another is incremented) and \counterwithout (which
unsets such a relationship).

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chngcntr
%doc %{_texmfdistdir}/doc/latex/chngcntr

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
