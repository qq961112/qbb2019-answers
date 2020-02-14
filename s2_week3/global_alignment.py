#!/usr/bin/env python3

"""
Usage: ./global_alignment.py
"""

import numpy as np

seq_1 = "CATAAACCCTGGCGCGCTCGCGGCCCGGCACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAAAAAAAAAAAAAAAAAAA"
seq_2 = "GGGGCTGCCAACACAGAGGTGCAACCATGGTGCTGTCCGCTGCTGACAAGAACAACGTCAAGGGCATCTTCACCAAAATCGCCGGCCATGCTGAGGAGTATGGCGCCGAGACCCTGGAAAGGATGTTCACCACCTACCCCCCAACCAAGACCTACTTCCCCCACTTCGATCTGTCACACGGCTCCGCTCAGATCAAGGGGCACGGCAAGAAGGTAGTGGCTGCCTTGATCGAGGCTGCCAACCACATTGATGACATCGCCGGCACCCTCTCCAAGCTCAGCGACCTCCATGCCCACAAGCTCCGCGTGGACCCTGTCAACTTCAAACTCCTGGGCCAATGCTTCCTGGTGGTGGTGGCCATCCACCACCCTGCTGCCCTGACCCCGGAGGTCCATGCTTCCCTGGACAAGTTCTTGTGCGCCGTGGGCACTGTGCTGACCGCCAAGTACCGTTAAGACGGCACGGTGGCTAGAGCTGGGGCCAACCCATCGCCAGCCCTCCGACAGCGAGCAGCCAAATGAGATGAAATAAAATCTGTTGCATTTGTGCTCCAG"

if len(seq_1) <=  len(seq_2): # seq1 is a longer 1, will be the columns
    seq1 = seq_2
    seq2 = seq_1
else:
    seq1 = seq_1
    seq2 = seq_2



sigma = [ [   91, -114,  -31, -123 ],
          [ -114,  100, -125,  -31 ],
          [  -31, -125,  100, -114 ],
          [ -123,  -31, -114,   91 ] ]
          
gap = 300

# HoxD70 matrix of Chiaromonte, Yap, Miller 2002,


def show_matrix(mat):
    for i in range(0, len(mat)):
        print("[", end = "")
        for j in range(0, len(mat[i])):
            print(mat[i][j], end = "")
            if j != len(mat[i]) - 1:
                print("\t", end = "")
        print("]\n")




def matching(a, b):
    if a == b:
        if b == "A":
            return 91
        if b == "C":
            return 100
        if b == "G":
            return 100
        if b == "T":
            return 91
    else: ## a != b
        g = max(a, b)
        s = min(a, b)
        if g == "C":
            return -114
        if g == "G":
            if s == "A":
                return -31
            else:
                return -125
        else:
            if s == "A":
                return -123
            if s == "C":
                return -31
            else:
                return -114

            



#Initializing the first row/column
# nrow = len(seq1) + 1
# ncol = len(seq2) + 1

track = []

# seq1 = "ATCG"
# seq2 = "G"


ncol = len(seq1) + 1

nrow = len(seq2) + 1

#seq2 is a shorter one


aligning_mat = np.zeros((nrow, ncol), dtype = "int")

delta = gap

for i in range(1, ncol):
    aligning_mat[0, i] = aligning_mat[0, i-1] - delta

for j in range(1, nrow):
    aligning_mat[j, 0] = aligning_mat[j-1, 0] - delta


for i in range(1, nrow):
    for j in range(1, ncol):
        alignment = aligning_mat[i-1][j-1] + matching(seq1[j-1], seq2[i-1])
        deletion = aligning_mat[i-1][j] - delta
        addition = aligning_mat[i][j-1] - delta
        aligning_mat[i][j] = max(alignment, deletion, addition)
    
#show_matrix(aligning_mat)
np.savetxt('Alignment_matrix.txt', aligning_mat, fmt="%d")


i = nrow - 1
j = ncol - 1

while ((i != 0) or (j != 0)):
    align = aligning_mat[i-1][j-1]
    up = aligning_mat[i-1][j]
    left = aligning_mat[i][j-1]
    max_score = max(align, up, left)
    if max_score == align:
        track.append("A")                                                                                           
        i -= 1
        j -= 1
    if max_score == up:
        track.append("V")
        i -= 1
    if max_score == left:
        track.append("H")
        j -= 1
 
# for i in range(nrow -1, -1, -1):
#     if

aseq1 = []
aseq2 = []

vec1 = len(seq1) - 1
vec2 = len(seq2) - 1

for i in range(len(track)):
    if track[i] == "A":
        aseq1.append(seq1[vec1])
        aseq2.append(seq2[vec2])
        vec1 -= 1
        vec2 -= 1
    if track[i] == "V":
        aseq1.append("-")
        aseq2.append(seq2[vec2])
        vec2 -= 1
    if track[i] == "H":
        aseq2.append("-")
        aseq1.append(seq1[vec1])
        vec1 -= 1

#
# for i in range(len(aseq1)-1, -1, -1):
aseq1 = aseq1[::-1]
aseq2 = aseq2[::-1]
rseq1 = ''.join([str(elem) for elem in aseq1]) 
rseq2 = ''.join([str(elem) for elem in aseq2]) 

print("Aligned sequence 1 is:")
print(rseq1,"\n")
print("Aligned sequence 2 is:")
print(rseq2)
# print(aligning_mat[nrow-1][ncol-1])
    
        
    
        


