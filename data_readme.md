## Data information:

To find the list of firms that you will study, download the Data_Excel folder and either in the MSCI folder if your group studies ESG scores and in the Trucost folder if your group studies CO2 emissions. Then you can will restrict to the list of firms based on the country of interest of your group (using the ISIN you can identify the firm’s country) or sector (information related to the sector of each firm is available in the Trucost folder)

## Trucost

-	DataF.TC_Scope1, DataF.TC_Scope2, DataF.TC_Scope3 DataF.TC_Scope1Intensity, DataF.TC_Scope2Intensity, DataF.TC_Scope3Intensity  (https://www.spglobal.com/marketintelligence/en/documents/trucost_general_fi_brochure_20200602_final.pdf ; https://www.spglobal.com/spdji/en/documents/additional-material/faq-trucost.pdf )
-	DataF.TC_Country: ISIN, name, Country
-	DataF.Region: ISIN, name, Region
-	DataF.TC_GICS: ISIN, name, Sector, Industry group, Industry, Subindustry
-	DataF.DS_RI_T_USD_M: ISIN, name, monthly total return index (price including dividends) from 31/12/1999 to 31/12/2020 all in USD
-	DataF.DS_MV_USD_M (monthly market value in million USD): can be used to compute value weights in the portfolio
-	Accounting data: DS_DY (dividend yield), DS_PE (price earnings ratio), DS_MTBV (market to book value), DS_ROA return on assets, DS_ROE return on equity


## Folder MSCI_ESGFF: (FF structure) contains Fama-French factors for each available zone, with 3 factors (market, smb for small minus big, hml for high minus low), momentum factor, and also risk-free rates (https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html)

-	ESG scores https://www.msci.com/documents/1296102/21901542/MSCI+ESG+Ratings+Methodology+-+Exec+Summary+Nov+2020.pdf

-	Monthly returns (including dividends) for all firms

-	Fundamentals: Accounting variables: DivYield, PE (price earnings ratio), PBV (price to book value), ROA return on assets, ROE return on equity, MV (market value in USD)

-	Static variables: ISIN, Name, Country, Sector


