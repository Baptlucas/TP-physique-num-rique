# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 10:44:24 2021

@author: lucas
"""

import numpy as np 

def matrices_E_nm_nxm(U, all_E, all_p, x, dx):
    pn=np.array(all_p)
    nm=np.dot(pn, pn.T)*dx
    print('nm=\n',nm)
    pn1=pn*x
    nxm=np.dot(pn1, pn.T)*dx
    print('\nnxm=\n',nxm)#entre quel niveaux ont peut avoir émission de photons
    
    
    
    

def Aplus_Aminus(U, E, all_p, all_dpdx, x, dx):
    p=np.array(all_p)   
    dpdx=np.array(all_dpdx)
    n_a_moins_m=np.dot(p,(p*x+dpdx).T)*dx
    n_a_plus_m=np.dot(p,(p*x-dpdx).T)*dx
    print('\nna-m=\n',n_a_moins_m)#permet de passer à l'état inférieur opérateur d'anihilation
    print('\nna+m=\n',n_a_plus_m)#permet de passer à l'état suppérieur opérateur de création
    
    
    
    