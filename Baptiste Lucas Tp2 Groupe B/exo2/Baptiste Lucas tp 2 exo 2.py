# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:15:26 2021

@author: lucas
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def equation_premier_ordre(y,t):
    """
    

    Parameters
    ----------
    y : TYPE
        DESCRIPTION.
    t : TYPE
        DESCRIPTION.

    Returns
    -------
    dydt : TYPE
        DESCRIPTION.

    """
    dydt = -y + t*y**2
    return dydt

plt.figure(figsize=(8,5), dpi=320)
y0 = 1
t = np.linspace(0,10,200)
sol1 =  odeint(equation_premier_ordre , y0, t)
plt.plot(t , sol1[:,0], 'bo', label= 'y(t)')
plt.plot(t , 1/(1+t), 'red', label= 'y(t) analytique')
plt.title('équation différentiel')
plt.xlabel('t')
plt.ylabel('y(t)')
plt.legend()
plt.show()

g=9.81
t = np.linspace(0,2,70)

def position(z,t):
    """
    

    Parameters
    ----------
    z : position en z.
    t : temps.

    Returns
    -------
    dvzdt : .

    """
    dvzdt=-g*t+10
    return dvzdt
z=0
sol3= odeint(position,z,t )
plt.figure(figsize=(9,6), dpi=320)
plt.subplot(1,2,1)
plt.plot(t , sol3[:,0], 'bo', label= 'z(t)')
plt.xlabel('t')
plt.title('position')
plt.legend()


def equation_balistique(vz,t):
    """
    

    Parameters
    ----------
    vz : TYPE
        DESCRIPTION.
    t : temps.

    Returns
    -------
    dvzdt : TYPE
        DESCRIPTION.

    """
    dvzdt = -g
    return dvzdt
vz0=10
z=0


sol2= odeint(equation_balistique,vz0,t )
plt.subplot(1,2,2)
plt.plot(t , sol2[:,0], 'bo', label= 'vz(t)')
plt.xlabel('t')
plt.title('équation balistique')
plt.legend()
plt.show()


valeur_C=[50,35,20]
for C in valeur_C:
    B = C*0.5/100
    Y = 1/10
   
    def epidemie(y,t):
        """
        

        Parameters
        ----------
        y : TYPE
            DESCRIPTION.
        t : temps.

        Returns
        -------
        dSdt : relatif aux personnes saines.
        dIdt : relatif aux personnes infectées.
        dRdt : relatif aux personnes rétablies.

        """
  
        S = y[0]
        I = y[1]
        R = y[2]
        dSdt = -B*S*I
        dIdt = B*S*I - Y*I
        dRdt = Y*I      
        return dSdt, dIdt , dRdt

    N = 70*pow(10,6)
    I_init = 1000/N
    S_init = 1-1000/N-0
    R_init = 0
    Y_init = [S_init, I_init, R_init]

    t = np.linspace(0, 180, 1000)
    sol4 = odeint(epidemie, Y_init, t )
    plt.figure(figsize=(9,6), dpi=320)    
    plt.plot(t, sol4[:,0],'blue', label = 'personnes saines') 
    plt.plot(t, sol4[:,1],'red', label = 'personnes infecté')
    plt.plot(t, sol4[:,2],'green', label = 'personnes rétablies') 
    plt.title('modèle épidémiologique')
    plt.legend()
    plt.show() 
    




    
    
    
    
    
    
    
    