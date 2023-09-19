#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 17:59:37 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt

# Function for part a)
def part_a(a = None, b = None, c = None):
    delta = (b**2 - 4*a*c)**(1/2)
    sol_1 = (-b + delta)/(2*a)
    sol_2 = (-b - delta)/(2*a)
    return sol_1, sol_2

# Function for part b)
def part_b(a = None, b = None, c = None):
    delta = (b**2 - 4*a*c)**(1/2)
    sol_1 = 2*c/(-b - delta)
    sol_2 = 2*c/(-b + delta)
    return sol_1, sol_2

# Function for part c)
def part_c(a = None, b = None, c = None):
    delta = b**2 - 4*a*c
    
    if b > 0:
        sol_1 = 2*c/(-b - delta**(1/2))
        sol_2 = (-b - delta**(1/2))/(2*a)
    
    else:
        sol_1 = sol_1 = (-b + delta**(1/2))/(2*a)
        sol_2 = 2*c/(-b + delta**(1/2))

    return sol_1, sol_2


print("The two solutions for part a) are: ", part_a(0.001, 1000,0.001))
print("The two solutions for part b) are: ", part_b(0.001, 1000,0.001))
print("The two solutions for part c) are: ", part_c(0.001, 1000,0.001))