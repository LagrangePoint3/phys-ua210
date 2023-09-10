#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 19:46:25 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt

# Plot between -10 and 10 with 0.01 steps.
x_axis = np.arange(-10, 10, 0.01)
  
# Calculating mean and standard deviation
mean = 0
sd = 3
y = [np.exp(-(x-mean)**2/(2*sd**2))/(np.sqrt(2*np.pi*sd**2)) for x in x_axis]
  
plt.plot(x_axis, y)
plt.suptitle("Gaussian.png.")
plt.xlabel("range[-10,10] for x")
plt.ylabel("Probability Density")
plt.savefig("gaussian.png", dpi = 300)
plt.show()