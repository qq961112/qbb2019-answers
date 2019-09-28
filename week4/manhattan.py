#!/usr/bin/env python3

"""
Usage: ./manhattan.py phenotype.txt    

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy


phenos = []
paths = []

for i, line in enumerate(open(sys.argv[1])): ## sys.argv[1] is the phenotype text
    if i == 0:
        fields = line.rstrip("\n").split("\t")
        for field in fields:
            if "ID" not in field:
                phenos.append(field)
    else:
        break

# print(phenos)
l = len(phenos)

for i in range(l):
    path = "/Users/cmdb/qbb2019-answers/week4/plink." + phenos[i] + ".qassoc"
    paths.append(path)


# print(paths)


for j in range(l):
     pos = []
     pval = []
     logp = []
     counter = 0
     for i, line in enumerate(open(paths[j])): 
         if i == 0:
             continue 
         if "NA" in line:
             continue
         cols = line.rstrip("\n").split()
         pval = float(cols[8])
         if pval != 0:
             logp.append(-(np.log10(pval)))
             counter += 1
             pos.append(counter)


     fig, ax = plt.subplots()
     for i in range(len(pos)):
         if logp[i] < 5:
             ax.scatter(pos[i],logp[i], alpha = 0.3, color = "blue", s = 3)
         else:
             ax.scatter(pos[i],logp[i], alpha = 0.3, color = "red", s = 3)
     ax.set_title("GWAS Manhattan Plot__"+phenos[j])
     ax.set_ylabel("Log10(P)")
     ax.set_xlabel("SNP Position")
     fig.savefig(phenos[j]+".png")
     plt.close(fig)
     
     print(phenos[j]+" Plotted ")
     

        




