#!/usr/bin/env python3

#Usage: ./week9_exercise2.py


from __future__ import division
import matplotlib
import numpy as np
import math
from pylab import *
matplotlib.rcParams.update({"axes.formatter.limits": (-3,3)})
plotStyles={"markersize":10,"markeredgewidth":2.0,"linewidth":2.0}
stepStyles={"markersize":12,"markeredgewidth":3.0,"linewidth":3.0,"where":"post"}

import numpy.random as rnd

k1=0.15
k2=0.07
ts=[0.0]   # a list of the times when a state change has occurred
states=[0] # state 0 is unfolded, state 1 is folded
tf=1000.0   # the final time of the simulation

waittime_f = [] # a list of the wait times to fold
waittime_uf = [] # a list of the wait times to unfold


while (ts[-1]<tf):
    
    # If we are in the unfolded state, figure out when the molecule transitions to the folded state.
    if states[-1] == 0:
        last = ts[-1]
        ts.append(ts[-1]+rnd.exponential(1/k1))
        waittime_f.append(ts[-1] - last)
        states.append(1)
        
    # If we are in the folded state, figure out when the molecule transitions to the unfolded state.
    else:
        last = ts[-1]
        ts.append(ts[-1]+rnd.exponential(1/k2))
        waittime_uf.append(ts[-1]- last)
        states.append(0)


# print(waittime_f)
# print(waittime_uf)


fig,(ax1,ax2) = plt.subplots(nrows=1,ncols=2)

hist1, bin_edges1 = np.histogram(waittime_f, bins = 20)
bin_width1 = bin_edges1[1] - bin_edges1[0]
bin_center1 = []
avg_count1 = []
sum1 = sum(hist1)


for i in range(1,len(bin_edges1)):
    bin_center1.append(mean(bin_edges1[i]+bin_edges1[i-1]))
    avg_count1.append(hist1[i-1]/(sum1 * bin_width1))


pdf1 = []
for i in range(len(bin_center1)):
    #p(t)=k*e^{-k*t}
    pdf1.append(k1 * math.exp(- k1 * bin_center1[i]))

    
ax1.bar(bin_center1, avg_count1, width = 1.6, color = "red")
ax1.plot(bin_center1, pdf1, color = "darkred", linewidth = 2 )
ax1.set_xlabel("Waiting time / s")
ax1.set_ylabel("Probability density")
ax1.set_title("Unfolded -> Folded")




hist2, bin_edges2 = np.histogram(waittime_uf, bins = 20)
bin_width2 = bin_edges2[1] - bin_edges2[0]
bin_center2 = []
avg_count2 = []
sum2 = sum(hist2)


for i in range(1,len(bin_edges2)):
    bin_center2.append(mean(bin_edges2[i]+bin_edges2[i-1]))
    avg_count2.append(hist2[i-1]/(sum2 * bin_width2))


pdf2 = []
for i in range(len(bin_center2)):
    #p(t)=k*e^{-k*t}
    pdf2.append(k1 * math.exp(- k2 * bin_center2[i]))

    
ax2.bar(bin_center2, avg_count2, width = 1.6 * bin_center2[-1]/ bin_center1[-1], color = "blue")
ax2.plot(bin_center2, pdf2, color = "darkblue", linewidth = 2)
ax2.set_xlabel("Waiting time / s")
ax2.set_ylabel("Probability density")
ax2.set_title("Folded -> Unfolded")


# ax1.set_xlim([0,max(bin_center2)])
# ax2.set_xlim([0,max(bin_center2)])


fig.tight_layout()
fig.savefig("Waiting_time_PDF.png")
plt.close(fig)
