#!/usr/bin/env python3

"""
Usage: ./methylation_difference.py SRR1035452_1_bismark_bt2_pe.bedGraph SRR1035454_1_bismark_bt2_pe.bedGraph

"""


import sys

file1 = open(sys.argv[1])
file2 = open(sys.argv[2])

input1 = []

overlap = []

file1uniq = []
file2uniq = []

for i, line in enumerate(file1):
    if i == 0:
        continue
    input1.append(line)
    

# print(input1)
counter = 0
for i, line in enumerate(file2):
    if i == 0:
        continue
    if line not in input1:
        file2uniq.append(line)
    else:
        overlap.append(line)
    counter += 1

for item in input1:
    if item not in overlap:
        file1uniq.append(item)
        
# print(len(overlap))
# print(len(input1))
# print(len(file1uniq))
# print(len(file2uniq))
# print(counter)

print("The methylation sites in “ES_f_mC” but not in “EpiSC_mC” are:\n")
for item in file2uniq:
    print(item)
print("****************************************************")
print("The methylation sites in “EpiSC_mC” but not in “ES_f_mC” are:\n")
for item in file1uniq:
    print(item)



