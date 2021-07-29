# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 18:06:32 2021

@author: lucas
"""

import tkinter 
import numpy as np
import matplotlib.pyplot as plt
from tkinter import messagebox



eps = np.spacing(1)
file='valeurs.txt'

x_fichier=np.loadtxt(file,dtype=float,usecols=0)# import de la position en X des charges du ficher
q_fichier=np.loadtxt(file,dtype=float,usecols=1)# import des charges du ficher 

a=4#distance aux charges plus cette valeur est importante plus les charges sont loins
x=np.linspace(-a,a,100)
y=np.linspace(-a,a,100)
x_mesh,y_mesh = np.meshgrid(x,y)
z=x_mesh+y_mesh*1j       

                                          
def potentiel_complexe(q,x0,y0):
    
   z0=x0+y0*1j
   Z=z-z0
   Z[Z==0]= np.spacing(2)#remplacemetn de la valeur de Z=0 pour éviter une erreur plus loin
   w_z=-2*q*np.log(Z)#calcule du potentiel complexe
   return w_z                                                        
    
  
def charge_unique(*args):
    
    plt.close()#ferme un graph ouvert 
    q=float(valeur_Q_unique_E.get())#récupére une valeur dans une des zones de saisie tkinter
    if q==0:#si la charge est nul le programme renvoit un message d'erreur
        messagebox.showwarning('Attention!','Pour une charge nul le programme retourne une erreur',)#informe de l'erreur pour q=0
        plt.close()                   
    else:    
        w_z=potentiel_complexe(q,0,0) # création de la charge 
        
        A=w_z.imag
        phi=w_z.real
        n=32
        half =False

        shift0_5 = 0.5/n if half else 0
        nAmin= (int(np.min(A)/(2*np.pi))*2 - 1 - shift0_5)*4*np.pi
        nAmax= (int(np.max(A)/(2*np.pi))*2 + 1 + shift0_5)*4*np.pi
        isoA= np.arange(nAmin, nAmax+eps, 1./n*4*np.pi)

        km,kM,r=1,1,0.3# je me suis permis de modifier les valeurs  de km,kM et r dans certain cas, pour avoir des figure plus belle
        #ces valeurs détermine la taille de la figure dans le cadre et le nombre de levels donc le nombre d elinges de champ et d'équipotentielles
        isoPhi=np.arange(int(km*np.min(phi))-1, int(kM*np.max(phi))+1, r)
        print(phi[50])
        plt.figure('Charge unique',figsize=(9,6),dpi=100)
        plt.contourf(x_mesh,y_mesh,phi,levels=isoPhi,cmap='inferno')
        plt.colorbar(label='Equipotentielles')
        cphi=plt.contour(x_mesh,y_mesh,phi,colors='grey',levels=isoPhi)
        cA=plt.contour(x_mesh,y_mesh,A,levels=isoA,colors='b')
        labels = ['équipotentielles','lignes de champs']
        

        cA.collections[1].set_label(labels[1])
        cphi.collections[0].set_label(labels[0])  
        plt.xlabel('X')
        plt.ylabel('Y')
        
        plt.axis('image')
        plt.title('Charge unique (q={0})'.format(q))
        plt.legend(loc=2 , ncol=1 , borderaxespad=2)
    
    
def deux_charges_identiques(*args):  
        
        plt.close()#ferme un graph ouvert 
        messagebox.showinfo('valeurs charges','les charges valent (q=1)')
        w_z=potentiel_complexe(1,-1,0) +potentiel_complexe(1,1,0) 
        
        A=w_z.imag
        phi=w_z.real
        n=32
        half =False

        shift0_5 = 0.5/n if half else 0
        nAmin= (int(np.min(A)/(2*np.pi))*2 - 1 - shift0_5)*4*np.pi
        nAmax= (int(np.max(A)/(2*np.pi))*2 + 1 + shift0_5)*4*np.pi
        isoA= np.arange(nAmin, nAmax+eps, 2./n*4*np.pi)

        km,kM,r=1,1,0.3
        isoPhi=np.arange(int(km*np.min(phi))-1, int(kM*np.max(phi))+1, r)
        
            
        plt.figure('Deux charges identiques',figsize=(9,6),dpi=100)
        plt.contourf(x_mesh,y_mesh,phi,levels=isoPhi,cmap='inferno')
        plt.colorbar(label='Equipotentielles')
        cphi=plt.contour(x_mesh,y_mesh,phi,colors='grey',levels=isoPhi)
        cA=plt.contour(x_mesh,y_mesh,A,levels=isoA,colors='b')
        labels = ['équipotentielles','lignes de champs']
        
            

        cA.collections[1].set_label(labels[1])
        cphi.collections[0].set_label(labels[0])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis('image')
        plt.title('deux charges identiques (q=1)')
        plt.legend(loc=2 , ncol=2 , borderaxespad=0)
        
        
def dipôle(*args):
        plt.close()#ferme un graph ouvert 
        messagebox.showinfo('valeurs charges','les charges valent (q=1) et (q=-1)')
        w_z=potentiel_complexe(-1,-1,0) +potentiel_complexe(1,1,0) 
        
        A=w_z.imag
        phi=w_z.real
        n=32
        half =False

        shift0_5 = 0.5/n if half else 0
        nAmin= (int(np.min(A)/(2*np.pi))*2 - 1 - shift0_5)*4*np.pi
        nAmax= (int(np.max(A)/(2*np.pi))*2 + 1 + shift0_5)*4*np.pi
        isoA= np.arange(nAmin, nAmax+eps, 1./n*4*np.pi)

        km,kM,r=0.8,0.8,0.2
        isoPhi=np.arange(int(km*np.min(phi))-1, int(kM*np.max(phi))+1, r)
        plt.figure('Dipôle',figsize=(9,6),dpi=100)
        plt.contourf(x_mesh,y_mesh,phi,levels=isoPhi,cmap='inferno')
        plt.colorbar(label='Equipotentielles')
        cphi=plt.contour(x_mesh,y_mesh,phi,colors='grey',levels=isoPhi)
        cA=plt.contour(x_mesh,y_mesh,A,levels=isoA,colors='b')
        labels = ['équipotentielles','lignes de champs']


        cA.collections[1].set_label(labels[1])
        cphi.collections[0].set_label(labels[0])  
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis('image')
        plt.title('dipôle (q=1 et q=-1)')    
        plt.legend(loc=2 , ncol=2 , borderaxespad=0)
        
        
def deux_charges(*args):
    plt.close()#ferme un graph ouvert 
    q1=float(valeur_Q_differents_E1.get())#récupére une valeur dans une des zones de saisie tkinter
    q2=float(valeur_Q_differents_E2.get())#récupére une valeur dans une des zones de saisie tkinter
    q=abs(q1)+abs(q2)#cette ligne permet juste de savoir si tout les charges sont nul
    if q==0:#si les charges sont nul le programme renvoit un message d'erreur
        messagebox.showwarning('Attention!','Pour deux charges nul le programme retourne une erreur',)#informe de l'erreur pour q=0
        plt.close()
    
    else:    
        
        w_z=potentiel_complexe(q1,-1,0) +potentiel_complexe(q2,1,0) 
        
        A=w_z.imag
        phi=w_z.real
        n=32
        half =False

        shift0_5 = 0.5/n if half else 0
        nAmin= (int(np.min(A)/(2*np.pi))*2 - 1 - shift0_5)*4*np.pi
        nAmax= (int(np.max(A)/(2*np.pi))*2 + 1 + shift0_5)*4*np.pi
        isoA= np.arange(nAmin, nAmax+eps, 2./n*4*np.pi)

        km,kM,r=0.8,0.8,0.8
        isoPhi=np.arange(int(km*np.min(phi))-1, int(kM*np.max(phi))+1, r)
        plt.figure('Deux charges',figsize=(9,6),dpi=100)  
        plt.contourf(x_mesh,y_mesh,phi,levels=isoPhi,cmap='inferno')
        plt.colorbar(label='Equipotentielles')
        cphi=plt.contour(x_mesh,y_mesh,phi,colors='grey',levels=isoPhi)
        cA=plt.contour(x_mesh,y_mesh,A,levels=isoA,colors='b')
        labels = ['équipotentielles','lignes de champs']


        cA.collections[1].set_label(labels[1])
        cphi.collections[0].set_label(labels[0]) 
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis('image')
        plt.title('deux charges différentes (q={0} et q={1})'.format(q1,q2))
        plt.legend(loc=2 , ncol=2 , borderaxespad=0)
        
        
def quadrupôle(*args):
    plt.close()#ferme un graph ouvert 
    q1=float(valeur_Q_BG.get())#récupére une valeur dans une des zones de saisie tkinter
    q2=float(valeur_Q_HG.get())#récupére une valeur dans une des zones de saisie tkinter
    q3=float(valeur_Q_BD.get())#récupére une valeur dans une des zones de saisie tkinter
    q4=float(valeur_Q_HD.get())#récupére une valeur dans une des zones de saisie tkinter
    q=abs(q1)+abs(q2)+abs(q3)+abs(q4)#cette ligne permet juste de savoir si tout les charges sont nul
    if q==0:#si les charges sont nul le programme renvoit un message d'erreur
        messagebox.showwarning('Attention!','Si les quatre charges nul le programme retourne une erreur',)#informe de l'erreur pour q=0
        plt.close()
    else:    
        w_z=potentiel_complexe(q4,1,1) +potentiel_complexe(q3,1,-1)+potentiel_complexe(q1,-1,-1)+potentiel_complexe(q2,-1,1)
        A=w_z.imag
        phi=w_z.real
        n=32
        half =False

        shift0_5 = 0.5/n if half else 0
        nAmin= (int(np.min(A)/(2*np.pi))*2 - 1 - shift0_5)*4*np.pi
        nAmax= (int(np.max(A)/(2*np.pi))*2 + 1 + shift0_5)*4*np.pi
        isoA= np.arange(nAmin, nAmax+eps, 2./n*4*np.pi)

        km,kM,r=0.8,0.8,0.2
        isoPhi=np.arange(int(km*np.min(phi))-1, int(kM*np.max(phi))+1, r)
        plt.figure('Quadrupôle',figsize=(9,6),dpi=100)
        plt.contourf(x_mesh,y_mesh,phi,levels=isoPhi,cmap='inferno')
        plt.colorbar(label='Equipotentielles')
        cphi=plt.contour(x_mesh,y_mesh,phi,colors='grey',levels=isoPhi)
        cA=plt.contour(x_mesh,y_mesh,A,levels=isoA,colors='b')
        labels = ['équipotentielles','lignes de champs']


        cA.collections[1].set_label(labels[1])
        cphi.collections[0].set_label(labels[0]) 
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis('image')
        plt.title('quadrupôle')
        plt.legend(loc=2 , ncol=2 , borderaxespad=0)
        
        
def charges_ponctuelle_champ_uniforme(*args): 
        plt.close()#ferme un graph ouvert 
        E0=4
        A_theo=E0*y_mesh
        phi_theo=-E0*x_mesh
        w_inter= phi_theo-A_theo*1j
        w_z=w_inter+potentiel_complexe(1,0,0)
        
        A=w_z.imag
        phi=w_z.real
        n=32
        half =False
        plt.figure('Charge ponctuelle dans un champ uniforme',figsize=(9,6),dpi=100)
# ---------------------------------------------------------------------
#détermination de la position des potentiel nul,pour avoir une courbe plus lisse il faut augmenter le nombre de valeur de x et y       
        Zero=[]        
        for i in range(0,len(phi)):
            
            x_petit=x_mesh[i]
            for t in range(0,len(phi[i])):
                if abs(phi[i][t])==min(abs(phi[i])) :
                    
                    Zero.append(x_petit[t])
                   
        ù=np.linspace(-a,a,len(Zero)) 
        plt.plot(Zero,ù,'k')
#---------------------------------------------------------------------          
        shift0_5 = 0.5/n if half else 0
        nAmin= (int(np.min(A)/(2*np.pi))*2 - 1 - shift0_5)*4*np.pi
        nAmax= (int(np.max(A)/(2*np.pi))*2 + 1 + shift0_5)*4*np.pi
        isoA= np.arange(nAmin, nAmax+eps, 2*(0.24*a)/n*4*np.pi)

        km,kM,r=1,1,0.5*(0.6*a)
        isoPhi=np.arange(int(km*np.min(phi))-1, int(kM*np.max(phi))+1, r)
       
        plt.contourf(x_mesh,y_mesh,phi,levels=isoPhi,cmap='inferno')
        plt.colorbar(label='Equipotentielles')
        cphi=plt.contour(x_mesh,y_mesh,phi,colors='grey',levels=isoPhi)
        cA=plt.contour(x_mesh,y_mesh,A,levels=isoA,colors='b')
        labels = ['équipotentielles','lignes de champs']
        

        cA.collections[1].set_label(labels[1])
        cphi.collections[0].set_label(labels[0])  
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis('image')
        plt.legend(loc=2 , ncol=2 , borderaxespad=0)
        
        
def pseudo_condensateur_diélectrique(*args):
        plt.close()#ferme un graph ouvert 
        w_z=0#potentiel complexe initial
        for t in np.linspace(-1,1,401):#boucle qui créer 401 charges positives égales à 1/401 sur une ligne, de même pour les charges négatives
            w_zp=potentiel_complexe(1/401,t,0.5)#détermination de la position d'une charge positive
            w_zn=potentiel_complexe(-1/401,t,-0.5)#détermination de la position d'une charge négative
            w_z+=w_zn+w_zp
            
        A=w_z.imag
        phi=w_z.real
        n=32
        half =False

        shift0_5 = 0.5/n if half else 0
        nAmin= (int(np.min(A)/(2*np.pi))*2 - 1 - shift0_5)*4*np.pi
        nAmax= (int(np.max(A)/(2*np.pi))*2 + 1 + shift0_5)*4*np.pi
        isoA= np.arange(nAmin, nAmax+eps, 1./n*4*np.pi)

        km,kM,r=0.8,0.8,0.2
        isoPhi=np.arange(int(km*np.min(phi))-1, int(kM*np.max(phi))+1, r)
        plt.figure('Pseudo condensateur diélectrique',figsize=(9,6),dpi=100)
        plt.contourf(x_mesh,y_mesh,phi,levels=isoPhi,cmap='inferno')
        plt.colorbar(label='Equipotentielles')
        cphi=plt.contour(x_mesh,y_mesh,phi,colors='grey',levels=isoPhi)
        cA=plt.contour(x_mesh,y_mesh,A,levels=isoA,colors='b')
        labels = ['équipotentielles','lignes de champs']


        cA.collections[1].set_label(labels[1])
        cphi.collections[0].set_label(labels[0]) 
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis('image')
        plt.legend(loc=2 , ncol=2 , borderaxespad=0)
        
        
def condensateur_métallique(*args):  
        plt.close()#ferme un graph ouvert 
        w_z=0#potentiel complexe initial
                
        for t in range(0,len(q_fichier)):
            q_f=q_fichier[t]#valeurs des charges issue du ficher , la somme vaut 1
            x_f=x_fichier[t]#position des charges
            w_zp=potentiel_complexe(q_f,x_f,0.5)
            w_zn=potentiel_complexe(-q_f,x_f,-0.5)
            w_z+=w_zn+w_zp
   


        A=w_z.imag
        phi=w_z.real
        n=32
        half =False

        shift0_5 = 0.5/n if half else 0
        nAmin= (int(np.min(A)/(2*np.pi))*2 - 1 - shift0_5)*4*np.pi
        nAmax= (int(np.max(A)/(2*np.pi))*2 + 1 + shift0_5)*4*np.pi
        isoA= np.arange(nAmin, nAmax+eps, 1./n*4*np.pi)
        
        km,kM,r=0.8,0.8,0.3
        isoPhi=np.arange(int(km*np.min(phi))-1, int(kM*np.max(phi))+1, r)
        plt.figure('Condensateur métallique',figsize=(9,6),dpi=100)
        plt.contourf(x_mesh,y_mesh,phi,levels=isoPhi,cmap='inferno')
        plt.colorbar(label='Equipotentielles')
        cphi=plt.contour(x_mesh,y_mesh,phi,colors='grey',levels=isoPhi)
        cA=plt.contour(x_mesh,y_mesh,A,levels=isoA,colors='b')
        labels = ['équipotentielles','lignes de champs']
        
        
        cA.collections[1].set_label(labels[1])
        cphi.collections[0].set_label(labels[0])  
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis('image')
        plt.legend(loc=2 , ncol=2 , borderaxespad=0)    
#
#---------------Partie pour le fun---------------------------
#        
def charge_répartie_cercle(*args):
#cette focntion est uniquement présente car je voulais obtenir la figure du topo     
        plt.close()#ferme un graph ouvert 
        
        nb=valeur_Cercle.get()+1#récupére une valeur dans une des zones de saisie tkinter
        w_z=0#potentiel complexe initial
        t=0#condition initiale de l'angle qui va de 0° à 360°
        for i in range(1,nb):
            
            z=2*np.pi/(nb-1)#divise une cerle en un nombre de partie égale au nombe de charges souhaité
            
             
            if i%2==0:#condition pour faire un alternance de signes sur le cercle
                 w_z+=potentiel_complexe(0.5,np.cos(t),np.sin(t))
            else:
                 w_z+=potentiel_complexe(-0.5,np.cos(t),np.sin(t)) 
            t+=z#on ajoute z à t pour créer une nouvelle charge plus loin d'un angle z sur le cercle
            
                 
        A=w_z.imag
        phi=w_z.real
        n=32
        half =False
        if nb <= 20:#condition pour, ensuite poser une question a l'utilisateur si il veut continuer,
                    #car pour nb>20 le resultat est moins parlant            
            b=1
            a=0.2
        else:
           message=messagebox.askquestion('valeur importante',
                                   'voulez vous vraiment continuer avec {0} charges\nle résultat ne sera pas clair'.format(valeur_Cercle.get()))
           if message =='yes': 
                b=1.5
                a=0.4
           else:
                plt.close()
            
        shift0_5 = 0.5/n if half else 0
        nAmin= (int(np.min(A)/(2*np.pi))*2 - 1 - shift0_5)*4*np.pi
        nAmax= (int(np.max(A)/(2*np.pi))*2 + 1 + shift0_5)*4*np.pi
        isoA= np.arange(nAmin, nAmax+eps, b/n*4*np.pi)
        
        
        km,kM,r=0.8,0.8,a
        isoPhi=np.arange(int(km*np.min(phi))-1, int(kM*np.max(phi))+1, r)
        plt.figure('Charges répartie en cercle',figsize=(9,6),dpi=100)
        plt.contourf(x_mesh,y_mesh,phi,levels=isoPhi,cmap='inferno')
        plt.colorbar(label='Equipotentielles')
        cphi=plt.contour(x_mesh,y_mesh,phi,colors='grey',levels=isoPhi)
        cA=plt.contour(x_mesh,y_mesh,A,levels=isoA,colors='b')
        labels = ['équipotentielles','lignes de champs']
        
        
        cA.collections[1].set_label(labels[1])
        cphi.collections[0].set_label(labels[0])  
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis('image')
        plt.legend(loc=2 , ncol=2 , borderaxespad=0)  
        
        
def atome_fonc(*args):
#cette fonction est un test, pour voir si cétait possible de représenter fidélement un atome avec ce programme     
#c'est loin d'être fini, il y a beaucoup de régles à mettre en place pour se rapprocher de la réalité 
        
        K=valeur_Q_K.get()
        L=valeur_Q_L.get()
        M=valeur_Q_M.get()
        N=valeur_Q_N.get()
        nb=K+L+M+N
        plt.close()#ferme un graph ouvert 
        
        w_z=0#potentiel complexe initial
        t=0#condition initiale de l'angle qui commence à 0°
        for i in range(0,K):
            
            z=2*np.pi/(K)#divise une cerle en un nombre de partie égale au nombe de charges souhaité
            w_z+=potentiel_complexe(-1,2*np.cos(t),2*np.sin(t))
            t+=z
        t=0
        for i in range(0,L):   
            #répartion équitable sur le cercle dans le cas d'un nombre impaire d'électrons
            if L%2==1:
             m=int(L/2)+1  
            else:
             m=L/2   
               
            z=2*np.pi/(m)#divise une cerle en un nombre de partie égale au nombe de charges souhaité
            if i <L/2:#condition obligatoire si l'on veut le bon nombre d'électron sur la couche  
                      #car les electron sont par paire donc sans cette condition on aurai deux fois trop d'électrons sur la couche
                #if L%2==1:
                if i ==int(L/2) and L%2==1 :#cas d'un nombre impaire sur la couche
                    w_z+=potentiel_complexe(-1,4*np.cos((np.pi/4)+t),4*np.sin((np.pi/4)+t))
                    #sur cette couche j'ai effectué une rotation de 90° des position pour éviter un alignement trop fréquent entre les couches
                else:   
                    w_z+=potentiel_complexe(-1,4*np.cos((np.pi/4)+t),4*np.sin((np.pi/4)+t))#électron
                    w_z+=potentiel_complexe(-1,4*np.cos((np.pi/4)+t+0.11),4*np.sin((np.pi/4)+t+0.11))#électron voisin décalé de 0.11 rad
                            
            
            t+=z
        t=0    
        for i in range(0,M):
            #répartion équitabel sur le cercle dans le cas d'un nombre impaire d'électrons
            if M%2==1:
             m=int(M/2)+1  
            else:
             m=M/2              
            z=2*np.pi/(m)#divise une cerle en un nombre de partie égale au nombe de charges souhaité
            if i <M/2:
                if i ==int(L/2) and M%2==1:#cas d'un nombre impaire sur la couche
                    w_z+=potentiel_complexe(-1,6*np.cos(t),6*np.sin(t))
                else:
                    w_z+=potentiel_complexe(-1,6*np.cos(t),6*np.sin(t))
                    w_z+=potentiel_complexe(-1,6*np.cos(t+0.11),6*np.sin(t+0.11))
            t+=z
        t=0    
        for i in range(0,N):
            #répartion équitabel sur le cercle dans le cas d'un nombre impaire d'électrons
            if N%2==1:
             m=int(N/2)+1  
            else:
             m=N/2 
            z=2*np.pi/(m)#divise une cerle en un nombre de partie égale au nombe de charges souhaité
            if i <N/2:
                if i ==int(L/2) and N%2==1:#cas d'un nombre impaire sur la couche
                    w_z+=potentiel_complexe(-1,8*np.cos((np.pi/4)+t),8*np.sin((np.pi/4)+t))
                else:
                    w_z+=potentiel_complexe(-1,8*np.cos((np.pi/4)+t),8*np.sin((np.pi/4)+t))
                    w_z+=potentiel_complexe(-1,8*np.cos((np.pi/4)+t+0.11),8*np.sin((np.pi/4)+t+0.11))
            t+=z
            
        w_z+=potentiel_complexe(1*nb,0,0)#noyau de l'atome de charge   
        
       
        if nb <= 15:#condition pour, ensuite poser une question a l'utilisateur si il veut continuer,
                    #car pour nb>20 le resultat est moins parlant            
            b=2.5*(0.5*a)
            e=0.6*(0.3*a)
        else:
           message=messagebox.askquestion('valeurs importantes',
                                   'voulez vous vraiment continuer avec {0} charges\nle résultat ne sera pas clair'.format(nb))
           if message =='yes': 
                b=4*(0.9*a)
                e=0.75*(1.5*a)
           else:
                plt.close()
        A=w_z.imag
        phi=w_z.real
        n=32
        half =False    
        shift0_5 = 0.5/n if half else 0
        nAmin= (int(np.min(A)/(2*np.pi))*2 - 1 - shift0_5)*4*np.pi
        nAmax= (int(np.max(A)/(2*np.pi))*2 + 1 + shift0_5)*4*np.pi
        isoA= np.arange(nAmin, nAmax+eps, b/n*4*np.pi)
        
        
        km,kM,r=0.8,0.8,e
        isoPhi=np.arange(int(km*np.min(phi))-1, int(kM*np.max(phi))+1, r)
        plt.figure('Atome',figsize=(9,6),dpi=100)
        plt.contourf(x_mesh,y_mesh,phi,levels=isoPhi,cmap='inferno')
        plt.colorbar(label='Equipotentielles')
        
        cphi=plt.contour(x_mesh,y_mesh,phi,colors='grey',levels=isoPhi)
        cA=plt.contour(x_mesh,y_mesh,A,levels=isoA,colors='b')
        labels = ['équipotentielles','lignes de champs']

        cA.collections[1].set_label(labels[1])
        cphi.collections[0].set_label(labels[0])  
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.axis('image')
        plt.legend(loc=2 , ncol=2 , borderaxespad=0) 
        
#---------------tkinter-------------------------------
#tout ce qui arrive est simplement la mise en forme de la fenêtre tkinter
#(bouton, zone de saisie, labels, et autres)
app = tkinter.Tk()
app.title('étude de champs')

Grand_frame1=tkinter.Frame(app)
Grand_frame2=tkinter.Frame(app)
frame0=tkinter.Frame(Grand_frame1)
frame1=tkinter.LabelFrame(Grand_frame1,text='charge unique')
frame2=tkinter.LabelFrame(Grand_frame1,text='deux_charges_identiques')
frame3=tkinter.LabelFrame(Grand_frame2,text='dipôle')
frame4=tkinter.LabelFrame(Grand_frame1,text='deux_charges')
frame5=tkinter.LabelFrame(Grand_frame1,text='quadrupôle')
frame6=tkinter.LabelFrame(Grand_frame2,text='charges_ponctuelle_champ_uniforme')
frame7=tkinter.LabelFrame(Grand_frame2,text='pseudo_condensateur_diélectrique')
frame8=tkinter.LabelFrame(Grand_frame2,text='condensteur_métallique')
frame9=tkinter.LabelFrame(Grand_frame2,text='charges en cercle')
frame10=tkinter.LabelFrame(Grand_frame2,text='atome')

def quitter(*args):
    message=messagebox.askquestion('quitter','Voulez vous quitter ?',)
    if message == 'yes':
        app.destroy()
    else:
        pass
    
def info(*args):   
    """    éviter les valeurs de charge trop importante,
    sinon le temps de calcule sera long et le  
    résultat sera compliqué à exploiter. """
    messagebox.showinfo('info',info.__doc__)
                            
    
#-------------Boutons tkinter---------------------------

bouton_info=tkinter.Button(frame0,command=info,text='INFO',fg = 'blue')  
 
bouton_quitter=tkinter.Button(frame0, 
                              command=quitter,
                              text='QUITTER',fg = 'red')
                                                   
bouton_atome=tkinter.Button(frame10, 
                              command=atome_fonc,
                              text='atome').pack(side='right',ipadx=50,padx=50)                                                       
bouton_charge_unique=tkinter.Button(frame1, 
                              command=charge_unique,
                              text='charge unique').pack(side='right',ipadx=50,padx=50)


bouton_deux_charges_identiques=tkinter.Button(frame2, 
                              command=deux_charges_identiques,
                              text='deux charges identiques').pack(ipadx=25)

                                                 
bouton_dipôle=tkinter.Button(frame3, 
                              command=dipôle,
                              text='dipôle').pack(ipadx=73)

    
bouton_deux_charges=tkinter.Button(frame4, 
                              command=deux_charges,
                              text='deux charges').pack(ipadx=55)
                                                     
                
bouton_quadrupôle=tkinter.Button(frame5, 
                              command=quadrupôle,
                              text='quadrupôle').pack(ipadx=65)


bouton_charges_ponctuelle_champ_uniforme=tkinter.Button(frame6, 
                              command=charges_ponctuelle_champ_uniforme,
                              text='charges ponctuelle champ uniforme').pack(ipadx=1)

                                                              
bouton_pseudo_condensateur_diélectrique=tkinter.Button(frame7, 
                              command=pseudo_condensateur_diélectrique,
                              text='pseudo condensateur diélectrique').pack(ipadx=10) 
                                                    

bouton_condensateur_métallique=tkinter.Button(frame8,                                              
                              command=condensateur_métallique,
                              text='condensateur métallique').pack(ipadx=40)

bouton_charge_cercle=tkinter.Button(frame9,                                              
                              command=charge_répartie_cercle,
                              text='charges en cercle').pack(ipadx=40,side='right',padx=50)


#---------zone de saisie charge unique-----------------

Label_Q_unique_E=tkinter.StringVar()
Label_Q_unique=tkinter.Label(frame1,textvariable=Label_Q_unique_E).pack(side='left',padx=5)
Label_Q_unique_E.set('valeur de la charge :')

valeur_Q_unique_E=tkinter.StringVar()
valeur_Q_unique=tkinter.Entry(frame1,textvariable=valeur_Q_unique_E).pack(side='left',pady=1)
valeur_Q_unique_E.set('1')

#-----------zone de saisie deux charges------------------

Label_Q_double_E=tkinter.StringVar()
Label_Q_double=tkinter.Label(frame4,textvariable=Label_Q_double_E).pack()
Label_Q_double_E.set('valeur de la charge (1) :')

valeur_Q_differents_E1=tkinter.StringVar()
valeur_Q_differents1=tkinter.Entry(frame4,textvariable=valeur_Q_differents_E1).pack(pady=1)
valeur_Q_differents_E1.set(1)

Label_Q_double_E2=tkinter.StringVar()
Label_Q_double2=tkinter.Label(frame4,textvariable=Label_Q_double_E2).pack()
Label_Q_double_E2.set('valeur de la charge (2) :')

valeur_Q_differents_E2=tkinter.StringVar()
valeur_Q_differents2=tkinter.Entry(frame4,textvariable=valeur_Q_differents_E2).pack(pady=1)
valeur_Q_differents_E2.set('-2')



#---------zone de saisie quadripole-----------------------

valeur_Q_BG=tkinter.StringVar()
valeur_Q_HG=tkinter.StringVar()
valeur_Q_BD=tkinter.StringVar()
valeur_Q_HD=tkinter.StringVar()

Label_Q_BG=tkinter.StringVar()
Label_Q_BG_E=tkinter.Label(frame5,textvariable=Label_Q_BG).pack()
Label_Q_BG.set('charge bas gauche :')

valeur_Q_BG_E=tkinter.Entry(frame5,textvariable=valeur_Q_BG).pack(pady=1)
valeur_Q_BG.set('1')
 
Label_Q_HG=tkinter.StringVar()
Label_Q_HG_E=tkinter.Label(frame5,textvariable=Label_Q_HG).pack()
Label_Q_HG.set('charge haut gauche :')

valeur_Q_HG_E=tkinter.Entry(frame5,textvariable=valeur_Q_HG).pack(pady=1)
valeur_Q_HG.set('-1')
     
Label_Q_BD=tkinter.StringVar()
Label_Q_BD_E=tkinter.Label(frame5,textvariable=Label_Q_BD).pack()
Label_Q_BD.set('charge bas droit :')

valeur_Q_BD_E=tkinter.Entry(frame5,textvariable=valeur_Q_BD).pack(pady=1)
valeur_Q_BD.set('-1')
    
Label_Q_HD=tkinter.StringVar()
Label_Q_HD_E=tkinter.Label(frame5,textvariable=Label_Q_HD).pack()
Label_Q_HD.set('charge haut droit :')

valeur_Q_HD_E=tkinter.Entry(frame5,textvariable=valeur_Q_HD).pack(pady=1)
valeur_Q_HD.set('1')

#-----------zone de saisie charge cercle----------------


Label_Cercle=tkinter.StringVar()
Label_Cercle_E=tkinter.Label(frame9,textvariable=Label_Cercle).pack(side='left',padx=5)
Label_Cercle.set('Nombre de charges:')

valeur_Cercle=tkinter.IntVar()
valeur_Cercle_E=tkinter.Entry(frame9,textvariable=valeur_Cercle).pack(pady=1,side='left')
valeur_Cercle.set(6)


#---------zone de saisie atome-------------------------
valeur_Q_K=tkinter.IntVar()
valeur_Q_L=tkinter.IntVar()
valeur_Q_M=tkinter.IntVar()
valeur_Q_N=tkinter.IntVar()
    
Label_Q_K=tkinter.StringVar()
Label_Q_K_E=tkinter.Label(frame10,textvariable=Label_Q_K).pack()
Label_Q_K.set('nombre électron couche (K) (max=2) :')


valeur_Q_K_E=tkinter.Entry(frame10,textvariable=valeur_Q_K).pack(pady=1)

 
Label_Q_L=tkinter.StringVar()
Label_Q_L_E=tkinter.Label(frame10,textvariable=Label_Q_L).pack()
Label_Q_L.set('nombre électron couche (L) (max=8):')


valeur_Q_L_E=tkinter.Entry(frame10,textvariable=valeur_Q_L).pack(pady=1)

     
Label_Q_M=tkinter.StringVar()
Label_Q_M_E=tkinter.Label(frame10,textvariable=Label_Q_M).pack()
Label_Q_M.set('nombre électron couche (M) (max=18):')


valeur_Q_M_E=tkinter.Entry(frame10,textvariable=valeur_Q_M).pack(pady=1)

    
Label_Q_N=tkinter.StringVar()
Label_Q_N_E=tkinter.Label(frame10,textvariable=Label_Q_N).pack()
Label_Q_N.set('nombre électron couche (N) (max=32):')


valeur_Q_N_E=tkinter.Entry(frame10,textvariable=valeur_Q_N).pack(pady=1)

Label_info=tkinter.StringVar()
Label_info_E=tkinter.Label(frame10,textvariable=Label_info).pack()
Label_info.set("Les valeurs maximal sont purrement indicative rien n'empéche d'aller au dela,\nce sont juste les valeurs maximal réel des couches électroniques")




bouton_info.pack(padx=50,pady=5,ipadx=80,side='left') 



bouton_quitter.pack(padx=50,pady=5,ipadx=70,side='right') 
frame0.pack(side='top',fill='x',ipady=5,padx=10)  
frame1.pack(side='top',fill='x',ipady=5,padx=10)
frame2.pack(side='top',fill='x',ipady=5,padx=10)
frame3.pack(side='top',fill='x',ipady=5,padx=10)
frame4.pack(side='top',fill='x',ipady=5,padx=10)
frame5.pack(side='top',fill='x',ipady=5,padx=10)
frame6.pack(side='top',fill='x',ipady=5,padx=10)
frame7.pack(side='top',fill='x',ipady=5,padx=10)  
frame8.pack(side='top',fill='x',ipady=5,padx=10)
frame9.pack(side='top',fill='x',ipady=5,padx=10)
frame10.pack(side='top',fill='x',ipady=5,padx=10)
Grand_frame1.pack(side='left',fill='x',ipady=5,padx=10)
Grand_frame2.pack(side='left',fill='x',ipady=5,padx=10)                                                                       
app.mainloop()































































