#!/usr/bin/env python3

#Usage: ./week9_exercise1.py


from __future__ import division
import matplotlib
import numpy as np
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
# fig = plt.figure(figsize=(10, 6))


hist1, bin_edges1 = np.histogram(waittime_f, bins = 20)
# print(hist)
# print(bin_edges)
bin_center1 = []
for i in range(1,len(bin_edges1)):
    bin_center1.append(mean(bin_edges1[i-1]+bin_edges1[i]))

ax1.bar(bin_center1, hist1, width = 1.6, color = "red")
ax1.set_xlabel("Waiting time / s")
ax1.set_ylabel("Number of transitions")
ax1.set_title("Unfolded -> Folded")


hist2, bin_edges2 = np.histogram(waittime_uf, bins = 20)
# print(hist)
# print(bin_edges)
bin_center2 = []
for i in range(1,len(bin_edges2)):
    bin_center2.append(mean(bin_edges2[i-1]+bin_edges2[i]))

ax2.bar(bin_center2, hist2, width = 1.6 * bin_center2[-1]/ bin_center1[-1], color = "blue")
ax2.set_xlabel("Waiting time / s")
ax2.set_ylabel("Number of transitions")
ax2.set_title("Folded -> Unfolded")

fig.tight_layout()
fig.savefig("Waiting_times.png")
plt.close(fig)



