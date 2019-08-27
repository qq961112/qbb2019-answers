#!/usr/bin/env python3 


f = open("/Users/cmdb/qbb2019-answers/day1-homework/day1-homework.SAM")


#Counting the number of the alignments
counter = 0
for line in f:
    fields = line.split("\t")
    if fields[5] == "*":
        continue
    else:
        counter += 1

print(counter)