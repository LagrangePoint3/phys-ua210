#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 17:15:26 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg

L = 1.e-8
sigma = 1.e-10
k = 5.e10
N = 1000
a = L/N
m = 9109.e-34

h = 1.e-18
h_bar = 1055.e-37

x_0 = L/2
b1 = complex(1, -h*h_bar/(2*m*a**2))
b2 = complex(0, h*h_bar/(4*m*a**2))
a1 = complex(1, h*h_bar/(2*m*a**2))
a2 = complex(0, -h*h_bar/(4*m*a**2))

def psi_t0(x):
    #image_exp = complex(0, x*k)
    return np.exp(-((x-x_0)**2)/(2*sigma**2))*np.exp(1j*x*k)

v = np.zeros((N,1), dtype = complex)
for i in np.arange(1, N+1):
    v[i-1][0] = b1*psi_t0(i*a)
    if i != N:
        v[i-1][0] += b2*psi_t0((i+1)*a)
    if i != 1:
        v[i-1][0] += b2*psi_t0((i-1)*a)

B = np.zeros((N ,N), dtype = complex)
for i in np.arange(0,N):
    B[i][i] = b1
    if i != 0:
        B[i][i-1] = b2
    if i != N-1:
        B[i][i+1] = b2

psi_t = np.zeros((1000,2),dtype = complex)
for i in np.arange(0,1000):
    psi_t[i][0] = psi_t0(a+a)
    
A = np.zeros((N ,N), dtype = complex)
for i in np.arange(0,N):
    A[i][i] = a1
    if i != 0:
        A[i][i-1] = a2
    if i != N-1:
        A[i][i+1] = a2


#x = linalg.solve(A, v)

#fig = plt.figure() 
#axis = plt.axes() 

fig, axis = plt.subplots(1,1)


# line, = axis.plot([],[]) 
# xdata, ydata = [], [] 
x_real_list = []

position = np.linspace(0,L,1000)

#time = np.arange(1,101)

x_real = np.zeros(1000)
#number = time[i]

N = 1000
v = np.zeros((N,1), dtype = complex)
for i in np.arange(1, N+1):
    v[i-1][0] = b1*psi_t0(i*a)
    if i != N:
        v[i-1][0] += b2*psi_t0((i+1)*a)
    if i != 1:
        v[i-1][0] += b2*psi_t0((i-1)*a)
x = linalg.solve(A, v)
  
num_steps = 300
    
for num in np.arange(0, num_steps):
        v = B.dot(x)
        x = linalg.solve(A, v)
        x_real = x.real 
        x_real_list.append(x_real)


def psi(i):
    axis.clear()
    y = x_real_list[i-1]

    plt.plot(position, y)
    plt.ylim(-1, 1)
    plt.xlabel("$position$ (m)")
    plt.ylabel(r"$\psi$")
    plt.title("Wavefunction")

from matplotlib import animation
anim = animation.FuncAnimation(fig, psi, frames=num_steps +1)

from matplotlib.animation import PillowWriter
writer = PillowWriter(fps=24)
anim.save("sine_example6.gif", dpi=300, writer=writer)









