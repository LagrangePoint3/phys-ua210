#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:42:20 2023

@author: zhaoyilin
"""

import astropy.io.fits
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
from numpy.linalg import eigh
from numpy.linalg import eig
from numpy.linalg import solve
from scipy.linalg import svd
from numpy import linalg as LA
import time


hdu_list = astropy.io.fits.open('specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data

# Part a)
# Make a plot for the first 4 galaxies
plt.figure(figsize = (10,6))
plt.plot(logwave, flux[0], label = "Galaxy 1")
plt.plot(logwave, flux[1], label = "Galaxy 2")
plt.plot(logwave, flux[2], label = "Galaxy 3")
plt.plot(logwave, flux[3], label = "Galaxy 4")
plt.title("Flux from different galaxies versus Wavelength")
plt.xlabel("$wavelength(\log_{10}{\lambda})~10^{-10}m$")
plt.ylabel("$flux~10^{-17}erg~s^{-1}~cm^{-2}~A^{-1}$")

plt.legend(loc = 'lower right')

#---------------------------------------------------

# Part b)
# Normalize the flux
# Define the normalization method
def normalization(x = None):
    nor = x/sum(x)
    return nor

# Create a two-dimensional array to contain the normalized data
new_flux = np.zeros((9713,4001))
for i in np.arange(0,9713):
    new_flux[i] = normalization(flux[i])

# Make the plot
plt.figure(figsize = (10,6))
plt.plot(logwave, new_flux[0], label = "Galaxy 1")
plt.plot(logwave, new_flux[1], label = "Galaxy 2")
plt.plot(logwave, new_flux[2], label = "Galaxy 3")
plt.plot(logwave, new_flux[3], label = "Galaxy 4")
plt.title("Normalized Flux versus Wavelength")
plt.xlabel("$wavelength(\log_{10}{\lambda})~10^{-10}m$")
plt.ylabel("$flux~10^{-17}erg~s^{-1}~cm^{-2}~A^{-1}$")

plt.legend(loc = 'lower right')

#---------------------------------------------------

# Part c)
def residual(arr = None):
    res = np.zeros((len(arr),len(arr[0])))
    iteration = 0
    for i in arr:
        # Get the average value of each array of flux(galaxy)
        avg = sum(i)/len(i)
        res[iteration] = i - avg
        iteration += 1
        
    return res

res = residual(new_flux)

#---------------------------------------------------

# Part d)

st_d = time.time()
# Firstly I get the 
matrix_A = np.matmul(res.T, res)
# To get the eigenvectors of the covariance matrix
x, V = eig(matrix_A)

et_d = time.time()

plt.figure(figsize = (10,6))
plt.plot(logwave, V[:, 0], label = "Eigenvector 1")
plt.plot(logwave, V[:, 1], label = "Eigenvector 2")
plt.plot(logwave, V[:, 2], label = "Eigenvector 3")
plt.plot(logwave, V[:, 3], label = "Eigenvector 4")
plt.plot(logwave, V[:, 4], label = "Eigenvector 5")
plt.title("Plot of the first five eigenvectors")
plt.xlabel("$wavelength(\log_{10}{\lambda})~10^{-10}m$")
plt.ylabel("Eigenvector")

plt.legend(loc = 'lower right')


#---------------------------------------------------
# Part e)

st_e = time.time()
# Use the SVD method to get V
(U, w, res_VT) = svd(res.T, full_matrices=False)
res_V = res_VT.T
eigen = res.T.dot(res_V)
et_e = time.time()

# Get the first five eigenvectors
parte_V1 = eigen[:, 0]/(np.linalg.norm(eigen[:, 0]))
parte_V2 = eigen[:, 1]/(np.linalg.norm(eigen[:, 1]))
parte_V3 = eigen[:, 2]/(np.linalg.norm(eigen[:, 2]))
parte_V4 = eigen[:, 3]/(np.linalg.norm(eigen[:, 3]))
parte_V5 = eigen[:, 4]/(np.linalg.norm(eigen[:, 4]))


plt.figure(figsize = (10,6))
plt.plot(logwave, parte_V1, label = "Eigenvector 1")
plt.plot(logwave, parte_V2, label = "Eigenvector 2")
plt.plot(logwave, parte_V3, label = "Eigenvector 3")
plt.plot(logwave, parte_V4, label = "Eigenvector 4")
plt.plot(logwave, parte_V5, label = "Eigenvector 5")
plt.title("SVD method to get the first five eigenvectors")
plt.xlabel("$wavelength(\log_{10}{\lambda})~10^{-10}m$")
plt.ylabel("$normalized~flux~10^{-17}erg~s^{-1}~cm^{-2}~A^{-1}$")
plt.legend()


time_d = et_d - st_d
time_e = et_e - st_e
print("Running time for method in part d): ", time_d)
print("Running time for the SVD method: ", time_e)

#---------------------------------------------------

# Part e)
time_C = LA.cond(matrix_A)
time_R = LA.cond(res.T)

print("The condition number for matrix C is: ", time_C)
print("The condition number for matrix R is: ", time_R)


#---------------------------------------------------

# Part g)
# Set of coefficients
set_c = res_VT.T

# Get the estimated residuals through the first 5 coefficients
esti_res = set_c[:, 0:5].dot(eigen.T[0:5, :])

N = 9713
nor_constant = np.zeros(N)
avg = np.zeros(N)
esti_flux = np.zeros((N, 4001))
# Get the original data
for i in np.arange(0,N):
    # Get the normalization constant
    nor_constant[i] = sum(flux[i])
    # get the average flux value for each galaxy
    avg[i] = sum(new_flux[i])/4001
    # fi = fm + r
    esti_flux[i] = (esti_res[i] + avg[i])*nor_constant[i]
    
# Plot the estimated flux versus wavelength
plt.figure()
plt.plot(logwave, esti_flux[0], label = "estimated Galaxy 1")
plt.plot(logwave, esti_flux[1], label = "estimated Galaxy 2")
plt.plot(logwave, esti_flux[2], label = "estimated Galaxy 3")
plt.plot(logwave, esti_flux[3], label = "estimated Galaxy 4")
plt.title("Estimated flux versus wavelength")
plt.xlabel("$wavelength(\log_{10}{\lambda})~10^{-10}m$")
plt.ylabel("$flux~10^{-17}erg~s^{-1}~cm^{-2}~A^{-1}$")

plt.legend(loc = 'lower right')


#---------------------------------------------------

# Part h)
plt.figure(figsize = (9,6))
plt.scatter(np.arange(0, 9713), set_c[:,0]/set_c[:, 1], label = "c0 vs c1")
plt.scatter(np.arange(0, 9713), set_c[:,0]/set_c[:, 2], label = "c0 vs c2")
plt.title("$c_0~vs~c_1~and~c_0~vs~c_2$")
plt.xlabel("Number of Galaxy")
plt.ylabel("$C_0/C_n$")
plt.grid()
plt.legend(loc = "lower right")


#---------------------------------------------------

# Part i)

def estimate_flux(N = None):
    esti_res = set_c[:, 0:N].dot(eigen.T[0:N, :])
    galaxy = 9713
    nor_constant = np.zeros(galaxy)
    avg = np.zeros(galaxy)
    esti_flux = np.zeros((galaxy, 4001))
    for i in np.arange(0,galaxy):
        nor_constant[i] = sum(flux[i])
        avg[i] = sum(new_flux[i])/4001
        esti_flux[i] = (esti_res[i] + avg[i])*nor_constant[i]
    
    return esti_flux

def sq_res(esti_flux = None):
    res_flux = (flux - esti_flux)/esti_flux
    return sum(res_flux**2)

# Vary from N = 1 to 20.
esti_flux = np.zeros(20)
sum_resflux = np.zeros(20)
for i in np.arange(1,21):
    sum_resflux[i-1] = sum(sq_res(estimate_flux(i)))

# Make the plot
plt.figure(figsize = (9,6))
plt.yscale("log")
plt.plot(np.arange(1,21), sum_resflux)
plt.title("Changes of fractional residuals as N increases")
plt.xlabel("Number of N from 1 to 20")
plt.ylabel("summation of the squared fractional residuals")




















