#!/usr/bin/env python3

"""
Usage: ./wright_fisher.py
"""

import numpy as np
import matplotlib.pyplot as plt


def stimulation(n, p, trials, s):
    pop_size = n
    for i in range(trials):
        freq = p
        gen = 0
        while True:
            out = np.random.binomial(2 * pop_size, freq)
            freq = (out * (1 + s)) / (( 2 * pop_size) - out+ out * ( 1 + s ))
            gen += 1
            if (freq == 0.0) or (freq == 1.0):
                break

    return(gen)

selection = []
 
for i in range(200):
    selection.append(0.002 * i - 0.2)
    
    
fix_gen = []
for j in selection:
    k = stimulation(200, 0.5, 1, j)
    fix_gen.append(k)
#
fig, ax = plt.subplots()
ax.scatter(selection, fix_gen, s= 5)
ax.set_title("Selection coefficient vs Generations to fix ")
ax.set_xlabel("Selection coefficient")
ax.set_ylabel("# of generation for fixation")
fig.savefig("Selection_coefficient.png")
plt.close(fig)
    