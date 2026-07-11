%global tl_name clrscode
%global tl_revision 51136

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.7
Release:	%{tl_revision}.1
Summary:	Typesets pseudocode as in Introduction to Algorithms
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/clrscode
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clrscode.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/clrscode.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows you to typeset pseudocode in the style of
Introduction to Algorithms, Second edition, by Cormen, Leiserson,
Rivest, and Stein. The package was written by the authors. You use the
commands the same way the package's author did when writing the book,
and your output will look just like the pseudocode in the text.

