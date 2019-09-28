#!/usr/bin/env python3

"""
Usage: ./pca_generelatedness.py plink.eigenvec    

"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy
from sklearn.decomposition import PCA


df = pd.read_csv(sys.argv[1],sep = " ", header = None)
# print(df)
# print(df.iloc[:,3])
# print(type(df.iloc[0,3]))

fig, ax = plt.subplots()
ax.scatter( x = df.iloc[:,2], y = df.iloc[:,3])
ax.set_title("PCA of Gene Relatedness")
ax.set_ylabel("PC2")
ax.set_xlabel("PC1")
fig.savefig("pca_generelatedness.png")
plt.close(fig)








# n, p = df.shape
# col_names = df.columns.values.tolist()
#
# fit = PCA().fit_transform(df.T)