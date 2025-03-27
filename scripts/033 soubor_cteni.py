# -*- coding: utf-8 -*-
"""
Created on Wed Feb 01 09:19:44 2012

@author: Radek
"""
"""     Soubory (čtení)
        
readlines() - vrátí seznam řádků souboru od akt. poz.          
readline() - přečte řetězec od aktuální pozice do 
             konce řádku  
read(x) - přečte řetězec o zadané délce, když neuvedeme
          hodnotu, přečte celý soubor
        - při pokusu o čtení na konci souboru vrací
          prázdný řetězec ""
tell() - vrací aktuální pozici v souboru
seek(pocet) - posune aktuální pozici o daný počet
              bytů od začátku souboru

Užitečné textové funkce
splitlines() - jako split, oddělovačem je "\n"
"""


# soub=open("narozeniny.txt","r")
# seznam=soub.readlines()
# soub.close()
# print (seznam)


#Jak se zbavit konců řádků? Např. takto:
#for i in range(len(sez)):
#    sez[i]=sez[i][0:-1]
#print (sez)



# soubor=open("narozeniny.txt","r")
# for i in range(2):
#     soubor.readline()
# radek=soubor.readline()
# soubor.close()
# print(radek)


# soubor=open("narozeniny.txt","r")
# vsechno=soubor.read()
# print (vsechno)
# soubor.close()

#ukázka příkazu tell()
# soubor=open("narozeniny.txt","r")
# pozice=soubor.tell()
# print("Aktuální pozice je:",pozice) 
# text=soubor.read(10)
# print(text)
# pozice=soubor.tell()
# print("Aktuální pozice je:",pozice) 
# soubor.close()


#ukázka příkazu seek()
# soubor=open("narozeniny.txt","r")
# soubor.seek(11)
# text=soubor.readline()
# print (text)
# soubor.close()


#ošetření otvírání a práce s koncem souboru
# try:
#     soubor=open("narozeniny.txt","r")
#     radek=soubor.readline()
#     while radek!="":
#         print(radek,end="")
#         radek=soubor.readline()
#     soubor.close()
# except:
#     print("Chyba při otvírání souboru!")


"""
Úkoly:
1) Otevřete soubor pokus.txt a vypište jeho 
   obsah do souboru kopie.txt. 
    Použijte buď readlines + writelines nebo read + write.
   """
# soubor=open("pokus.txt","r")
# vsechno=soubor.read()
# soub=open("kopie.txt","w")
# soub.write(vsechno)
# soubor.close()
# soub.close()
"""
2) Přečtěte soubor PISMENA.TXT pomocí příkazu read(1) a 
   zjistěte, kolik je v něm písmen "a".
    """
# soubor=open("PISMENA.txt","r")
# vsechno=soubor.read()
# z=0
# for i in vsechno:
#     if i=="a":
#         z+=1
# print("Obsahuje ",z,"písmen a.")
# soubor.close()
"""
3) Vygenerujte soubor VSTUP.TXT, ve kterém budou dva
   sloupce dvojciferných čísel oddělené mezerou. V
   každém bude 100 čísel.
   VSTUP.TXT:
   12 35\n
   43 71\n
   10 99\n
   ...
   Tento soubor postupně přečtěte a do souboru SOUCTY.TXT
   vypište řádkové součty ve formátu a+b=c.
   SOUCTY.TXT:
   12+35=47\n
   43+71=114\n
   10+99=109\n
   ...
    """
# try:
#     soub=open("SOUCTY.txt","r+")
#     soubor=open("vstup.txt","r")
#     radek=soubor.readline()
#     while radek!="":
#         print(radek,end="")
#         radek=soubor.readline()
#     for radek in soubor:
#         cislo1=int(radek[:2])
#         cislo2=int(radek[3:])
#         soucet=cislo1+cislo2
#         soub.writelines(cislo1,"+",cislo2,"=",soucet)
#     soubor.close()
# except:
#     print("Chyba při otvírání souboru!")
"""
4) Načtěte ze souboru řetězec o délce 10 znaků,
   který představuje datum a otestujte správnost 
   jeho formátu (dd.mm.rrrr). Jen formát, hodnoty čísel
   nemusí být pravdivé.
    """
# try:
#     soubor=open("datum.txt","r")
#     datum=soubor.read(10)
#     soubor.close()
#     vystup=True
#     if not datum[:2].isdigit():
#         vystup= False
#     if datum[2]!=".":
#         vystup=False
#     if not datum[3:5].isdigit():
#         vystup= False
#     if datum[5]!=".":
#         vystup=False
#     if not datum[6:].isdigit():
#         vystup= False
    
#     if vystup== True:
#         print(datum,"Datum je spravne")
#     else:
#         print("Datum není spravne.")
# except:
#     print("Soubor se nepodařilo otevřít.")
"""
5) Načtěte od uživatele 5 řetězců do seznamu, ke každému
   přidejte \n a pomocí operace WRITELINES zapište seznam
   do souboru.
    """
# x=0
# o=0
# sez=[]
# soubor=open("retez.txt","w")
# while x!=5:
#     y=input("Zadejte řetezec: ")
#     z=y,"\n"
#     sez.append(z)
#     x+=1
# while o!=5:
#    soubor.writelines(sez[o])
#    o+=1
# soubor.close
"""
6) Pokuste se otevřít neexistující soubor v módu "a" a
   přidat na konec krátký text.
    """
# soubor=open("neex.txt","a")
# soubor.writelines("Krátký text")
# soubor.close
"""
7) Otevřete nějaký soubor pro čtení a spočítejte, kolik má
   znaků. (Nápověda - přečtěte soubor jako jeden celý
   řetězec a zjistěte jeho délku)
    """
# soubor=open("PISMENA.txt","r")
# vsechno=soubor.read()
# z=0
# for i in vsechno:
#    z+=1
# print("Obsahuje ",z,"znaků.")
# soubor.close()
"""
8) V souboru neznámé délky jsou na řádcích údaje:
   věk - jméno
   věk - jméno
   ...
   Čtěte ze souboru data a zjistěte jméno nejstaršího člověka.
   Vypište jej na obrazovku. Můžete využít operaci split().
   Věk může být až trociferný.
"""
try:
    soubor=open("vek.txt", "r")
    radky = soubor.readlines()

    nejstarsi_vek = 0
    nejstarsi_jmeno =""
    for radek in radky:
        vek, jmeno = radek.split(" - ")
        vek = int(vek)
        if vek > nejstarsi_vek:
            nejstarsi_vek = vek
            nejstarsi_jmeno = jmeno
    soubor.close()
except:
    print("Soubor se nepodařilo otevřít.")
print("Nejstarší člověk je",nejstarsi_jmeno,"s věkem",nejstarsi_vek,"let.")
















