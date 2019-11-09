#!/usr/bin/env python3

"""
Usage: ./differentially_expressed_genes.py hema_data.txt
    

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
import seaborn as sns
import scipy.stats as sp
from sklearn.cluster import KMeans



hema_data = open(sys.argv[1])

gene_name = []


df1 = pd.read_csv(hema_data, sep = "\t", header = 0, index_col = "gene")

# hema_data.seek(0)
# df2 = pd.read_csv(hema_data, sep = "\t")
# print(df2)



diff_exp_high = (((df1['CFU'] + df1['unk'])/2)/((df1['poly'] + df1['int'])/2)) >= 2
diff_exp_low = (((df1['CFU'] + df1['unk'])/2)/((df1['poly'] + df1['int'])/2)) <= 0.5

diff_exp_genes = df1[diff_exp_high | diff_exp_low]


# print(diff_exp_genes)

# df2 = (diff_exp_genes['CFU'] + diff_exp_genes['unk'])/2
# df3 = (diff_exp_genes['poly'] + diff_exp_genes['int'])/2

cfu1 = list(diff_exp_genes["CFU"].values)
poly1 = list(diff_exp_genes["poly"].values)
int1 = list(diff_exp_genes["int"].values)
unk1 = list(diff_exp_genes["unk"].values)

gene_name1 = list(diff_exp_genes.index.values)

l = len(gene_name1) 
# print(l)
# print(gene_name1)
sig_de_genes = []
for i in range(l):
    early = [cfu1[i], unk1[i]]
    late = [poly1[i], int1[i]]
    t, p  = (sp.ttest_rel(early, late))
    if p <= 0.05:
        sig_de_genes.append(gene_name1[i])
        most_de = i

print(sig_de_genes)
# print(cfu1[most_de]+unk1[most_de])
# print(poly1[most_de]+int1[most_de])

# print(cfu1[most_de])
# print(poly1[most_de])

cfu = list(df1["CFU"].values)
poly1 = list(df1["poly"].values)
all_gene_names = list(df1.index.values)

for i, gene in enumerate(all_gene_names):
    if gene == sig_de_genes[0]:
        most_de_in_all = i

# print(most_de_in_all)

kmeans = KMeans(n_clusters=3).fit(df1)
my_dict = {i: np.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}

for i in range(3):
    if most_de_in_all in my_dict[i]:
        cluster = i

# print(cluster)
similar_genes = []
for j in my_dict[cluster]:
    similar_genes.append(all_gene_names[j])
    
# print(similar_genes)

for gene_name in similar_genes:
    print(gene_name)


        



