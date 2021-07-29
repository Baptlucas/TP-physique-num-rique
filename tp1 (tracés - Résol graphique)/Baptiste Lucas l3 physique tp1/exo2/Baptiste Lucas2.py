# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:12:10 2021

@author: lucas
"""

"""
résolution d'équation non linéaire
"""

from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
eps = np.spacing(1)#zéro machine
x = np.linspace(0,5,1000)
m = np.tanh(x) 

plt.figure(figsize=(10,6), dpi=100)

plt.plot(x,m,label="tanh") 


"""
2.1)Résolution graphique
"""

for t in (0.25, 0.5, 0.75, 1, 1.25, 1.5):
    y = t*x
    plt.plot(x,y,label="t="+str(t))
    plt.legend()
    
plt.title("tangente hyperbolique")
plt.ylabel("f(x) ")#"et t*x")
plt.xlabel("x")
plt.ylim(0,1.2)
plt.show
"""
2.2) Résolution numérique
    
solution m1 pour t=0.5
"""
t=0.5
def g1(m,t):
    """
    
    Parameters
    ----------
    m : aimantation normalisée.
    t : Température normalisée. The default is 0.5.

    Returns
    -------
    y : TYPE
        DESCRIPTION.

    """
    y = np.tanh(m/t)-m
    return y

x_ini = 1
m1 = fsolve(g1,x_ini,args=(t))
print('m1 =',m1)

"""
solution m2 pour t=0.9
"""
t=0.9
def g2(m,t):
    """
    

    Parameters
    ----------
    m : aimantation normalisée.
    t : Température normalisée. The default is 0.9.

    Returns
    -------
    y : TYPE
        DESCRIPTION.

    """
    y = np.tanh(m/t)-m
    return y
m_ini = 1
m2 = fsolve(g2,m_ini,args=(t))
print('m2 =',m2)

def g0(m,t2):
   
    y = np.tanh(m/t2)-m
        
    return y 

M=[]
x= np.linspace(0,10,1)     
t2=np.arange(0.1,1.1,0.1) 
for t2 in np.arange(0.1,1.1,0.1):
       
    m0_ini = 1
    m0 = fsolve(g0,m0_ini,args=(t2))
    M.append(m0)
t2=np.arange(0.1,1.1,0.1)     
plt.figure(figsize=(10,6), dpi=100)
plt.subplot(1,2,1)  
plt.plot(t2,M)
plt.scatter(t2,M)
plt.title('solutions $m_{0}$ et fonction de $t_{2}$')
plt.xlabel('$m_{0}$')
plt.ylabel('$t_{2}$')

plt.subplot(1,2,2)

x = np.linspace(0,5,1000)
m = np.tanh(x)
plt.plot(x,m,label="tanh")

for t in (0.25, 0.5, 0.75, 1, 1.25, 1.5):
    y = t*x
    plt.plot(x,y,label="t="+str(t))
    plt.legend()
  
plt.title("tangente hyperbolique")
plt.ylabel("f(x) ")#"et t*x")
plt.xlabel("x")
plt.ylim(0,1.2)
plt.show













     

