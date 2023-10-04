#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:16:09 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
from gaussxw import gaussxw 

def f(a, x):
    return 2*np.sqrt(2)/(np.sqrt(a**4 - x**4))

# Calculate the sample points
N = 20
x,w = gaussxw(N)
def T(N,x,w,up_limit,low_limit):
    N = 20
    
    xp = 0.5*(up_limit - low_limit)*x + 0.5*(up_limit + low_limit)
    wp = 0.5*(up_limit - low_limit)*w
    s = 0.0
    for k in range(N):
        x_1 = xp[k]
        s += wp[k]*f(up_limit,x_1)
    return s

# Create an array with 100 elements to contain the values of period
s_arr = np.zeros(100)
iteration = -1

# Build the x-axis for the plots
x_axis = np.linspace(0.1,2,100)
for n in x_axis:
    iteration += 1
    s_arr[iteration] = T(20, x, w, n, 0)
    
# Make the plots
plt.scatter(x_axis, s_arr)
plt.xlabel("Amplitude a ")
plt.ylabel("Period T (s)")
plt.title("Period versus Amplitude")