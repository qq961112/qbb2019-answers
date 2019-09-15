#!/usr/bin/env python3

"""
Parse and print contig length info from a FASTA file

./parse-config-fasta.py vresult1/contigs.fa
./parse-config-fasta.py sresults/K21/simplified_contigs.fasta

"""
import sys


class FASTAReader(object):
    def __init__(self, fh):
        self.fh = fh
        self.last_ident = None
        self.eof = False
    
    def next(self):
        if self.eof:
            return None, None
        elif self.last_ident == None:
            line = self.fh.readline()
            assert line.startswith(">"), "Not a FASTA file"
            ident = line[1:].rstrip("\n")
        else:
            ident = self.last_ident
            
        sequences = []
        while True:
            line = self.fh.readline()
            if line == "":
                self.eof = True
                break
            elif line.startswith(">"):
                self.last_ident = line[1:].rstrip("\n") #To store the next identifier
                break
            else:
                sequences.append(line.strip())
                
        sequence = "".join(sequences)
        return ident, sequence
        

reader = FASTAReader(open(sys.argv[1]))
contigs = []

while True:
    ident, sequence = reader.next()
    if ident is None:
        break
    #print (ident, sequence)
    contigs.append(sequence)

#print(contigs)
print("The number of contigs = ", len(contigs))

l = len(contigs)
total_length = 0

for i in range(l):
    total_length += len(contigs[i])

average_length = total_length/l    

def Sorting(lst):
    lst.sort(key=len, reverse = True)
    return lst

contigs_sorted = Sorting(contigs)
#print(contigs_sorted)
print("max length = ",len(contigs_sorted[0]))
print("min length = ",len(contigs_sorted[-1]))
print("average length = ", average_length)

acc = 0
for i in range(l):
    acc += len(contigs_sorted[i])
    if acc >= total_length/2:
        print("N50 = ",len(contigs_sorted[i]))
        break
