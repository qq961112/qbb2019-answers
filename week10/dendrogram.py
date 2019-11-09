#!/usr/bin/env python3

"""
Usage: ./dendrogram.py hema_data.txt
    

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

genedf = df1.iloc[1:,:]

T_genedf = genedf.transpose()

Z2 = linkage(T_genedf, 'average')

k2 = leaves_list(Z2)


celltype_list = ["CFU", "poly", "unk", "int", "mys", "mid"]
new_list = []
for item in k2:
    new_list.append(celltype_list[item])

fig, ax = plt.subplots()
ax = dendrogram(
    Z2,
    truncate_mode='lastp',  
    p=6,  
    leaf_rotation=90.,
    leaf_font_size=12.,
    show_contracted=True,  
    orientation='right',
    distance_sort='ascending',
    labels = new_list
)


fig.tight_layout()
fig.savefig("dendrogram.png")
plt.close()