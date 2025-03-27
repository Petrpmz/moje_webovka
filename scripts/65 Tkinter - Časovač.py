# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 09:54:43 2013

@author: Radek
"""
"""
Funkce after
- jedná se o časové zpoždění v milisekundách
- je to funkce hlavního okna, volá se tedy hl.after(...)
- po jeho uplynutí času se buď nestane nic (např. hl.after(1000))
- nebo se spustí požadovaná funkce (např. hl.after(1000,funkce))
"""

# from tkinter import messagebox
# from tkinter import *
# import random

# hlavni=Tk()
# hlavni.geometry("250x100")

# def Okno():
#     messagebox.showinfo("Hlášení","Proběhne prodleva 5000 ms") 
#     hlavni.after(3000)
#     hlavni.after(2000)
#     messagebox.showinfo("Hlášení","Proběl časový interval 5000 ms") 

# tlacitko=Button(hlavni,text="Test čekání programu",command=Okno)
# tlacitko.pack()


# def Funkce1():
#     print("Proběhla Funkce1")

# def Funkce2():
#     print("Proběhla Funkce2")

# def TestCasovace():
#     hlavni.after(4000,Funkce1)
#     hlavni.after(2500,Funkce2)

# tlacitko = Button(hlavni, text="Test souběžného spuštění", command=TestCasovace)
# tlacitko.place(relx=0.5, rely=0.5, anchor=CENTER)

"""
Úkol:
1) Každou sekundu změňte barevné pozadí hlavního okna
   na náhodnou barvu.


"""


from tkinter import messagebox
from tkinter import *
import random

hlavni=Tk()
hlavni.geometry("250x100")

def ZmenBarvu():
    hexaznaky = "0123456789ABCDEF"
    barva = "#"
    for i in range(6):
        barva += random.choice(hexaznaky)
    hlavni["bg"] = barva
    
    hlavni.after(1000, ZmenBarvu)

ZmenBarvu()
mainloop()

"""
2) Naprogramujte nastavitelný timer (odpočet), použijte 
   Spinbox. Stačí jeden Spinbox obsahující sekundy.
   Při stisku tlačítka Start se časovač spustí a 
   nepotřebné komponenty se nastaví na "disabled".
   Po uplynutí času se komponenty nastaví opět na 
   "normal".
"""


from tkinter import *
import random



hlavni = Tk()
hlavni.geometry("250x150")
hlavni.title("Časovač")


def starts():
    cas = int(spinbox.get())
    odp(cas)
    spinbox["state"]= "disabled"
    start["state"]= "disabled"
def konec():

    spinbox["state"]= "normal"
    start["state"]= "normal" 

def odp(cas):
    odpo["text"]=str(cas)
    if cas > 0:
        hlavni.after(1000, odp, cas - 1)  
    else:
        konec()

spinbox_label = Label(hlavni, text="Nastavte čas:")
spinbox_label.pack()

spinbox = Spinbox(hlavni, from_=1, to=300, width=5)
spinbox.pack()

start = Button(hlavni, text="Start", command=starts)
start.pack()

odpo = Label(hlavni, text="0")
odpo.pack()

hlavni.mainloop()


"""
0)
"""

from tkinter import *
import random



hlavni = Tk()
hlavni.geometry("1800x700")
hlavni.title("KOnec")

    
def pohyb():
    tlacitko1.place(anchor="nw",x=random.randint(100,1700),y=random.randint(50,650),width=100,height=50)
    hlavni.after(1000, pohyb)

tlacitko1=Button(hlavni,text="Konec", bg="blue",command=hlavni.destroy)

tlacitko1.place(anchor="nw",x=random.randint(100,1700),y=random.randint(50,650),width=100,height=50)
hlavni.after(1000, pohyb)

hlavni.mainloop()
