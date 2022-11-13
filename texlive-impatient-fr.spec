Name:		texlive-impatient-fr
Version:	54080
Release:	1
Summary:	Free edition of the book "TeX for the Impatient"
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/impatient
License:	FDL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impatient-fr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/impatient-fr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
This directory mirrors the canonical source of the project
which is maintaining the book "TeX for the Impatient", which is
now out of print. The book is also available in French
translation.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/plain/impatient-fr/README
%doc %{_texmfdistdir}/doc/plain/impatient-fr/config.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/eplain.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fbackm.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fbook.pdf
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fbook.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fcapsule.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fconcept.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fcopyrgh.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fdl.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/ferrors.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fexamples.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/ffrontm.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fgenops.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fmacros.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fmath.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fmodes.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fonts.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fpages.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fparas.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fpreface.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fread1st.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/ftips.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fusebook.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fusermacs.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fusingtex.tex
%doc %{_texmfdistdir}/doc/plain/impatient-fr/fxmptext.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
