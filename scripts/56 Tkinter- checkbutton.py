# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:06:38 2012

@author: Radek
"""
# from tkinter import * 


# hlavni = Tk()
# v = IntVar() #BooleanVar()
# v.set(1)

# c = Checkbutton(hlavni, text="Přepínač", variable=v) 
# c.grid(row=0,column=1) 

# def tisk():
#     print (v.get())    
    
# tlacitko=Button(hlavni,text="Kontrola",command=tisk)
# tlacitko.grid(row=0,column=0)
 
# mainloop() 
"""
Úkol:
1) Vložte do okna 2 zaškrtávací políčka a tlačítko
   "Inverze", které invertuje u obou políček jejich
   nastavení.
   Nápověda: Využijeme operaci v.set()
"""   
from tkinter import * 


hlavni = Tk()
v = IntVar() #BooleanVar()
v.set(1)
e = IntVar() #BooleanVar()
e.set(1)

c = Checkbutton(hlavni, text="Přepínač", variable=v) 
c.grid(row=0,column=1) 
g = Checkbutton(hlavni, text="Přepínač", variable=e) 
g.grid(row=0,column=2) 

def inverzee():
    if e.get()== 0:
        e.set(1)
        if v.get()== 1:
            v.set(0)
        elif v.get()== 0:
            v.set(1)
    else:
        e.set(0)
        if v.get()== 1:
            v.set(0)
        elif v.get()== 0:
            v.set(1)

tlacitko=Button(hlavni,text="Inverze",command=inverzee)
tlacitko.grid(row=0,column=0)
 
mainloop() 