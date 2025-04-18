# SDSSV_DR19_QSO_VAC

We have measured detailed spectral parameters of DR19 quasars using the latest version of [PyQSOFit](https://github.com/legolason/PyQSOFit) with host decomposition priors. Visual inspection is applied before the catalog is compiled.

## Tutorials
[Tutorial on how to read this VAC](https://github.com/QiaoyaWu/SDSSV_DR19_QSO_VAC/blob/main/how_to_use_the_VAC.ipynb)

[Tutorial on how to visualize a single spectral fits file](https://github.com/QiaoyaWu/SDSSV_DR19_QSO_VAC/blob/main/how_to_access_fits.ipynb)

## Systematic redshift
We applied the same recipe as described in the [SDSS DR16Q catalog](https://iopscience.iop.org/article/10.3847/1538-4365/ac9ead/meta) and [DESI EDR catalog](https://iopscience.iop.org/article/10.3847/2515-5172/acf580/meta). (There might be future updates on the method, especially for low-$z$ objects.)

![The composite spectra for large velocity discrepancy objects]([https://github.com/QiaoyaWu/SDSSV_DR19_QSO_VAC/blob/main/composite_spec.jpg)

![https://github.com/QiaoyaWu/SDSSV_DR19_QSO_VAC/blob/main/zhist.jpg](The histogram of the systematic redshift. | width=100)


## Catalog format description
The catalog format is similar to the [SDSS DR16Q](https://github.com/QiaoyaWu/sdss4_dr16q_tutorial/tree/main).

| Column | Description |
| ---- | ------ |
| `FIELD` | SDSS-V object spectroscopic field |
| `MJD` | SDSS-V object spectroscopic MJD |
| `CATALOGID` | SDSS-V object catalog ID |
| `FITS_FILE` | FIELD-MJD-CATALOGID the output fits file name |
| `VERSION` | v6_1_3 |
| `RA` | Right ascension (J2000) |
| `DEC` | Declination (J2000) |
| `NEXP` | Number of exposure |
| `EXPTIME` | Exposure time |
| `PROGRAMNAME` | Program name |
| `SURVEY` | Survey type|
| `Z_PIPE` | Pipeline generated redshift |
| `FIRSTCARTON` | Object type |
| `OBJTYPE` | Object type |
| `CLASS` | Object type |
| `SUBCLASS` | Object type |
| `VI_REMARK` | Visual inspection marks |
| `Z_VI` | Visual inspection redshift |
| `Z_FIT` | Redshift for PyQSOFit |
| `Z_SYS` | Systemartic redshift |
| `Z_SYS_ERR` | Systemartic redshift err |
| `SN_RATIO_CONTI` | SNR computed at continuum |
| `EBV` | Milky Way extinction E(B − V) |
| `CONTI_PARA` | Best-fit parameters for the continuum model |
| `CONTI_PARA_ERR` | Uncertainties in the best-fit parameters for the continuum model |
| `FE_UV_PARA` | Best-fit parameters for the UV FeII model |
| `FE_UV_PARA_ERR` | Uncertainties in the best-fit parameters for the UV FeII model |
| `FE_OP_PARA` | Best-fit parameters for the optical FeII model |
| `FE_OP_PARA_ERR` | Uncertainties in the best-fit parameters for the optical FeII model |
| `LOGL1350` | Continuum luminosity at rest-frame 1350Å |
| `LOGL1350_ERR` | Uncertainties of the continuum luminosity at rest-frame 1350Å |
| `LOGL1700` | ... |
| `LOGL1700_ERR` | ... |
| `LOGL2500` | ... |
| `LOGL2500_ERR` | ... |
| `LOGL3000` | ... |
| `LOGL3000_ERR` | ... |
| `LOGL4200` | ... |
| `LOGL4200_ERR` | ... |
| `LOGL5100` | ... |
| `LOGL5100_ERR` | ... |
| `CONTI_NPIX` | Pixel number of the continuum fitting |
| `FRAC_HOST_4200` | Host galaxy flux fraction at 4200Å |
| `FRAC_HOST_5100` | Host galaxy flux fraction at 5100Å |
| `DN4000` | 4000Å break index |
| `HOST_DECOMP_PARA` | The host galaxy decomposition eigenvalues |
| | peak wavelength, flux, logL of lines, FWHM, rest-frame equivalent width, 50% flux centoid wavelength |
| `HALPHA` |  |
| `HALPHA_ERR` |  |
| `HALPHA_BR` |  |
| `HALPHA_BR_ERR` |  |
| `HALPHA_NA` |  |
| `HALPHA_NA_ERR` |  |
| `NII6549` |  |
| `NII6549_ERR` |  |
| `NII6585` |  |
| `NII6585_ERR` |  |
| `SII6718` |  |
| `SII6718_ERR` |  |
| `SII6732` |  |
| `SII6732_ERR` |  |
| `HBETA` |  |
| `HBETA_ERR` |  |
| `HBETA_BR` |  |
| `HBETA_BR_ERR` |  |
| `HEII4687` |  |
| `HEII4687_ERR` |  |
| `HEII4687_BR` |  |
| `HEII4687_BR_ERR` |  |
| `OIII5007` |  |
| `OIII5007_ERR` |  |
| `OIII5007C` |  |
| `OIII5007C_ERR` |  |
| `OIII4960` |  |
| `OIII4960_ERR` |  |
| `OIII4960C` |  |
| `OIII4960C_ERR` |  |
| `HGAMMA` |  |
| `HGAMMA_ERR` |  |
| `HDELTA` |  |
| `HDELTA_ERR` |  |
| `CAII3934` |  |
| `CAII3934_ERR` |  |
| `OII3728` |  |
| `OII3728_ERR` |  |
| `NEV3426` |  |
| `NEV3426_ERR` |  |
| `MGII` |  |
| `MGII_ERR` |  |
| `MGII_BR` |  |
| `MGII_BR_ERR` |  |
| `CIII_BR` |  |
| `CIII_BR_ERR` |  |
| `SIIII1892` |  |
| `SIIII1892_ERR` |  |
| `ALIII1857` |  |
| `ALIII1857_ERR` |  |
| `NIII1750` |  |
| `NIII1750_ERR` |  |
| `CIV` |  |
| `CIV_ERR` |  |
| `HEII1640` |  |
| `HEII1640_ERR` |  |
| `HEII1640_BR` |  |
| `HEII1640_BR_ERR` |  |
| `SIIV_OIV` |  |
| `SIIV_OIV_ERR` |  |
| `OI1304` |  |
| `OI1304_ERR` |  |
| `LYA` |  |
| `LYA_ERR` |  |
| `NV1240` |  |
| `NV1240_ERR` |  |
| `Ha_STAT` | Complex line window pixel number, reduced chi square |
| `Hb_STAT` |  |
| `Hr_STAT` |  |
| `Hd_STAT` |  |
| `MgII_STAT` |  |
| `CIII_STAT` |  |
| `CIV_STAT` |  |
| `SiIV_STAT` |  |
| `Lya_STAT` |  |
| `CaII_STAT` |  |
| `OII_STAT` |  |
| `NeV_STAT` |  |
| `LOGLBOL` | Bolometric luminosity |
| `LOGLBOL_ERR` |  |
| `LOGMBH_HB` | Single-epoch BH mass using Hbeta |
| `LOGMBH_HB_ERR` |  |
| `LOGMBH_MGII` | Single-epoch BH mass using MgII |
| `LOGMBH_MGII_ERR` |  |
| `LOGMBH_CIV` | Single-epoch BH mass using CIV |
| `LOGMBH_CIV_ERR` |  |
| `LOGMBH` | Single-epoch BH mass |
| `LOGMBH_ERR` |  |
| `LOGLLEDD_RATIO` | Eddington ratio |
| `LOGLLEDD_RATIO_ERR` |  |
| `ZSYS_BEST` | Systematic redshift from the line zsys with the lowest errorbar |
| `ZSYS_BEST_ERR` |  |
| `ZSYS_WEIGHT` | Systematic redshift from the weighted mean |
| `ZSYS_WEIGHT_ERR` |  |
| `ZSYS_LINES` | Systematic redshift from Hβ_BR, [OIII]5007, CaII3934, [OII]3728, MgII, CIII], CIV, SiIV |
| `ZSYS_LINES_ERR` |  |
