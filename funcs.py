#!/usr/bin/python3
import os,sys,time
import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt
import warnings
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
from astropy.table import Table
from matplotlib.ticker import MultipleLocator
warnings.filterwarnings("ignore")
from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
from wand.image import Image as WImage
from astropy.modeling.physical_models import BlackBody
from scipy import interpolate
from scipy import integrate
from astropy import constants as const
from astropy import units as u

fe_uv = np.genfromtxt('/home/qiaoyaw2/package/PyQSOFit_v2/src/pyqsofit/fe_uv.txt')
fe_op = np.genfromtxt('/home/qiaoyaw2/package/PyQSOFit_v2/src/pyqsofit/fe_optical.txt')

def Manygauss(xval, pp):
    """ Multiple Gaussian model used to fit the emission lines
    pp=[scale1, center1, sigma1, scale2, center2, sigma2, ...]
    xx in log wavelength space
    """
    return np.sum(pp[:, 0] * np.exp(-(xval[:, np.newaxis] - pp[:, 1]) ** 2 / (2 * pp[:, 2] ** 2)), axis=1)

def PowerLaw(xval, pp):
    return pp[0]*(xval/3000.0)**pp[1]

def PolyConti(xval, pp, x0=3000):
    xval2 = xval - x0
    yvals = [(pp[i] / 1e6) * xval2 ** (i + 1) for i in range(len(pp))]
    return np.sum(yvals, axis=0)

def BalmerConti(xval, pp):
    """Fit the Balmer continuum from the model of Dietrich+02"""
    # xval = input wavelength, in units of A
    # pp=[norm, Te, tau_BE] -- in units of [--, K, --]
    xval = xval * u.AA
    lambda_BE = 3646.  # A
    bb_lam = BlackBody(pp[1] * u.K, scale=1.0 * u.erg / (u.cm ** 2 * u.AA * u.s * u.sr))
    bbflux = bb_lam(xval).value * 3.14  # in units of ergs/cm2/s/A
    tau = pp[2] * (xval.value / lambda_BE) ** 3
    result = pp[0] * bbflux * (1 - np.exp(-tau))
    ind = np.where(xval.value > lambda_BE, True, False)
    if ind.any() == True:
        result[ind] = 0
    return result

def FeII_uv_Conti(xval, pp):
        "Fit the UV FeII component on the continuum from 1200 to 3500 A based on Boroson & Green 1992."
        yval = np.zeros_like(xval)
        wave_Fe_mgii = 10 ** fe_uv[:, 0]
        flux_Fe_mgii = fe_uv[:, 1] * 1e15
        Fe_FWHM = pp[1]
        xval_new = xval * (1.0 + pp[2])

        ind = np.where((xval_new > 1200.) & (xval_new < 3500.), True, False)
        if np.sum(ind) > 100:
            if Fe_FWHM < 900.0:
                sig_conv = np.sqrt(910.0 ** 2 - 900.0 ** 2) / 2. / np.sqrt(2. * np.log(2.))
            else:
                sig_conv = np.sqrt(Fe_FWHM ** 2 - 900.0 ** 2) / 2. / np.sqrt(2. * np.log(2.))  # in km/s
            # Get sigma in pixel space
            sig_pix = sig_conv / 106.3  # 106.3 km/s is the dispersion for the BG92 FeII template
            khalfsz = np.round(4 * sig_pix + 1, 0)
            xx = np.arange(0, khalfsz * 2, 1) - khalfsz
            kernel = np.exp(-xx ** 2 / (2 * sig_pix ** 2))
            kernel = kernel / np.sum(kernel)

            flux_Fe_conv = np.convolve(flux_Fe_mgii, kernel, 'same')
            tck = interpolate.splrep(wave_Fe_mgii, flux_Fe_conv)
            yval[ind] = pp[0] * interpolate.splev(xval_new[ind], tck)
        return yval

def FeII_opt_Conti(xval, pp):
        "Fit the optical FeII on the continuum from 3686 to 7484 A based on Vestergaard & Wilkes 2001"
        yval = np.zeros_like(xval)

        wave_Fe_balmer = 10 ** fe_op[:, 0]
        flux_Fe_balmer = fe_op[:, 1] * 1e15
        ind = np.where((wave_Fe_balmer > 3686.) & (wave_Fe_balmer < 7484.), True, False)
        wave_Fe_balmer = wave_Fe_balmer[ind]
        flux_Fe_balmer = flux_Fe_balmer[ind]
        Fe_FWHM = pp[1]
        xval_new = xval * (1.0 + pp[2])
        ind = np.where((xval_new > 3686.) & (xval_new < 7484.), True, False)
        if np.sum(ind) > 100:
            if Fe_FWHM < 900.0:
                sig_conv = np.sqrt(910.0 ** 2 - 900.0 ** 2) / 2. / np.sqrt(2. * np.log(2.))
            else:
                sig_conv = np.sqrt(Fe_FWHM ** 2 - 900.0 ** 2) / 2. / np.sqrt(2. * np.log(2.))  # in km/s
            # Get sigma in pixel space
            sig_pix = sig_conv / 106.3  # 106.3 km/s is the dispersion for the BG92 FeII template
            khalfsz = np.round(4 * sig_pix + 1, 0)
            xx = np.arange(0, khalfsz * 2, 1) - khalfsz
            kernel = np.exp(-xx ** 2 / (2 * sig_pix ** 2))
            kernel = kernel / np.sum(kernel)
            flux_Fe_conv = np.convolve(flux_Fe_balmer, kernel, 'same')
            tck = interpolate.splrep(wave_Fe_balmer, flux_Fe_conv)
            yval[ind] = pp[0] * interpolate.splev(xval_new[ind], tck)
        return yval

def continuum_all(wave_val, conti_ip_val):
    return PowerLaw(wave_val, conti_ip_val[0:2])\
        + PolyConti(wave_val, conti_ip_val[2:5])\
        + FeII_uv_Conti(wave_val, conti_ip_val[5:8])\
        + FeII_opt_Conti(wave_val, conti_ip_val[8:])

def continuum_PL_poly(wave_val, conti_ip_val):
    return PowerLaw(wave_val, conti_ip_val[0:2])\
        + PolyConti(wave_val, conti_ip_val[2:5])

def qsofit_op_flux(op_data, op_spec_wave):
    conti_keyword = ['PL_norm', 'PL_slope', 'conti_a_0', 'conti_a_1', 'conti_a_2',\
                 'Fe_uv_norm', 'Fe_uv_FWHM', 'Fe_uv_shift', 'Fe_op_norm', 'Fe_op_FWHM', 'Fe_op_shift']
    conti_ip_val = np.array([op_data[conti_keyword[i]] for i in range(len(conti_keyword))])
    conti_flux = continuum_all(op_spec_wave, conti_ip_val)
    
    gaussian_lines = np.array([kw[:-11] for kw in op_data.names if ('centerwave' in kw) and ('err' not in kw) and ('OII3728' not in kw) and ('CaII3934' not in kw) and ('NeV3426' not in kw)])
    gaussian_pp = np.zeros((len(gaussian_lines), 3))
    for i in range(len(gaussian_lines)):
        gaussian_pp[i, 0] = op_data[gaussian_lines[i]+'_scale']
        gaussian_pp[i, 1] = op_data[gaussian_lines[i] + '_centerwave']
        gaussian_pp[i, 2] = op_data[gaussian_lines[i] + '_sigma']
    gaussian_flux = Manygauss(np.log(op_spec_wave), gaussian_pp)

    return conti_flux, gaussian_flux