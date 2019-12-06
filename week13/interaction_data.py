#!/usr/bin/env python2

""
#Usage: ./interaction_data.py chr10_rna_binned.bed chr10_activity_binned.bed
""

import hifive
import numpy
import sys

rna_data = open(sys.argv[1])
activity_data = open(sys.argv[2])
rna_expression = {}
activity_value = {}
rna_index = []
activity_index = []


for i, line in enumerate(rna_data):
    if i == 0:
        continue
    col = line.rstrip("\n").split("\t")
    if int(col[1]) >= 5000000 and int(col[2])<=40000000:
        index = (int(col[1]) - 5000000) / 5000
        rna_index.append(index)
        rna_expression[index] = col[4]
        # print(index)
# print(rna_index)
            
for i, line in enumerate(activity_data):
    if i == 0:
        continue
    col = line.rstrip("\n").split("\t")
    if int(col[1]) >= 5000000 and int(col[2])<=40000000:
        index = (int(col[1]) - 5000000) / 5000
        activity_index.append(index)
        activity_value[index] = col[4]
        # print(index)
# print(rna_index)
            

hic = hifive.HiC('project_chr10', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)

interaction_activity = {}

for index in rna_index:
    int_act = 0
    for index2 in activity_index:
        int_act += float(activity_value[index2]) * data[index][index2]
    interaction_activity[index] = int_act 
    
# print interaction_activity

# print "Indices", "Prediction_Value"
# for index in rna_index:
#     print index, interaction_activity[index]


rna_expression_list = []
interaction_activity_list = []

for index in rna_index:
    rna_expression_list.append(float(rna_expression[index]))
    interaction_activity_list.append(interaction_activity[index])

rna_array = numpy.array(rna_expression_list)
interaction_activity_array = numpy.array(interaction_activity_list)

        
R_value = numpy.corrcoef(rna_array, interaction_activity_array)[0, 1]
print "R coefficient =" , R_value