# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 09:21:47 2013

@author: Radek
"""
"""
Souborové dialogy
- musíme importovat filedialog
- slouží k získání cesty k souboru, nic neotvírají
- danou cestu musíme použít v příkazu open
- pozor, když dialog někdo stornuje, bude cesta prázdná ("")

dialog -> řetězec s cestou -> open(cesta,"mód")
"""
# from tkinter import filedialog
# from tkinter import *

# hlavni=Tk()
# hlavni.geometry("250x100")

# def Otevrit():
#     cesta = filedialog.askopenfilename(title="Otevřít soubor",filetypes=(('Python File', ('*.py','*.pyw')),('Text File', '*.txt'),('All Files', '*')))
#     print (cesta)
#     #zde proběhne otevření souboru pro čtení, čtení a uzavření
#     soubor=open(cesta,"r")
#     data=soubor.read()
#     soubor.close()
#     print(data)

    
# def Ulozit():
#     cesta = filedialog.asksaveasfilename(defaultextension='.txt',title="Uložit soubor", initialdir="P:\\")
#     print (cesta) 
#     #zde proběhne otevření pro zápis, zápis a uzavření
#     import random
#     soubor=open(cesta,"w")
#     for i in range(100):
#         soubor.write(str(random.randint(500,999))+"\n")
#     soubor.close()


# button1=Button(hlavni,text="Otevřít",command=Otevrit)
# button1.pack(pady=3) 
# button2=Button(hlavni,text="Uložit",command=Ulozit)
# button2.pack(pady=3) 
# mainloop()

"""
Úkol:
1) Vložte do okna jedno Entry a tlačítko Uložit. Uložte do 
   souboru text z Entry.
   Použijte dialog asksaveasfilename. 

"""



from tkinter import filedialog
from tkinter import *

hlavni=Tk()
hlavni.geometry("250x100")
vstup=Entry(hlavni,state="normal")
vstup.pack(pady=3)

def Ulozit():
    cesta = filedialog.asksaveasfilename(filetypes=(('Python File', ('*.py','*.pyw')),('Text File', '*.txt'),('All Files', '*')),defaultextension=".txt",title="Text", initialdir="H:\\")
    soubor=open(cesta,"w")
    soubor.write(vstup.get()+"\n")
    soubor.close()

button2=Button(hlavni,text="Uložit",command=Ulozit)
button2.pack(pady=3) 
mainloop()
