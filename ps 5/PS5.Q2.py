#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 23:46:32 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from scipy.linalg import svd
from numpy import linalg as LA

returns = pd.read_csv('signal.dat', delimiter = '|', header = 0, names = ["1","time","signal", "2"])
time = returns["time"].to_numpy()
signal = returns["signal"].to_numpy()

# Part a: plot the data
plt.figure()
plt.scatter(time,signal)
plt.title("Signal versus Time")
plt.xlabel("Time(s)")
plt.ylabel("Signal")


#-----------------------------------------------------------

# Part b,c
A = np.array((time**0, time, time**2, time**3)).T

# Use SVD method to get matrix U, w, VT
(U, w, VT) = svd(A, full_matrices=False)

# invert w and make it into a diagonal matrix
w_in = np.zeros(len(w))
for i in range(len(w)):
    if w[i] != 0:
        w_in[i] = 1./w[i]   
        
# A^(-1) = (U w VT)^(-1)
Ainv = VT.transpose().dot(np.diag(w_in)).dot(U.transpose())

# x = A^(-1) * b
x = Ainv.dot(signal)

y = x[0] + time * x[1] + time**2 * x[2] + time**3 * x[3] 
res = signal - y

plt.figure()
plt.scatter(time, signal, c = "blue", label = "signal")
plt.plot(time, y, color = "red", label = "model")
plt.scatter(time, res, c = "grey", label = "residual")
plt.legend()
plt.title("Third-order polynomial model in time to signal", c = "green")
plt.xlabel("Time")
plt.ylabel("Signal")


#-----------------------------------------------------------


# Part d
# Define the order of polynomial
N = 8


A_1 = np.zeros((len(time), N + 1))
for i in range(N + 1):
    A_1[:, i] = time ** (i)

# Use SVD method to get matrix U, w, VT
(U_1, w_1, VT_1) = svd(A_1, full_matrices=False)

# invert w and make it into a diagonal matrix
w_1_in = np.zeros(len(w_1))
for i in range(len(w_1)):
    if w_1[i] != 0:
        w_1_in[i] = 1./w_1[i]  
        
# A^(-1) = (U w VT)^(-1)
A_1_inv = VT_1.transpose().dot(np.diag(w_1_in)).dot(U_1.transpose())
x_1 = A_1_inv.dot(signal)

# Get the function y with high order polynomials
y_1 = x_1[0]
for i in range(N):
    w = time ** (i+1) * x_1[i + 1]
    y_1 += w
    
res_1 = signal - y_1

plt.figure()
plt.scatter(time, signal, c = "blue", label = "signal")
plt.plot(time, y_1, color = "red", label = "model")
plt.scatter(time, res_1, c = "grey", label = "residual")
plt.legend()
plt.title("Eighth-order polynomial model in time to signal", c = "green")
plt.xlabel("Time")
plt.ylabel("Signal")



#-----------------------------------------------------------

# Part e
A_2 = np.zeros((len(time), 3))
A_2[:, 0] = np.cos(time)
A_2[:, 1] = np.sin(time)
A_2[:, 2] = time **0

(U_2, w_2, VT_2) = svd(A_2, full_matrices=False)

# invert w and make it into a diagonal matrix
w_2_in = np.zeros(len(w_2))
for i in range(len(w_2)):
    if w_2[i] != 0:
        w_2_in[i] = 1./w_2[i]  
        
# A^(-1) = (U w VT)^(-1)
A_2_inv = VT_2.transpose().dot(np.diag(w_2_in)).dot(U_2.transpose())
x_2 = A_2_inv.dot(signal)

y_2 = x_2[0]*np.cos(time) + x_2[1]*np.sin(time) + x_2[2]
res_2 = signal - y_2

plt.figure()
plt.scatter(time, signal, c = "blue", label = "signal")
plt.plot(time, y_2, color = "red", label = "model")
plt.scatter(time, res_2, c = "grey", label = "residual")
plt.legend()
plt.title("sin and cos function model in time to signal", c = "green")
plt.xlabel("Time")
plt.ylabel("Signal")




