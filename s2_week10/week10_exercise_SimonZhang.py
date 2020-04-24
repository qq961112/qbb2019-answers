#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Andrew Gordus
April, 2020
Quantitative Biology and Biophysics (AS.020.674/250.644)	Spring 2020
Gordus Lab #1

"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.optimize import minimize

file_path = '/Users/cmdb/qbb2019-answers/s2_week10/'
file_name = 'bob_pairing_data.xlsx'
fname = file_path + file_name
data_df = pd.read_excel(fname)

sample_names = list(set(data_df.iloc[:,1]))
sample_names.sort()
sample_names = sample_names[-1:] + sample_names[:-1]
num_samples = len(sample_names)

# print(sample_names)

#convert dataframe to numpy array
data_n = data_df.to_numpy()
data_n = pd.to_numeric(data_n[:,0])
data_n.resize(num_samples,100)
data_n = np.transpose(data_n)
# print(len(data_n[:,0]))

# Set up the matplotlib figure
f, axes = plt.subplots(2, 2, figsize=(7, 7))
sns.despine(left=True)
sns.set(style="whitegrid")


sns.swarmplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[0, 0])

sns.violinplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[0, 1])

sns.boxplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[1, 0])

sns.barplot(x=data_df.columns[1], y=data_df.columns[0], data=data_df,ax=axes[1, 1])

# plt.show()

for i in range(num_samples):
    
    # Gaussian

    x = data_n[:, i]
    mu_ = np.nanmean(x)
    sigma_ = np.nanstd(x)



    def gauss_fun(x,mu,sigma):

        p = np.exp((-(x-mu)**2) / (2 * sigma**2)) / (2 * math.pi * sigma**2)**(1/2)


        return p


    # Gaussian logL

    def gausslogl(x):

        mu = np.nanmean(x)
        sigma = np.nanstd(x)

        p = gauss_fun(x, mu, sigma)

        lnl = sum(np.log(p))

        return lnl

    # Double Gaussian LogL
    # NOTE: It returns the NEGATIVE of the logL

    def dgausslogl(params,x):

        mu1 = params[0]
        mu2 = params[1]
        sigma1 = params[2]
        sigma2 = params[3]
        w = params[4]

        # Set maximum range for parameters
        if mu1 < np.nanmin(x):
            mu1 = np.nanmin(x)
        elif mu1 > np.nanmax(x):
            mu1 = np.nanmax(x)

        if mu2 < np.nanmin(x):
            mu2 = np.nanmin(x)
        elif mu2 > np.nanmax(x):
            mu2 = np.nanmax(x)


        if sigma1 <= 0:
            sigma1 = 0.0001

        if sigma2 <= 0:
            sigma2 = 0.0001

        if w <= 0:
            w = 0.0001
        elif w > 1:
            w = 1 - 0.0001


        dp = w * np.exp((-(x-mu1)**2) / (2 * sigma1**2)) / (2 * math.pi * sigma1**2)**(1/2) +\
        (1-w) * np.exp((-(x-mu2)**2) / (2 * sigma2**2)) / (2 * math.pi * sigma2**2)**(1/2)

        # Can only use np.sum() otherwise minimize() will output a ValueError
        dlnl = -sum(np.log(dp))

        return dlnl


    # Find most probable values for double gaussian

    params0 = [mu_-sigma_, mu_+sigma_, sigma_, sigma_, 0.5]


    result = minimize(dgausslogl, params0, args= x, method='Nelder-Mead')



    # BIC: Best model has LOWEST BIC

    k = [2,5]
    logL1 = gausslogl(x)
    logL2 = -dgausslogl(result.x,x)
    n = len(x)

    # print(logL1)
    # print(logL2)

    def bic_calc(n,k,logL1,logL2):

        bic_val = []
        bic_val.append(k[0] * np.log(n) - 2 * logL1)
        bic_val.append(k[1] * np.log(n) - 2 * logL2)

        if bic_val[0] <= bic_val[1]:
            bic_val.append("SINGLE gaussian model")
        else:
            bic_val.append("DOUBLE gaussian model")

        return bic_val




    BIC = bic_calc(n,k,logL1,logL2)

    print("For sample %s" %sample_names[i])

    print("Log-likelihood for the DOUBLE guassian model is:\n", -dgausslogl(result.x,x))

    print(" BIC for SINGLE gaussian model is:\n", BIC[0], "\n", "BIC for DOUBLE gaussian model is:\n", BIC[1])

    print(" The more likely model is the %s"%BIC[2])

    print("\n\n")

