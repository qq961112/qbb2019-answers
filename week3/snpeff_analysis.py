#!/usr/bin/env python3

"""
Usage: ./dp_distribution.py vcf_files/snpeff.vcf
    

"""

import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import statsmodels.api as sm
import scipy

vcf = open(sys.argv[1])
dps = []
gqs= []
afs = []
effs = []
impacts = []
impact_value = []
effects = {}
for line in vcf:
    if line.startswith("#"):
        continue
    fields = line.rstrip("\n").split("\t")
    para = fields[7].rstrip("\t").split(";")
    dp = para[7].split("=")
    dps.append(dp[1])
    
    gq = fields[5].rstrip('\t')
    gqs.append(int(float(gq)))
    
    af = para[3].split("=")
    afs.append(af[1])
    
    # for i in range(len(para)):
    #     if "ANN" in para[i]:
    #         print(para[i])
            # annotation = para[i].rstrip("\n").split[","]
            # print(annotation[0])
            # ann = annotation[1].split["|"]
            # eff = ann[1]
            # effs.append(eff)
            
    ann = para[41].rstrip("\t").split("|")
    eff = ann[1]
    effs.append(eff)
            
    
for effect in effs:
    if effect == "":
        effect = "N/A"
    if effect not in impacts:
        impacts.append(effect)
        effects[effect] = 1
    else:
        effects[effect] += 1
            
for impact in impacts:
    impact_value.append(effects[str(impact)])
       
    
l = len(dps)
# print(dps)
# print(gqs)
# print(afs)
# print(effs)
# print(effects)
# print(impacts)
# print(impact_value)

fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2)

ax1.hist(dps, bins = 100, density = True)
ax1.xaxis.set_ticks_position('none')
empty_string_labels = ['']*l
ax1.set_xticklabels(empty_string_labels)
ax1.set_title("Read Depth Distribution")
ax1.set_ylabel("Read Depth")
ax1.set_xlabel("Position of SNP")


ax2.hist(gqs, range=(0,3000), bins = 50, density = True)
ax2.xaxis.set_ticks_position('none')
ax2.set_title("Genotype Quality Distribution")
ax2.set_ylabel("Genotype Quality")
ax2.set_xlabel("Variants")

ax3.hist(afs, bins = 100, density = True)
# ax3.xaxis.set_ticks_position('none')
empty_string_labels = ['']*l
ax3.set_xticklabels(empty_string_labels)
ax3.set_title("Allele Frequency Spectrum")
ax3.set_ylabel("Alleles Frequency")
ax3.set_xlabel("Alleles")

ax4.bar(impacts, impact_value, align='center', alpha=0.5)
ax4.set_xticklabels(impacts, rotation = "vertical",size = 4)
ax4.set_title("Predicted Effects Summary")
ax4.set_ylabel("# of Variants")
ax4.set_xlabel("Predicted Effects")

fig.tight_layout()
fig.savefig("four_subplots_final.png")
plt.close(fig)


