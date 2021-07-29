# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 11:14:49 2021

@author: lucas
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.optimize import curve_fit
import scipy.optimize 
from matplotlib import animation
import matplotlib as mpl


x0 = 1#  position initiale de la planète  en x
vx0 = 0# position initiale de la planète  en x sur le diagramme de vitesse 
y0 = 0#  position initiale de la planète  en y
vy0 = np.sqrt(1/4)#  position initiale de la planète  en y sur le diagramme de vitesse 
alpha = 0.0008

param_init = [x0,y0,vx0,vy0]# variable qui contient les valeurs initiale pour les fournire au module odeint de scipy.integrate

t = np.linspace(0,10,1500)#définition de l'intervalle de temps

def mvt_auround_sun(param_init,t):# fonction retournant les quatres équations différentielles du mouvement de la planète
    y=param_init[1]
    x=param_init[0]
    vx=param_init[2]
    vy=param_init[3]
    
    dxdt=param_init[2]
    dvxdt=-(x)/(x**2+y**2)**(3/2) 
    dydt=param_init[3]
    dvydt=-(y)/(x**2+y**2)**(3/2) 
    #changemement de trajectoire (question 8)
    #dxdt=vx
    #dvxdt=-(x)/(x**2+y**2)**(3/2) - alpha*x/((x**2+y**2)**(5/2))
    #dydt=vy
    #dvydt=-(y)/(x**2+y**2)**(3/2) - alpha*y/((x**2+y**2)**(5/2))
    
    return (dxdt,dydt,dvxdt,dvydt)


sol=odeint(mvt_auround_sun,param_init,t)#calcule des solutions des équations différentielles 

x = sol[:,0]
y = sol[:,1]
vx = sol[:,2]
vy = sol[:,3]


# subplot orbite / hodographe
fig,ax = plt.subplots(1,2, gridspec_kw = {'width_ratios':(3,2)}, num = 'Orbite',
                      clear = True)



ax[0].set_aspect('equal')#réglage des axes pour qu'ils soit de même taille 
ax[1].set_aspect('equal')#réglage des axes pour qu'ils soit de même taille 

# Affichage d'une grille
ax[0].grid()
ax[1].grid()

ax[0].set_xlabel('x')#labelde l'axe x de la figure 1 du subplot
ax[0].set_ylabel('y')#labelde l'axe y de la figure 1 du subplot
ax[0].set_title('Orbite pour x0={0} , vy0={1}'.format(x0 , vy0))#titre de la figure 1 du subplot

ax[1].set_xlabel('vx')#labelde l'axe x de la figure 2 du subplot
ax[1].set_ylabel('vy')#labelde l'axe y de la figure 2 du subplot
ax[1].set_title('Diagramme de vitesse (holographe)')#titre de la figure 2 du subplot


ax[0].plot(x,y,label='valeurs numériques')

ax[1].plot(vx,vy,label='valeurs numériques')



# Question 2 

def rphi(phi,p,eps):#équation coordonnées polaire
    return p/(1+eps*np.cos(phi))

r = np.sqrt(x**2+y**2)#norme du rayon 
phi = np.arccos(x/r)


pfit,pcov = curve_fit(rphi, phi, r)

p = pfit[0]#paramètre de l'ellipse
eps = pfit[1]#excentricité 

fig1,ax1 = plt.subplots(1,1, num = 'Comparaison', clear = True)
#ax1.plot(t,r-rphi(phi,pfit[0],pfit[1]),label='r-rphi')
#ax1.set_title("Ecart entre les points numériques et théoriques vy0={0}".format(vy0))
ax1.set_xlabel('temps')
ax1.set_ylabel('y')
plt.grid()


# Question 3

phiv=np.linspace(-np.pi,np.pi,30)

vr=vy0/(1+eps)

vrx=vr*(np.cos(phiv))
vry=vr*(np.sin(phiv))+eps*vr

ax[1].plot(vrx,vry,'or',label='valeurs théorique')



#Question 4

p = pfit[0]#paramètre de l'ellipse
eps = pfit[1]#excentricité 

grandaxe= p/(1-eps**2) + p/ (1-eps**2)#p/(1-eps**2) formule du demi grand axe

print("Longueur du grand axe=",grandaxe)

n=0

while y[n]>=0:# determination de la demi période pour y positif
    n+=1# on prend la valeur suivante de n tant que y[n] est positif
    demiT=t[n-1]#demi période ,(n-1) care on retire la dérnière valeur de n , car c'est la première  valeur négative  
T=2*demiT# période
    
print ("période de l'orbite", T)

constante = T**2/grandaxe**3

print ("constante pour les trajectoires elliptiques :", constante)

"""Longueur du grand axe= 1.1428560062583568
période de l'orbite 2.7084723148765844
constante pour les trajectoires elliptiques : 4.914442479365276"""



def dist(T):# determination de la valeur exacte de la période
    sol = odeint (mvt_auround_sun, param_init, [0,T])
    x = sol[:,0]
    y = sol [:,1]
    
    return ((x[0]-x[-1])**2 + (y[0]-y[-1])**2)
T_exact = scipy.optimize.fmin(dist,T)# fmin est un module de scipy.optimize qui minimise une fonction

print("valeur exacte de la période =",T_exact)#valeur exacte de la période
print("valeur exacte de la constante=",T_exact**2/grandaxe**3)#valeur exacte du grand axe




#Question 5

x=sol[:,0]
y=sol[:,1]

SF=-eps*grandaxe#distance entre le soleil et le foyer
SP=np.sqrt(x**2+y**2)#distance entre le soleil et la planète
PF=np.sqrt((x+grandaxe*eps)**2+y**2)#distance entre le foyer et la planète

grandaxe2=SP+PF

print(grandaxe2[0])
#ax1.plot(t,SP+PF-grandaxe,label='SP+PF-grandaxe' )


#Question 6

V=np.sqrt(vx**2+vy**2)
sinteta= (x*vy-y*vx)/(SP*np.sqrt(vx**2+vy**2))
sintetaf= ((x+grandaxe*eps)*vy-y*vx)/(PF*np.sqrt(vx**2+vy**2))

print(sinteta)
print (sintetaf)

#ax1.plot(t,sinteta-sintetaf,label='sinteta-sintetaf')

plt.show()

"""La différence d'angle est suffisament petite pour dire 
que l'angle incident est égal à l'angle reflété"""



#Question 7


Lexp=x*vy-y*vx
Lth=x0*vy0

ax1.plot(t,Lexp-Lth,label='Lexp-Lth') #différence très faible entre les 2

"""on vérifie ainsi que le moment cinétique est conservé"""


"""quand le 1/r**2 n'est pas respecté (par exemple proche du soleil), l'ellipse n'est
plus fermée, on observe ainsi une rotation"""
    

#Question 9

#Animation 


eps=np.spacing(1)

# returns nice mathematical font used before Matplotlib 2.0

mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'

planete,= ax[0].plot(1,0,'og',)
#text_planete=ax[0].text(1,0,'planète',)

soleil,=ax[0].plot(0,0,'r')
ax[0].text(0,0,'soleil')

foyer_2=ax[0].plot(0.8,0,'^b')
ax[0].text(0.8,-0.05,'second foyer')
deuxiemefoyer,= ax[0].plot(-eps*grandaxe,0,'*y',)

lignes,=ax[0].plot([0,x[0],-eps*grandaxe],[0,y[0],0],'--k',)


U=[0,vx[0],0]
V=[0,vy[0],eps*vr]
U=vx[0]
V=vy[0]
lignes2,=ax[1].plot(U,V,'--k')



def step(n):
    planete.set_data(x[n],y[n])
    #planete.text('planète')
    lignes.set_data([0,x[n],-eps*grandaxe],[0,y[n],0])
    lignes2.set_data([0,vx[n],0],[0,vy[n],eps*vr])

my_anim = animation.FuncAnimation(fig,step,frames=len(t),interval=20)
plt.show(block=False)

# plt.draw()

ax[0].legend(bbox_to_anchor=(0,1.02,1,0.102),loc=2 , ncol=2 , borderaxespad=0)
ax[1].legend(bbox_to_anchor=(0,1.02,1,0.102),loc=2 , ncol=2 , borderaxespad=0)
ax1.legend(bbox_to_anchor=(0,1.02,1,0.102),loc=2 , ncol=2 , borderaxespad=0)