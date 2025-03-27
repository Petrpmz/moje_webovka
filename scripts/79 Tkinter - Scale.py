# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 11:52:05 2013

@author: Radek
"""

from tkinter import *

hlavni=Tk()

hodnota=IntVar()
hodnota.set(100)

def Nastav(value):
    l["text"]=str(value)

w = Scale(from_=0, to=1000, variable=hodnota,command=Nastav, label="Stupnice")
w.pack()
l= Label(hlavni,text="0")
l.pack()





mainloop()

"""
Úkol:
1) Pomocí tří posuvníků s rozsahem (0-255) a tlačítka
   nastavte barvu komponenty Frame.
2) Přidejte tlačítko, které nastaví na posuvnících
   náhodnou barvu.
"""   