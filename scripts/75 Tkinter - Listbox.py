# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 08:44:03 2014

@author: Radek
"""

from Tkinter import *

hlavni = Tk()

ram=Frame(hlavni)
ram.pack()

scrollbar = Scrollbar(ram, orient=VERTICAL)
seznam=Listbox(ram,yscrollcommand=scrollbar.set)
seznam.pack(side=LEFT)
scrollbar.config(command=seznam.yview)
scrollbar.pack(side=RIGHT,fill=Y)

for i in [u"jedna", u"dva", u"tři", u"čtyři"]:
    seznam.insert(END, i)

seznam.insert(0, u"Pokusné vložení")

for i in range(50):
    seznam.insert(END, u"položka")

def Smazat():
    seznam.delete(0,0)   #smaze polozky s indexem od-do

tlac=Button(text="Smaz",command=Smazat)
tlac.pack()

hlavni.mainloop()

"""
Úkol:
1) Do aplikace umístěte Entry, Listbox a tlačítka "Vložit" a "Smazat".
   Postisku tlačítka "Vlozit" se do Listboxu vloží text z Entry.
   Totéž se provede i po stisku klávesy "Enter" v Entry.    
   Entry se následně samo smaže.
   "Smazat" smaže poslední položku.
"""   