#!/usr/bin/env python3

"""ER4_CTCF_annotation.txt or 
Usage: ./CTCF_annotation_count.py ER4_CTCF_annotation.txt >> Annotation_counting.out
       or 
       ./CTCF_annotation_count.py G1E_CTCF_annotation.txt >> Annotation_counting.out

"""

import sys

overlap = open(sys.argv[1])
promoter = 0
exon = 0
intron = 0
# counter = 0
for line in overlap:
    fields = line.rstrip("\n").split("\t")
    annotation = fields[3]
    # print(annotation)
    # counter += 1
    if annotation == "promoter":
        promoter += 1
    elif annotation == "exon":
        exon += 1
    elif annotation == "intron":
        intron += 1
    else:
        print("error!")

print("The number of promoter is %d" % promoter)
print("The number of exon is %d" % exon)
print("The number of intron is %d" % intron)
# print(counter)
    


