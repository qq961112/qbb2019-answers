#!/usr/bin/env python3

import sys

flyID = []
uniID = []
counter = 0
flag = 0

#flyID and uniID work as a dict together:)


#Four arguments are needed in order: .py file (this one), mapping file, .ctab file, function option
#Function option: 0 for not printing the unmatched lines, others for printing a default value

function = sys.argv[3]

for line in open(sys.argv[1]):
    id = line.rstrip("\n").split("\t")
    uniID.append(id[0])
    flyID.append(id[1].lstrip(" "))
    counter += 1


for i, line in enumerate(open(sys.argv[2])):
    if i == 0:
        continue
    flag = 0
    output =""
    columns = line.rstrip("\n").split("\t")
    gene_ID = columns[8]
    for k in range(counter):
        # print(gene_ID,pID[k])
        if gene_ID == flyID[k]:
            output = uniID[k]
            flag = 1
            break
        k += 1
    if flag == 1:
        print(line.rstrip("\n"), "\t", output)
    else:
        if function != "0":
            output = "N/D"
            print(line.rstrip("\n"), "\t", output)







    