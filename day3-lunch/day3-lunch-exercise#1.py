#!/usr/bin/env python3

import sys

pc = []
length = 0

for i, line in enumerate(open(sys.argv[1])):
    if "protein_coding" in line:
        fields = line.rstrip("\n").split("\t")
        if fields[0] == "3R" and fields[2] == "gene":
            pc.append(line)
            length +=  1
#print(length)

startpos = []             
#genename = []
genedict = {}

for i in range(length):
    fields = pc[i].rstrip("\n").split("\t")
    startpos.append(int(fields[3]))
    gene_name = fields[8].split(";")
    #genename.append(gene_name[2])
    genedict[fields[3]] = gene_name[2]
    i += 1

#print(genedict)

length1 = len(startpos)
mutation = 21378950
#mutation_test = int(input("try:"))


def binary_search(lst, m):
    l = len(lst)
    first = 0
    last = l-1
    flag = 0
    distance = 0
    iteration = 0
    while first <= last:
        mid = int((first + last) / 2)
        iteration += 1
        if lst[mid] == m:
            flag = 1
            break
        elif lst[mid] > m:
            last = mid - 1
        else:
            first = mid + 1
            
            
    if flag == 0 and mid+1 < l:
        if lst[mid+1] - m >= m - lst[mid]:
            distance = m - lst[mid]
            return lst[mid], distance, iteration
        else:
            distance = lst[mid+1] - distance
            return lst[mid+1], distance, iteration
    elif mid + 1 >= l:
        distance = m - lst[mid]
        return lst[mid], distance, iteration
    else:
        return lst[mid], distance, iteration 
        


answer= binary_search(startpos, mutation)
key = str(answer[0])
dis = int(answer[1])
itera = int(answer[2])

print("nearest gene is ", genedict[key],"\n", "disntance=", dis,"bp\n", "iteration=", itera)   

    



