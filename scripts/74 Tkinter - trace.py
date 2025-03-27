# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 08:19:45 2014

@author: Radek
"""

from Tkinter import *

hlavni = Tk()
hlavni.title("Metoda trace")



cislo = IntVar()
cislo.set(1)

def tisk(*param):
    print cislo.get()
    print param

cislo.trace("w",tisk)

def Nastav():
    cislo.set(cislo.get()+1)    

tlac=Button(hlavni,text="Nastav proměnnou",command=Nastav)
tlac.pack()

"""
Úkol:
1) Zobrazte uživateli tři volby pomocí RadioButton.
   Při změně volby proveďte pomocí Trace změnu barvy pozadí.
"""    

hlavni.mainloop()