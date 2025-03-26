Name:		python-pdfminer-six
Version:	20250324
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pdfminer-six/pdfminer.six-%{version}.tar.gz
Summary:	PDF parser and analyzer
URL:		https://pypi.org/project/pdfminer-six/
License:	MIT
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch
Provides:	python%{pyver}dist(pdfminer-six) = %{version}

%description
PDF parser and analyzer

%files
%{_bindir}/dumppdf.py
%{_bindir}/pdf2txt.py
%{py_puresitedir}/pdfminer
%{py_puresitedir}/pdfminer.six-*.*-info
