#!/usr/bin/env python3

"""
./transform_id.py BYxRM_PhenoData.txt

"""

import sys
import os
import pandas as pd

familyid = []
sampleid = []
phenotype = {}
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.split("\t")
    id = str(fields[0]).split("_")
    familyid.append(id[0])
    sampleid.append(id[1])
    
    
# print(familyid)

df = pd.read_csv(sys.argv[1],sep = "\t")
df["FID"] = familyid
df["IID"] = sampleid

newdf = df.loc[:,["FID","IID"]]
phenotype = df.iloc[:,1:47]
newdf1 = pd.concat((newdf,phenotype), axis = 1)

pd.DataFrame.to_csv(newdf1, "phenotype.txt", sep = "\t", index = False, na_rep = "NA")