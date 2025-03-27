# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 10:27:03 2013

@author: Radek
"""
"""
Příkaz lambda
- převede cokoliv na funkci bez parametrů
- můžeme tak používat volání fcí s parametrem v tlačítku
"""

"""
Srovnání
def Fce
"""

from tkinter import *
from random import *

hlavni=Tk()


def Mocnina(x):
    print (x, "->", x*x)

tlac1 = Button(hlavni, text=u"Mocnina náhodného čísla",
               command=lambda:Mocnina(randint(1,10)))
tlac1.pack()

mainloop()



"""
Úkol:
1) Napište fci Obdelnik(a,b), která spočítá obvod 
   obdelníku a vypíše jej do Labelu v okně. 
   Tuto funkci spousťte pomocí tlačítka a parametry 
   dosaďte náhodné.
   Přidejte ještě Label s názvem aplikace a tlačítko 
   "Konec".
2) Přepište hru "Kámen, nůžky, papír" z loňského
   roku pomocí okna a tlačítek.
   Tlačítka budou volat společnou funkci Hra(symbol).

"""

