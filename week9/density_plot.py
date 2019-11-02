#!/usr/bin/env python3

"""
Usage: ./density_plot.py memechip_out/fimo_out_1/fimo.tsv 
    

"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

pos = open(sys.argv[1])

motif_start = []

for i,line in enumerate(pos):
    if i == 0:
        continue
    if i > 140:
        continue
    fields = line.rstrip("\n").split("\t")
    # print(fields)
    startsite = fields[3]
    score = round(float(fields[6]))
    for j in range(score):
        motif_start.append(int(startsite))
    # print(motif_start)
    

motif_start.sort()

# print(motif_start)


chr19 = [0]*61431566

#
for i in motif_start:
    for j in range(20):
        chr19[i+j] += 1
#
position = []
for i in range(len(chr19)):
    if chr19[i]!=0:
        for j in range(chr19[i]):
            position.append(i)

# print(position)
#
fig, ax = plt.subplots()
sns.distplot(position, hist= True, rug = True, kde = True)
ax.set_xlim(0,61431566)

x_string_labels = ['0','10000000','20000000','30000000','40000000','500000000','60000000','70000000']
ax.set_xticklabels(x_string_labels)
fig.autofmt_xdate()


ax.set_title("ER4 Top 100 Matched Motif Occurances")
ax.set_ylabel("Frequency")
ax.set_xlabel("Position on Chr 19")
fig.tight_layout()
# plt.show()
fig.savefig("Matched_Motif_Occurance_Frequency.png")
plt.close(fig)

