#!/usr/bin/env python3

"""
Usage: ./k_means.py hema_data.txt
    

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import seaborn as sns
from sklearn.cluster import KMeans



hema_data = open(sys.argv[1])

gene_name = []


# df1 = pd.read_csv(hema_data, sep = "\t", names = ["gene_name_", "cfu","poly","unk","int","mys","mid"], index_col = "gene_name_")

hema_data.seek(0)
df3 = pd.read_csv(hema_data, sep = "\t", header = 0, index_col = "gene")


cfu1 = df3["CFU"].values
poly1 = df3["poly"].values

# genedf = df1.iloc[1:,:]
#
# cfu = genedf["cfu"].values
# poly = genedf["poly"].values



df2 = pd.DataFrame({"cfu": cfu1, "poly": poly1})
# print(df2)

# df4 = pd.DataFrame({"x": cfu, "y": poly})
# print(df4)

kmeans = KMeans(n_clusters=3).fit(df2)
centroids = kmeans.cluster_centers_
print(centroids)

fig, ax = plt.subplots()
ax.scatter(df2['cfu'], df2['poly'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
ax.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
ax.set_title("K_means Clustering (k=3)")
ax.set_xlabel("Expression in CFU")
ax.set_ylabel("Expression in poly")
fig.tight_layout()
fig.savefig("k_means.png")
plt.close(fig)
