#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Andrew Gordus
May, 2020
Quantitative Biology and Biophysics (AS.020.674/250.644)	Spring 2020
Gordus Lab #2

"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


#---------------#
# Set Variables #
#---------------#

S0 = 1 # Actual NYC population: 8*np.power(10,6)
I0 = 30 / (8*np.power(10,6))

R0 = 2.2
gamma = 0.44
beta = R0*gamma/S0


#-------------------#
# Current NYC Stats #
#-------------------#

# Current NYC Stats
# Shelter in Place occurred t = 12 days
# Confirmed cases was ~17644 at this point

Conf = 167000 #52 days from t0
Dead = 13000 #52 days from t0
Rec = 40000 #52 days from t0


f = Dead/Conf


#-------------#
# PHASE PLANE #
#-------------#

# Null Clines

Sn = gamma/beta
In = 0


Sspan = np.linspace(0,S0,10)
Ispan = np.linspace(0,S0,10)

# Grid of x & y values
S, I = np.meshgrid(Sspan, Ispan)

# Empty matrices to fill in with velocity data
dS = np.zeros(np.shape(S))
dI = np.zeros(np.shape(I))

# Fill velocities into grid.
for m in range(S.shape[0]):
    for n in range(I.shape[0]):
        dS[m,n] = -beta * S[m][n] * I[m][n]
        dI[m,n] = beta * S[m][n]* I[m][n] - gamma * I[m][n]
        

#----------------------#
# NUMERICAL SIMULATION #
#----------------------#


# ODE

y0 = [S0, I0, 0, 0]


def SIR(t,y):
    s_, i_, r_, d_ = y
    return [-beta*s_*i_, beta*s_*i_ - gamma*i_, (1-f)*gamma*i_, f*gamma*i_]
    


sol1 = solve_ivp(SIR, [0,13], y0, max_step = 1)

t_lst1 = sol1.t
s_lst1, i_lst1, r_lst1, d_lst1 = sol1.y

print(i_lst1[-1], r_lst1[-1], d_lst1[-1])


sol2 = solve_ivp(SIR, [0,51], y0, max_step = 1)

t_lst2 = sol2.t
s_lst2, i_lst2, r_lst2, d_lst2 = sol2.y


sol3 = solve_ivp(SIR, [0,101], y0, max_step = 1)

t_lst3 = sol3.t
s_lst3, i_lst3, r_lst3, d_lst3 = sol3.y


i_lst4 = []
for i in range(len(t_lst3)):
    i_lst4.append(i_lst3[i] + r_lst3[i] + d_lst3[i])
    

# NOTE:
# sol.t = time vector
# sol.y = matrix of output. Rows are S, I, R, D; Columns are time

# Set up the matplotlib figure


X = np.arange(-10, 10, 1)
Y = np.arange(-10, 10, 1)
U, V = np.meshgrid(X, Y)


fig, ax = plt.subplots(3,2)

ax[0,0] = plt.subplot2grid((8,8),(0,0), rowspan=3, colspan=3)
q = ax[0,0].quiver(S , I , dS, dI)
ax[0,0].quiverkey(q, X=0.3, Y=1.1, U=1,label='Quiver key, length = 1', labelpos='E')
ax[0,0].plot([Sn, Sn], [0,S0])
ax[0,0].set_xlabel('Susceptible/%')
ax[0,0].set_ylabel('Infected/%')
ax[0,0].set_ylim(-0.2,1.2)
ax[0,0].set_xlim(-0.2,1.2)
# ax[0,0].set_title("Quiver key, length = 1")

ax[0,1] = plt.subplot2grid((8,8),(0,4), rowspan=2, colspan = 3)
ax[0,1].plot(t_lst1, s_lst1 , color = "darkgreen", label = "Susceptible")
ax[0,1].plot(t_lst1, i_lst1 , color = "red", label = "Infected")
ax[0,1].plot(t_lst1, r_lst1 , color = "blue", label = "Recovery")
ax[0,1].plot(t_lst1, d_lst1 , color = "brown", label = "Death")
ax[0,1].set_xlabel('Time/day')
ax[0,1].set_ylabel('Proportion/%')
ax[0,1].set_title("12 Days")

ax[1,1] = plt.subplot2grid((8,8),(3,4), rowspan=2, colspan = 3)
ax[1,1].plot(t_lst2, s_lst2 , color = "darkgreen", label = "Susceptible")
ax[1,1].plot(t_lst2, i_lst2 , color = "red", label = "Infected")
ax[1,1].plot(t_lst2, r_lst2 , color = "blue", label = "Recovery")
ax[1,1].plot(t_lst2, d_lst2 , color = "brown", label = "Death")
ax[1,1].set_xlabel('Time/day')
ax[1,1].set_ylabel('Proportion/%')
ax[1,1].set_title("50 Days")

ax[2,1] = plt.subplot2grid((8,8),(6,4), rowspan=2, colspan = 3)
ax[2,1].plot(t_lst3, s_lst3 , color = "darkgreen", label = "Susceptible")
ax[2,1].plot(t_lst3, i_lst3 , color = "red", label = "Infected")
ax[2,1].plot(t_lst3, r_lst3 , color = "blue", label = "Recovery")
ax[2,1].plot(t_lst3, d_lst3 , color = "brown", label = "Death")
ax[2,1].set_xlabel('Time/day')
ax[2,1].set_ylabel('Proportion/%')
ax[2,1].set_title("100 Days")

ax[1,0] = plt.subplot2grid((8,8),(5,0), rowspan=3, colspan = 3)
ax[1,0].plot(t_lst3, i_lst4 , color = "red", label = "Infected")
ax[1,0].plot(t_lst3, d_lst3 , color = "brown", label = "Death")
ax[1,0].set_xlabel('Time/day')
ax[1,0].set_ylabel('Proportion/%')
ax[1,0].set_title("Accumulated Infection or Death")


handles, labels = ax[0,1].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower right')
fig.tight_layout()

plt.show()

