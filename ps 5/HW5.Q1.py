#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 23:09:59 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
from gaussxw import gaussxwab
from gaussxw import gaussxw 
import math

# Part a)
def f(x = None, a = None):
    return x**(a-1)*np.e**(-x)

# Create the function for a = 2,3,4
x = np.linspace(0,5,100)
y1 = f(x,2)
y2 = f(x,3)
y3 = f(x,4)

plt.figure()
plt.scatter(x,y1)
plt.scatter(x,y2)
plt.scatter(x,y3)
plt.legend(['a= 2', 'a = 3', 'a = 4'])
plt.plot([0],[0], color = "black")
plt.title("$f(x) = x^{a-1} e^{-x} ~for~x \in [0,5]$")
plt.ylabel("f(x)")
plt.xlabel("x")


# Part e)
def f_p(x = None, a = None):
    power = np.log(x)*float(a-1)
    return np.e**(-x)*(np.e**power) 

def fz(x = None, a = None):
    return f_p(x*(a-1)/(1-x), a)*(a-1)/(1-x)**2

# Perform the integral using Guassian quadrature with N = 100 sample points.
def gamma(a = None):
    
    N = 100

    a1 = 0
    b1 = 1
    x, w = gaussxwab(N, a1 ,b1)
    s = 0.0
    for k in np.arange(N):
        s += w[k]*fz(x[k], a)

    return s

print("The value of gamma(3/2) is: ", gamma(1.5))


# Part f)
print("The value of gamma(3) is: ", gamma(3))
print("The value of gamma(6) is: ", gamma(6))
print("The value of gamma(10) is: ", gamma(10))
