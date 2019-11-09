#!/usr/bin/env python3

"""
Usage: ./heatmap.py hema_data.txt
    

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import seaborn as sns



hema_data = open(sys.argv[1])

gene_name = []


df1 = pd.read_csv(hema_data, sep = "\t", names = ["gene_name_", "cfu","poly","unk","int","mys","mid"], index_col = "gene_name_")

# hema_data.seek(0)
# df2 = pd.read_csv(hema_data, sep = "\t")
# print(df2)


genedf = df1.iloc[1:,:]


gene_list = df1.index.tolist()

# print(gene_list)

T_genedf = genedf.transpose()

celltype_list = ["CFU", "poly", "unk", "int", "mys", "mid"]

# print(genedf)
# print(T_genedf)

Z1 = linkage(genedf, 'average')
Z2 = linkage(T_genedf, 'average')
# print(Z)

k1 = leaves_list(Z1)
k2 = leaves_list(Z2)

# print(genedf)

genedf_1 = genedf.iloc[k1,:]
genedf_2 = genedf_1.iloc[:,k2]

x_label = ['']
for i in k2:
    x_label.append(celltype_list[i])


FPKM_matrix = genedf_2.values.astype(float)


fig, ax = plt.subplots()
im = ax.imshow(FPKM_matrix, aspect = "auto")

cbar = fig.colorbar(im, ax = ax)
cbar.ax.set_yticklabels(['low','','','','','','high'],rotation = 270,  size = 8)
cbar.set_label('Expression', rotation=270,size = 13)
cbar.ax.yaxis.set_ticks_position('none')


ax.set_title("Heatmap of Six Cell Types")
ax.set_xlabel("Cell Types")
ax.set_ylabel("FPKM of genes", rotation = 90)
ax.yaxis.set_ticks_position('none')
y_string_labels = ['']*500
ax.set_yticklabels(y_string_labels)
x_string_labels = x_label
ax.set_xticklabels(x_string_labels)
fig.tight_layout()
fig.savefig("heatmap.png")
plt.close()
