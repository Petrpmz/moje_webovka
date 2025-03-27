# -*- coding: utf-8 -*-


"""
Vyzkoušet widget.grid_forget() - odstranění prvku z gridu
"""

from tkinter import *

# hl_okno=Tk()          # toto vytvoří hlavní okno

# jmeno=Label(hl_okno, text="Zadej jméno:")
# jmeno.grid(row=0,sticky=E)         
# prijmeni=Label(hl_okno, text="Zadej příjmení:")
# prijmeni.grid(row=1,sticky=E)  
# vstup1=Entry(hl_okno)
# vstup1.grid(row=0,column=1)         
# vstup2=Entry(hl_okno)
# vstup2.grid(row=1,column=1)         

# kontrola=Label(hl_okno,text="")
# kontrola.grid(row=2,columnspan=2)

# def Zkontroluj():
#     ret1=vstup1.get()
#     ret2=vstup2.get()
#     ret3=ret1+" "+ret2
#     kontrola["text"]=ret3

# tlacitko1=Button(hl_okno,text="Kontrola",command=Zkontroluj)
# tlacitko1.grid(row=3)
# tlacitko2=Button(hl_okno,text="Kontrola",command=Zkontroluj)
# tlacitko2.grid(row=4,sticky=W+E)

# tlacitko3=Button(hl_okno,text="Konec",command=hl_okno.destroy)
# tlacitko3.grid(row=3,column=1,rowspan=2, sticky=W+E+N+S)

# hl_okno.mainloop() 


"""
Úkol:
1) Rozmístěte tlačítka a ostatní komponenty jako na
   kalkulačce pomocí rozmístění GRID 
   (P:\stejskal\Python\Cvičení Tkinter\cv2 - grid.jpg).
"""      


from tkinter import *

hl_okno=Tk()          # toto vytvoří hlavní okno

jmeno=Label(hl_okno, text="Kalkulačka", font="Arial, 25")
jmeno.grid(row=0,column=0, columnspan=4, sticky=W + E)         
vstup=Entry(hl_okno)
vstup.grid(row=1,column=0, columnspan=4, sticky=W + E)         




tlacitko12=Button(hl_okno,width=5, height=3,text="+")
tlacitko12.grid(row=2,column=3)

tlacitko13=Button(hl_okno,width=5, height=3,text="9")
tlacitko13.grid(row=2,column=2)

tlacitko14=Button(hl_okno,width=5, height=3,text="8")
tlacitko14.grid(row=2,column=1)

tlacitko15=Button(hl_okno,width=5, height=3,text="7")
tlacitko15.grid(row=2,column=0)


tlacitko22=Button(hl_okno,width=5, height=3,text="-")
tlacitko22.grid(row=3,column=3)

tlacitko23=Button(hl_okno,width=5, height=3,text="6")
tlacitko23.grid(row=3,column=2)

tlacitko24=Button(hl_okno,width=5, height=3,text="5")
tlacitko24.grid(row=3,column=1)

tlacitko25=Button(hl_okno,width=5, height=3,text="4")
tlacitko25.grid(row=3,column=0)




tlacitko32=Button(hl_okno,width=5, height=3,text="=")
tlacitko32.grid(row=4,column=3, rowspan=2, sticky=N + S)

tlacitko33=Button(hl_okno,width=5, height=3,text="3")
tlacitko33.grid(row=4,column=2)

tlacitko34=Button(hl_okno,width=5, height=3,text="2")
tlacitko34.grid(row=4,column=1)

tlacitko35=Button(hl_okno,width=5, height=3,text="1")
tlacitko35.grid(row=4,column=0)



tlacitko43=Button(hl_okno,width=5, height=3,text=",")
tlacitko43.grid(row=5,column=2)



tlacitko45=Button(hl_okno, height=3,text="0")
tlacitko45.grid(row=5,column=0, columnspan=2, sticky=E + W)


hl_okno.mainloop() 