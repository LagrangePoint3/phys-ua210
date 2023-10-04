#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:13:03 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt

# f(x)
def f(x = None):
    return x**4 - 2*x + 1

# Function for the trapezoidal method
def trapezoidal(N = None):
    a = 0
    b = 2
    h = (b-a)/N
    s = 0.5*f(a) + 0.5*f(b)
    
    for k in range(1, N):
        s += f(k*h + a)
        
    return (h*s)

error_20 = (trapezoidal(20)-trapezoidal(10))/3
error_true = 4.4 - trapezoidal(20)

print("for N = 20, the integral is: ", trapezoidal(20))
print("The error calculated through Eq(5.28) is: ", error_20)
print("The true error is: ", error_true)