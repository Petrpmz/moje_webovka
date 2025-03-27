# -*- coding: utf-8 -*-
"""
Created on Mon Sep 15 11:50:02 2014

@author: Radek
"""

"""
Opakovací úkoly:
1) Načtěte z klávesnice délku řádku a
   vypište pomocí cyklu FOR hvězdičky
   dle vzoru.
   Př:
   Zadej číslo: 6
   6: ******     
   """
# delka=int(input("Napište délku řádku"))
# for i in range(delka):
#   print("*", end="")

"""


2) Načtěte počet řádků a vypište diagram
   z náhodně dlouhých řádků.
   Př:
   Zadej počet řádků: 3
   2: **
   7: *******
   4: ****    

"""
# import random
# pocetradku=int(input("Napište počet řádku:"))
# for i in range(pocetradku):
#     delka = random.randint(1, 10) 
#     radek = "*" * delka
#     print(delka,":",radek)
"""

3) Načítejte postupně řadu čísel ukončenou
   hodnotou -1. Čísla budou vždy minimálně
   dvě a budou zadána korektně. Použijte 
   cyklus WHILE. Vypište 2. nejmenší číslo
   z řady.
"""
# prvni= int(input("zadej číslo:"))
# druhe= int(input("zadej číslo:"))
# if prvni>druhe:
#   prvni,druhe= druhe,prvni
# while True:
#   vstup = int(input("Zadej číslo:"))
#   if vstup<=prvni:
#     druhe=prvni
#     prvni=vstup
#   elif vstup < druhe:
#     druhe=vstup
# print("Druhe nejmensi cislo je:", druhe)

"""
    
4)Slovníky 
	Založte slovník ZBOZI a vypište jej: 
  {"chleb":30, "maslo":36, "mleko":17}
  Cyklem for zdražte ve slovníku všechno 
  zboží o 5 kč. 
  Cyklem vypište celý slovník takto:
    Slovník zboží:
    chleb: 35 Kc
    maslo: 41 Kc
    mleko: 22 Kc
"""
# Zbozi={"chleb":30, "maslo":36, "mleko":17}

# for i in Zbozi:
#   Zbozi[i]+=5
# for i in Zbozi:
#   print(i,":",Zbozi[i], "Kč")
"""
5)Funkce
  Napište funkci GenerujHeslo(delka),
  která vrátí náhodné heslo dané délky.
  Heslo se může skládat z malých a velkých
  písmen a z číslic. 
  
  Př: GenerujHeslo(5) -> aB8xu
"""

"""
6)Graf
  Zobrazte graf funkce y=sin(3*x)-3*cos(x).
  Přidejte popisky os a název grafu.    
"""
import pylab as p
x=p.arange(1,15,0.1)
y1=p.sin(3*x)-3*p.cos(x)
p.plot(x,y1,"r-o",label="y=sin(3*x)-3*cos(x)")
p.legend(loc="upper center")
p.show()

"""
7)Formát řetězce
  Vygenerujte náhodnou registrační značku vozidla.
  Na první pozici nesmí být 0, ostatní číslice mohou
  nulu obsahovat. (např. 2M0 4012)

8)Seznamy
  Nadefinujte si seznamy A a B. Budeme je chápat
  jako množiny. Vytvořte seznam PRUNIK, který
  bude obsahovat průnik obou množin. Tedy všechny
  hodnoty, které se vyskytují jak v A tak v B.
  Seznam PRUNIK setříděte a vypište.

9) Soubory
Načtěte si obsah souboru "lide.txt". Na každém 
řádku je uvedeno toto: "jméno;příjmení;email".
Pomocí funkce split() si vytáhněte jednotlivé
části řádku a vytvořte z nich do výstupního 
souboru "lide.html" HTML tabulku.

10) Soubory
V souboru vstup.txt je na každém řádku několik
čísel oddělených mezerami. Počet není upřesněn.
Počet řádků též není upřesněn. Na každém řádku
je minimálně jedno číslo.
Vytvořte soubor vystup.txt, kde na každém řádku
bude součet hodnot ze stejného řádku ve vstupním
souboru.

"""

# min1 = int(input("Zadej číslo:"))
# min2 = int(input("Zadej číslo:"))
# if min2 < min1:
#   min1, min2 = min2, min1  
 
# while True:
#   vstup = int(input("Zadej číslo:"))
#   if vstup == -1:
#     break  
#   if vstup < min1:
#     min2 = min1
#     min1 = vstup
#   elif vstup < min2:
#     min2 = vstup

# print("Druhé nejmenší číslo je:", min2)

















# pocet = int(input("Zadej počet hvězdiček:"))
# print(str(pocet)+": ", end="")
# for i in range(pocet):
#     print("*",end="")
# print()















# import random
# pocet = int(input("Zadej počet řádků:"))
# for i in range(pocet):
#     delka = random.randint(1,15)
#     print(str(delka) + ":", delka * "*")


















# vstup = 0
# nejmensi = int(input("Zadej číslo: "))
# druhe_nejmensi = int(input("Zadej číslo: "))

# if druhe_nejmensi < nejmensi:
#   nejmensi, druhe_nejmensi = nejmensi, druhe_nejmensi

# while True:
#   vstup = int(input("Zadej číslo: "))
#   if vstup == -1:
#     break
#   if vstup < nejmensi:
#     druhe_nejmensi = nejmensi
#     nejmensi = vstup 
#   elif vstup < druhe_nejmensi:
#     druhe_nejmensi = vstup 

# print("Druhé nejmenší číslo je", druhe_nejmensi