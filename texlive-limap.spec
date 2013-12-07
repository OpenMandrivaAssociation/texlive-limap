# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gene/limap
# catalog-date 2007-01-08 23:14:30 +0100
# catalog-license lppl
# catalog-version undef
Name:		texlive-limap
Version:	20070108
Release:	4
Summary:	Typeset maps and blocks according to the Information Mapping method
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gene/limap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/limap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/limap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The Information Mapping method provides a methodology for
structuring and presenting information. It claims to be useful
for readers who are more concerned about finding the right
information than reading the document as a whole. Thus short,
highly structured, and context free pieces of information are
used. A LaTeX style and a LaTeX class are provided. The style
contains definitions to typeset maps and blocks according to
the Information Mapping method. The class provides all
definitions to typeset a whole document.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/limap/limap.cls
%{_texmfdistdir}/tex/latex/limap/limap.sty
#- source
%doc %{_texmfdistdir}/source/latex/limap/Makefile
%doc %{_texmfdistdir}/source/latex/limap/limap.dtx
%doc %{_texmfdistdir}/source/latex/limap/limap.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070108-2
+ Revision: 753309
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070108-1
+ Revision: 718859
- texlive-limap
- texlive-limap
- texlive-limap
- texlive-limap

