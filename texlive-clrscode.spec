Name:		texlive-clrscode
Version:	51136
Release:	1
Summary:	Typesets pseudocode as in Introduction to Algorithms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clrscode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrscode.r51136.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrscode.doc.r51136.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows you to typeset pseudocode in the style of
Introduction to Algorithms, Second edition, by Cormen,
Leiserson, Rivest, and Stein. The package was written by the
authors. You use the commands the same way the package's author
did when writing the book, and your output will look just like
the pseudocode in the text.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/clrscode
%doc %{_texmfdistdir}/doc/latex/clrscode

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
