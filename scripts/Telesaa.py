# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 08:23:59 2012

@author: Martin
"""

"""          MODULY (knihovny)
Použití:
    1) import modul  -> modul.funkce()
    2) import modul as m -> m.funkce()
    3) from modul import * -> funkce() 
       - POZOR, může dojít k přepsání importovaných
       proměnných nebo fcí, pokud se v importovaných
       modulech jmenují stejně

Vlastní moduly:
    = obyčejné soubory s příponou *.py
    - při spuštění vznikne soubor *.pyc
    - z modulu můžeme použít globální proměnné a
    funkce
"""
"""
import mujsoubor
- příkazy -> provedou
- proměnné -> můžu je použít
- funkce (podprogramy) -> můžu je volat (spouštět)
"""

PI = 3.141

def PovrchKoule(r):
    return (4*PI*r**2)
import math
"""
Úkoly:
    Vytvořte modul Telesa, ve kterém budou k
    dispozici tyto funkce pro výpočet objemů a povrchů:
    1) ObjemKrychle(a)
"""
def ObjemKrychle(a):
    objem = a*a*a
    return objem

strana_krychle = 5
objem = ObjemKrychle(strana_krychle)
print("Objem krychle s hranou délky", strana_krychle," je ",objem)
"""
    2) PovrchKrychle(a)
"""
def povrch_krychle(a):
    povrch= 6*a**2
    return povrch
povrch = povrch_krychle(strana_krychle)
print("Povrch krychle s hranou délky", strana_krychle," je ",povrch)
"""
    3) ObjemKvadru(a,b,c)
"""
def objem_kvadru(a,b,c):
    objemk= a*b*c
    return objemk
akvadr = 5
bkvadr = 6
ckvadr = 7
objemk = objem_kvadru(akvadr,bkvadr,ckvadr)
print("Objem kvadru je ",objemk)
"""
    4) PovrchKvadru(a,b,c)
"""
def povrch_kvadru(a,b,c):
    povrchk= 2*a*b+2*b*c+2*c*a
    return povrchk
povrchk = povrch_kvadru(akvadr,bkvadr,ckvadr)
print("Povrch kvadru je ",povrchk)
"""

    5) ObjemJehlanu (a,v)
    6) PovrchJehlanu (a,v)
"""    







