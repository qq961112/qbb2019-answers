#!/usr/bin/env python3

"""
Usage: ./day5-lunch-exercise#4.py H3K4me1.tab H3K4me3.tab H3K9me3.tab
    

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy


df1 = pd.read_csv(sys.argv[1],sep = "\t", names = ["t_name_", "size","covered","sum","mean0","H3K4me1"])
df2 = pd.read_csv(sys.argv[2],sep = "\t", names = ["t_name", "size","covered","sum","mean0","H3K4me3"])
df3 = pd.read_csv(sys.argv[3],sep = "\t", names = ["t_name", "size","covered","sum","mean0","H3K9me3"])
fpkm = pd.read_csv(sys.argv[4], sep = "\t")

# print(fpkm)
#fpkm = pd.read_csv(sys.argv[4], index_col = "t_id")

# print(fpkm)

mean1 = df1.loc[:,["t_name_","H3K4me1"]]
mean2 = df2.loc[:,"H3K4me3"]
mean3 = df3.loc[:,"H3K9me3"]
fpkms = fpkm.loc[:,"FPKM"]
lm = pd.concat((mean1,mean2,mean3,fpkms),axis = 1)
# print(fpkms)
# print(lm)




#print(lm)
# print(mean)


model = sm.formula.ols(formula = "FPKM ~ H3K4me1 + H3K9me3 + H3K4me3", data = lm)

ols_results = model.fit()

print(ols_results.summary())

