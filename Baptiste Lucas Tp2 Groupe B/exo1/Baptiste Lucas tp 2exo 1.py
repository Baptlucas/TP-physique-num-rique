# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 20:32:21 2021

@author: lucas
"""
"""
1.1)
"""
import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
axis_font = {'fontname':'Arial','size':'15','color':'black'}
fname = 'loi malus.txt'
R = np.loadtxt(fname, dtype=float, usecols=(1))#R est la résistance
phi = np.loadtxt(fname, dtype=float, usecols=(0))#A est l'angle

I=1/R**1.6

plt.figure(figsize=(9,6), dpi=320)
plt.scatter(phi,I,facecolors='white',edgecolors='red' ,label='intensité')
plt.xlabel("angle d'inclinaison du polariseur",**axis_font)
plt.ylabel("valeur de l'intensité lumineuse",**axis_font)
plt.legend()

"""
1.2)
"""
def malus(phi, amplitude, phase, shift):
    return shift+amplitude*np.cos((phase+phi)*(np.pi)/180)**2
    
pfit,pcov = curve_fit(malus, phi, I )
phi_fit=np.linspace(min(phi),max(phi),201 )
I_fit = malus(phi_fit,*pfit)


plt.plot(phi_fit,I_fit, label='courbe arrangé')
plt.ylabel("valeur ajustée de l'intensité ",**axis_font)
plt.xlabel("angle d'inclinaison du polariseur",**axis_font)
plt.legend()
plt.show()

