# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/clrscode
# catalog-date 2007-03-29 23:17:09 +0200
# catalog-license lppl
# catalog-version 1.7
Name:		texlive-clrscode
Version:	1.7
Release:	6
Summary:	Typesets pseudocode as in Introduction to Algorithms
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/clrscode
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrscode.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/clrscode.doc.tar.xz
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
%{_texmfdistdir}/tex/latex/clrscode/clrscode.sty
%doc %{_texmfdistdir}/doc/latex/clrscode/README
%doc %{_texmfdistdir}/doc/latex/clrscode/clrscode.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.7-2
+ Revision: 750255
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.7-1
+ Revision: 718072
- texlive-clrscode
- texlive-clrscode
- texlive-clrscode
- texlive-clrscode
- texlive-clrscode

