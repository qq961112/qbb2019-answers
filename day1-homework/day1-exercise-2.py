#!/usr/bin/env python3 
#Counting the number of the perfect hits
f = open("/Users/cmdb/qbb2019-answers/day1-homework/day1-homework.SAM")
perfect_match = 0


for line in f:
    fields1 = line.split("\t")
    for field1 in fields1:
        if field1 == "NM:i:0":
            perfect_match += 1

                    
print(perfect_match)