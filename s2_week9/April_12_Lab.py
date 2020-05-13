# April 12 Lab
#
# Submit your answers to Blackboard as either python scripts and associated figures or as a single working iPython notebook file.
#
# In this lab we will be running kinetic simulations of an individual single molecule undergoing a folding and unfolding reaction. We will save the time series data and analyze them to learn about the kintic rates.
# We will model a single molecule folding and unfolding using two first order reactions:
# U -> F with a rate constant of K1
# F -> U with a rate constant of K2
#
# Below is a Python script that simulates the kinetics of a single protein folding and unfolding.

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
tf=100.0   # the final time of the simulation
while (ts[-1]<tf):
    
    # If we are in the unfolded state, figure out when the molecule transitions to the folded state.
    if states[-1] == 0:
        ts.append(ts[-1]+rnd.exponential(1/k1))
        states.append(1)
        
    # If we are in the folded state, figure out when the molecule transitions to the unfolded state.
    else:
        ts.append(ts[-1]+rnd.exponential(1/k2))
        states.append(0)

matplotlib.rcParams.update({'font.size': 15, "figure.figsize": (15,5)})
step(ts,states, **stepStyles)
xlabel('t'); ylim([-0.1,1.1]); ylabel('State');

# Read through and try to understand the code above. Save the script to a file and make sure you can run it, you may need to adjust the plotting code for your preferred plotting method.
#
# Problem 1.
# Run a folding simulation for 1000 seconds. Create a list of waiting times (the time between transitions) in both the folded and unfolded state. Use the np.histogram function to calculate a histogram of the waiting times for both states, using 20 bins. Plot the two histograms as bar plots. Hint: the np.histogram function returns the bin edges, you will want to plot the bars located at the bin centers. Hint 2: for n bins there will be n+1 edges and n centers.
#
# Problem 2.
# The histogram function returns the number of counts in each bin. To compare with our kinetics equations, we need to convert the counts into a probability density function (PDF). To do so, divide the histogram counts by the sum of all the counts and also by the width of the bin. The bins are all the same size by default, so you can divide each count by the width of the first bin. Plot the calculated PDFs for the folding and unfolding transition times as a bar plot. On top of the bar plots, plot the PDF for an exponential distribution: p(t)=k*e^{-k*t}, where k is K1 or K2 as appropriate.
# Problem 3.
# Write a python script to fit your calculated PDFs to exponential distributions to estimate K1 and K2. Plot the calculated PDFs as bar plots overlaid with the best fit estimates. What is the relative error in your estimated K1 and K2 vs the actual K1 and K2? Change the time of the simulation to 10000 seconds and run the analysis again. Now what are the estimated errors in K1 and K2?
