#!/usr/bin/env python3


from fasta import FASTAReader
import sys

target = FASTAReader(open(sys.argv[1]))
query = FASTAReader(open(sys.argv[2]))
k = int(sys.argv[3])



kmers = {}
extender = []
extender_k = []
savetarget={}
for ident1, sequence1 in target:
    #print(ident1)
    savetarget[ident1]=sequence1
    for i in range(0, len(sequence1) - k + 1):
        kmer1 = sequence1[i:i+k]
        if kmer1 in kmers:
            kmers[kmer1].append((ident1, i))
        else:
            kmers[kmer1] = [(ident1, i)]

#for indent1, sequence1 in target:
for ident2, sequence2 in query:
    for i in range(0, len(sequence2) - k + 1 ):
        kmer2 = sequence2[i:i+k]
        if kmer2 in kmers:
            for duple in kmers[kmer2]:
                genename = duple[0].split(" ")
                target_start = int(duple[1])
                query_start = i
                #print(duple[0])
                #extender.append((genename[0], duple[1], i, kmer2))
                x = 0
                #print(target_start)
                #print(query_start)
                #print(len(sequence1))
                #print(len(sequence2))
                sequence_t = str(savetarget[duple[0]])
    
                if sequence_t[target_start-1] != sequence2[query_start-1] and target_start > 1 and query_start > 1 and (target_start+k+x < len(sequence_t)-1) and (query_start+k+x < len(sequence2)-1):
                    while (sequence_t[target_start+k+x] == sequence2[query_start+k+x]) and (target_start+k+x < len(sequence_t)-1) and (query_start+k+x < len(sequence2)-1):
                        x += 1
                        sequence_t[target_start+k+x]
                        sequence2[query_start+k+x]
                        target_start+k+x < len(sequence_t)-1
                        query_start+k+x < len(sequence2)-1
                    extender_k.append((x,sequence_t[target_start:target_start+k+x]))
                extender_k.sort()
                extender_k.reverse()
                unique_list = []
                for n in range(1,len(extender_k)):
                    if extender_k[n] != extender_k[n-1]:
                        unique_list.append(extender_k[n])            
                            
                            
                print(genename,"\n",unique_list)
                
                
                    



