# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:00:55 2021

@author: lucas
"""
#from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import tkinter
import numpy as np
from scipy.optimize import curve_fit
from scipy.integrate import odeint
from math import sqrt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter.filedialog as tkD

#fenêtre principale tkinter
app= tkinter.Tk()
app.geometry("830x330")

#cadres de tkinter dans la fenêtre princiaple
frame1= tkinter.LabelFrame(app,text='Variables')
frame2= tkinter.LabelFrame(app,text='représentation')
frame3= tkinter.LabelFrame(app,text='représentation resonanceRLC.txt')


#Cadres dans frame1
#tkinter.LabelFrame(argument1, text='votre texte') avec argument1= (nom de la fenêtre/cadre où mettre ce cadre)
Mframe1= tkinter.LabelFrame(frame1,text='')
Mframe2= tkinter.LabelFrame(frame1,text='')
Mframe3= tkinter.LabelFrame(frame1,text='')
Mframe4= tkinter.LabelFrame(frame1,text='')
Mframe5= tkinter.LabelFrame(frame1,text='')

#Bouton et zonne de saisie pour la vairable gamma
#(Entry ou Label on les mêmes arguments)     Nomwidget= tkinter.Entry(Nomfenêtre/cadre,  textvariable = nomVaraible(exemple: Gamme_label))
Gamma_label= tkinter.StringVar()#définition du type de variable  (String, Int , Double) ici Double correspond  à des varaibles flotantes
Gamma = tkinter.IntVar()
Entre_gamma = tkinter.Entry(Mframe1 , textvariable = Gamma)
Label_gamma = tkinter.Label(Mframe1 , textvariable = Gamma_label)
Gamma_label.set('Valeur gamma :')#Nomvariable.set(argument) prend comme argument une valeur de type (string, int , float) selon les envies

X0_label= tkinter.StringVar()
X0 = tkinter.IntVar()
Entre_X0 = tkinter.Entry(Mframe2 , textvariable = X0)
Label_X0 = tkinter.Label(Mframe2 , textvariable = X0_label)
X0_label.set('Valeur x0 :')

V0_label= tkinter.StringVar()
V0 = tkinter.IntVar()
Entre_V0 = tkinter.Entry(Mframe3 , textvariable = V0)
Label_V0 = tkinter.Label(Mframe3 , textvariable = V0_label)
V0_label.set('Valeur v0 :' )

W0_label= tkinter.StringVar()
W0 = tkinter.IntVar()
Entre_W0 = tkinter.Entry(Mframe4 , textvariable = W0)
Label_W0 = tkinter.Label(Mframe4 , textvariable = W0_label)
W0_label.set('Valeur w0 :')

WF_label= tkinter.StringVar()
WF = tkinter.IntVar()
Entre_WF = tkinter.Entry(Mframe5 , textvariable = WF)
Label_WF = tkinter.Label(Mframe5 , textvariable = WF_label)
WF_label.set('Valeur wf :')

VALEURS_label=tkinter.StringVar()
Label_VALEURS = tkinter.Label(frame1 , textvariable = VALEURS_label)
VALEURS_label.set('Valeurs initales suggérés (figure1)\n x0 = 1 ; v0 = 0 ; w0 = 1 ; gamma = 0.1 ; Wf = 0.9 ')

#valeurs du temps  np.linspace(départ,arrivé, nombre de valeurs)
time = np.linspace(0,140,1000)


#partie I représentation d'une oscilation harmonique amortie ( solution analytique et numérique).
# et  représentation du portrait de phase

def Représentation1(*args):#fonction qui est la command du bouton 'figure1'
    plt.close()# cette ligne permet de fermer la fenêtre déjà ouverte si c'est le cas pour pouvoir ouvrir la nouvelle
    x0 = int(Entre_X0.get())#valeur initiale de X
    v0 = int(Entre_V0.get())#valeur initiale de v
    w0 = int(Entre_W0.get())#valeur initiale de W , w0 est la pulsation propre
    gamma =float( Entre_gamma.get())#coef d'amortissement
    w=np.sqrt((w0**2)-(gamma**2))
    
    def équation_ordre_deux(xv,t):   
        x = xv[0]
        v = xv[1]
        dxdt = v #dérivé temporelle  de la position, soit la vitesse
        dvdt= -2*gamma*v-w0**2*x #équation oscilateur harmonique amortie 
        return (dxdt,dvdt)
    
    
    y0=[x0,v0]#condition initiales
    sol = odeint(équation_ordre_deux,y0,time) #odeint() intégre une équation différentiel et retourne ses solutions
    x=sol[:,0]#solution numérique
    v=sol[:,1]#solution numérique       
    p=x0*(np.cos(w*time)+(gamma*np.sin(w*time))/w)*np.exp(-gamma*time) #solution analytique 
    #ligne ci-dessous établie le subplot et défini ses dimensions
    fig, (ax1,ax2) = plt.subplots(1, 2, gridspec_kw ={'width_ratios':(1.7,1) } ,
                                  num = 'fig name', clear = True)
    ax1.set_ylim(-1,1)
    #ax1 est le premier graph du subplot , ax2 le deuxième
    
    ax1.plot(time,sol[:,1],'r--',label='dx/dt numérique')

    ax1.plot(time,sol[:,0],'-b' ,label='x(t) numérique')

    #ax1.plot(time, p ,'bo' ,markevery=5,label='x(t) analytique')

    #ax1.plot(time,-x0*((w0**2)/w)*np.sin(w*time)*np.exp(-gamma*time),'r+', 
            # markevery=5, label='dx/dt analytique')

    ax1.set_xlim(0,30)
    ax1.set_xlabel(r'$temps,\ t$')
    ax1.set_ylabel('x(t), dx/dt')
    ax1.grid()#affiche une grille sur le graph
    ax1.set_title('')#titre du graph 1
    ax1.legend(bbox_to_anchor=(0,1.02,1,0.102), loc=3, ncol=2 , borderaxespad=0)
    #crée une legende, les arguments dedans permettent de positionner la legende hos du graph
    
    
    ax2.plot(v,x, 'b')
    ax2.set_ylabel('x(t)')
    ax2.set_xlabel('dx/dt')
    ax2.set_xlim(-1,1)
    ax2.set_ylim(-1,1)
    ax2.set_title('Portrait de phase \nGamma = {}'.format(Entre_gamma.get()))
    ax2.grid()
      
 
#%%

time = np.linspace(0,140,1000)
def Représentation2(*args):

    plt.close()
    x0 = float(Entre_X0.get())
    v0 = float(Entre_V0.get())
    w0 = float(Entre_W0.get())
    gamma =float( Entre_gamma.get())
    
    def fonction_creneau(time):#définition de la fonction créneau qui vaut 1 dans un interval t=[0,50], 0 sinon
        if time < 50 and time >0:
            p=1
        else:
            p=0
        return p

    def oscilateur1(y,time):
        x=y[0]
        v=y[1]
        dxdt=v
        dvdt=fonction_creneau(time)-2*gamma*v-(w0**2)*x
        return dxdt, dvdt

    sol = odeint(oscilateur1,(x0,v0),time)#odeint() intégre une équation différentiel et retourne ses solutions
    plt.subplot(1,2,1)#plt.subplot() permet de mettre plusieurs graph dans une même fenêtre
    plt.xlabel(r'$temps,\ t$')#nom de l'axe des abscisses
    plt.ylabel('x(t), dx/dt')#nom de l'axe des ordonnées
    plt.plot(time,sol[:,0],label='x(t)')
    plt.plot(time,sol[:,1],label='dx/dt')
    plt.legend(bbox_to_anchor=(0,1.02,1,0.102), loc=3, ncol=2 , borderaxespad=0)
    plt.grid()
    plt.subplot(1,2,2)
    plt.grid()
    plt.plot(sol[:,1],sol[:,0],label= 'dx/dt en fonction de x(t)')#
    plt.title('portait de phase')#titre de la figure
    plt.legend()
def Représentation3(*args):
    
    plt.close()#plt.close() permet de fermer le graphique existant, lorsque l'on clique sur le bouton 'figureX'        
    w0 = float(Entre_W0.get())
    gamma =float( Entre_gamma.get())
    wf=float( Entre_WF.get())
    f =np.sin(wf*time)
    def oscilateur2(y,time):
        x=y[0]
        v=y[1]
        dxdt=v
        dvdt=np.sin(wf*time)-2*gamma*v-(w0**2)*x
        return dxdt,dvdt
    
    sol=odeint(oscilateur2,(0,0),time)#odeint() intégre une équation différentiel et retourne ses solutions
    plt.figure()
    plt.subplot(1,2,1)
    plt.grid()
    plt.plot(time/np.pi,sol[:,0],label='x(t)')    
    plt.plot(time/np.pi,f,'r',label='f(t)')   
    plt.xlabel(r'$temps,\ t$')
    plt.ylabel('x(t), dx/dt')
    plt.legend(bbox_to_anchor=(0,1.02,1,0.102), loc=3, ncol=2 , borderaxespad=0)
    plt.title('oscillation forcées')
    
    plt.subplot(1,2,2)
    plt.grid()
    plt.plot(sol[:,1],sol[:,0])
    plt.title('portrait de phase\ndx/dt en fonction de x(t)')
    plt.show()
    
    
def Représentation4(*args):
    
    plt.close()
    x0 = float(Entre_X0.get())
    v0 = float(Entre_V0.get())
    w0 = float(Entre_W0.get())
    gamma =float( Entre_gamma.get())
    wf=float( Entre_WF.get())
    allw = np.linspace(0.2,2,200)

    a=0.01
    for f0 in [0.5,1,2,3]:
        allax = []       
        
        def eq_oscillateur_forcé(y,time):
            x = y[0]
            v = y[1]
            dxdt = v
            dvdt = f0*np.sin(wf*time) - 2*gamma*v - (w0**2)*(x+a*x**3)
            return dxdt, dvdt
    
        for wf in allw:
            x,v = odeint(eq_oscillateur_forcé, (x0,v0), time).T#odeint() intégre une équation différentiel et retourne ses solutions
            ax = max(abs (x[time>90]))                       
            allax += [ax]
            
            
        plt.plot(allw, allax, label = 'f0= {0}'.format(f0) )        
        plt.ylim(0,11,1)
        plt.title("Résonance : \u03B3 = 0.10; a = + 0.0100")
        plt.xlabel('w/w0')
        plt.ylabel('amplitude stationaire de x(t)')
        plt.legend()
        plt.show()
        plt.grid()
       
#%% circuitRLC, import de datas

Fichier=[]#liste vide où l'on va noter le chemin du fichier à traiter
List2=[]#liste vide où l'on va noter les valeurs de chaque lignes du fichier
def nom_document(*args): #focntion pour selectionner un fichier   
    if Fichier == []:#condition si lla liste est vide on execute les lignes ci-dessous
        Fichier.append(tkD.askopenfilename(title = "fichier à gérer",filetypes = [('all','.*')])) 
        bouton_recherche_e.set(Fichier[0])
        
    else:
        Fichier.remove(Fichier[0])
    print(Fichier)
bouton_recherche_e     = tkinter.StringVar()
bouton_recherche       = tkinter.Button(frame3 ,command= nom_document , 
                                        text='recherche')
bouton_recherche_entry = tkinter.Entry(frame3, 
                                       textvariable= bouton_recherche_e )


def entré_fichier(*args):
    
        with open(Fichier[0]) as Fich:#lecture du fichier ouvert plus haut
            lines = [line.strip('\n') for line in Fich.readlines()]
        
      
        for line in lines:
            F=line.split()
            List2.append(F)   
            
        Valeurs_x=[]
        Valeurs_y=[]
        for t in range(0,len(List2)):
            List_t=List2[t]
            Valeurs_x.append(float(List_t[0]))
            Valeurs_y.append(float(List_t[1])*1000)
        plt.figure(figsize=(9,5), dpi=100)
        plt.title('RLC résonance (1 H, 0.1 µF, 350\u03A9 ­)' )  
        plt.xlabel('Fréquence (Hz)')       
        plt.ylabel('Amplitude (mV)')
        plt.grid()    
        plt.plot(Valeurs_x,Valeurs_y)
        plt.xlim(300,700,50)
            
#%% bouton pour afficher les graphs    
#bouton= tkinter.Button([nom de la fenêtre/cadre],command= nom_fonction_à_executer , text='texte dand le bouton')
Repre1_bouton= tkinter.Button(frame2, command= Représentation1, text='figure1')     
Repre2_bouton= tkinter.Button(frame2, command= Représentation2, text='figure2') 
Repre3_bouton= tkinter.Button(frame2, command= Représentation3, text='figure3')
Repre4_bouton= tkinter.Button(frame2, command= Représentation4, text='figure4')
Repre5_bouton= tkinter.Button(frame3, command= entré_fichier  , text='figure5')     



 
#%% pack ------ Nomwidget.pack() permet à ce widget d'apparaître sur la fenêtre
#les arguments de .pack():  
#side='top/left/right/bottom' (pour définir la position dans la fenêtre)
#ipady ou ipadx = nb de pixels (défini le nb de pixels à l'intérieur du widget)
#pady ou padx = nb de pixels (défini le nb de pixels qui sépare ce widget d'un autre élément) 


Label_VALEURS.pack(side = 'top') 
Label_gamma.pack(side   = 'top' ,padx=2)   
Entre_gamma.pack(side   = 'top' ,padx=2) 

Label_X0.pack(side      = 'top' ,padx=2)   
Entre_X0.pack(side      = 'top' ,padx=2) 

Label_V0.pack(side      = 'top' ,padx=2)   
Entre_V0.pack(side      = 'top' ,padx=2) 

Label_W0.pack(side      = 'top' ,padx=2)   
Entre_W0.pack(side      = 'top' ,padx=2) 

Label_WF.pack(side      = 'top' ,padx=2)   
Entre_WF.pack(side      = 'top' ,padx=2) 

bouton_recherche.pack(pady = 5)
bouton_recherche_entry.pack(pady = 5)

Mframe1.pack(side       = 'left',padx=2)
Mframe2.pack(side       = 'left',padx=2)
Mframe3.pack(side       = 'left',padx=2)
Mframe4.pack(side       = 'left',padx=2)
Mframe5.pack(side       = 'left',padx=2)


frame1.pack(ipady=10) 
frame2.pack(ipady=10) 
frame3.pack(ipady=10)

Repre1_bouton.pack(side = 'left',padx=10,pady=10) 
Repre2_bouton.pack(side = 'left',padx=10,pady=10)  
Repre3_bouton.pack(side = 'left',padx=10,pady=10)
Repre4_bouton.pack(side = 'left',padx=10,pady=10)
Repre5_bouton.pack(padx=10,pady=10)
app.mainloop()









