# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:16:38 2021

@author: lucas
"""

import numpy as np
import matplotlib.pyplot as plt
from random import uniform
import tkinter
from tkinter import messagebox
app=tkinter.Tk()
app.title('ondes')


plt.ion()

# %% model parameters

nx = 200
length = 1
g = 1.
tend = 0.5
courant_number = 0.9
# %% setup the grid and allocate the model's variables
dx = length/nx

# xc : cell centers
xc = np.linspace(dx*0.5, length-dx*0.5, nx)

# xe : cell edges
xe = np.linspace(0, length+dx, nx+1)

# extended domain: one extra cell on each side to deal with
# the boundary conditions
xc_extended = np.linspace(-dx*0.5, length+dx*0.5, nx+2)

# h is discretized at cell centers on the extended domain
h = np.zeros_like(xc_extended)

# u is discretized at cell edges
# they don't have the same length!
u = np.zeros_like(xe)


# %% define H(x)
def define_depth(x):
    """ define the depth
    should return a vector, same size as x"""
    # method 1
    # depth = x*0+1

    # method 2
    _depth = np.zeros_like(x)
    #_depth[:] = 4.
    sig=length/10
    #_depth[x <length/2] = 1.#discontinuité du milieu    
    #_depth[x>length/2] = 2.
    
    #_depth[abs(x - length/2) <sig] = 2.
    #_depth[abs(x - length/2) >sig] = 1.
    # define your own function
     
    _depth[:]=(x+1/2)+np.exp(x**2)
    
    
    return _depth


# depth is defined at cell edges, like u ...
# reason: the term depth*u in the dh/dt
depth = define_depth(xe)

# %% deduce the time step and the number of iterations
cmax = np.sqrt(g*np.max(depth))
dt = courant_number*dx/cmax
nt = int(round(tend/dt)+1)

print('                cmax = %g' % cmax)
print('                  dx = %g' % dx)
print('           time step = %g' % dt)
print('number of iterations = %i' % nt)


# %% array to store the time evolution
uo = np.zeros((nt, nx+1))
ho = np.zeros((nt, nx))
time = np.zeros((nt,))
energy = np.zeros((nt,))


def save_model(k, t, u, h):
    """ the model state variable in arrays
    for post analysis of the results"""
    uo[k, :] = u
    ho[k, :] = h[1:-1]  # exclude the ghostpoints
    time[k] = t
    energy[k] = 0.5*(np.sum(depth*u**2)
                     + np.sum(g*h[1:-1]**2))*dx


# %% initial conditions
def hprofile(x):
    """ define the initial profile for the height
    should return a vector, same size as x """  
    # define your own profile
    sigma_wave = 0.02    
    hini = np.exp(-(x-0.3)**2/(2*sigma_wave**2))      
   # hini=np.zeros(x.shape)    
   # hini[(x>0.2)&(x<0.3)]=1        
    return hini

Z=np.sqrt(depth/g)
m=hprofile(xe)/Z




t = 0.2
h[:] = hprofile(xc_extended)
u[:] = m #si u[:]=0 l'onde va dans les deux sens sinon avec u[:] =hprofile(xe)/Z  l'onde se propage seulemement vers la droite 
#mais il reste un résidue vers la gauche
save_model(0, t, u, h)


def grad(phi, dx):
    """ returns the gradient of phi at mid points
    if phi has n elements, grad will have n-1 elements """ 
    return (phi[1:]-phi[:-1])/dx
 

# % time loop
for k in range(1, nt):
    # update u & h
    # TODO: implémenter le schéma avant-arrière
    # et remplir les points fantomes pour h
    
    u += -g*(dt)*grad(h,dx)
    h[1:-1] += -grad(depth*u,dx)*dt
    h[0]=h[1]  
    h[-1]=h[-2]          
    t += dt

    save_model(k, t, u, h)

#question 4.2)

depthI=1
depthT=2

zt=np.sqrt(depthT/g)
zi=np.sqrt(depthI/g)
def coef_transmition(zt,zi):
    T=2*zt/(zi+zt)
    return T

def coef_réflexion(zt,zi):
    R=(zi-zt)/(zi+zt)
    return R
R=coef_réflexion(zt,zi)
T=coef_transmition(zt,zi)
print('La réflexion = {0}'.format(R))
print('La tranmition = {0}'.format(T))
print('somme R et T ={0}'.format(R+T))

hu=depth*uo
#flux=g*ho*0.5(hu[:,1:]+hu[:,:-1]) #faire la moyenne du flux a gauche et à droite
#flux d'énergie  ---> F(x,t)=gH(x)+u(x,t)+h(x,t)
    
    
t0=0.2
k=np.argmin(np.abs(time-t0))

# %% plot the space-time diagram

plt.close('all')
def figure1(*args):
    
    plt.figure(dpi=100)
    plt.pcolor(xc, time, ho, cmap='RdBu_r')
    plt.xlabel('X')
    plt.ylabel('time')
    plt.title("densité d'énergie , nombre Courant ={0}".format(courant_number))
    plt.colorbar(label="anomalie de hauter d'eau")

def figure2(*args):
    plt.figure(dpi=100)
    plt.pcolor(xe, time, uo, cmap='RdBu_r')
    plt.xlabel('X')
    plt.ylabel('time')
    plt.title("vitesse de l'onde")
    plt.colorbar(label="vitesse")

def figure_lignes(*args):
    plt.figure()
    for k in range (0,nt,5):
        plt.plot(xc,ho[k,:]*0.05+time[k],'k')
        
def figure3(*args):    
    plt.figure(dpi=100)
    plt.plot(xc,ho[k,:], label='h')
    plt.plot(xe,uo[k,:], label='u')
    plt.xlabel('x')
    plt.ylabel('')
    plt.title('t= {0}'.format(t0))
    plt.legend()

def energie_figure(*args):
    plt.figure(dpi=100)
    plt.plot(time,energy/energy[0], label='energie')
    plt.xlabel('x')
    plt.ylabel('')
    plt.title('t= {0}'.format(t0))
    plt.legend()

def figure4(*args):
    e=(uo**2)*depth[np.newaxis:]
    plt.figure(dpi=100)
    plt.pcolor(xe, time, e, cmap='RdBu_r')
    plt.xlabel('X')
    plt.ylabel('time')
    plt.title('u')
    plt.colorbar(label="anomalie de hauter d'eau")

def figure_flux(*args):
    plt.figure()
    #plt.pcolor(xe,time,flux,cmap='RdBu_r')
    plt.xlabel('x')
    plt.ylabel('temps')


#-----------------Tkinter--------------------------------
def quitter(*args):
    message=messagebox.askquestion('quitter','Voulez vous quitter ?',)
    if message == 'yes':
        app.destroy()
    else:
        pass
        #------------------frames---------------------------------- 
       
frame1=tkinter.LabelFrame(app,text='Figures')
frame1.pack(side='top',fill='x',ipady=10)

        #------------------Boutons---------------------------------- 

bouton_figure1=tkinter.Button(frame1,command=figure1,text='figure1').pack(side='left',ipadx=18,padx=12)
bouton_figure2=tkinter.Button(frame1,command=figure2,text='figure2').pack(side='left',ipadx=18,padx=12)
bouton_figure3=tkinter.Button(frame1,command=figure3,text='figure3').pack(side='left',ipadx=18,padx=12)
bouton_figure4=tkinter.Button(frame1,command=figure4,text='figure4').pack(side='left',ipadx=18,padx=12)
bouton_figure_lignes=tkinter.Button(frame1,command=figure_lignes,text='figure lignes').pack(side='left',ipadx=4,padx=12)
bouton_energie_figure=tkinter.Button(frame1,command=energie_figure,text='energie figure').pack(side='left',ipadx=0,padx=12)
bouton_figure_flux=tkinter.Button(frame1,command=figure_flux,text='figure flux').pack(side='left',ipadx=10,padx=12)
    
    
Bouton_quitter=tkinter.Button(app,command=quitter,text='quitter').pack(pady=10)
app.mainloop()

# figure propres + legende
# texte qui s'appuit de la figure et la décrit physiquement
# extraire de la physique et l'exprimer avec des mots en français
# pas de pages de calcule, plutot du blabla


