#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 00:16:13 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt

# Make a function to find values of Mandelbrot set
def def_M(c = None):
    z_prime = c
    num_z = 0
    iteration = 0
    while (iteration < 100):
        iteration +=1
        z_prime = num_z**2 + c
        num_z = z_prime
        
        if np.absolute(z_prime) > 2:
            return False
        
    return True



def M_set(N = int()):
    
    # Coordiantes of potential values of the set
    array_x = np.linspace(-2,2,N)
    array_y = np.linspace(-2,2,N)
    coord_x, coord_y = np.meshgrid(array_x, array_y)
    
    # Transform them into complex numbers
    c = complex(0, 1)
    array_c = coord_x + coord_y*c

    # Find thse values that are in the set
    vec_c = np.vectorize(def_M)
    mask = vec_c(array_c)
    
    # Coordinates of values in the Mandelbrot set
    x_set = np.array(np.real(array_c[mask]))
    y_set = np.array(np.imag(array_c[mask]))

    plt.plot(coord_x, coord_y, marker = "o", markersize = 3, color = "w", linestyle='none')
    plt.plot(x_set, y_set, marker = "o", markersize = 3, color = "k", linestyle='none')
    plt.xlabel("X(real part)")
    plt.ylabel("Y(imaginary part)")
    plt.title("The plot for  Mandelbrot set")

    plt.grid(color = 'brown', linestyle = 'solid')



M_set(5000)
