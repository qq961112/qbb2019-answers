#!/usr/bin/env python3


"""
Command line will be 
./day4-homework-exercise#2.py Sxl all.csv 

"""
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

gene_name = sys.argv[1]
fpkm_file = sys.argv[2]

#Getting gene of interest and booleans
df = pd.read_csv(fpkm_file, index_col = "t_name")
goi = df.loc[:,"gene_name"]== gene_name

#Generating malelist and femalelist
firstline = []
femalelist = []
malelist = []
for i, line in enumerate(open(sys.argv[2])):
    if i == 0:
      fields = line.rstrip("\n").split(",")
      #print(fields)
      for field in fields:
          if "name" not in field:
              if "female" in field:
                  femalelist.append(field)
              else:
                  malelist.append(field)
                  
#Generating subdataframes
fpkms = df.drop(columns = "gene_name")
male_fpkms = fpkms.loc[:,malelist]
female_fpkms = fpkms.loc[:,femalelist]


#Plotting two subplots and labeling with sample names
fig,(ax1,ax2) = plt.subplots(2,1,figsize=(12,6))
fig.suptitle('Two FPKM subplot from Male and Female')
ax1.boxplot(male_fpkms.loc[goi,:].T)
ax1.set_xticks([1,2,3,4,5,6,7,8])
ax1.set_xticklabels(malelist)

ax2.boxplot(female_fpkms.loc[goi,:].T)
ax2.set_xticks([1,2,3,4,5,6,7,8])
ax2.set_xticklabels(femalelist)

fig.savefig("boxplot.png")
plt.close(fig)