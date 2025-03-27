# -*- coding: utf-8 -*-
"""
Vše lze nalézt na:
http://tkinter.programujte.com (pro Python 2)

http://tkinter.py.cz (pro Python 3, musí být http:// !!!)
https://www.root.cz/clanky/graficke-uzivatelske-rozhrani-v-pythonu-knihovna-tkinter/
https://www.root.cz/clanky/graficke-uzivatelske-rozhrani-v-pythonu-menu-v-knihovne-tkinter/
https://www.root.cz/clanky/graficke-uzivatelske-rozhrani-v-pythonu-knihovna-tkinter-3-cast/

fce Tk() - založí hlavní okno programu
fce mainloop() - zobrazí okno a čeká na uživatele
"""

from tkinter import *

hl_okno=Tk()          # toto vytvoří hlavní okno


# hl_okno.title("Výuková aplikace")

# hl_okno.minsize(300,200)
# hl_okno.maxsize(400,300)
# #hl_okno.geometry("400x300")

# hl_okno.resizable(False,False)

# data = "123"

# def zmen_napis():
#     global data
#     napis.configure(text="Jiny napis", fg="blue")

# def zmen_napis2():
#     global data
#     print (napis["text"])
#     napis["text"]=napis["text"]+"!"
#     napis["fg"]="black"
#     tlacitko3["command"]=hl_okno.destroy

# napis=Label(hl_okno,text="Popisek v Labelu",fg="red", bg="#00FF00", font=("Arial",25))  # label napis
# napis.pack()    

# tlacitko1=Button(hl_okno, text="Vypnout",command=hl_okno.destroy )
# tlacitko1.pack() 

# tlacitko2=Button(hl_okno, text="Změna nápisu", width=30, height=3,command=zmen_napis)
# tlacitko2.pack() 

# tlacitko3=Button(hl_okno, text="Druhá změna nápisu", width=30, height=3,command=zmen_napis2)
# tlacitko3.pack() 


hl_okno.mainloop() #nekonečná smyčka, čeká na události od uživatele

"""
Úkol:
1) Naprogramujte počítač kliknutí.
   Bude obsahovat 4 tlačítka a 1 label s číslem:
       - plus
       - minus
       - reset
       - end
   Pozor, budeme-li pracovat s proměnnými, musíme použít global!!!
    
2) Naprogramujte generátor příkladů na násobení.
   Na stisk tlačítka se vygeneruje náhodný příklad a 
   zobrazí se pomocí labelu.
 """

#Předávání dat mezi funkcemi 1
def Generuj():
    global x 
    x = random.randint()

def Kontrola():
    global x
    if x==int(vstup.get())

#Předávání dat mezi funkcemi 2
x = IntVar()

def Generuj():
    x.set(random.randint())

def Kontrola():
     x.get()==int(vstup.get())

