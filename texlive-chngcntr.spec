# revision 17157
# category Package
# catalog-ctan /macros/latex/contrib/chngcntr
# catalog-date 2010-03-09 12:54:42 +0100
# catalog-license lppl
# catalog-version 1.0a
Name:		texlive-chngcntr
Version:	1.0a
Release:	1
Summary:	Change the resetting of counters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/chngcntr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chngcntr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chngcntr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Defines commands \counterwithin (which sets up a counter to be
reset when another is incremented) and \counterwithout (which
unsets such a relationship).

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chngcntr/chngcntr.sty
%doc %{_texmfdistdir}/doc/latex/chngcntr/chngcntr.pdf
%doc %{_texmfdistdir}/doc/latex/chngcntr/chngcntr.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
