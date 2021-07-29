# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:31:09 2021

@author: lucas
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

def schroedinger_animation(nm,all_E,all_p,x,save):
    
    
    #dt=0.09
    n=nm[0]
    m=nm[1]
    En=float(all_E[n])
    Em=float(all_E[m])
    pn=all_p[n]
    pm=all_p[m]
    dt=2*np.pi/100*(En-Em)#mouvement interminable car dt défini sur un cercle
    
    def pnm(t):
        pnm=1/2*(pn*np.exp(1j*En*t)+pm*np.exp(1j*Em*t))*(pn*np.exp(-1j*En*t)+pm*np.exp(-1j*Em*t))
        return pnm.real
    fig=plt.figure('anim')
    plt.clf()
    line,=plt.plot(x,pnm(0))

    def setpt(n):
        t=n*dt
        line.set_data(x,pnm(t))
        
  
    ani=animation.FuncAnimation(fig,setpt,frames=100,interval=20)
    plt.show()
    plt.draw()
    return ani
    
    
#plot /n> et /m>   
    
