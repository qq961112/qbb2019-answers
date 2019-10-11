#!/usr/bin/env python3

"""
Usage: ./two_subplot.py G1E_CTCF_annotation.txt ER4_CTCF_annotation.txt loss_binding.bed gain_binding.bed
    

"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy

overlap_G1E = open(sys.argv[1])
promoter1 = 0
exon1 = 0
intron1 = 0
for line in overlap_G1E:
    fields = line.rstrip("\n").split("\t")
    annotation = fields[3]
    if annotation == "promoter":
        promoter1 += 1
    elif annotation == "exon":
        exon1 += 1
    elif annotation == "intron":
        intron1 += 1
        

overlap_ER4 = open(sys.argv[2])
promoter2 = 0
exon2 = 0
intron2 = 0
for line in overlap_ER4:
    fields = line.rstrip("\n").split("\t")
    annotation = fields[3]
    if annotation == "promoter":
        promoter2 += 1
    elif annotation == "exon":
        exon2 += 1
    elif annotation == "intron":
        intron2 += 1
        
loss_CTCF = open(sys.argv[3])
loss = 0
for line in loss_CTCF:
    loss += 1

gain_CTCF = open(sys.argv[4])
gain = 0
for line in gain_CTCF:
    gain += 1
    
output = ["Promoter_G1E", "Exon_G1E", "Intron_G1E", "Promoter_ER4", "Exon_ER4", "Intron_ER4"]
# output_1st = ["Promoter_G1E", "Exon_G1E", "Intron_G1E"]
# output_2nd = ["Promoter_ER4", "Exon_ER4", "Intron_ER4"]
output_value = [promoter1, exon1, intron1, promoter2, exon2, intron2]

output2 = ["Gain","Loss"]
output2_value = [gain, loss]
# print(output)

fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2)
fig = plt.figure(figsize=(10, 6))
ax1 = plt.subplot2grid((1, 3), (0, 0), colspan=2)
ax1.bar(output[0], output_value[0],color = "red")
ax1.bar(output[1], output_value[1],color = "orange")
ax1.bar(output[2], output_value[2],color = "yellow")
ax1.bar(output[3], output_value[3],color = "green")
ax1.bar(output[4], output_value[4],color = "cyan")
ax1.bar(output[5], output_value[5],color = "blue")
ax1.xaxis.set_ticks_position('none')
ax1.set_xticklabels(output)
ax1.set_title("Annotation of CTCF sites")
ax1.set_ylabel("# of CTCF sites")

ax2 = plt.subplot2grid((1, 3), (0, 2), colspan=2)
ax2.bar(output2[0], output2_value[0],color = "black")
ax2.bar(output2[1], output2_value[1],color = "grey")
ax2.set_title("Changes in CTCF sites")
ax2.set_ylabel("# of CTCF sites")


fig.tight_layout()
fig.savefig("two_subplots.png")
plt.close(fig)

