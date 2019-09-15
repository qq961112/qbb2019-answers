#!/usr/bin/env python3

"""
generating dot plot from velvet/SPAdes results with multiple contigs

./dotplot.py velvet_test.csv
./dotplot.py spades_test.csv

"""


import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(sys.argv[1],sep = "\t", names = ["#score", "name1","strand1","size1","zstart1","end1","name2","strand2","size2","zstart2","end2","identity","idPct","coverage","covPct"])
df1 = df.loc[1:,:]
df1 = pd.DataFrame(df1)
#print(df1)

df1["zstart1"] = pd.to_numeric(df1["zstart1"], downcast ='signed', errors='coerce')
df2 = df1.sort_values(by=['zstart1'])
# print(df2)

config_size = df2["size2"].tolist()
config_start_x = df2["zstart1"].tolist()
config_start_y = []
config_end_x = []
config_end_y = []
lineup = 0
for i in range(len(config_size)):
    config_end_x.append(config_start_x[i] + int(config_size[i]))
    config_start_y.append(lineup)
    lineup += int(config_size[i])
    config_end_y.append(lineup)
    

# print(config_start_y)
# print(config_end_y)
#
# print(config_start_x)
# print(config_end_x)
l = len(config_size)


fig, ax = plt.subplots()
for i in range(l):
    ax.plot([config_start_x[i],config_end_x[i]],[config_start_y[i],config_end_y[i]], color = "black")

fig.savefig("dotplot_velvet.png")
plt.close(fig)
