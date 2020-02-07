#!/usr/bin/env python3

"""
Usage: ./wright_fisher.py
"""

import numpy as np
import matplotlib.pyplot as plt


def stimulation(n, p, trials):
    pop_size = n
    counter = []
    for i in range(trials):
        freq = p
        gen = 0
        while True:
            out = np.random.binomial(2 * pop_size, freq)
            freq = out/( 2 * pop_size ) 
            gen += 1
            if (freq == 0.0) or (freq == 1.0):
                break

        counter.append(gen)

    # print(counter)

    fig, ax = plt.subplots()
    hist = ax.hist(counter)
    ax.set_title("Stimulation for 1000 trials")
    ax.set_xlabel("# of generations to get fixation")
    ax.set_ylabel("# of trials")                      
    fig.savefig("Histogram_of_1000_trials.png")       
    plt.close(fig)
    

stimulation(100, 0.5, 1000)