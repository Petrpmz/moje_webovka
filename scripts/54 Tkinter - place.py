# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 11:37:21 2012

@author: Radek
"""
"""
Metoda place
Umožňuje umístění komponenty na konkrétní souřadnice:
a) Absolutní - v pixelech, počítá se z levého horního rohu
   place(x= , y= )
b) Relativní - v desetinných číslech, nejmenší hodnota je 0 a
               největší je 1
   place(relx= , rely= )

Můžeme přidat i parametr anchor, což je kotevní bod komponety.
Jsou tyto: "n", "ne", "e", "se", "s", "sw", "w", "nw", "center"
Možno použít i jako N, NE, E, ... (bez uvozovek)

POZOR! V jednom okně nelze kombinovat více zobrazovacích metod!
"""

# from tkinter import *

# hlavni = Tk()

# napis=Label(hlavni,text="Toto je text na abs. souřadnicích")
# napis.place(x=50, y=50, anchor="nw")

# napis2=Label(hlavni,text="Toto je text na relativních. souřadnicích")
# napis2.place(relx=0.5, rely=0.5, anchor="center")

# def Zmena():
#     tlacitko.place(x=200,y=200,width=150,height=80)

# tlacitko=Button(hlavni,text="Konec",command=Zmena)
# tlacitko.place(x=50,y=100,width=100,height=40)
   
# hlavni.mainloop()
"""
Úkol:
1) Stanovte si velikost okna.
   Umístěte do okna tři tlačítka "Konec" na náhodné 
   souřadnice tak, aby nepřekračovalo hranice okna.
   Přidejte tlačítko "Rozmístit" do levého horního rohu.
   Po jeho stisknutí se všem třem tlačítkům nastaví
   nové náhodné souřadnice.
"""   




from tkinter import *
import random

hlavni = Tk()
hlavni.geometry("1800x700")
hlavni.title("Random")

def Zmena():
    tlacitko1.place(anchor="nw",x=random.randint(100,1700),y=random.randint(50,650),width=100,height=50)
    tlacitko2.place(anchor="nw",x=random.randint(100,1700),y=random.randint(50,650),width=100,height=50)
    tlacitko3.place(anchor="nw",x=random.randint(100,1700),y=random.randint(50,650),width=100,height=50)
tlacitko=Button(hlavni,text="Rozmístit",command=Zmena)
tlacitko.place(width=100, height=50,anchor="nw")

tlacitko1=Button(hlavni,text="Konec", bg="blue",command=hlavni.destroy)
tlacitko2=Button(hlavni,text="Konec", bg="blue",command=hlavni.destroy)
tlacitko3=Button(hlavni,text="Konec",bg="blue", command=hlavni.destroy)
Zmena()

hlavni.mainloop()


















































