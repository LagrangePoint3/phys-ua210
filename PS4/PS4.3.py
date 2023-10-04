#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 21:49:57 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
import math

# Make the function for H(n,x)
def H(n,x):
    # Create a list for H(n,x) with different n
    list1 = [1,2*x]
    for i in np.arange(2, n+1):
        list1.append(2*x*list1[i-1] - 2*(i-1)*list1[i-2])
    return list1[n]

# Make the function for the point particel in the potential well.
def psi(n,x):
    initial = 1/(np.sqrt(2**n*math.factorial(n)*np.sqrt(np.pi)))
    return initial*np.exp(-x**2/2)*H(n,x)

# Part a)
x_arr = np.linspace(-4,4,100)

# Array for psi function with n = 0
iteration = 0
psi_0 = np.zeros(100)
n = 0
for x in x_arr:
    psi_0[iteration] = psi(n,x)
    iteration += 1
    
# Array for psi function with n = 1
iteration = 0
psi_1 = np.zeros(100)
n = 1
for x in x_arr:
    psi_1[iteration] = psi(n,x)
    iteration += 1

# Array for psi function with n = 2
iteration = 0
psi_2 = np.zeros(100)
n = 2
for x in x_arr:
    psi_2[iteration] = psi(n,x)
    iteration += 1

# Array for psi function with n = 3    
iteration = 0    
psi_3 = np.zeros(100)
n = 3
for x in x_arr:
    psi_3[iteration] = psi(n,x)
    iteration += 1
 
# Make the plot for part a)    

plt.figure()
plt.plot(x_arr, psi_0)
plt.plot(x_arr, psi_1)
plt.plot(x_arr, psi_2)
plt.plot(x_arr, psi_3)
plt.legend(["n = 0", " n = 1", "n = 2", "n = 3"], loc = "upper right")
plt.xlabel("Position of the particle")
plt.ylabel("Psi function")
plt.title("Quantum uncertainty in the harmonic oscillator")


#--------------------------------------


# Part b)
# Create the array for x-axis
x2_arr = np.linspace(-10,10,500)

# Array for psi function with n = 30
iteration = 0    
psi_30 = np.zeros(500)
n = 30
for x in x2_arr:
    psi_30[iteration] = psi(n,x)
    iteration += 1
 
 # Make the plot for part b)
plt.figure()
plt.plot(x2_arr, psi_30)
plt.xlabel("Position of the particle")
plt.ylabel("Psi function")
plt.title("Quantum uncertainty for n = 30") 

#----------------------------------------

# Part c)
def f(n, x):
    return x**2*(np.absolute(psi(n,x)))**2

def fz(n,x):
    return f(n,np.tan(x))/np.cos(x)**2

N = 100

a = -np.pi/2
b = np.pi/2
x, w = gaussxwab(N, a ,b)
s = 0.0
for k in np.arange(N):
    s += w[k]*fz(5,x[k])

print("part c): The square root of the uncertainty is: ", np.sqrt(s))
    
 
#--------------------------------------------

# Part d)
def func_f(n, x):
     return x**2/(2**n*math.factorial(n)*np.sqrt(np.pi))*(H(n, x))**2
(x, weight) = np.polynomial.hermite.hermgauss(100)
gaussher_integral = (func_f(5, x) * weight).sum()

print("part d): The square root of the uncertainty is: ", np.sqrt(gaussher_integral))










 
    