# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 14:16:26 2021

@author: lucas
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation

x=np.linspace(-3,3,100)
y=np.linspace(-3,3,100)
fig = plt.figure(1)
plt.clf()
ax = axes3d.Axes3D(fig)
X, Y = np.meshgrid(x,y)
limit = 1.3
omega = 2*np.pi
dt = 0.01
time = np.arange(0, 1.0-dt/2, dt)

x1=0
x2=2
y1=-2
y2=3
Z1= np.cos(2*np.pi*(np.sqrt((X-x1)**2+(Y-y1)**2)))/np.sqrt((X-x1)**2+(Y-y1)**2)
Z2= np.cos(2*np.pi*(np.sqrt((X-x2)**2+(Y-y2)**2)))/np.sqrt((X-x2)**2+(Y-y2)**2)
    
#print(help(ax.plot_surfaces))
Z= Z1+Z2
wframe = ax.plot_surface(X,Y,Z,rstride=1, cstride=1,shade=False,linewidth=0,antialiased=0,cmap= 'ocean')
"""
def step(n):
    global wframe
    Zt = Z*np.exp(-1j*omega*time[n])
    wframe.remove()
    wframe = ax.plot_surface(X, Y, np.real(Zt), lw=0,
                         rstride=1, cstride=1,
                         vmin=-limit, vmax=limit,
                         shade = True,
                         cmap = "ocean")

animator = animation.FuncAnimation(fig, step,
                                   frames=len(time),
                                   interval=20,
                                   repeat = False)
"""