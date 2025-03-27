# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 11:35:00 2013

@author: Radek
"""
from tkinter import colorchooser
from tkinter import *


# hlavni=Tk()
# hlavni.geometry("250x100")

# def ZmenBarvu():
#    barva=colorchooser.askcolor(title="Barva")
#    print (barva)
#    hlavni["bg"]=barva[1]

# tlacitko = Button(hlavni, text = "Barva pozadí", command=ZmenBarvu)
# tlacitko.pack() 

# mainloop()

"""
Úkol:
1) Do aplikace vložte tlačítko pro výběr barvy.
   Výběr barvy proveďte pomocí barevného dialogu.
   Vybranou barvu nastavte na pozadí tlačítka.
"""   


from tkinter import colorchooser
from tkinter import *


hlavni=Tk()
hlavni.geometry("250x100")

def ZmenBarvu():
   barva=colorchooser.askcolor(title="Barva")
   tlacitko["bg"]= barva[1]


tlacitko = Button(hlavni, text = "Barva pozadí", command=ZmenBarvu)
tlacitko.pack() 

mainloop()











import tkinter as tk
from tkinter import messagebox

def calculate_dph():
    try:
        amount = float(entry_amount.get())
        if amount < 0:
            raise ValueError("Zadaná částka nesmí být záporná.")

        # Get the selected DPH rate
        selected_rate = dph_rate.get()
        dph_value = amount * (selected_rate / 100)

        # Display the result
        label_result.config(text=f"DPH: {dph_value:.1f} Kč")
    except ValueError as e:
        messagebox.showerror("Chyba", f"Neplatná hodnota: {e}")

# Create the main application window
app = tk.Tk()
app.title("Výpočet DPH")

# Input for amount
label_amount = tk.Label(app, text="Zadejte částku (Kč):")
label_amount.grid(row=0, column=0, padx=10, pady=10)

entry_amount = tk.Entry(app)
entry_amount.grid(row=0, column=1, padx=10, pady=10)

# Radiobuttons for DPH selection
dph_rate = tk.DoubleVar()
dph_rate.set(21)  # Default DPH rate

label_dph = tk.Label(app, text="Vyberte sazbu DPH:")
label_dph.grid(row=1, column=0, padx=10, pady=10)

radio_21 = tk.Radiobutton(app, text="21%", variable=dph_rate, value=21)
radio_21.grid(row=2, column=0, padx=10, pady=5)

radio_15 = tk.Radiobutton(app, text="15%", variable=dph_rate, value=15)
radio_15.grid(row=3, column=0, padx=10, pady=5)

radio_10 = tk.Radiobutton(app, text="10%", variable=dph_rate, value=10)
radio_10.grid(row=4, column=0, padx=10, pady=5)

# Button to calculate DPH
button_calculate = tk.Button(app, text="Spočítat DPH", command=calculate_dph)
button_calculate.grid(row=5, column=0, columnspan=2, pady=10)

# Label for the result
label_result = tk.Label(app, text="DPH: ---", font=("Arial", 12))
label_result.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
app.mainloop()
