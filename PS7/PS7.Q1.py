#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 13:16:21 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# Implement Brent's 1D minimization method
def f(x = None):
    return (x-0.3)**2*np.exp(x)

# The quadratic method
def quadratic(a=None, b=None, c=None):
    
    fa = f(a)
    fb = f(b)
    fc = f(c)
    denom = (b - a) * (fb - fc) - (b -c) * (fb - fa)
    numer = (b - a)**2 * (fb - fc) - (b -c)**2 * (fb - fa)
    
    # If singular, just return b 
    if(np.abs(denom) < 1.e-15):
        x = b
    else:
        x = b - 0.5 * numer / denom
    return(x)
    return s0+s1+s2

def order(a = None, b = None, c = None):
    v = [a, b, c]
    func = [f(a), f(b), f(c)]
    min_f = func[0]
    index = 0
    for i in np.arange(1,3):
        if func[i] < min_f:
            min_f = func[i]
            index = i
    b = v[index]
    del v[index]
    a, c = v[0], v[1]
    return a,b,c

def min_optimize():
    a = 0.2
    b = 1
    c = 3
    
    # Tolerence of error
    tol = 1e-3
    gsection = (3. - np.sqrt(5)) / 2
    x = 0
    
    # Record the stepsize of each iteration
    step = [b, b]
    
    # Number of iterations
    ite = 0
    
    # Whether use the Golden Search Method
    golden = True
    
    err = (abs(a - b) + abs(b - c) + abs(c - a))/2
    err_list, b_list = [err], [b]
    
    while (err > tol):
        
        # Try to use the Quadratic Search Method
        bold = quadratic(a,b,c)
        
        # Conditions on the quadratic method
        if ((bold > max(a, b, c) or (a < min(a, b, c)))) or\
        (golden == False) and ((abs(step[ite] - step[ite-1]) >= abs(bold - step[ite+1]))):
            # Golden Search Section
            # Swap the paraemters if needed for golden section
            a, b, c = order(a, b, c)
            
            if((b - a) > (c - b)):
                x = b
                b = b - gsection * (b - a)
            else:
                x = b + gsection * (c - b)
                
            if(f(b) < f(x)):
                c = x
            else:
                a, b =b, x
            
            step.append(b)
            golden = True
            
        else:
            golden = False
            step.append(bold)
             
            # Sort the order of a, b, c
            arr = np.array([a,b,c])
            arr.sort()
            a, b, c = arr[0], arr[1], arr[2]
            
            bold, b = b, bold
            
            if(b < bold):
                c = bold
            else:
                a = bold
            
        ite += 1
            
        #update error to check for convergence
        err = (abs(a - b) + abs(b - c) + abs(c - a))/2
        err_list.append(err)
        b_list.append(b)
        
    #print(f'minimum = {b}')
    return b

minimum = min_optimize()

# scipy.optimize.brent implementation results
minimizer = optimize.brent(f, brack=(0.2,0.5))

error_1 = 0.3 - minimum
error_2 = 0.3 - minimizer
print("The result by implementing the Brent's method:", minimum, " The error is:", error_1)
print("The result by the scipy.optimize.brent:" , minimizer, " The error is:", error_2)