#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:41:07 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from numpy.fft import rfft

def Lorentz(t = None, N = None):
    sigma = 10
    r = 28
    b = 8/3
    
    a = 0.0
    # h is the time interval
    h = (t-a)/(N*t) 
    t_points = np.arange(a,t,h)
    
    # Create three lists to store the angle degrees
    x_points = []
    y_points = []
    z_points = []
    
    # initial velocity
    x = 0
    y = 1
    z = 0
    
    for t in t_points:
        x_points.append(x)
        y_points.append(y)
        z_points.append(z)
        
        k11 = h*dxdt(x, y, z)
        k12 = h*dydt(x, y , z)
        k13 = h*dzdt(x, y, z)

        k21 = h*dxdt(x + 0.5*k11, y + 0.5*k12, z + 0.5*k13)
        k22 = h*dydt(x + 0.5*k11, y + 0.5*k12, z + 0.5*k13)
        k23 = h*dzdt(x + 0.5*k11, y + 0.5*k12, z + 0.5*k13)

        k31 = h*dxdt(x + 0.5*k21, y + 0.5*k22, z + 0.5*k23)
        k32 = h*dydt(x + 0.5*k21, y + 0.5*k22, z + 0.5*k23)
        k33 = h*dzdt(x + 0.5*k21, y + 0.5*k22, z + 0.5*k23)

        k41 = h*dxdt(x + k31, y + k32, z + k33)
        k42 = h*dydt(x + k31, y + k32, z + k33)
        k43 = h*dzdt(x + k31, y + k32, z + k33)
    
        x += (k11 + 2*k21 + 2*k31 + k41)/6
        y += (k12 + 2*k22 + 2*k32 + k42)/6
        z += (k13 + 2*k23 + 2*k33 + k43)/6
    
    return x_points, y_points, z_points, t_points
        
def dxdt(x, y, z):
    sigma = 10
    return sigma*(y - x)

def dydt(x, y, z):
    r = 28
    return r*x - y - x*z

def dzdt(x, y, z):
    b = 8/3
    return x*y - b*z

x_points, y_points, z_points, t_points = Lorentz(50, 1000)

plt.figure()
plt.figure(figsize = (12, 6))
plt.plot(t_points, y_points)
plt.title("y coordinates versus time(t)")
plt.xlabel("time(t)")
plt.ylabel("y coordinate")

plt.figure()
plt.plot(figsize = (12, 6))
plt.plot(x_points, z_points)
plt.title("z coordiantes versus x coordinates")
plt.xlabel("x coordinate")
plt.ylabel("z coordinate")


