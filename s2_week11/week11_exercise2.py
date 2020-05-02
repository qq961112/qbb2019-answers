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
# dS = np.zeros(np.shape(S))
# dI = np.zeros(np.shape(I))
#
# # Fill velocities into grid.
# for m in range(S.shape[0]):
#     for n in range(I.shape[0]):
#         dS[m,n] = -beta * S[m][n] * I[m][n]
#         dI[m,n] = beta * S[m][n]* I[m][n] - gamma * I[m][n]
#

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

#On day12, I12 = 0.0035470475596105643, R12 = 0.0027392665954311447

i12 = 0.0035470475596105643
r12 = 0.0027392665954311447
d12 = 0.00023123679052340835
y12 = [0.42*S0, i12, r12, d12]

sol2 = solve_ivp(SIR, [0,38], y12, max_step = 1)

t_lst2 = sol2.t
s_lst2, i_lst2, r_lst2, d_lst2 = sol2.y

for i in range(len(t_lst2)):
    t_lst2[i] += max(t_lst1)


t_lst2_new = list(t_lst1) + list(t_lst2[1:])
i_lst2_new = list(i_lst1) + list(i_lst2[1:])
r_lst2_new = list(r_lst1) + list(r_lst2[1:])
d_lst2_new = list(d_lst1) + list(d_lst2[1:])

# print(t_lst2_new)


sol3 = solve_ivp(SIR, [0,88], y12, max_step = 1)

t_lst3 = sol3.t
s_lst3, i_lst3, r_lst3, d_lst3 = sol3.y

for i in range(len(t_lst3)):
    t_lst3[i] += max(t_lst1)

t_lst3_new = list(t_lst1) + list(t_lst3[1:])
i_lst3_new = list(i_lst1) + list(i_lst3[1:])
r_lst3_new = list(r_lst1) + list(r_lst3[1:])
d_lst3_new = list(d_lst1) + list(d_lst3[1:])

i_lst4_new = []
for i in range(len(t_lst3_new)):
    i_lst4_new.append(i_lst3_new[i] + r_lst3_new[i] + d_lst3_new[i])
    
    
sol5 = solve_ivp(SIR, [0,100], y0, max_step = 1)

t_lst5 = sol5.t
s_lst5, i_lst5, r_lst5, d_lst5 = sol5.y

i_lst5_new = []
for i in range(len(t_lst5)):
    i_lst5_new.append(i_lst5[i] + r_lst5[i] + d_lst5[i])


# NOTE:
# sol.t = time vector
# sol.y = matrix of output. Rows are S, I, R, D; Columns are time

# Set up the matplotlib figure



fig, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(nrows=2,ncols=3)


ax1.plot(t_lst1, i_lst1 , color = "red", label = "Infected")
ax1.plot(t_lst1, r_lst1 , color = "blue", label = "Recovery")
ax1.plot(t_lst1, d_lst1 , color = "brown", label = "Death")
ax1.set_ylabel('Proportion/%', fontsize = 8)
ax1.set_title("12 Days without Intervention", fontsize = 8)



ax2.plot(t_lst2_new, i_lst2_new, color = "red", label = "Infected")
ax2.plot(t_lst2_new, r_lst2_new, color = "blue", label = "Recovery")
ax2.plot(t_lst2_new, d_lst2_new, color = "brown", label = "Death")
ax2.set_xlabel('Time/day', fontsize = 8)
ax2.set_ylabel('Proportion/%', fontsize = 8)
ax2.set_title("50 Days with Intervention from Day 12", fontsize = 8)



ax3.plot(t_lst3_new, i_lst3_new, color = "red", label = "Infected")
ax3.plot(t_lst3_new, r_lst3_new, color = "blue", label = "Recovery")
ax3.plot(t_lst3_new, d_lst3_new, color = "brown", label = "Death")
ax3.set_ylabel('Proportion/%', fontsize = 8)
ax3.set_title("100 Days with Intervention from Day 12", fontsize = 8)

ax4.plot(t_lst3_new, i_lst4_new, color = "red", label = "Infected")
ax4.plot(t_lst3_new, d_lst3_new, color = "brown", label = "Death")
ax4.set_xlabel('Time/day', fontsize = 8)
ax4.set_ylabel('Proportion/%', fontsize = 8)
ax4.set_title("Accumulated Infection or Death with Intervention from Day 12",fontsize = 8)

ax6.plot(t_lst3_new, i_lst4_new, color = "purple", label = "No Intervention")
ax6.plot(t_lst5, i_lst5_new, color = "red", label = "Intervention")
ax6.legend(loc="center right")
ax6.set_xlabel('Time/day', fontsize = 8)
ax6.set_ylabel('Proportion/%', fontsize = 8)
ax6.set_title("Intervention vs No Intervention, Infection% drops > 50%", fontsize = 8)



handles, labels = ax1.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper right')
# fig.tight_layout()
plt.xlabel('xlabel', fontsize=4)
plt.show()

