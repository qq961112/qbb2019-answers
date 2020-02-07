#!/usr/bin/env python3

"""
Usage: ./wright_fisher.py
"""

import numpy as np
import matplotlib.pyplot as plt
import math



def stimulation(n, p, trials):
    pop_size = n
    for i in range(trials):
        freq = p
        gen = 0
        while True:
            out = np.random.binomial(2 * pop_size, freq)
            freq = out/( 2 * pop_size ) 
            gen += 1
            if (freq == 0.0) or (freq == 1.0):
                break
    return(gen)

    # print(counter)

    # fig, ax = plt.subplots()
#     hist = ax.hist(counter)
#     fig.savefig("hist.png")
#     plt.close(fig)
    
sizes = [100, 1000, 10000, 100000, 1000000, 10000000]
fix_gens = []
log_sizes = []


for begin_size in sizes:
    fix_gen = stimulation(begin_size, 0.5, 1)
    fix_gens.append(math.log10(fix_gen))
    log_sizes.append(math.log10(begin_size))
    print(begin_size, "finished!")

# print(fix_gens)

fig, ax = plt.subplots()
ax.plot(log_sizes, fix_gens ,color = "red")
ax.set_title("Correlation of pop sizes and fixation times")
ax.set_xlabel("log. # of population sizes")
ax.set_ylabel("log. # of generations")
fig.savefig("different_pop_sizes.png")
plt.close(fig)


    
    
    