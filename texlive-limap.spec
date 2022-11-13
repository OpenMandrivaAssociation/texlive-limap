Name:		texlive-limap
Version:	44863
Release:	1
Summary:	Typeset maps and blocks according to the Information Mapping method
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gene/limap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/limap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/limap.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/limap
#- source
%doc %{_texmfdistdir}/source/latex/limap

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex source %{buildroot}%{_texmfdistdir}
