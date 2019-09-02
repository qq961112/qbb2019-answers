#!/usr/bin/env python3

"""
Usage: ./day5-lunch-exercise#4.py H3K4me1.tab H3K4me3.tab H3K9me3.tab t_data.ctab
    

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy


df1 = pd.read_csv(sys.argv[1],sep = "\t", names = ["t_name_", "size","covered","sum","mean0","H3K4me1"], index_col = "t_name_")
df2 = pd.read_csv(sys.argv[2],sep = "\t", names = ["t_name", "size","covered","sum","mean0","H3K4me3"], index_col = "t_name")
df3 = pd.read_csv(sys.argv[3],sep = "\t", names = ["t_name", "size","covered","sum","mean0","H3K9me3"], index_col = "t_name")
fpkm = pd.read_csv(sys.argv[4], sep = "\t", index_col = "t_name")

# print(fpkm)
#fpkm = pd.read_csv(sys.argv[4], index_col = "t_id")

# print(df1)

mean1 = df1.loc[:,"H3K4me1"]
mean2 = df2.loc[:,"H3K4me3"]
mean3 = df3.loc[:,"H3K9me3"]
fpkms = fpkm.loc[:,"FPKM"]
lm = pd.concat((mean1,mean2,mean3,fpkms),axis = 1)


# print(lm)
# print(mean)


model = sm.formula.ols(formula = "FPKM ~ H3K4me1 + H3K4me3 + H3K9me3", data = lm)

ols_results = model.fit()
print(ols_results.summary())

