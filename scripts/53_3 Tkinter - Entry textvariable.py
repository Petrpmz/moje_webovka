# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 08:24:32 2013

@author: Radek
"""
# from tkinter import *

# hlavni=Tk()

# t=StringVar()
# t.set("Vánoce přicházejí")

# vstup=Entry(hlavni,textvariable=t)
# vstup.pack()

# vstup2=Entry(hlavni,textvariable=t, state="disabled")
# vstup2.pack()

# def Nastav():
#      t.set("Pokusný text")
#      print(t.get())

# tlacitko=Button(hlavni,text="Vlož text",command=Nastav)
# tlacitko.pack()

# mainloop()  


from tkinter import *
hlavni = Tk()

hlavni.geometry("300x300")
t=StringVar()


frame1 = Frame(hlavni,bd=1,bg="blue")
frame1.pack(pady=10)
vst=Label(frame1, text="Vstup:")
vst.pack()
vstup=Entry(frame1,textvariable=t)
vstup.pack()


def Nastav():
     vystup.config(text=t.get())
     print(t.get())



tlacitko=Button(hlavni,text="Kopie",command=Nastav)
tlacitko.pack()

frame2 = Frame(hlavni,bd=1, bg="green")
frame2.pack(pady=10)
vystup=Label(frame2,text="")
vystup.pack()

tlacitko1=Button(hlavni,text="Konec",command=hlavni.destroy)
tlacitko1.pack()


mainloop() 







import tkinter as tk
from tkinter import messagebox

# Funkce pro výpočet řešení rovnice
def vypocet():
    try:
        a = float(entry_a.get())  # Získáme hodnotu a
        b = float(entry_b.get())  # Získáme hodnotu b
        
        if a == 0:
            if b == 0:
                vysledek_label.config(text="Nekonečně mnoho řešení")
            else:
                vysledek_label.config(text="Neexistuje žádné řešení")
        else:
            x = -b / a
            vysledek_label.config(text=f"x = {x:.4f}")  # Výsledek zobrazíme na 4 desetinná místa
    except ValueError:
        messagebox.showerror("Chyba", "Prosím zadejte platná čísla!")

# Funkce pro ukončení programu
def konec():
    okno.destroy()

# Vytvoření hlavního okna
okno = tk.Tk()
okno.title("Řešení lineární rovnice ax + b = 0")

# Popisek a vstup pro 'a'
label_a = tk.Label(okno, text="Zadejte hodnotu a:")
label_a.pack()
entry_a = tk.Entry(okno)
entry_a.pack()

# Popisek a vstup pro 'b'
label_b = tk.Label(okno, text="Zadejte hodnotu b:")
label_b.pack()
entry_b = tk.Entry(okno)
entry_b.pack()

# Tlačítko pro výpočet
vypocet_button = tk.Button(okno, text="Výpočet", command=vypocet)
vypocet_button.pack()

# Popisek pro zobrazení výsledku
vysledek_label = tk.Label(okno, text="")
vysledek_label.pack()

# Tlačítko pro ukončení programu
konec_button = tk.Button(okno, text="Konec", command=konec)
konec_button.pack()

# Hlavní smyčka aplikace
okno.mainloop()
