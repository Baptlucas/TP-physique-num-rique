# -*- coding: utf-8 -*-

"""
my_fonctions_fourier.py
Functions for Fourier transformation and reconstruction
Created on Sat Jan 26 12:10:46 2019
@author: mIv
"""

import numpy as np
T = 2*np.pi

def Fstr2ft(fstr):
    """
    Transforms text (string) to Python function:
    fstr - text (string) containing Numpy expression of f(t)
    Returns: function f(t)

    Exemple:
        f1 = Fstr2ft('np.sin(t)**3')
        t = np.linspace(-1,1,242)*np.pi
        plt.plot(t,f1(t))

    mIv: 2019/01/26
    """
    # fstr should be in python numpy format
    def f(t): # Here this function is defined
        return eval(fstr)
    return f


def aNbN_de_Ft(f,t,N):
    """
    My function to calculate first N Fourier coefficients of F(t).
    Arguments:
        f - Python function f(t)
        t - Numpy array of t from -np.pi to +np.pi
        N - number of Fourier coefficients to calculate, should be N>=1.
    Returns a tuple containing a0, list of an and list of bn.

    Exemple:
        t = np.linspace(-1,1,242)*np.pi
        (a0,an,bn) = aNbN_de_Ft(np.sin,t,3)

    mIv: 2019/01/26
    """
    if N<1:
        print ('N<1 !!!')
        return 0

    a0 = np.trapz(f(t),t)/(2*np.pi)
    an = [np.trapz(f(t)*np.cos(n*t)/np.pi,t) for n in range(1,N+1)]
    bn = [np.trapz(f(t)*np.sin(n*t)/np.pi,t) for n in range(1,N+1)]

    return (a0,an,bn)


def Ft_de_aNbN(t,a0=0.0,an=[],bn=[]):
    """
    My function to reconstruct a function from given Fourier coefficients.
    Arguments:
        t - Numpy array of t from -np.pi to +np.pi
        aO, an, bn - Fourier coefficients
        a0 - float number
        an - a list of float numbers (can be a tuple or a Numpy array)
        bn - same as an

    Returns Numpy array of reconstructed f(t).

    Exemple:
        t = np.linspace(-1,1,242)*np.pi
        bn = [(-1)**(n+1)/n for n in range(1,7)]
        y = Ft_de_aNbN(t,bn=bn)
        plt.plot(t,y)

    mIv: 2019/01/26
    """
    yan = sum([a*np.cos((n+1)*t) for n,a in enumerate(an)])
    ybn = sum([b*np.sin((n+1)*t) for n,b in enumerate(bn)])
    return a0*np.ones(np.shape(t)) + yan + ybn