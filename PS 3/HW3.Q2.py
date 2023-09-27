#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 19:00:38 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import zeros
import random 
import timeit

# The method with for loops
def matrix_1(N = None):
    
    A = np.random.randint(100, size = (N, N))
    B = np.random.randint(100, size = (N, N))
    C = zeros([N,N] , float) 
    
    for i in range(N): 
        for j in range(N): 
            for k in range(N): 
                C[i,j] += A[i,k]*B[k,j]
    return C

# The method with dot-method
def matrix_2(N = None):
    A = np.random.randint(100, size = (N, N))
    B = np.random.randint(100, size = (N, N))
    return np.dot(A,B)


def matrix_plot(begin = None, end = None):
    N_arr = np.arange(begin, end)
    
    # Create lists 
    mat_1 = np.zeros(end - begin)
    mat_2 = np.zeros(end - begin)
    
    for N in N_arr:
        # Get running time for the for-loop method
        time_1_start = timeit.default_timer()
        matrix_1(N)
        time_1_end = timeit.default_timer()
        time_1 = time_1_end - time_1_start
        # Get running time for the dot-method
        time_2_start = timeit.default_timer()
        matrix_2(N)
        time_2_end = timeit.default_timer()
        time_2 = time_2_end - time_2_start
        
        mat_1[N-begin] = time_1
        mat_2[N-begin] = time_2
    
    plt.figure()
    plt.autoscale()
    plt.scatter(N_arr, mat_1, c = "blue")
    plt.scatter(N_arr, mat_2, c = "red")
    plt.plot(N_arr, mat_1)
    plt.plot(N_arr, mat_2)
    
    plt.legend(["for-loop method", "dot method"])
    plt.xlabel("matrix size N")
    plt.ylabel("running time (t)")
    plt.title("Running Time Versus Matrix Size")
    
    
    plt.figure()
    plt.autoscale()
    plt.scatter(N_arr**3, mat_1, c = "blue")
    plt.scatter(N_arr**3, mat_2, c = "red")
    plt.plot(N_arr**3, mat_1)
    plt.plot(N_arr**3, mat_2)
    
    plt.legend(["for-loop method", "dot method"])
    plt.xlabel(r"$cube~of~matrix~size~~N^3$")
    plt.ylabel("running time (t)")
    plt.title("Running Time Versus Matrix Size")

matrix_plot(10,51)



