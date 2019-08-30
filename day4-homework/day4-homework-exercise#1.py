#!/usr/bin/env python3

"""
Command line will be 
./day4-homework-exercise#1.py ~/qbb2019/data/samples.csv ../results/stringtie/
"""

import sys
import os
import pandas as pd

metadata = sys.argv[1]
ctab_dir = sys.argv[2]

#Inputing samples.csv and merging sex and stage as sexstage_id(ssid)
fpkms = {}
for i, line in enumerate(open(metadata)):
    if i == 0:
        continue
    fields = line.split(",")
    srr_id = fields[0]
    sex = str(fields[1])
    stage = str(fields[2]).rstrip("\n")
    ctab_path = os.path.join(ctab_dir, srr_id, "t_data.ctab")
    sexstage_id = sex + "_" + stage
    
    df = pd.read_csv(ctab_path, sep="\t", index_col="t_name")
    
    fpkms["gene_name"] = df.loc[:,"gene_name"]
    fpkms[sexstage_id] = df.loc[:,"FPKM"]


#Generating fpkms dataframe with ssid and save as .csv file   
df_fpkms = pd.DataFrame(fpkms)

pd.DataFrame.to_csv(df_fpkms, "all.csv")
    
    
    
    