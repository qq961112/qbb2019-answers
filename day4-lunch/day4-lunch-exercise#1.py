#!/usr/bin/env python3

"""
Usage : ./01-hist.py [tab]

plot RPKM
"""

import sys
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats 
import pandas as pd

fpkms = []
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) > 0: 
        fpkms.append(float(fields[11]))
   

my_data = np.log2(fpkms) 
# ctab = pd.read_csv(sys.argv[1], sep = "\t")s
# print(ctab.describe())

x = np.linspace( -15, 15, 100)
mu = 3.3
sigma = 2.3
y = stats.norm.pdf(x, mu, sigma)

x = np.linspace( -15, 15, 100)
# print(a)
# print(type(a))
degree = float(sys.argv[2])
mean = float(sys.argv[3])
std = float(sys.argv[4])
b = stats.skewnorm.pdf(x, degree, mean, std)
#try 1.5 1.4 3.1

text=["degree=", str(degree), "mean=", str(mean),"std=", str(std)]

fig, ax = plt.subplots()
ax.set_title("log2 FPKM distribution")
ax.set_xlabel("FPKM in log2")
ax.set_ylabel("% in total")
ax.hist(my_data, bins = 100, density = True)
ax.plot(x, y, color = "red", label = "A")
ax.plot(x, b, color = "green", label = "B")
ax.text(-15,0.175,text,fontsize=8)
fig.savefig("fpkm_sw_opt_labelled_text.png")
plt.close(fig)