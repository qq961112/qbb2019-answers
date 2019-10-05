#!/usr/bin/env python3

"""
Usage: ./back_nt.py new_blast_output.fa aa_alignment.out week5_query.fa

"""

import sys
from fasta import FASTAReader
import numpy as np
import matplotlib.pyplot as plt
import math


dna_reader = FASTAReader(open(sys.argv[1]))
dna_sequence = []
blast_dnaid = []
for ident, sequence in dna_reader:
   dna_sequence.append(sequence)
   blast_dnaid.append(ident)

# dna = dna_sequence[0]
# print(len(dna))

protein_reader = FASTAReader(open(sys.argv[2]))
protein_sequence = []

for ident, sequence in protein_reader:
   protein_sequence.append(sequence)
   
# print(len(protein_sequence))

l = len(protein_sequence)
aligned_dna = {}
# for i in range(len(protein_sequence)):
for i in range(len(protein_sequence)):
    dna = dna_sequence[i]
    gap_dna = ""
    count = 0
    for num, a in enumerate(protein_sequence[i]):
        if a == "-":
            gap_dna = gap_dna + "---"
            # print("***")
            # print(a)
            
        else:
            gap_dna = gap_dna + dna[count*3:count*3+3]
            count += 1
    # print(len(gap_dna))
    aligned_dna[blast_dnaid[i]] = gap_dna
    # print(len(dna))

# print(aligned_dna) 

protein_id = {} 

for i in range(len(protein_sequence)):
    protein_id[blast_dnaid[i]] = protein_sequence[i]
    
    
# print(protein_id)
# print(len(protein_id["M12294"]))
# print(len(protein_id["AY532665"]))
# print(len(aligned_dna["M12294"]))
# print(len(aligned_dna["AY532665"]))

total_number = len(protein_sequence)
length_aa = int(len(aligned_dna["M12294"])/3)

dS = [0] * length_aa
dN = [0] * length_aa

for i in range(0, len(aligned_dna["M12294"]), 3):
    q_codon = aligned_dna["M12294"][i:i+3]
    for j in range(1, 102):
        seq_id = blast_dnaid[j]
        dna_seq = aligned_dna[seq_id]
        # print(seq_id)
        seq_codon = dna_seq[i:i+3]
        if q_codon != seq_codon:
            q_aa = protein_id["M12294"][int(i/3)]
            seq_aa = protein_id[seq_id][int(i/3)]
            if q_aa == seq_aa:
                dS[int(i/3)] += 1
            if q_aa != seq_aa:
                dN[int(i/3)] += 1
                
    ### blast_dnaid[102]=blast_dnaid[103]=KJ883347, whose alignment is 'toxic' and very different from query. 
    ### So I skipped that.
    
    for j in range(104, total_number):
        seq_id = blast_dnaid[j]
        dna_seq = aligned_dna[seq_id]
        # print(seq_id)
        seq_codon = dna_seq[i:i+3]
        if q_codon != seq_codon:
            q_aa = protein_id["M12294"][int(i/3)]
            seq_aa = protein_id[seq_id][int(i/3)]
            if q_aa == seq_aa:
                dS[int(i/3)] += 1
            if q_aa != seq_aa:
                dN[int(i/3)] += 1

                

# print(aligned_dna["HM756673"])
# print(dS)
# print(dN)

# print(protein_id["M12294"])
# print("...")
# print(protein_id["KJ883347"])



dD_values = []
ratio = []
for i in range(length_aa):
    dD_values.append(dN[i] - dS[i])
    ratio.append((dN[i]+1)/(dS[i]+1))


# print(dD_values)
# print(ratio)

mean = np.mean(dD_values)
std = np.std(dD_values)

# print(len(dD_values))

z = []
for i in range(len(dD_values)):
    z.append(abs((dD_values[i]-mean)/std))


# print(z)

print("The mean of all D values is " + str(mean))
print("The standard deviation of all D values is " + str(std))
print("For Z-test, alpha = 0.05, critical z value = 1.645")


fig, ax = plt.subplots()
for i in range(len(ratio)):
    if z[i] < 1.645:
        ax.scatter(i, ratio[i], alpha = 0.3, color = "blue", s = 3)
    else:
        ax.scatter(i, ratio[i], alpha = 0.3, color = "red", s = 3)
ax.plot([0,len(ratio)],[1,1], color = "orange", label = "ratio = 1")
ax.set_title("dN/dS Ratio Distribution")
ax.set_ylabel("dN/dS")
ax.set_xlabel("Position within Query Amino Acid Sequence")
fig.savefig("dN_to_dS_distribution.png")
plt.close(fig)


    



    
