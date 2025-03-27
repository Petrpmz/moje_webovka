# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:01:49 2013

@author: Radek
"""
"""
Množství otevřených oken je možno regulovat pomocí globální 
proměnné.
"""

from tkinter import *

hlavni=Tk()
hlavni.minsize(300,150)
hlavni.title("Hlavní okno")
pocet=0

def ZavriOkno():
    global okno
    global pocet    
    pocet=0
    okno.destroy()    

def ZobrazOkno():
    global okno
    global pocet
    if pocet==0:
        okno=Toplevel()
        okno.minsize(300,100)
        pocet+=1
        okno.title("Vedlejší okno")
        
        tlZavriOkno=Button(okno,text="Zavři okno",command=ZavriOkno)
        tlZavriOkno.pack()
    okno.protocol("WM_DELETE_WINDOW",ZavriOkno)

tlac1 = Button(hlavni, text="Zobraz podokno",command=ZobrazOkno)
tlac1.pack()

mainloop()

