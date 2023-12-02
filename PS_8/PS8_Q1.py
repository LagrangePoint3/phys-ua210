#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 19:18:31 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from numpy.fft import rfft

# Part a)

sound = np.loadtxt('piano.txt')
sound_1 = np.loadtxt('trumpet.txt')

time = np.linspace(0,99999,100000)

plt.figure()
plt.scatter(time, sound)
plt.title("Waveform of Piano")
plt.xlabel("Number")
plt.ylabel("Data(Sound)")

plt.figure()
plt.scatter(time, sound_1)
plt.title("Waveform of Trumpet")
plt.xlabel("Number")
plt.ylabel("Data(Sound)")


# Discrete fourier transform for piano
c = np.fft.fft(sound)
#Get the magnitude of the coefficients
c_abs = np.abs(c)

n = len(sound)
rate = 44100
d = 1/rate
freq = np.fft.fftfreq(n, d)

# Get the magnitude of the frequency
freq_abs = np.abs(freq)

plt.figure()
plt.title("The Magnitude of Coefficients over Frequency for Piano")
plt.plot(freq_abs[:10000], c_abs[:10000])
plt.xlabel("Frequency $\omega$ (Hz)")
plt.ylabel("The Magnitude of Coefficents")


# Discrete fourier transform for Trumpet
c_1 = np.fft.fft(sound_1)

#Get the magnitude of the coefficients
c_abs_1 = np.abs(c_1)

n_1 = len(sound_1)
rate = 44100
d = 1/rate

freq_1 = np.fft.fftfreq(n_1, d)
freq_abs_1 = np.abs(freq_1)

# Make the plot
plt.figure()
plt.title("The Magnitude of Coefficients over Frequency for Trumpet")
plt.plot(freq_abs_1[:10000], c_abs_1[:10000])
plt.xlabel("Frequency $\omega$ (Hz)")
plt.ylabel("The Magnitude of Coefficents")

#--------------------------------------------------------------------------


# Part b)
highest_p_order = c_abs[:10000].argmax()
highest_p = freq_abs[highest_p_order]

plt.figure()
plt.title("The Magnitude of Coefficients over Frequency for Piano")
plt.plot(freq_abs[:10000], c_abs[:10000])
plt.xlabel("Frequency $\omega$ (Hz)")
plt.ylabel("The Magnitude of Coefficents")

for factor in [1, 2, 3, 4, 5, 6, 7, 8]:
    plt.axvline(factor * highest_p, color="g")
plt.axvline(highest_p, color="r")

plt.figure()
plt.title("The Magnitude of Coefficients over Frequency for Trumpet")
plt.plot(freq_abs_1[:10000], c_abs_1[:10000])
plt.xlabel("Frequency($s^{-1}$)")
plt.ylabel("The Magnitude of Frequency")

for factor in [1, 2, 3, 4, 5, 6, 7, 8]:
    plt.axvline(factor * highest_p, color="g")
plt.axvline(highest_p, color="r")


print("The dominant frequency is ", highest_p, "Hz")

