#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:51:57 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt

# Function of f(x)
def f_x(x = None):
    return x*(x-1)

# Function of derivative of f(x)
def de_x1 (delta = None):
    x = 1
    return (f_x(x + delta) - f_x(x))/delta


# Part a)
de_x1(10**(-2))
print("The programed value of derivative of f(x) is", de_x1(10**(-2)))


# Part b)
# Create array for x
x = [10**(-2), 10**(-4), 10**(-6), 10**(-8),10**(-10),10**(-12), 10**(-14)]
delta_arr = np.array(x)

# Create array for y
vec_c = np.vectorize(de_x1)
y = np.absolute(vec_c(delta_arr)-1)

plt.yscale("log")
plt.xscale("log")
plt.autoscale()
plt.xlabel(r"$\log_{10}(\delta)$")
plt.ylabel(r"$\log_{10}(y)$")
plt.title("$Error (y)~versus~\delta $")
plt.scatter(x,y, c = "blue")
plt.plot(x,y)




