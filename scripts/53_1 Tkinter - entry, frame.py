# -*- coding: utf-8 -*-

from tkinter import *


hlavni = Tk()
hlavni.title("Výpočet 2. mocniny")

ramecek=Frame(hlavni, bd=1, relief="ridge")
ramecek.pack()

def vypocet():
    x=int(vstup.get())
    napis["text"]=str(x**2)

tlacitko=Button(ramecek, text="Druhá mocnina", command=vypocet)
tlacitko.pack(side="left", padx=10, pady=10)

napis=Label(ramecek,text="0",font=("Arial",50))
napis.pack(side="left")

vstup=Entry(ramecek, width=25)
vstup.pack(side="left",padx=10, pady=10)

hlavni.mainloop()

"""
Úkol:
1) Vložte do okna dva Framy pod sebe. V prvním budou vedle sebe
   Label s textem "Vstup:" a jedno Entry.
   Ve druhém bude Label "Výstup:" a ještě jeden Label pro 
   výstupní text. konec vložte tlačítko. Při jeho stisku se text z Entry 
   předá do výstupního Labelu.
    """



kopirka = Tk()
kopirka.title("")
kopirka.geometry("300x200")

frame1 = Frame(kopirka)
frame1.pack(pady=10)
label_vstup = Label(frame1, text="Vstup:")
label_vstup.pack()
entry = Entry(frame1)
entry.pack( padx=5)


frame2 = Frame(kopirka)
frame2.pack(pady=10)
label_vystup = Label(frame2, text="Výstup:")
label_vystup.pack()
vystup_label = Label(frame2, text="", bg="white")
vystup_label.pack(padx=5)
def zkopiruj_text():
   vystup_label["text"] = entry.get()

tlacitko = Button(kopirka, text="Přenést text", command=zkopiruj_text)
tlacitko.pack(pady=10)


kopirka.mainloop()



"""

2) Napište aplikaci, která bude obsahovat:
   - Label "Tajná šifra" - zvětšené písmo
   - Entry pro vstup textu
   - Tlačítko "Šifruj vstup"
   - Label pro výstup
   - Tlačítko "Konec"
   - vhodně použijte Frame
   
   Po stisku tlačítka se řetězec ze vstupu zašifruje 
   libovolnou metodou a výsledek se zobrazí v labelu.
"""    



apl = Tk()
apl.title("")
apl.geometry("300x300")


frame11 = Frame(apl,bd=1)
frame11.pack(pady=10)
sifralab = Label(frame11,font=("Arial", 20), text="Tajná šifra:")
sifralab.pack()
vst = Entry(frame11)
vst.pack( padx=5)

frame12 = Frame(apl,bd=1)
frame12.pack(pady=10)
vyst = Label(frame12,font=("Arial", 20), text="Zašifrovaný text:")
vyst.pack()
vystl = Label(frame12, text="", bg="white")
vystl.pack(padx=5)

def sifruj_text():
    sifra=vst.get()
    


tlacitkos = Button(apl, text="Šifruj text", command=sifruj_text)
tlacitkos.pack(pady=10)

tlacitkos1 = Button(apl, text="Konec", command=apl.destroy)
tlacitkos1.pack(pady=10)

apl.mainloop()


