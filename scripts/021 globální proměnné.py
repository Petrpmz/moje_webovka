# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 12:19:13 2014

@author: Radek
"""
"""
Globální a lokální proměnné
- proměnné definované uvnitř funkcí, jsou tzv. 
  lokální = po skončení funkce přestanou existovat
- global x = definice globální proměnné x (existuje po 
  celou dobu trvání programu)   
- pokud chceme uvnitř funkce zapisovat do globální 
  proměnné, musíme před ni napsat global
- jestliže tato proměnná existovala, napojí se na ni,
  jinak se založí nová globální proměnná
"""


# def funkce1():
#     x=10      #vznik lokální proměnné
#     print (x)   #tisk lok. proměnné 

# # funkce1()
# # print(x)   #pokus o tisk lok. proměnné, která neexistuje





# z=1             #vznik globální proměnné z
# def funkce2():
#     z=10        #vznik lokální proměnné z!!!!!!
#     print (z)   #tisk lok. proměnné 

    
# # funkce2()
# # print (z)     #tisk globální proměnné




# y=1
# def funkce3():
#     global y   #vznik globální proměnné y uvnitř funkce,
#     y=100     #pokud již existovala, budeme pracovat s ní     
#     print (y)
    
# funkce3() #proměnná y bude existovat až po volání funkce3
# print (y)   #tisk globální proměnné y


"""
Úkol:
1) Napište program pro simulaci bankovního účtu. Bude mít 3 funkce:
   Vklad(castka) - přidá peníze na účet
   Vyber(castka) - odebere peníze z účtu
   Zustatek()    - vypíše zůstatek na účtu
   S účtem budou funkce pracovat jako s globální proměnnou 'ucet'.
   Snažte se v programu přehledně komunikovat s uživatelem.

2) Napište program pro evidenci lidí (jmen):
   Evidence bude v globálním seznamu.
   Napište funkce:
     Pridej(jmeno) - přidá jméno do evidence
     Smaz(jmeno) - smaže jméno v evidenci
     Zjisti(jmeno) - vrátí True nebo False
     Vypis() - vypíše celou evidenci
"""

#1
# ucet = 0 
# def Vklad(castka):
#   global ucet
#   ucet += castka
#   print ("Vkládáte ",castka," Kč")

# def Vyber(castka):  
#   global ucet
#   if castka > ucet:
#     print("Na účtu není dost peněz")
#   else:
#     ucet -= castka
#     print("Vybíráte",castka,"Kč")
# def Zustatek():
#   global ucet
#   print("Zůstatek na účtu je",ucet,"Kč")

# Vklad(int(input("Zadejte kolik chcete vložit:")))
# Zustatek()
# Vyber(int(input("Zadejte kolik chcete vybrat:")))
# Zustatek()
# Vyber(int(input("Zadejte kolik chcete vybrat:")))
# Zustatek()

#2


evidence = []

def Pridej(jmeno):
  global evidence
  if jmeno in evidence:
    print(jmeno,"už je v evidenci.")
  else:
    evidence.append(jmeno)
    print(jmeno,"bylo přidáno do evidence.")

def Smaz(jmeno):
  global evidence
  if jmeno in evidence:
    evidence.remove(jmeno)
    print(jmeno,"bylo smazáno z evidence.")
  else:
    print(jmeno,"nebylo nalezeno v evidenci.")

def Zjisti(jmeno):
  global evidence
  if jmeno in evidence:
    print("Jméno",jmeno,"se nachází v evidenci")
    return True
  else:
    print("Jméno",jmeno,"se nachází v evidenci")
    return False

def Vypis():
  global evidence
  print("Seznam jmen v evidenci:")
  for jmeno in evidence:
      print(jmeno)

Pridej("Petr")
Pridej("Franta")
Pridej("Ondra")
Pridej("Petr")
Vypis()
print(Zjisti("Ondra"))
print(Zjisti("Jirka"))
Smaz("Petr")
Vypis()
