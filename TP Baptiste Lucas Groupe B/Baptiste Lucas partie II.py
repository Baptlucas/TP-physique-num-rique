# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 16:45:10 2021

@author: lucas
"""


import matplotlib.pyplot as plt
import tkinter 
import tkinter.filedialog as tkD
from tkinter import messagebox
from math import sqrt



axis_font = {'fontname':'Arial','size':'8','color':'black'}  

#%% setup de la fenêtre

app=tkinter.Tk()
app.geometry("600x200")
app.title("representation graphique")
#%%frames

frame1=tkinter.LabelFrame(app,text = 'rechercher un fichier')


#%% widget pour quitter

def Quitter_F(*args):
    app.quit()
    app.destroy()
      
Quitter_e=tkinter.StringVar()
Quitter=tkinter.Button(app, command=Quitter_F, text='Quitter')


#%%recherche de fichier


Fichier=[]

def nom_document(*args):    
    if Fichier == []:
        Fichier.append(tkD.askopenfilename(title = "fichier à gérer",filetypes = [('all','.*')])) 
        bouton_recherche_e.set(Fichier[0])
        
    else:
        Fichier.remove(Fichier[0])
    print(Fichier)
bouton_recherche_e     = tkinter.StringVar()
bouton_recherche       = tkinter.Button(frame1 ,command= nom_document , 
                                        text='recherche')
bouton_recherche_entry = tkinter.Entry(frame1, 
                                       textvariable= bouton_recherche_e )

#%% supression des données inutiles

MG20=[];MG10=[];MG7=[];MG5=[];MG3=[];MG0=[]
ZN0=[];ZN10=[];ZN13=[];ZN15=[];ZN17=[];ZN20=[]
List2=[]  
#Fichier2=["Fx0 - Copie.xyz","Fx10 - Copie.xyz","Fx13 - Copie.xyz","Fx15 - Copie.xyz","Fx17 - Copie.xyz","Fx20 - Copie.xyz"]
List_entier=['#20','#21','#22','#23','#24','#25','#26']
oxy=[]
Centre=[]
MG_plot=[MG20,MG10,MG7,MG5,MG3,MG0]
ZN_plot=[ZN0,ZN10,ZN13,ZN15,ZN17,ZN20]

MG=[]
ZN=[]

O=[]

def entré_fichier(*args):
    
        with open(Fichier[0]) as Fich:
            lines = [line.strip('\n') for line in Fich.readlines()]
        
      
        for line in lines:
            F=line.split()
            List2.append(F)
        #print(List2)    


        List_entier1=['#20','#21','#22','#23','#24','#25','#26']
        for t in range(0,len(List2)):    #supression des liste vides et des liste de la forme [#*]
            Ligne=[]
            if Ligne in List2:
                List2.remove(Ligne)  
        for t in range(0,7):
            Ligne2=[List_entier1[t]]
            if Ligne2 in List2 :
                List2.remove(Ligne2) 
        #print(List2)
        
    



#%%traitement des données

        """
        determination des atomes centraux ,atomes oxygénes, atomes de magnésium et atomes de zinc
        """
    
        
    
        List_entier=[20,21,22,23,24,25,26]
  
        for t in range(0,len(List2)):
            List_t=List2[t] 
            print(List_t)
            if List_t[0]!='O':      #determination de la norme
                x=int(float(List_t[1]))
                y=int(float(List_t[2]))
                z=int(float(List_t[3]))
                norme = sqrt(x**2+y**2+z**2)
                
                #print(norme)
        
            for n in range(0,7):    #determination des valeur de Fukui des atomes centraux
            
                
                if int(List_t[5]) == List_entier[n] and norme == 0:
                    Centre.append(float(List_t[4]))           
                
                
            if List_t[0] =='O':     #determination des valeur de Fukui des atomes d'oxygénes
               O.append(float(List_t[4]))
        #print((O))             
        oxy.append((sum(O[0:1]))/1)
        oxy.append((sum(O[1:3]))/2)
        oxy.append((sum(O[3:6]))/3)
        oxy.append((sum(O[6:10]))/4)
        oxy.append((sum(O[10:15]))/5)
        oxy.append((sum(O[15:21]))/6)
        #print (oxy)
        #print(List2)
        for t in range(0,len(List2)): 
            List_t=List2[t]
            if List_t[0] == 'Mg' :
                MG.append(float(List_t[4]))
            elif List_t[0] == 'Zn' :
                ZN.append(float(List_t[4]))

        if len(MG) == 140 :              
           for x in range(0,140,20):    
                MG20.append((sum(MG[x:x+20]))/20)
        
        if len(ZN) == 140 :              
            for x in range(0,140,20):    
                ZN20.append((sum(ZN[x:x+20]))/20)

        if len(MG) == 70 :              
            for x in range(0,70,10):    
                MG10.append((sum(MG[x:x+10]))/10)
                ZN10.append((sum(ZN[x:x+10]))/10)
        
        if len(MG) == 49 :              
            for x in range(0,49,7): 
                MG7.append((sum(MG[x:x+7]))/7)
            for y in range(0,91,13):            
                ZN13.append((sum(ZN[y:y+13]))/13)
        
        if len(MG) == 35 :     
            Centre.append(0.0276)
            Centre.append(0.00553)
            Centre.append(0.02297)
            Centre.append(0.0105)
            Centre.append(0.0299)
            Centre.append(-0.0003)
            Centre.append(0.0202)
            for x in range(0,35,5): 
                MG5.append((sum(MG[x:x+5]))/5)
            for y in range(0,105,15):            
                ZN15.append((sum(ZN[y:y+15]))/15)
        
        if len(MG) == 21 :              
            for x in range(0,21,3): 
                MG3.append((sum(MG[x:x+3]))/3)  
            for y in range(0,119,17):             
                ZN17.append((sum(ZN[y:y+17]))/17)
        #print(List2)        
  
def clear(*args):
    TOTALE=[MG,ZN,List2,O,oxy,Centre,ZN0,ZN10,ZN13,ZN15,ZN17,ZN20,MG20,MG10,MG7,MG5,MG3,MG0]
    for n in TOTALE:
        if n != []:
            for t in range(0,len(n)):
                n.remove(n[0])
                
            
            """    
    Actions que fait la fonction clear:
        
    for t in range(0,len(MG)):
        MG.remove(MG[0])    
    for t in range(0,len(ZN)):
        ZN.remove(ZN[0])      
    for t in range(0,len(List2)):
        List2.remove(List2[0])
    for t in range(0,len(Normes)):
        Normes.remove(Normes[0])
    for t in range(0,len(O)):
        O.remove(O[0])    
    for t in range(0,len(oxy)):
        oxy.remove(oxy[0])
    for t in range(0,len(Centre)):
        Centre.remove(Centre[0])        
    for t in range(0,len(MG20)):
        MG20.remove(MG20[0])
        ZN20.remove(ZN20[0])
    for t in range(0,len(MG10)):
        MG10.remove(MG10[0])
        ZN10.remove(ZN10[0])
    for t in range(0,len(MG7)):
        MG7.remove(MG7[0])
    for t in range(0,len(MG5)):
        MG5.remove(MG5[0])
    for t in range(0,len(MG3)):
        MG3.remove(MG3[0])
    for t in range(0,len(ZN17)):
        ZN17.remove(ZN17[0])
    for t in range(0,len(ZN15)):
        ZN15.remove(ZN15[0])
    for t in range(0,len(ZN13)):
        ZN13.remove(ZN13[0])    
        """        
    #print (ZN13) 
    #print (MG7)
    
    
    messagebox.showinfo('clear','le zone de saisie est nettoyé')  
    
bouton_clear    = tkinter.Button(frame1 ,command= clear, text='clear')       
#%%représentation graphique

Nb_oxy=[0,1,2,3,4,5,6]
titres=['$Mg_{20}$','$Zn_{10}$ $Mg_{10}$','$Zn_{13}$ $Mg_{7}$','$Zn_{15}$ $Mg_{5}$','$Zn_{17}$ $Mg_{3}$','$Zn_{20}$']  
 
  
def repésentation_graph(*args):
       
    print(List2)
    plt.plot(Nb_oxy[1:7],oxy, 'g-o',label='f(oxygéne)')
    plt.plot(Nb_oxy[0:7],Centre, 'k:s',label='f(atomes centraux)')
    if len(MG) == 140 : 
            plt.plot(Nb_oxy[0:7],MG_plot[0], 'r-o',label='Mg')
            plt.title('$Mg_{20}$')
            
            
    if len(MG) == 70 : 
            plt.plot(Nb_oxy[0:7],MG_plot[1], 'r-o',label='f(Mg)')
            plt.plot(Nb_oxy[0:7],ZN_plot[1], 'k-o',label='Zn')
            plt.title('$Zn_{10}$ $Mg_{10}$')
            
    if len(MG) == 49 : 
            plt.plot(Nb_oxy[0:7],MG_plot[2], 'r-o',label='f(Mg)')
            plt.plot(Nb_oxy[0:7],ZN_plot[2], 'k-o',label='f(Zn)')
            plt.title('$Zn_{13}$ $Mg_{7}$')
            
    if len(MG) == 35 : 
            plt.plot(Nb_oxy[0:7],MG_plot[3], 'r-o',label='f(Mg)')
            plt.plot(Nb_oxy[0:7],ZN_plot[3], 'k-o',label='f(Zn)')
            plt.title('$Zn_{15}$ $Mg_{5}$')
           
    if len(MG) == 21 : 
            plt.plot(Nb_oxy[0:7],MG_plot[4], 'r-o',label='f(Mg)')
            plt.plot(Nb_oxy[0:7],ZN_plot[4], 'k-o',label='f(Zn)')
            plt.title('$Zn_{17}$ $Mg_{3}$')
            
    if len(ZN) == 140 :                         
            plt.plot(Nb_oxy[0:7],ZN_plot[5], 'k-o',label='f(Zn)')   
            plt.title('$Zn_{20}$')
    plt.xlabel('Nombre oxygène')
    plt.ylabel('f(e)')
    plt.ylim(0,0.07,0.005)                                       
    plt.legend()     
    plt.show()  
    
bouton_repesentation_graph       = tkinter.Button(frame1 ,command= repésentation_graph , 
                                        text='représentation graphique des data')      
bouton_traitement       = tkinter.Button(frame1 ,command= entré_fichier , 
                                        text='traitement data')  


#%%pack des frames

frame1.pack(fill='x',padx=10,ipady= 3)

#%%pack des différents widgets

bouton_recherche_entry.pack(fill='x',padx=10)
bouton_recherche.pack(pady=5)
bouton_traitement.pack()
bouton_clear.pack()
bouton_repesentation_graph.pack()

Quitter.pack(side='bottom')   
app.mainloop()    
    
    
    
    
    
    
    
    

    
    