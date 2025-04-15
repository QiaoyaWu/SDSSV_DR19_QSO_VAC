# SDSSV_DR19_QSO_VAC

We have measured detailed spectral parameters of DR19 quasars using the lastest version of [PyQSOFit](https://github.com/legolason/PyQSOFit) with host deomposition priors. Visual inspection is applied before the compilation of catalog.

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
| `CONTI_PARA` |  |
| `CONTI_PARA_ERR` |  |
| `FE_UV_PARA` |  |
| `FE_UV_PARA_ERR` |  |
| `FE_OP_PARA` |  |
| `FE_OP_PARA_ERR` |  |
| `LOGL1350` |  |
| `LOGL1350_ERR` |  |
| `LOGL1700` |  |
| `LOGL1700_ERR` |  |
| `LOGL2500` |  |
| `LOGL2500_ERR` |  |
| `LOGL3000` |  |
| `LOGL3000_ERR` |  |
| `LOGL4200` |  |
| `LOGL4200_ERR` |  |
| `LOGL5100` |  |
| `LOGL5100_ERR` |  |
| `CONTI_NPIX` |  |
| `FRAC_HOST_4200` |  |
| `FRAC_HOST_5100` |  |
| `DN4000` |  |
| `HOST_DECOMP_PARA` |  |
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
| `Ha_STAT` |  |
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
| `LOGLBOL` |  |
| `LOGLBOL_ERR` |  |
| `LOGMBH_HB` |  |
| `LOGMBH_HB_ERR` |  |
| `LOGMBH_MGII` |  |
| `LOGMBH_MGII_ERR` |  |
| `LOGMBH_CIV` |  |
| `LOGMBH_CIV_ERR` |  |
| `LOGMBH` |  |
| `LOGMBH_ERR` |  |
| `LOGLLEDD_RATIO` |  |
| `LOGLLEDD_RATIO_ERR` |  |
| `ZSYS_BEST` |  |
| `ZSYS_BEST_ERR` |  |
| `ZSYS_WEIGHT` |  |
| `ZSYS_WEIGHT_ERR` |  |
| `ZSYS_LINES` |  |
| `ZSYS_LINES_ERR` |  |
