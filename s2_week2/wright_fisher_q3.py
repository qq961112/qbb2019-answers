#!/usr/bin/env python3

"""
Usage: ./wright_fisher.py
"""

import numpy as np
import matplotlib.pyplot as plt
import math



def stimulation(n, p, trials):
    pop_size = n
    gen_list =[]
    for i in range(trials):
        freq = p
        gen = 0
        while True:
            out = np.random.binomial(2 * pop_size, freq)
            freq = out/( 2 * pop_size ) 
            gen += 1
            if (freq == 0.0) or (freq == 1.0):
                break
        gen_list.append(gen)
    return(gen_list)
    


start_freq = []
for i in range(10):
    start_freq.append(0.1 * i)



freq_gen = []
gen_mean = []
gen_std = []


for freq in start_freq:
    gen = []
    fix_gen = stimulation(1000, freq, 100)
    for item in fix_gen:
        gen.append(item)
        freq_gen.append((freq, item))
    gen_mean.append(np.mean(gen))
    gen_std.append(np.std(gen))


        
for item in freq_gen:
    frequency = []
    fix_time = []

for j in range(len(freq_gen)):
    frequency.append(freq_gen[j][0])
    fix_time.append(freq_gen[j][1])


# print(start_freq)
# print(gen)
# print(gen_std)

fig, ax = plt.subplots()
ax.scatter(frequency, fix_time, color = "#5BC0DE", s = 5)
ax.bar(start_freq, gen_mean, yerr = gen_std, width = 0.05, alpha = 0.9 ,align='center', ecolor='black', capsize=10)
ax.set_xticks(start_freq)
ax.set_title("Different allele frequencies vs Generations to fix")
ax.set_xlabel("Starting allele frequencies")
ax.set_ylabel("# of generations for fixation")
plt.tight_layout()
fig.savefig("Different_allele_frequencies.png")
plt.close(fig)


    
    
    