# revision 17157
# category Package
# catalog-ctan /macros/latex/contrib/chngcntr
# catalog-date 2010-03-09 12:54:42 +0100
# catalog-license lppl
# catalog-version 1.0a
Name:		texlive-chngcntr
Version:	1.0a
Release:	10
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-2
+ Revision: 750180
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 718057
- texlive-chngcntr
- texlive-chngcntr
- texlive-chngcntr
- texlive-chngcntr
- texlive-chngcntr

