# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 12:17:56 2012

@author: Radek
"""
"""
Parametry:
    state="readonly"/"disabled"/"normal" - čtení/nepřístupný

Metody:    
    delete() - smaže zvolený úsek řetězce v Entry
    insert() - vloží řetězec do Entry na zvolenou pozici
    Obě metody fungují jen ve stavu "normal"!!!
"""

from tkinter import *

hlavni=Tk()

vstup=Entry(hlavni,state="normal")
vstup.pack()

def Proved():
    vstup.delete(0,END)
    vstup["state"]="disabled"
    vstup.insert(0,"Přednastavený text")

tlacitko=Button(hlavni,text="Proveď",command=Proved)
tlacitko.pack()

mainloop() 



 





