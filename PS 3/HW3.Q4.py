#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:27:17 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
from random import random

half_t = 3.053*60
u = np.log(2)/half_t

z = np.random.random(1000)
decay_time = -1/u * (np.log(1-z))
sorted_decay_time = np.sort(decay_time)


notdecayed = np.arange(1000, 0, -1)


plt.plot(sorted_decay_time, notdecayed, c ="blue")
plt.xlabel("Decay Time t(s)")
plt.ylabel("Number of nondecay atoms n")
plt.title("Radioactive Decay")