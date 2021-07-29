# -*- coding: utf-8 -*-
# un ébauche de shroedinger_solveB.py  (B - revisions 1/01/2018)
# mIv 04/02/2018

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import fsolve # <---


#==========================================================================
def schroedinger_solve(str_E, U, xmax, auto = False):
    """ Solves Schroedinger equation in potential U(x)
for given energy E:  d^2p/dx^2 = 2*(U(x) - E)*p(x),
and plot the result.
Input: E in the text format (string) and function name of U(x)
    AND (new) auto to start auto adjustement
Output: arrays of x,
    the probability amplitude distribution p(x) (normalized),
    and dp/dx (normalized as p(x))
    (the latter to be used for operators creation and annihilation)
    AND (new) new value of energy in text format E_str (if auto)
"""
    # E = float(str_E)
    E = eval(str_E) # lets 'pitonic' expressions for E
    
    #dx = 0.01 # may terminate not at the end +xmax 
    # x = np.arange(-xmax, xmax+dx, dx)
    N = 1000 # number of intervals
    x = np.linspace(-xmax, xmax, N+1)
    dx = 2*xmax/N
    
    
    
    def sch_ode(pdp,x,E):
        """ Form of the Schroedinger equation for ODE solver """
        #
        p, dpdp = pdp
        dp2dx2=2*(U(x)-E)*p
        #
        
        return dpdp,dp2dx2
    def p_end(E):
        """ Function for AUTO solving using fsolve() """
        #
        
        sol=odeint(sch_ode,pdp0,x,args=(E,))  
        p_at_end=sol[-1,0]#4solution de l'équation de Schroedinger forme réduite
        
        
        return p_at_end
    
    pdp0 = [0, 0.01] # left edge conditions
   
    if auto:
        E, = fsolve(p_end, E)
        # print("Enew =", E)
        E_str = "{:.7f}".format(E) # New energy found 
    else: E_str = str_E            # just keeps the entered value
    
    pdp = odeint(sch_ode, pdp0, x, args=(E,)) # final ODE
    p = pdp[:,0]    # distribution of the probability amplitude p(x)
    dpdx = pdp[:,1] # dp/dx - to be used for operators creation and annihilation
    # p_at_end2 = pdp[-1,0]
    # print("Outside p at end =", p_at_end2)

    # normalization of p(x) and dp/dx
        #
    Proba=np.dot(p,p)*dx
    p=p/np.sqrt(Proba)
    dpdx=dpdx/np.sqrt(Proba)
    
    # plot test figure p(x) to make a choice
    plt.figure('test')
    plt.plot(x,p)
    plt.xlabel('')
    plt.ylabel('')
    plt.title(' ')
    plt.show()
    
        #
    
    return p, dpdx, x, dx, E_str


    
#==========================================================================
# UNCOMMENT the following when used separately
"""
def U(x):
    return 0.5*x**2

# An example how to use schroedinger_solve()
xmax = 4.0
E = "1.5"
p, dpdx, x, dx = schroedinger_solve(E, U, xmax)
print("normalized ? ", np.dot(p,p)*dx)
"""   
