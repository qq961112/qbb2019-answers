#!/usr/bin/env python3

"""
Create an MA-plot for two samples of your choice

Command line will be 
./day4-homework-exercise#1.py SRR072893 SRR072903 ../results/stringtie/
"""

import sys
import os
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

#Taking inputs and generate two sample lists (t_genes in the same order)
source1, source2 = sys.argv[1], sys.argv[2]
ctab_dir = sys.argv[3]

ctab_path1 = os.path.join(ctab_dir, source1, "t_data.ctab")
ctab_path2 = os.path.join(ctab_dir, source2, "t_data.ctab")

fpkms1={}
df1 = pd.read_csv(ctab_path1, sep="\t", index_col="t_name")
fpkms1[source1] = df1.loc[:,"FPKM"]
df_fpkms1 = pd.DataFrame(fpkms1)
list1=list(df_fpkms1.loc[:,str(source1)])

fpkms2={}
df2 = pd.read_csv(ctab_path2, sep="\t", index_col="t_name")
fpkms2[source2] = df2.loc[:,"FPKM"]
df_fpkms2 = pd.DataFrame(fpkms2)
list2=list(df_fpkms2.loc[:,str(source2)])


#Getting M and A
listm=[]
lista=[]

for i in range(len(list1)):
    m = np.log2(list1[i]+1)
    n = np.log2(list2[i]+1)
    listm.append(m-n)
    lista.append((m+n)/2)

#Plotting
fig, ax = plt.subplots()
fig.suptitle('M-A plot for SRR072893 vs SRR072903', fontsize = 20)
ax.set_xlabel("A")
ax.set_ylabel("M")
ax.scatter( x = lista, y = listm, color = "red", alpha = 0.3)
fig.savefig("M-A_plot.png")
plt.close(fig)
    

    