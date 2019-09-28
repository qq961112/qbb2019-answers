#!/usr/bin/env python3

"""
Usage: ./pca_generelatedness.py plink.frq    

"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy

df = open(sys.argv[1])

maf = []

for line in df:
    if "CHR" in line:
        continue
    fields = line.rstrip("\n").split()
    maf.append(float(fields[4]))

# print(maf)



fig, ax = plt.subplots()
ax.hist(maf, bins = 100, density = True)
ax.xaxis.set_ticks_position('none')
empty_string_labels = ['']*len(maf)
ax.set_xticklabels(empty_string_labels)
ax.set_title("Allele Frequency Spectrum")
ax.set_ylabel("Frequency")
ax.set_xlabel("Alleles")
fig.savefig("Allele_Frequency_Spectrum.png")
plt.close(fig)