#!/usr/bin/env python3

import sys
new_fly = []

for i, line in enumerate(sys.stdin):
    if "DROME" in line:
        new_fly.append(line)

flyID = []
uniID = []
counter = 0
for line1 in new_fly:
    sp = line1.rstrip("\n").split()
    for i in range(len(sp)):
        if "DROME" in sp[i]:
            uniID.append(sp[i+1])
            if len(sp[i+1:]) < 2:
                flyID.append("N/A")
            else:
                flyID.append(sp[i+2])
            break
        i += 1
        counter += 1

for i in range(counter):
    print(uniID[i], "\t",flyID[i])



            
        
    
        

