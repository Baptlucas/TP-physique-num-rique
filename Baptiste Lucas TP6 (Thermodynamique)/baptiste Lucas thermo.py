# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 09:29:00 2021

@author: lucas
"""

import tkinter#permet de créer des fenêtres où l'on peut y ajouter des widgets
import numpy as np
from math import log
import matplotlib.pyplot as plt
app= tkinter.Tk()#création de la fenêtre tkinter
app.geometry('600x300')#dimenssion de cette fenêtre

N_A= 6.02E23
R=8.31
h=6.626E-34
M_air=28.97E-3

Kb=R/N_A
y=h**2


U_var=tkinter.IntVar(value=(1000))#variable tkinter lié a une zone de saisie de la fenêtre
V_var=tkinter.IntVar(value=(1000))#idem
N_var=tkinter.IntVar(value=(1))#idem
L_entropie=tkinter.StringVar()#idem



def Entropie(*args):#fonction entropie pour Tkinter/c'est la fonction exécuté par le bouton 
    
        U=U_var.get()#permet de récupérer la valeur écrite dans la zone de saisie
        V=V_var.get()#idem
        n=N_var.get()#idem
        N=n*N_A
        m=n*M_air
        S=Kb*N*(log((V/N)*(((4*np.pi*m*U)/(3*y*N))**(5/2)))+7/2)
        
        L_entropie.set('valeur entropie = {0}'.format(S))#applique à un fonction de type label de tkinter un texte
        #le texte ci dessu est formaté pour pouvoir afficher différentes valeurs de l'entropie
#question 1-2
def entropie(u,v,n):
        N=n*N_A
        m=n*M_air
        S=Kb*N*(np.log((v/N)*(((4*np.pi*m*u)/(3*y*N))**(5/2)))+7/2)
        return S

plt.figure(figsize=(6,3), dpi = 100)
u= np.logspace(-5,5,10)
v= np.logspace(-5,5,10)
n=1
u,v=np.meshgrid(u,v)


S=entropie(u,v,n)
plt.xlabel('énergie interne (U)')
plt.ylabel('volume (V)')
plt.title('Entropie en fonction de U et V')
plt.contourf(np.log(u),np.log(v),S, 1000)
plt.colorbar(label='Entropie')


#question 3-4
def Temperature(u,v,n):#définition d ela température
   delta_U=u/1000
   T=(2*delta_U)/((entropie(u+delta_U,v,n)-(entropie(u-delta_U,v,n))))
   return T

print(Temperature(1000,1000,1))
    

def Pression(u,v,n):#définition de la pression
   delta_U=u/1000
   delta_V=v/1000
   T=(2*delta_U)/((entropie(u+delta_U,v,n)-(entropie(u-delta_U,v,n))))
   P=(((entropie(u,v+delta_V,n)-(entropie(u,v-delta_V,n))))*T)/(2*delta_V)
   return P

print(Pression(1000,1000,1))


    
u= np.logspace(-3,6,100)
v= np.logspace(-3,6,100)
n=1
u,v=np.meshgrid(u,v)
S=entropie(u,v,n)




plt.figure(figsize=(6,4), dpi = 100)
plt.contourf(np.log(u),np.log(v),np.log(Pression(u,v,n)), 1000)
plt.colorbar()
plt.title('P en fonction de  U et V ')
plt.xlabel('U')
plt.ylabel('V')




plt.figure(figsize=(6,4), dpi = 100)
plt.contourf(np.log(u),np.log(v),np.log(Temperature(u,v,n)), 1000)
plt.colorbar()
plt.title('T en fonction de  U et V ')
plt.xlabel('U')
plt.ylabel('V')


P= np.linspace(100, 1100,100)#valeurs de pression de la  troposphère en hpa
T= np.linspace(213.15 ,313.15,100)#valeurs de température de la  troposphère


T=Temperature(u,v,n)
plt.figure(figsize=(6,4), dpi = 100)
plt.plot(T[1,:],(5/2)*N_A*Kb*T[1,:],'ro',label='Gaz parfait diatomique (théorique de U)')
plt.plot(T[1,:], u[1,:],label='Valeurs numérique de (U)')
plt.xlabel("Température (T)")
plt.ylabel("énergie interne (U)")
plt.legend(bbox_to_anchor=(0,1.02,1,0.102),loc=2 , ncol=2 , borderaxespad=0)
#question 5
def Entropie2(T,P,n):#définition de l'entropie avec U théorique
    u=(5/2)*N_A*Kb*T
    v=(n*R*T)/P
    N=n*N_A
    m=n*M_air
    S=Kb*N*(np.log((v/N)*(((4*np.pi*m*u)/(3*y*N))**(5/2)))+7/2)
    return S
#question 6
def Temperature_potentiel(T,P):#définition de la température potentiel
    Cp=(7/2)*R
    P0=1000*100
    theta= T*(P/P0)**(-R/Cp)
    return theta

#theta= Temperature_potentiel(300,2E5)
#print('theta',theta)


def Rho_air(T,P):#définition de masse volumique de l'air
    v=(n*R*T)/P
    m=n*M_air
    rho= m/v
    return rho
rho= Rho_air(T,P)


#question 8-9
def altitude(T,P):#définition de l'altitude
    N=10000
    p0=100000
    z=0
    dp=(P-p0)/N
    g=9.81
    for i in range(N):
        dz= -dp/(Rho_air(T ,p0+i*dp)*g)
        z= z +dz
    return z 

z= altitude(220,9965)



T=np.linspace(273.15-80,273.15+50.,100 )#valeurs de température réaliste
P=np.linspace(1E5,1E4, 100) #valeurs de pression réaliste en Pa
T,P= np.meshgrid(T,P)


S=Entropie2(T,P,n)  
theta= Temperature_potentiel(T,P)
z= altitude(T,P)
plt.figure(figsize=(10,9), dpi = 100)   

#gestion des fichier 'profileX.npy' 
Nom=['profile1','profile2','profile2','profile4']
[z1, P1 , T1, theta1]= np.load('profile1.npy')
[z2, P2 , T2, theta2]= np.load('profile2.npy')
[z3, P3 , T3, theta3]= np.load('profile3.npy')
[z4, P4 , T4, theta4]= np.load('profile4.npy') 

Plist=[P1,P2,P3,P4]
Tlist=[T1,T2,T3,T4]
for n in range(0,4):
    plt.plot(Tlist[n],Plist[n]*100,label=Nom[n])

  
Zplot=plt.contour(T-273.15,P,z,19, colors='k') #lignes d'altitude
plt.clabel(Zplot,Zplot.levels,fmt='%2.f')
thetaplot=plt.contour(T-273.15,P,theta,20, colors='white',label='')#adiabatiques séche
plt.clabel(thetaplot,thetaplot.levels,fmt='%2.f')


plt.contourf(T-273.15,P,S, 1000, cmap='RdBu_r')
plt.ylim(100*1000,10*1000)
plt.yscale('log')
plt.xlim(-80,40)
plt.colorbar(label='Entropie')
plt.title('entropie en fonction de  T et P')
plt.xlabel('Témpérature (T) °C ')
plt.ylabel('Pression (P) Pa ')
plt.legend(bbox_to_anchor=(0,1.02,1,0.102),loc=2 , ncol=2 , borderaxespad=0)

#question 7
def Rho_air(T,P):
    v=(n*R*T)/P
    m=n*M_air
    rho= m/v
    return rho
rho= Rho_air(274,1E5)
print(rho)
T,P= np.meshgrid(np.linspace(273.15-80,273.15+50., 100),np.linspace(1E5,1E4, 100))
rho= Rho_air(T,P)  
#plt.figure(figsize=(6,4), dpi=100) 
#plt.contourf(T , P, rho,1000)    
#plt.title('masse volumique de air en fonction T et P')   
    
#question 10 














    



  
U_entre=tkinter.Entry(app, textvariable= U_var)#définition d'une zone de saisie app est la fenêtre principale
V_entre=tkinter.Entry(app, textvariable= V_var)#les textvariable servent a nommer la varialble de ce widget pour pouvoir la définir 
N_entre=tkinter.Entry(app, textvariable= N_var)#les variables sont définient au début
Bouton_Execution=tkinter.Button(app, command=Entropie, text='entropie')#bouton tkinter pour exécuter une fonction ici 'Entropie'
Label_entropie=tkinter.Label(app,textvariable=L_entropie)#définition du label qui affiche l'entropie


Bouton_Execution.pack()#les .pack() permettent de faire apparaître les widget dans la fenêtre
U_entre.pack()
V_entre.pack()
N_entre.pack()
Label_entropie.pack()

app.mainloop()#permet a la fenêtre d'être infini sauf si on la quitte 

