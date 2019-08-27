#!/usr/bin/env python3 


f = open("/Users/cmdb/qbb2019-answers/day1-homework/day1-homework.SAM")

twoLcount = 0
for line in f:
    fields = line.split("\t")
    if fields[5] == "*":
        continue
    else:
        if fields[2] == "2L":
            if int(fields[3]) >= 10000 and int(fields[3]) <= 20000:
                twoLcount += 1

#Counting number of reads begin between 10000 to 20000 on chrom 2
print(twoLcount)
            