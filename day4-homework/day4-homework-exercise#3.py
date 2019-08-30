#!/usr/bin/env python3

"""    
Plot a second series from male samples, style the plot and add stage 14 replicates

Command line will be 
./day4-homework-exercise#3.py FBtr0331261 ~/qbb2019/data/samples.csv all.csv ~/qbb2019/data/replicates.csv
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

t_name = sys.argv[1]

#Generating list for male and female samples
femalelist = []
malelist = []
fulllist = []
for i, line in enumerate(open(sys.argv[3])):
    if i == 0:
        fields = line.rstrip("\n").split(",")
        for field in fields:
            if "name" not in field:
                fulllist.append(field)
                if "female" in field:
                    femalelist.append(field)
                else:
                    malelist.append(field)
                  

#Getting a list with unique stages
allstage = []
stage = []
for i, line in enumerate(open(sys.argv[2])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split(",")
    allstage.append(fields[len(fields)-1])

for i in allstage:
    if i not in stage:
        stage.append(i)
    

#Load FPKMs
fpkms = pd.read_csv(sys.argv[3], index_col = "t_name")


#Extract data in the t_name row
female_data = []
male_data = []

for ssid in fulllist:
    if ssid in femalelist:
        female_data.append(fpkms.loc[t_name,ssid])
    else:
        male_data.append(fpkms.loc[t_name,ssid])
        
        
#Adding stage 14 replicates from replicate.csv        
rp_fpkms={}
f_goi_re_fpkms=[]
m_goi_re_fpkms=[]
#14 replicates
ctab_dir = "../results/stringtie/"
for i, line in enumerate(open(sys.argv[4])):
    if i == 0:
        continue
    fields = line.split(",")
    srr_id = fields[0]
    rsex = str(fields[1])
    rstage = str(fields[2]).rstrip("\n")
    ctab_path = os.path.join(ctab_dir, srr_id, "t_data.ctab")
    rsexstage_id = rsex + "_" + rstage
    
    df = pd.read_csv(ctab_path, sep="\t", index_col="t_name")
    rp_fpkms["gene_name"] = df.loc[:,"gene_name"]
    rp_fpkms[rsexstage_id] = df.loc[:,"FPKM"]

#Seperating replicates into male_replicates and female_replicates
replicate_fpkms = pd.DataFrame(rp_fpkms)
replicate_fpkms = replicate_fpkms.drop(columns = "gene_name")
rp_male_fpkms = replicate_fpkms.loc[:,malelist]
rp_female_fpkms = replicate_fpkms.loc[:,femalelist]

male_replicate=list(rp_male_fpkms.loc[t_name,:])[4:]
female_replicate=list(rp_female_fpkms.loc[t_name,:])[4:]

#Setting the range for new plots of replicates
latestage=[4,5,6,7]


#Plotting male and female samples
fig, ax = plt.subplots(figsize=(6,4.8))
fig.suptitle('Sxl', fontsize = 20)
ax.plot(female_data,color="red", label="female")
ax.plot(male_data,color="blue", label="male")
ax.set_xlabel("development stage")
ax.set_ylabel("mRNA abundance (RPKM)")
ax.set_xticks([0,1,2,3,4,5,6,7])
ax.set_xticklabels(stage,fontsize = 6, rotation = 90)


#Plotting replicates
ax.scatter( x = latestage, y = female_replicate, color="black",marker = 10)
ax.scatter( x = latestage, y = male_replicate, color="orange")
ax.plot(latestage,female_replicate,color="black", label="female_re")
ax.plot(latestage,male_replicate,color="orange", label="male_re")

#Legend outside plot area
box = ax.get_position()
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

fig.savefig("timecourse.png")
plt.close(fig)