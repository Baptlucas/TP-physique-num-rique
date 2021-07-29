# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 11:19:33 2021

@author: lucas
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


k0=30*2*np.pi #vecteur d'onde central
n=4# valeur variant de 2 à 8 dans le sujet, pour faire varier la largeur
delta_k=n*2*np.pi#largeur du paquet en espace k
dx=0.001
x=np.arange(-0.5,0.5+dx,dx)#définition de la variable x
delta_x= 2/delta_k

v_phase = 0.6 #vitesse de phase
v_group = 0.4 #vitesse de phase
dispersion = 0.001 #dispersion

# Questions 1-3) 
def omegaK(k):#fréquence circulaire en fonction du vecteur d'onde k
    return k0*v_phase + v_group*(k-k0) + dispersion*0.5*(k-k0)**2

def u(x, t):    # Définition d'une fonction "paquet gaussien d'ondes harmoniques"
    paquet=(((2*np.sqrt(np.pi))/delta_k)*sum([np.exp(-((2*np.pi*n-k0)/(delta_k))**2)
                                              *np.cos(2*np.pi*n*x-omegaK(2*np.pi*n)*t) for n in range(0,50)]))
    return  paquet

# Question 2) Ajout d'une enveloppe au paquet d'ondes

def U(x):#enveloppe positive
    Enveloppe=np.exp(-(x/delta_x)**2)
    return Enveloppe

def U1(x):#enveloppe négative
    Enveloppe1=-np.exp(-(x/delta_x)**2)
    return Enveloppe1

fig = plt.figure('1',figsize=(6,3), dpi=100)


line, = plt.plot(x, u(x, 0), '-b', lw=1) # paquet d'ondes
l_Up, = plt.plot(x, U(x), '--r') # envelop +
l_Dn, = plt.plot(x, U1(x), '--r') # envelop -


plt.xlabel('x')
plt.ylabel('u')
plt.title("Paquet d'ondes, delta k / 2pi = {0}".format(n))
plt.show()


d_time = 0.01


#Question 4)
def U3(x,t):#enveloppe qui évolue avec le temps et en fonction de la dispersion
        tau_disp=2/((dispersion)*delta_k**2)
        A=1/np.sqrt(1+(t/tau_disp)**2)
        delta_xt=2/(A*delta_k)
        p=-((((x-v_group*t)+0.5)%(2*0.5)-0.5)/delta_xt)**2
        U=np.sqrt(A)*np.exp(p)
        return U
    

def animate(num):#animation du paquet d'onde

    t = d_time*num
    ut = u(x, t)
    line.set_data(x, ut)
    envt =U3(x,t)
    l_Up.set_data(x, +envt)
    l_Dn.set_data(x, -envt)
    return True
        # animation1.py in Visualisation Cookbook
        # walker.py in Kinder(Princeton)2015
        
DoAnimation = True
if DoAnimation: 
    num_frames = 252

else: num_frames = 1


animator = animation.FuncAnimation(fig, animate,
                                       frames=num_frames,
                                       interval=50,
                
                                       repeat=True, blit=False)
SaveAnimation = False

if SaveAnimation and DoAnimation:
#        animator.save('packet_motion.mp4',
#                      codec = 'mpeg4', fps = 20, bitrate = 4000)
        # codec must be given, can be 'mpeg4' or better 'h264'
        animator.save('packet_motion.gif', dpi=96, writer='magick')
        # ImageMagick has to be installed

