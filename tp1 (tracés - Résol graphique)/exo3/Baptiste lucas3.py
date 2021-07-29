# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 15:27:04 2021

@author: lucas
"""

import numpy as np
import matplotlib.pyplot as plt 
esp=np.spacing(1)
p = float(input('Emax=?'))

E_max = np.sqrt(p-2)

def fE(x,y,z):
    somca= x**2+y**2+z**2
    return somca

Nx,Ny,Nz = np.meshgrid(nx,ny,nz)