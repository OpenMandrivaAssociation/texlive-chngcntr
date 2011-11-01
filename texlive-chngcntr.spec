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
Requires(post):	texlive-tlpkg
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
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/chngcntr/chngcntr.sty
%doc %{_texmfdistdir}/doc/latex/chngcntr/chngcntr.pdf
%doc %{_texmfdistdir}/doc/latex/chngcntr/chngcntr.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
