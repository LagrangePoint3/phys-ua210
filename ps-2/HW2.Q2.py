#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:59:07 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
import timeit


# Version #1
# Calculate each coordiante of (i,j,k).
def funcM(i = None ,j = None, k = None):
    return ((i**2 + j**2 + k**2)**(-1/2))

# Make a summation to get the Madelung constant.
def cal_M(L = None):
    list_L = np.arange(-L,L+1,1)
    M_constant = 0
    for i in list_L:
        for j in list_L:
            for k in list_L:
                if not i == j == k == 0:
                    if (i + j + k)%2 == 0:
                        M_constant += funcM(i,j,k)
                    else:
                        M_constant -= funcM(i,j,k)
                
                
    return M_constant


# Version #2
def cal_M2(L = None):
    # Create an array from -L to L.
    array_1 = np.linspace(-L,L,2*L+1)
    
    # Array of oordiantes of the each particle
    i, j , k = np.meshgrid(array_1,array_1, array_1)
    
    mask = i**2+j**2+k**2 != 0
    
    # mask those coordinates that i+j+k is odd 
    mask_odd = (i + j + k)%2 != 0
    sum_odd = np.sum((i[mask_odd]**2 + j[mask_odd]**2 + k[mask_odd]**2)**(-1/2))
    
    return np.sum((i[mask]**2 + j[mask]**2 + k[mask]**2)**(-1/2)) - sum_odd*2

L = 100

print("Madelung constant for the version with for loops: ", cal_M(L))
print("Madelung constant for the version without for loops: ", cal_M2(L))
print("The time for the version with for loops: ", timeit.timeit('cal_M(L)', globals=globals(), number=1), "s, L = ", L)
print("The time for the version without for loops: ", timeit.timeit('cal_M2(L)', globals = globals(), number = 1), "s, L = ", L)
