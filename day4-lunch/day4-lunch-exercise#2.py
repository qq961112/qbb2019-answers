#!/usr/bin/env python3


import sys
import matplotlib.pyplot as plt
import numpy as np 
import scipy.stats as stats 
import pandas as pd
import os

name1 = sys.argv[1].split(os.sep)[-1]
ctab1 = pd.read_csv(sys.argv[1], sep="\t",index_col="t_name")
name2 = sys.argv[2].split(os.sep)[-1]
ctab2 = pd.read_csv(sys.argv[2], sep="\t",index_col="t_name")

 
# fpkm = {name1 : ctab1.loc[:,"FPKM"],
#         name2 : ctab2.loc[:,"FPKM"]}
        
# df = pd.DataFrame(fpkm)
#
# print(df)
# print(type(df))

fpkms1 = []
#exons1 = []
#lengths1= []
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) >= 0: 
        fpkms1.append(float(fields[11]))
    # exons1.append(int(fields[6]))
    # lengths1.append(int(fields[7]))

# print(fpkms1)

fpkms2 = []
# exons2 = []
# lengths2= []
for i, line in enumerate(open(sys.argv[2])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    if float(fields[11]) >= 0: 
        fpkms2.append(float(fields[11]))
    # exons2.append(int(fields[6]))
    # lengths2.append(int(fields[7]))
        
# print(fpkms2)
fpkms1 = np.array(fpkms1)
fpkms2 = np.array(fpkms2)
data1 = np.log2(fpkms1 + 1)
data2 = np.log2(fpkms2 + 1)

# print(len(data1))
# print(len(data2))

fit = np.polyfit(data1, data2,1)
x = np.linspace(0, 12, 100)
z = np.poly1d(fit)

print("type of polyfit =", type(z))
print("polyfit value = ", z)






fig, ax = plt.subplots()
ax.plot(x, z(x), '--', color = "green")
# fig.savefig("test.png")
# plt.close(fig)



ax.set_title("FPKMs comparison")
ax.set_xlabel("FPKM from SRR072893")
ax.set_ylabel("FPKM from SRR072903")
ax.scatter( x = data1, y = data2, color = "purple", alpha = 0.3)
# #ax.plot(x,fit[1],color = "blue")
fig.savefig("two_FPKM_plots_polyfit.png")
plt.close(fig)





