from tkinter import *
hlavni = Tk()

hlavni.title("Kalkulačka")
hlavni.geometry("300x300")
prv=StringVar()
druh=StringVar()
tret=StringVar()

frame = Frame(hlavni,bg="blue")
frame.pack(pady=5)
kalk=Label(frame, text="Kalkulačka", font=("Arial",36))
kalk.pack()

frame1 = Frame(hlavni)
frame1.pack(pady=5)
vst=Label(frame1,  text="1. číslo:")
vst.grid(row=0, column=0)
vstup=Entry(frame1,textvariable=prv)
vstup.grid(row=0, column=1)
vst2=Label(frame1, text="2. číslo:")
vst2.grid(row=1, column=0)
vstup2=Entry(frame1,textvariable=druh)
vstup2.grid(row=1, column=1)



def plus():
    x=float(prv.get())
    y=float(druh.get())
    vysl=x+y
    tret.set(str(vysl))

def minus():
    x=float(prv.get())
    y=float(druh.get())
    vysl=x-y
    tret.set(str(vysl))

def krat():
    x=float(prv.get())
    y=float(druh.get())
    vysl=x*y
    tret.set(str(vysl))

def deleno():
    x=float(prv.get())
    y=float(druh.get())
    if y or x == 0:
        vysl= "Chyba"
    else:
        vysl=x/y
    tret.set(str(vysl))

def zbytek():
    x=float(prv.get())
    y=float(druh.get())
    if y or x == 0:
        vysl= "Chyba"
    else:
        vysl=x%y
    tret.set(str(vysl))

frame2 = Frame(hlavni)
frame2.pack(pady=10)

tlacitkop=Button(frame2, text="+", command=plus)
tlacitkop.grid(row=0, column=0)

tlacitko2=Button(frame2, text="-", command=minus)
tlacitko2.grid(row=0, column=1)

tlacitko3=Button(frame2, text="*", command=krat)
tlacitko3.grid(row=0, column=2)

tlacitko4=Button(frame2, text="//", command=deleno)
tlacitko4.grid(row=0, column=3)

tlacitko5=Button(frame2, text="%", command=zbytek)
tlacitko5.grid(row=0, column=4)



frame3 = LabelFrame(hlavni, bd=1, text="Výsledek")
frame3.pack(pady=5)

vystup = Entry(frame3, textvariable=tret, border=1, state="readonly", width=15)
vystup.pack(padx=5,pady=5)


tlacitko1=Button(hlavni,text="Konec",command=hlavni.destroy)
tlacitko1.pack()


mainloop() 