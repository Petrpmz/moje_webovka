# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:26:22 2013

@author: Radek
"""
# def Fce():
#     print("Výpis z funkce")

# print(Fce())   


from tkinter import *
from tkinter import messagebox

hl_okno=Tk()          # toto vytvoří hlavní okno

sez=[]

def ObsluhaTlacitka(x):
    messagebox.showinfo("Obsluha","Klikl jsi na tlačítko "+str(x))

for i in range(20):
    txt=StringVar()
    txt.set("Tlačítko "+str(i))
    b=Button(hl_okno,textvariable=txt,command=lambda x=i:ObsluhaTlacitka(x))
    sez.append(b)
    b.pack(fill=BOTH,expand=True)   

sez[13]["state"]=DISABLED


hl_okno.mainloop()


"""
Úkol:
0) Vykreslete tabulku 4x4 z komponent Entry.
"""
from tkinter import *

hl_okno=Tk()  


for y in range(4): 
    for x in range(4): 
        e=Entry(hl_okno)
        e.grid(row=y, column=x)

hl_okno.mainloop()

"""
1) Pomocí obdobného mechanismu vykreslete tabulku
   o 5-ti sloupcích a 10-ti řádcích složenou z komponent
   Entry + zmenšete jejich šířku. Použijte rozmístění Grid.

"""
from tkinter import *

hl_okno=Tk()  


for y in range(10): 
    for x in range(5): 
        e=Entry(hl_okno, width=5)
        e.grid(row=y, column=x,)

hl_okno.mainloop()
"""
2) Vložte do každého políčka jeho souřadnice.
"""
from tkinter import Tk, Entry

hl_okno = Tk()

for y in range(10):
    for x in range(5):
        e = Entry(hl_okno, width=5)
        e.insert(0, f"{y},{x}")  
        e.grid(row=y, column=x)

hl_okno.mainloop()
"""
3) Obarvěte políčka v každém řádku náhodnou barvou.
"""    
import random
from tkinter import Tk, Entry

hl_okno = Tk()

for y in range(10):
    random_color = f"#{random.randint(0, 255):02x}{random.randint(0, 255):02x}{random.randint(0, 255):02x}"
    for x in range(5):
        e = Entry(hl_okno, width=5)
        e.insert(0, f"{y},{x}")  
        e.grid(row=y, column=x)
        e["bg"]=random_color
hl_okno.mainloop()



