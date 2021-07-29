# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 11:45:19 2021

@author: lucas
"""

import numpy as np
import matplotlib.pyplot as plt
eps = np.spacing(1) 
axis_font = {'fontname':'Arial','size':'14','color':'black'}#définition de la police d'écriture, de sa taille et de sa couleur
""" 

tracé de fonction sinC(x)

"""
x = np.linspace(-4,4,101)*np.pi 
x[x==0] = np.spacing(1) # addition d'une valeur pour comblé le trou en 0 de la fonction sinC
y = (np.sin(x))/x

plt.figure(figsize=(8,6), dpi=100)#définition de la taille et de la résolution du graphique
plt.plot(x, y)
plt.title("fonction sinc",**axis_font)
plt.ylabel("Amplitude",**axis_font)
plt.xlabel("X",**axis_font)
plt.show()
"""
tracé de la fonction tan(x)
"""
x = np.arange(-1.5,1.5,1/100)*np.pi
y = np.tan(x)

#y[np.abs(y)>=10]=np.NaN

plt.figure(figsize=(8,6), dpi=100)#définition de la taille et de la résolution du graphique
plt.title("fonction tan",**axis_font)
plt.xlabel("x",**axis_font)
plt.ylabel("Amplitude",**axis_font)
plt.plot(x,y,'b',label='tan(x)')
plt.show()