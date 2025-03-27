# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 08:32:40 2011

@author: Radek
"""


# #Lepší způsob
# for i in "Olomouc":
#     print(i)


#Horší způsob
# print()

# ret="Olomouc"
# for i in range(len(ret)):
#     print (ret[i])


"""
Úkol:
1) Načtěte řetězec z klávesnice. Vytvořte z něj nový 
   řetězec tak, že za každé písmeno vložíte znak "*". 
   "Python" -> "P*y*t*h*o*n*"
2) Načtěte řetězec a spočítejte v něm písmena "a".  
3) Načtěte řetězec a spočítejte součet všech cifer, 
   které se v něm budou vyskytovat.
"""
# 1)
# vysledek=""
# for i in input("Napište slovo:"):
#     vysledek+=i+"*"
# print(vysledek)

# 2)
# x=0
# for i in input("Napište slovo:"):
#     if i == "a":
#         x+=1
# print(x)

# 3)
# x=0
# for i in input("Napište cifru:"):
#     if i in "1,2,3,4,5,6,7,8,9":
#         cislo=int(i)
#         x+=cislo
# print(x)