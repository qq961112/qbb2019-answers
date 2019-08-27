#!/usr/bin/env python3 


f = open("/Users/cmdb/qbb2019-answers/day1-homework/day1-homework.SAM")

one_hit = 0

for line in f:
    fields1 = line.rstrip("\n").split("\t")
    for field1 in fields1:
        if field1 == "NH:i:1":
            one_hit += 1

#Counting the number of alignments hit once
print(one_hit)