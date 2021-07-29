# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 14:18:19 2021

@author: lucas
"""
import my_fonction_fourier as fct
import numpy as np
import matplotlib.pyplot as plt
"""

simple somme de signaux sinusoïdaux

"""
plt.figure(figsize=(9,6), dpi=320)
t = np.linspace(-np.pi,np.pi,241)

y2Fourier = np.sin(t)-(1/2)*np.sin(2*t)

plt.plot(t, y2Fourier,label = 'y2Fourier')


t = np.linspace(-np.pi,np.pi,241)

y3Fourier = np.sin(t)-(1/2)*np.sin(2*t)+(1/3)*np.sin(3*t)

plt.plot(t, y3Fourier, label = 'y3Fourier')
#%%
"""

question: 3.1

"""
N=4

t = np.linspace(-np.pi,np.pi,241)

yFourier = sum([(-1)**(n+1)*np.sin(n*t)/n for n in range(1,N)])

plt.plot(t, yFourier,label = 'yFourier pour N=4')

N=90

t = np.linspace(-np.pi,np.pi,241)

yFourier = sum([(-1)**(n+1)*np.sin(n*t)/n for n in range(1,N)])

plt.plot(t, yFourier,label = 'yFourier pour N=90')


N=200

t = np.linspace(-np.pi,np.pi,241)

yFourier = sum([(-1)**(n+1)*np.sin(n*t)/n for n in range(1,N)])

plt.plot(t, yFourier,label = 'yFourier pour N=200')


g1=(1/2)*t

plt.plot(t,g1,'red',label = 'g1')
plt.title('somme de signaux sinusoïdaux')
plt.xlabel('t')

plt.legend()
plt.show()
#%%
"""

détermination des composantes d'un signal

"""
t = np.linspace(-np.pi,np.pi,1000)
M = np.trapz(np.sin(t), t)

N = np.trapz(t,np.sin(t)*np.sin(t))
plt.figure(figsize=(9,6), dpi=320)
plt.plot(t,np.sin(t)*np.sin(t),label='1')
plt.plot(t,np.sin(2*t)*np.sin(t),label = '2')

P = np.sin(t)*np.sin(t) - (1/2)*np.sin(2*t)*np.sin(t) +(1/3)*np.sin(3*t)*np.sin(t) - (1/4)*np.sin(4*t)*np.sin(t)
plt.plot(t,P,label = 'somme de plusieurs sinusoïdale')
plt.legend()

yFourier=sum([(-1)**(n+1)*np.sin(n*t)/n for n in [1,2,3,4]])
print([np.trapz(yFourier*np.sin(n*t),t)/np.pi for n in [1,2,3,4]])
#%%
"""
question 3.2 

"""
#%%
"""
question 3.3
"""
"""
3.3.a) sin^3(t))
"""
T = 2*np.pi
f1 = fct.Fstr2ft('np.sin(t)**3')
t = np.linspace(-1,1,242)*np.pi
plt.figure(figsize=(9,6),dpi=320)
plt.plot(t/T,f1(t),label='sinus au cube')
plt.legend()

(a0,an,bn) = fct.aNbN_de_Ft(f1,t,32)

y = fct.Ft_de_aNbN(t,bn=bn)
plt.plot(t,y,label='fonction reconstruite')
plt.legend()


plt.figure(figsize=(9,6),dpi=320)
n=np.linspace(0,7,8)
plt.grid()
plt.bar(n,a0,label='a0')
plt.bar(n,an,label='an')
plt.bar(n,bn,label='bn')
plt.legend()
plt.show() 











