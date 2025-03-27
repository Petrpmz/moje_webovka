# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:44:14 2012

@author: Radek
"""

# from tkinter import * 

# hlavni = Tk()
# hlavni.geometry("200x150")
# hlavni.resizable(False,False)

# ramecek = Frame(hlavni)
# ramecek.pack()


# skupina=LabelFrame(ramecek,bd=2,text="Volba", relief="ridge")
# skupina.grid(row=0)

# v = IntVar() 
# v.set(2)

# def tisk():
#     print (v.get())
    
# r1=Radiobutton(skupina, text="Jedna", variable=v, value=1)
# r1.grid(row=0,sticky=W) 
# r2=Radiobutton(skupina, text="Dva", variable=v, value=2)
# r2.grid(row=1,sticky=W)
# r3=Radiobutton(skupina, text="Tri", variable=v, value=3) 
# r3.grid(row=2,sticky=W) 
    
# tlacitko=Button(ramecek,text="Kontrola",command=tisk)
# tlacitko.grid(row=1)
 
# mainloop() 

"""
1) Vytvořte skupinu tří radiobuttonů s různými pozdravy.
   Přidejte tlačítko 'Pozdrav'. Po jeho stisku se 
   zobrazí hláška s daným pozdravem (použijte showinfo).
"""   


from tkinter import * 
from tkinter import messagebox

hlavni = Tk()
hlavni.geometry("200x150")
hlavni.resizable(False,False)

ramecek = Frame(hlavni)
ramecek.pack()


skupina=LabelFrame(ramecek,bd=2,text=";Volba", relief="ridge")
skupina.grid(row=0)

v = StringVar() 
v.set("Čau")

def tisk():
    messagebox.showinfo("Pozdrav",v.get())
    
r1=Radiobutton(skupina, text="Čau", variable=v, value="Čau")
r1.grid(row=0,sticky=W) 
r2=Radiobutton(skupina, text="Ahoj", variable=v, value="Ahoj")
r2.grid(row=1,sticky=W)
r3=Radiobutton(skupina, text="Čus", variable=v, value="Čus") 
r3.grid(row=2,sticky=W) 
    
tlacitko=Button(ramecek,text="Pozdrav",command=tisk)
tlacitko.grid(row=1)
 
mainloop() 


