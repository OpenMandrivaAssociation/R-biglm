%global packname  biglm
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9.1
Release:          1
Summary:          bounded memory linear and generalized linear models
Group:            Sciences/Mathematics
License:          GPL
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/biglm_0.9-1.tar.gz
Requires:         R-DBI R-methods 
Requires:         R-RSQLite R-RODBC 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-DBI R-methods
BuildRequires:    R-RSQLite R-RODBC 

%description
Regression for data too large to fit in memory

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
