#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 20:24:24 2023

@author: zhaoyilin
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import optimize


def fp(x = None, beta_0 = None, beta_1 = None):
    return 1/(1 + np.exp(-(beta_0 + beta_1*x)))

data = pd.read_csv("survey.csv")  

age = data["age"].to_numpy()
recog = data["recognized_it"].to_numpy()

beta_0 = np.linspace(-5,5, 100)
beta_1 = np.linspace(-5,5,100)
beta = np.meshgrid(beta_0, beta_1)



def log_likelihood(beta, age, recog):
    beta_0 = beta[0]
    beta_1 = beta[1]
    epsilon = 1e-16
    l_list = [recog[i]*np.log(fp(age[i], beta_0, beta_1)/(1-fp(age[i], beta_0, beta_1)+epsilon)) 
              + np.log(1-fp(age[i], beta_0, beta_1)+epsilon) for i in range(len(age))]
    ll = np.sum(np.array(l_list), axis = -1)
    return -ll 

# Covariance matrix of the likelihood
def covar_matrix(hess_inv, variance):
    return hess_inv * variance

# Error of the likelihood
def error(hess_inv, resVariance):
    covariance = covar_matrix(hess_inv, resVariance)
    return np.sqrt( np.diag( covariance ))

# Initial Guess
x0 = np.array([1, 2])

result = optimize.minimize(log_likelihood, x0,  args=(age, recog))

# inverse of hessian matrix
hess_inv = result.hess_inv
variance = result.fun/(len(recog)-len(x0)) 
f_err = error( hess_inv,  variance)
print("Maximum likelihood value of beta_0 is: " , result.x[0], ", with the error of ", f_err[0])
print("Maximum likelihood value of beta_1 is: " , result.x[1], ", with the error of ", f_err[1])
print("The covariance matrix of beta_0 and beta_1 is: " , covar_matrix( hess_inv,  variance))

plt.title("Logic Model")
plt.scatter(age, recog, label = "data")
age = np.sort(age)
plt.plot(age, fp(age, result.x[0], result.x[1]), label = "logic model", color = "red")
plt.xlabel("age(year)")
plt.ylabel("yes or no / likelihood")
plt.legend()