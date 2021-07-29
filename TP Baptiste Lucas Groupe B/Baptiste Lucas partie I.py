# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 14:28:21 2021

@author: lucas
"""

"""
tp4

partie I. Administration du répertoire
"""
#tkD.askopenfilename(title = "fichier à renommer",
                             #filetypes = [('ASCII file','.csv'),('all','.*')])
import os
import tkinter
import tkinter.filedialog as tkD
from tkinter import messagebox
import fnmatch

"""
mise en place de la fenêtre tkinter
"""
app = tkinter.Tk()
app.geometry("800x600")
app.title("Gestion de fichiers")

"""
mise en place des sous fenêtres
"""
frame1 = tkinter.LabelFrame(app,text = 'recherche fichier') #recherche
frame2 = tkinter.LabelFrame(app,text = "supression fichier d'extension .xXx")
frame3 = tkinter.LabelFrame(app,text = "changement de nom de fichier")
frame4 = tkinter.LabelFrame(app,text = "création de répertoire")
frame5 = tkinter.LabelFrame(app,text = "transfère de fichiers")



#%%
"""
setup des différents widget
"""

#%% quitter

def quitter(*args):
    app.quit()
    app.destroy()

Exit_bouton = tkinter.Button(app ,command= quitter, text='quitter')


#%% recherche du fichier


Fichier=[]
def nom_document(*args):    
    if Fichier == []:
        Fichier.append(tkD.askdirectory(title = "fichier à gérer"))   
        bouton_recherche_e.set(Fichier[0])
        
def clear1(*args):
    bouton_recherche_entry.delete(0,'end')    
    Fichier.remove(Fichier[0])
    messagebox.showinfo('clear','le zone de saisie est nettoyé')        
bouton_clear1    = tkinter.Button(frame1 ,command= clear1, text='clear')     
    
bouton_recherche_e     = tkinter.StringVar()
bouton_recherche       = tkinter.Button(frame1 ,
                                        command= nom_document ,
                                        text='recherche')
bouton_recherche_entry = tkinter.Entry(frame1, textvariable= bouton_recherche_e )



#%% supression de fichier avec certaines extensions  
       

"""
1)ASCII 
"""
label_extensions_e  = tkinter.StringVar()
bouton_supression_e = tkinter.StringVar()


def suppression_fichier_extension(*args):
    x=extension_entry_e.get()     
    z='*{0}'.format(x)
    
    try:
        nombre = 0
        for file1 in os.listdir(Fichier[0]):
             
            if fnmatch.fnmatch(file1, z):
                file2 = os.path.abspath(Fichier[0])  + '\\' + file1
                
                os.remove(file2)
                nombre = nombre + 1
        if (nombre > 0):
            messagebox.showinfo("Suppression de fichier",
                                "Les fichier '{}' ont bien été supprimés !".format(x))
        if (nombre == 0):
            messagebox.showerror("Suppression de fichier",
                                 "Il n'y a aucun fichier '{}' dans le dossier !".format(x))
    except:
        retrycancel = messagebox.askretrycancel("Erreur suppression de fichier",
                                                "Il y a eu une erreur pendant la suppresion des fichiers {} !".format(x))
        if retrycancel == True:
            suppression_fichier_extension()

bouton_suppression = tkinter.Button(frame2 ,
                                   command=suppression_fichier_extension  ,
                                   text='supprimer')       
  
extension_entry_e = tkinter.StringVar()
label_extensions  = tkinter.Label(frame2, textvariable=label_extensions_e)
extension_entry   = tkinter.Entry(frame2, textvariable = extension_entry_e)

label_extensions_e.set("Nom de l'extension :")


      
#%%  renommer des fichiers   


"""
2) renommer des fichiers 
""" 

Fichier_renommer=[]
def nom_document2(*args): 
   
    if Fichier_renommer == []:
        Fichier_renommer.append(tkD.askopenfilename(title = "fichier à renommer",
                             filetypes = [('ASCII file','.csv'),('all','.*')]))
        bouton_recherche_e2.set(Fichier_renommer[0])
    else:
        Fichier_renommer.remove(Fichier_renommer[0])
    messagebox.showinfo("info", "renommer le fichier dans la zone de saisie , puis cliquer sur 'Renommer'")
bouton_recherche_e2     = tkinter.StringVar()
bouton_recherche2       = tkinter.Button(frame3 ,command= nom_document2 , text='recherche')
bouton_recherche_entry2 = tkinter.Entry(frame3, textvariable= bouton_recherche_e2 )

def renommer(*args):
    x=bouton_recherche_e2.get()
    y=Fichier_renommer[0]
    os.rename(y,x)
    messagebox.showinfo('Renommer','le fichier à bien était renommé')
    
    
def clear3(*args):
    bouton_recherche_entry2.delete(0,'end')    
    Fichier_renommer.remove(Fichier_renommer[0])
    messagebox.showinfo('clear','le zone de saisie est nettoyé')
bouton_renommer = tkinter.Button(frame3 ,command= renommer , text='renommer')
bouton_clear3    = tkinter.Button(frame3 ,command= clear3, text='clear') 



#%% création et transfère de fichier


"""
3)création et transfère de fichier (utilise la premiére zone de recherche de répertoire, tout en haut)
"""  


var_label_nom_fichier = tkinter.StringVar()
bouton_creation_e     = tkinter.StringVar() 



creation=[]
def création_fichier(*args): 
    
    if Fichier == []:
        messagebox.showerror('Erreur!', 'Pas de chemin pour crée {}'.format(bouton_creation_entry.get()))
   
    else :
        creation.append(bouton_creation_entry.get())
        os.makedirs(Fichier[0]+'/'+creation[0])
        messagebox.showinfo('Création','Le fichier à bien était crée')
    
    
def clear4(*args):
    bouton_creation_entry.delete(0,'end')
    creation.remove(creation[0])
    messagebox.showinfo('clear','le zone de saisie est nettoyé')
        
label_nom_fichier     = tkinter.Label(frame4,textvariable=var_label_nom_fichier)    
bouton_clear4         = tkinter.Button(frame4 , command = clear4, text='clear')     
bouton_creation       = tkinter.Button(frame4 , command = création_fichier , text='création')
bouton_creation_entry = tkinter.Entry(frame4, textvariable= bouton_creation_e,)

var_label_nom_fichier.set('Nom du répertoire à créer :')


"""
transfère de fichier
"""


label_repertoir_cible_e      = tkinter.StringVar()
repertoir_cible_e            = tkinter.StringVar()
bouton_tranfere_e            = tkinter.StringVar()
label_transfere_extensions_e = tkinter.StringVar()
transfere_extension_entry_e  = tkinter.StringVar()
bouton_recherche_cible_e     = tkinter.StringVar()


repertoir_cible=[]

def repertoir_cible_f(*args): 
    messagebox.showinfo("attention", "le répertoire mère est celui selectionné tout en haut")
    if repertoir_cible == []:
        repertoir_cible.append(tkD.askdirectory(title = "fichier à transférer"))
        repertoir_cible_e.set(repertoir_cible[0])
        
def clear5(*args):
    repertoir_cible_entry.delete(0,'end')    
    repertoir_cible.remove(repertoir_cible[0])
    messagebox.showinfo('clear','le zone de saisie est nettoyé')        
bouton_clear5    = tkinter.Button(frame5 ,command= clear5, text='clear')         
    
def transfère_fichier_extension(*args):
    
    x=transfere_extension_entry_e.get()     
    z='*{0}'.format(x)
    
    try:
        nombre = 0
        for file1 in os.listdir(Fichier[0]):
             
            if fnmatch.fnmatch(file1, z):
                file2 = os.path.abspath(Fichier[0])  + '\\' + file1
                file3 = os.path.abspath(repertoir_cible[0])  + '\\' + file1
                os.replace(file2,file3)
                nombre = nombre + 1
        if (nombre > 0):
            messagebox.showinfo(title="Transfère de fichier",
                                message="Les fichier '{}' ont bien été transféré !".format(x))
        if (nombre == 0):
            messagebox.showerror(title="Transfère de fichier",
                                 message="Il n'y a aucun fichier '{}' dans le dossier !".format(x))
    except:
        retrycancel = messagebox.askretrycancel(title="Erreur transfère de fichier",
                                                message="Il y a eu une erreur pendent le transfère des fichier '{}' !".format(x))
        if retrycancel == True:
            transfère_fichier_extension()



        
bouton_recherche_cible_e     = tkinter.StringVar()
bouton_recherche_cible       = tkinter.Button(frame5 ,
                                              command= repertoir_cible_f , 
                                              text='recherche')
           
transfere_bouton             = tkinter.Button(frame5 , 
                                              command = transfère_fichier_extension ,
                                              text='transfère')   
         
label_transfere_extensions   = tkinter.Label(frame5,
                                             textvariable = label_transfere_extensions_e)
transfere_extension_entry    = tkinter.Entry(frame5, 
                                             textvariable = transfere_extension_entry_e)
repertoir_cible_entry        = tkinter.Entry(frame5,
                                             textvariable = repertoir_cible_e)
label_repertoir_cible        = tkinter.Label(frame5, 
                                             textvariable = label_repertoir_cible_e)

label_transfere_extensions_e.set("Nom de l'extension :")
label_repertoir_cible_e.set("  Répertoire cible :")



#%%

"""
4)production d'une liste 
"""

Liste_boite=[]
def Liste_repertoire(*args):
    x=bouton_recherche_entry.get()
    Liste_boite.append(os.listdir(x))
    
    for valeurs in Liste_boite[0]: 
        Liste.insert('end', valeurs)
        
        
scrollbar = tkinter.Scrollbar(app)
Liste=tkinter.Listbox(app)
Liste_creation=tkinter.Button(app,command=Liste_repertoire , text='Liste')
   

scrollbar.config(command = Liste.yview) 

def clear6(*args):
    Liste.delete(0,'end')    
    Liste_boite.remove(Liste_boite[0])
    messagebox.showinfo('clear','le zone de saisie est nettoyé')        
bouton_clear6    = tkinter.Button(app ,command= clear6, text='clear')         

#%% list des frames


frame1.pack(fill='x',padx=5)
frame2.pack(fill='x',padx=5)
frame3.pack(fill='x',padx=5)
frame4.pack(fill='x',padx=5)
frame5.pack(fill='x',padx=5)


#%%frame2

label_extensions.pack(side='left')
extension_entry.pack(side='left')
bouton_suppression.pack(side='left',pady= 5)


#%%frame1

bouton_recherche_entry.pack(padx=15,fill='x')
bouton_recherche.pack(pady=5)
bouton_clear1.pack()

#%%frame3

bouton_recherche2.pack(pady=5)
bouton_recherche_entry2.pack(padx=15,fill='x')
bouton_renommer.pack(pady=5)
bouton_clear3.pack(pady=5)


#%%frame4

label_nom_fichier.pack(side='left')
bouton_creation_entry.pack(side='left',padx=25,ipadx= 100,pady=5)
bouton_creation.pack(side='left',padx=25,pady=5)
bouton_clear4.pack(side='left',padx=25,pady=5) 


#%%frame5

label_transfere_extensions.pack(side='left')
transfere_extension_entry.pack(side='left',padx=5)
label_repertoir_cible.pack(side='left')
repertoir_cible_entry.pack(side='left',ipadx=20)
bouton_recherche_cible.pack(side='left',padx=5)
transfere_bouton.pack(pady=5, side='left')
bouton_clear5.pack(padx=5,side='left')

#%% main frame


Liste_creation.pack(side='left',padx=5)
Liste.pack(side='left', fill = 'y',pady=5)
scrollbar.pack(side='left', fill = 'y',pady=5)
bouton_clear6.pack(side='left')
Exit_bouton.pack(side="bottom",ipady= 10, ipadx=50)
app.mainloop()

