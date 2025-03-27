 # -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 11:14:56 2012

@author: Radek
"""
"""
showinfo - zobrazení hlášky + tlačítko Ok
askyesno - zobrazení otázky + tlačítka Yes a No, vrací True nebo False
"""
from tkinter import *
from tkinter import messagebox


hl_okno=Tk()

messagebox.showinfo("Informace","Prosím, přečtěte si následující informaci.")

x=messagebox.askyesno("Otázka","Chcete pokračovat?")
print (x)

mainloop()


"""
Úkol: 
1) Položte uživateli libovolnou zjišťovací otázku.
   Když správně odpoví vypište na konzolu pochvalu,
   jinak vypište správnou odpověď.
"""