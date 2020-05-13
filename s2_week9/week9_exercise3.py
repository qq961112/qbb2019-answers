#!/usr/bin/env python3

#Usage: ./week9_exercise3.py


from __future__ import division
import matplotlib
import numpy as np
import math
from pylab import *
from scipy.optimize import curve_fit
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


fig,((ax1,ax2), (ax3, ax4)) = plt.subplots(nrows=2,ncols=2)

hist1, bin_edges1 = np.histogram(waittime_f, bins = 20)
bin_width1 = bin_edges1[1] - bin_edges1[0]
bin_center1 = []
avg_count1 = []
sum1 = sum(hist1)

def func(x, a):
    return a * np.exp(-a * x)


for i in range(1,len(bin_edges1)):
    bin_center1.append(mean(bin_edges1[i]+bin_edges1[i-1]))
    avg_count1.append(hist1[i-1]/(sum1 * bin_width1))
    
pdf1 = []
for i in range(len(bin_center1)):
    #p(t)=k*e^{-k*t}
    pdf1.append(k1 * math.exp(- k1 * bin_center1[i]))

bin_center1 = np.array(bin_center1, dtype = float)
avg_count1 = np.array(avg_count1, dtype = float)

popt1, pcov1 = curve_fit(func, bin_center1, avg_count1)
reerr1 = abs(popt1[0] - k1) / k1


best_fit1 = func(bin_center1, popt1[0])
  
ax1.bar(bin_center1, best_fit1, width = 1.6, color = "magenta", label = "Best fit", alpha = 0.5)
ax1.bar(bin_center1, pdf1, width = 1.6 ,color = "darkred", label = "Calculated PDF", alpha = 0.5)
ax1.legend(loc="upper right")
ax1.text(max(bin_center1)/4, max(pdf1)/2, "Relative error = %f" %reerr1)
ax1.set_xlabel("Waiting time / s")
ax1.set_ylabel("Probability density")
ax1.set_title("Unfolded -> Folded, tf = 1000s")


###  Folded to unfolded in 1000s stimulation

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
    pdf2.append(k2 * math.exp(- k2 * bin_center2[i]))

bin_center2 = np.array(bin_center2, dtype = float)
avg_count2 = np.array(avg_count2, dtype = float)

popt2, pcov2 = curve_fit(func, bin_center2, avg_count2)
reerr2 = abs(popt2[0] - k2) / k2

best_fit2 = func(bin_center2, popt2[0])
  
ax2.bar(bin_center2, best_fit2, width = 1.6 * bin_center2[-1]/ bin_center1[-1], color = "purple", label = "Best fit", alpha = 0.5)
ax2.bar(bin_center2, pdf2, width = 1.6 * bin_center2[-1]/ bin_center1[-1] ,color = "darkblue", label = "Calculated PDF", alpha = 0.5)
ax2.legend(loc="upper right")
ax2.text(max(bin_center2)/4, max(pdf2)/2, "Relative error = %f" %reerr2)
ax2.set_xlabel("Waiting time / s")
ax2.set_ylabel("Probability density")
ax2.set_title("Folded -> Unfolded, tf = 1000s")


scale_f = bin_center1[-1]



### Stimulation time = 10000s

tf = 10000.0

waittime_f = [] 
waittime_uf = [] 


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

bin_center1 = np.array(bin_center1, dtype = float)
avg_count1 = np.array(avg_count1, dtype = float)

popt1, pcov1 = curve_fit(func, bin_center1, avg_count1)
reerr1 = abs(popt1[0] - k1) / k1


best_fit1 = func(bin_center1, popt1[0])
  
ax3.bar(bin_center1, best_fit1, width = 1.6 * bin_center1[-1]/ scale_f, color = "magenta", label = "Best fit", alpha = 0.5)
ax3.bar(bin_center1, pdf1, width = 1.6 * bin_center1[-1]/ scale_f ,color = "darkred", label = "Calculated PDF", alpha = 0.5)
ax3.legend(loc="upper right")
ax3.text(max(bin_center1)/4, max(pdf1)/2, "Relative error = %f" %reerr1)
ax3.set_xlabel("Waiting time / s")
ax3.set_ylabel("Probability density")
ax3.set_title("Unfolded -> Folded, tf = 10000s")


### Folded to unfolded in 10000s

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
    pdf2.append(k2 * math.exp(- k2 * bin_center2[i]))

bin_center2 = np.array(bin_center2, dtype = float)
avg_count2 = np.array(avg_count2, dtype = float)

popt2, pcov2 = curve_fit(func, bin_center2, avg_count2)
reerr2 = abs(popt2[0] - k2) / k2

best_fit2 = func(bin_center2, popt2[0])
  
ax4.bar(bin_center2, best_fit2, width = 1.6 * bin_center2[-1]/ scale_f, color = "purple", label = "Best fit", alpha = 0.5)
ax4.bar(bin_center2, pdf2, width = 1.6 * bin_center2[-1]/ scale_f ,color = "darkblue", label = "Calculated PDF", alpha = 0.5)
ax4.legend(loc="upper right")
ax4.text(max(bin_center2)/4, max(pdf2)/2, "Relative error = %f" %reerr2)
ax4.set_xlabel("Waiting time / s")
ax4.set_ylabel("Probability density")
ax4.set_title("Folded -> Unfolded, tf = 10000s")



fig.tight_layout()
fig.savefig("Fitting_rate_constant.png")
plt.close(fig)
