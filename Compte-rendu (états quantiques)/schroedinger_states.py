# -*- coding: utf-8 -*-
# schroedinger_statesA.py .versions A for auto search E, and file printing
# schroedinger_statesB.py -versions B help buttons and more comments
# mIv 24/01/2017; some modifications (B) 30/12/2017
# this file surves as ROOT (MENU) for other schroedinger files
# Animation of a mixed state 6/04/2019 - version C
# C2 - try import
"""
Finds stationary states of the Schroedinger equation
using technique of Feynman described in his course
of physics (§16.6) and studies their properties.
"""

import tkinter as tk # module of online control of Python
from tkinter import messagebox as tkm

# mpl.use('TkAgg')
import matplotlib as mpl
mpl.rcParams['mathtext.fontset'] = 'cm'
mpl.rcParams['mathtext.rm'] = 'serif'

import numpy as np
import matplotlib.pyplot as plt
plt.ion() # Turn interactive mode ON. ???


#%% Import functions containing parts of the program
try:
    from schroedinger_solveB_ebauche import schroedinger_solve # solve the schroedinger
# equation for given E and plot the solution.
#
# from schroedinger_solve import U # changed to an introduction of
# equations of U(x) trought tkinter menu
    eXistSolve = True
except ModuleNotFoundError as err:
    errText = ("Attention (no file):\n{:s}.\nStill to develop...".
                                                    format(str(err)))
    print('\n' + errText)
    # tkm.showinfo("No", errText)
    eXistSolve = False
except ImportError as err:
    errText = ("Attention (no function):\n{:s}.\nStill to develop...".
                                                    format(str(err)))
    print('\n' + errText)
    # tkm.showinfo("No", errText)
    eXistSolve = False

#
try:
    from schroedinger_matricesB import matrices_E_nm_nxm, Aplus_Aminus
# print matrices (particularly for harmonic oscilator U(x)=x**2/2)
# matrices_E_nm_nxm(): En, <n|m>, <n|x|m>
# Aplus_Aminus(): a_plus (creation), a_minus (annihilation)
    eXistMatrice = True
except ModuleNotFoundError as err:
    errText = ("Attention (no file):\n{:s}.\nStill to develop...".
                                                    format(str(err)))
    print('\n' + errText)
    # tkm.showinfo("No", errText)
    eXistMatrice = False
except ImportError as err:
    errText = ("Attention (no function):\n{:s}.\nStill to develop...".
                                                    format(str(err)))
    print('\n' + errText)
    # tkm.showinfo("No", errText)
    eXistMatrice = False
#
try:
    from schroedinger_animation import schroedinger_animation
# shcroedinger_animation.py
    eXistAnimate = True
except ModuleNotFoundError as err:
    errText = ("Attention (no file):\n{:s}.\nStill to develop...".
                                                    format(str(err)))
    print('\n' + errText)
    # tkm.showinfo("No", errText)
    eXistAnimate = False
except ImportError as err:
    errText = ("Attention (no function):\n{:s}.\nStill to develop...".
                                                    format(str(err)))
    print('\n' + errText)
    # tkm.showinfo("No", errText)
    eXistAnimate = False


def equations(): # to show possible equations: U(x) Label to Button # 30/12/2017
    """ Possible equations to replace initial U(x)=x**2/2
U(x)=x**2*2 # also harmonic, but more narrow potential #
U(x)=np.amin(np.vstack(((x-1.5)**2,(x+1.5)**2)),0)
    # two close harmonic potential wells for tunnel effect #
U(x)=np.amin(np.vstack(((x-1.5)**2,(x+1.5)**2+0.1)),0)
    # the same, but with left well less deep than right;
    tunneling ? #
U(x)=100*((x<-1)+(x>1)) # square potential well with
    "infinite" walls #
U(x)=100*np.all([[(x<-2.1)+(x>-.1)],[(x>2.1)+(x<.1)]],0)[0]
    # tunnel effect through the rectangular domain wall #
U(x)=100*np.all([[(x<-2.1)+(x>-.1)],[(x>3.1)+(x<.1)]],0)[0]
    # tunnel effect ?? #
#Shorter expression for the double weel:
U(x)=100*(abs(abs(x)-2)<1)
    # 1-width, 2-displacement from 0
    """
    print (equations.__doc__)
    tkm.showinfo("Info", equations.__doc__ +
                 "\nThe same info is printed in Console")


def U(x): # define the potential U(x)
    """
    Defines the function of the potential U(x) in Python's form
    to be obtained as u.get() and be used in schroedinger_solve()
    """
    return eval(u.get() ) # from the tkinter-Entry u
    # it is not a function of menu, just a function definition

def stop_button():
    """ Close the tkinter menu ("root.destroy()")
    version with "root.quit()" quit from Pyplot when used separately
    from the editor.
    """
    # root.quit()
    root.destroy()

def solve_button():
    """ Initialises parameters for schroedinger_solve() and starts it.
    """
    plt.close()
    global Energy
    global p, dpdx, x, dx
    Energy = e.get() # Energy in text form obtained from e = tk.Entry
    xmax = eval(y.get())[0] # to reduce or extend the interval of
    # calculations relatively to the visible [-4,4]
    # (first value from tuple entry y = tk.Entry)
    #
    # Solve the Schroedinger equation for given E (Energy)
    # and U(x) (potential)
    if eXistSolve:
        p, dpdx, x, dx, Energy = schroedinger_solve(Energy, U, xmax, auto.get() )
    else:
        print('\nAttention! No solution!')
    # p - np.array: the density of the probability amplitude p(x)
    # dpdx - np.array: the divergence of p(x) - dp(x)/dx
    # x - np.array: x from -xmax to +xmax with step dx
    # Energy - E value in the text format (evenually found authomatically)
    #
    # plt.draw()
    # auto.set(False) # Desactivate choise of "secret" auto solution
    engy.set(Energy) # Update the Energy value in case of auto solution
    # plt.show(block = False)

def add_button():
    """ Adds a new good solution (proper energy E and stationary state p(x))
    approved by the user (button 'Add') to matrices collecting all solutions
    and being used to calculate matrices (if initialased by another button
    'Matrix').
    Starts their presentation together in a synthetic graph (Figure 2)
    """
    global fg2
    global p, dpdx, x, dx
    global all_E, all_p, all_dpdx, all_align
    print("Add Energy", Energy)
    #%% Combine solutions together (lists of arrays)
    all_E += [Energy]
    all_p += [p]
    all_dpdx += [dpdx]
    # wher to put markers above ('bottom') or below ('top') E-line
    if position.get():
        all_align += ["bottom"]
    else:
        all_align += ["top"]
    #%% Plot a nice graph of all obtained states pn(x) and U(x)
    fg2 = plt.figure(2)
    plt.clf()   # clean axes in order to replot the graph each time
    plt.plot(x, U(x), '-k')  # plot potential energy
    for i, E in enumerate(all_E):
        # plot p(x) on the corresponding energy level E
        plt.plot(x, all_p[i]/2+float(E), '-b') # p/2 prevents overlapping
        plt.plot(x, np.ones(np.shape(x))*float(E), '--r') # E levels
        # plot energy value at the corresponding level
        # dictionary of text box properties
        box_props = {'boxstyle':'round',
                     'facecolor':'white',
                     'edgecolor':'none',
                     'alpha': 0.7 }
        plt.text(2.45, float(E), r'$E_{%i}='%(i,)+E+'$',
                                     # E as entered (text)
                 fontsize = 12,
                 bbox = box_props,
                 verticalalignment=all_align[i])

        # plot level number (state)
        plt.text(-3.9, float(E), r'$\left | %i \right\rangle $'%(i,),
                 fontsize = 12,
                 bbox = box_props,
                 verticalalignment=all_align[i])
    plt.draw_all()
    limits = eval(y.get())
    if np.size(limits) == 3:
        # zoom vertically the graph if limits are given
        plt.ylim(limits[1], limits[2])
    plt.xlim(-4,4) # x limits are always [-4,4]
    
    # axes labels
    plt.xlabel("$x$", fontsize = 12)
    plt.ylabel("$p_n(x)+E_n,\ U(x)$", fontsize = 12)
    plt.title(r"$U(x)= %s $"%(u.get() ),
              fontsize = 12) # show equation of U(x) in the graph title
    #
    plt.show(block = False) # demonstrate the graph and pass
    # plt.show()
    position.set(True)

def matrix_button():
    """ activate printing of matrices """
    global x, dx
    global all_E, all_p, all_dpdx
    if all_E == []: return False
    if eXistMatrice:
        matrices_E_nm_nxm(u.get(), all_E, all_p, x, dx)
        if u.get()[:4]=="x**2": # only for U(x) parabolic
            Aplus_Aminus(u.get(), all_E, all_p, all_dpdx, x, dx)
    else:
        print('\nAttention! No matrix!')
    
    return True

def clear_button():
    """ Removes stocked solutions to replot the final graph,
    lets change the equation of U(x), parameters of plot and calculations,
    or simply correct errors """
    global all_E, all_p, all_dpdx, all_align
    all_E = []
    all_p = []
    all_dpdx = []
    all_align = []

def anim_button():
    """ Animate probability distribution of a mixted state (pn+pm)
    n = z[0], m = z[1]"""
    global animator
    global x, dx
    global all_E, all_p, all_dpdx
    nm = eval(z.get())
    if eXistAnimate:
        animator = schroedinger_animation(nm,all_E,all_p,x,save.get())
    else:
        print('\nAttention! No animation!')
    save.set(False) # return to 'Don't Save Animation'

def help_button():
    """ This is an explanation of the tkinter menu from left to right:
    ° Button "U(x)=" gives some examples of potential energy
    U(x) to be entered in the next field.
    ° Entry field for U(x) in Python form.
    ° Entry field after Label "E=" is to introduce a guess
    value of energy E, which is printed in the final graph
    (Figure 2) exactly as given. While approaching the good
    solution user gradually increase precision of E in this
    field. If auto solution mode is available this entry
    field is automatically updated with a maximal precision
    of 7 digits after comma.
    ° Button "Solve" initialise solution of Schroedinger
    equation with given energy value E. In the auto mode
    E is modified to find good solution (no divergence at
    the end).
    ° Checkbox (checkbutton) is to activate the auto mode
    if available.
    ° Button "Add" adds a new good solution to allready
    found ones and updates the final graph (Figure 2).
    ° Entry of tupple with maximum 3 values
    (solution_interval, low_E, hig_E) where 2nd and 3d
    values are optional - initially the tuple is (4.0,);
    [-solution_interval,+solution_interval] is to reduce
    it from initial [-4,+4], when solution becomes difficult,
    or to increase it in order to increase the precision;
    the interval x in Figure 2 is always [-4,+4].
    ° Button "Matrix" is to print vector En and matrices
    <n|m>, <n|x|m>, <n|a+|m> and <n|a-|m>  (also to file
    "schroedinger_matrices.txt") and plot in Figure 1
    a result of a-|0> (a+ and a- are operators of creation
    and annihilation)
    ° Button "Clear" clears all saved solution and lets
    recalculate and replot Figure 2 after changing of U(x),
    or simply an error..
    ° Button "Animate" starts animation of mixed states
    indicated in the next tuple.
    ° Entry of tuple with numbers of states to be mixed
    for animation - default value is (0,1).
    ° Checkbox following this is to save the animation in
    the file mixed_stateNM(t).gif, where N and M are given
    by the preceding tuple.
    ° Button "STOP" (red) is an exit from the program; all
    values are lossed.
    ° Button "Help" is this help text.
    """
    tkm.showinfo("Info", help_button.__doc__)
    # print (help_button.__doc__)

#%% START tk
root = tk.Tk()      # starts tkinter root
root.title("mIv 2017-2019") # title of tkinter menu

auto = tk.BooleanVar() # tk variables
engy = tk.StringVar()
save = tk.BooleanVar() # save animation
position = tk.BooleanVar() # True - above, False below

all_E = [] # empty lists to stock results
all_p = []
all_dpdx = []
all_align = []

# tk.Label(root, text = "U(x) = ").pack(side = tk.LEFT) # for the next Entry
# this Label is replaced by the following Button
button = tk.Button(root, text = "U(x) = ",
                   command=equations).pack(side = tk.LEFT)

u = tk.Entry(root,
             width = 30,
             justify=tk.LEFT) # to enter an equation of U(x)
u.pack(side = tk.LEFT)
u.insert(10, "x**2/2") # default is the harmonic U(x)=x**2/2


tk.Label(root, text = "E = ").pack(side = tk.LEFT) # label for next Entry

e = tk.Entry(root, textvariable = engy,
             width = 11,
             justify=tk.LEFT,
             font = "Verdana 14") # enters Energy (E) in text format
#e.grid(row = 0, column=1)
e.pack(side = tk.LEFT)
e.insert(10, "0.51")  # default value is near to the ground level of
                      # the default U(x)=x**2/2

# Button to start the solution of Schroedinger equation
button = tk.Button(root, text='Solve',
                   width=10,
                   command=solve_button).pack(side = tk.LEFT)

# Checkbox to activate automatic adjustement of E
tk.Checkbutton(root, variable=auto,
               text="auto").pack(side = tk.LEFT)

# Button to accumulate obtained GOOD solution and plot the nice graph
button = tk.Button(root, text='Add',
                   width=10,
                   command=add_button).pack(side = tk.LEFT)

y = tk.Entry(root,
             width = 10,
             justify=tk.CENTER) # enter limits: (xmax, y_low, y_high)
y.pack(side = tk.LEFT)
y.insert(10, "(4.0,)") # default is only xmax with y-limits auto

# Checkbox to indicate where to put the markers, above or below E-lines
ChP = tk.Checkbutton(root, variable = position,
                     text = "up/down").pack(side = tk.LEFT)
position.set(True)

# Button to plot matrices mostly useful for U(x)=x**2/2
button = tk.Button(root, text='Matrix',
                   width=10,
                   command=matrix_button).pack(side = tk.LEFT)
# Button to clear accumulated solutions and restart the nice graph
button = tk.Button(root, text='Clear',
                   width=10,
                   command=clear_button).pack(side = tk.LEFT)

button = tk.Button(root, text='Animate',
                   width=10,
                   command=anim_button).pack(side = tk.LEFT)

z = tk.Entry(root,
             width = 6,
             justify=tk.CENTER) # enter limits: (xmax, y_low, y_high)
z.pack(side = tk.LEFT)
z.insert(10, "(0,1)") # default is only xmax with y-limits auto

# Checkbox to save animation of a mixed state
tk.Checkbutton(root, variable=save, text="save").pack(side = tk.LEFT)

button = tk.Button(root, text='Help',
                   width=10,
                   command=help_button).pack(side = tk.RIGHT)

# Button to quit the program (tkinter loop)
button = tk.Button(root, text='STOP',
                   width=10, fg = 'red',
                   command=stop_button).pack(side = tk.RIGHT)

root.mainloop() # start tkinter loop
#%% FINISH tk-loop




