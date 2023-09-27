#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:38:03 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt

# Half-time of each isotope
half_t_Pb = 3.3 * 60 
half_t_Tl = 2.2 * 60
half_t_Bi213 = 46 * 60

# Probablity of decay of each isotope in the time interval of 1s
P_Pb = 1 - 2**(-1/half_t_Pb)
P_Tl = 1 - 2**(-1/half_t_Tl)
P_Bi213 = 1 - 2**(-1/half_t_Bi213)

def decay_chain(T = None):
    n_Bi213 = 10000
    n_Tl = 0
    n_Pb = 0
    n_Bi209 = 0
    
    list_Bi213 = []
    list_Tl = []
    list_Pb = []
    list_Bi209 = []
    
    # Build the x-axis for time
    time = np.arange(1, T + 1, 1)
    
    for t in range(T):
        # part a) process of Pb_209
        n_Pb_decay = P_Pb * n_Pb
        n_Pb -= n_Pb_decay
        n_Bi209 += n_Pb_decay

        # part b) process of Tl
        n_Tl_decay = P_Tl * n_Tl
        n_Tl = n_Tl_decay
        n_Pb += n_Tl_decay

        # part c) process of Bi_213
        n_Bi213_decay = P_Bi213 * n_Bi213
        n_Bi213 -= n_Bi213_decay
        n_Pb += n_Bi213_decay * 0.9791
        n_Pb += n_Bi213_decay * 0.0209
        
        # Add new results to lists
        list_Bi213.append(n_Bi213)
        list_Tl.append(n_Tl)
        list_Pb.append(n_Pb)
        list_Bi209.append(n_Bi209)
        
        
    return list_Bi213, list_Tl, list_Pb, list_Bi209, time


y_Bi213, y_Tl, y_Pb, y_Bi209, x_time = decay_chain(20000)

plt.autoscale()
plt.plot(x_time, y_Bi213, marker = "o", markersize = 1, c = "red")
plt.plot(x_time, y_Tl, marker = "o", markersize = 1, c = "black")
plt.plot(x_time, y_Pb, marker = "o", markersize = 1, c = "green")
plt.plot(x_time, y_Bi209, marker = "o", markersize = 1, c = "purple")
plt.legend(["Bi213", "Tl", "Pb", "Bi209"], loc = "upper right")
plt.xlabel("Time (s)")
plt.ylabel("Number of isotopes")
plt.title("Number of Different Isotopes Versus Time")









