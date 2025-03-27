# -*- coding: utf-8 -*-
"""
Validace vstupu
---------------
parametr validate
- říká, kdy se má volat validační funkce
- např. "key", "focusin", "focusout", "all"

parametr validatecommand
- tuto funkci volá hlavní okno a volá ji pokaždé, když
  nastane situace validate
- určuje validační funkci a její parametry
- parametry (zástupné symboly):
    %P - budoucí hodnota vstupu
    %d - při pokusu o vložení bude 1, při mazání bude 0, jinak -1
    %i - index, kam se bude vkládat nebo mazat
    %s - původní hodnota vstupu
    %S - vkládaný nebo mazaný text (Ctrl+V nebo delete)
    %W - jméno widgetu (komponenty)

funkce register
- aby hlavní okno mohlo volat validační funkci, musí
  ji mít zaregistrovanou  

odkazy:
https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/entry-validation.html
https://www.geeksforgeeks.org/python-tkinter-validating-entry-widget/
"""
from tkinter import *
from tkinter import messagebox

hlavni=Tk()
hlavni.geometry("300x200")

def test(hodnota,i,d):  #i,d
    print("Index, kam se vkládá:",i)
    print("Hodnota parametru d:",d)
    
    if hodnota.isdigit() or hodnota == "":
        return True
    else:
        return False    



reg_fce = hlavni.register(test)

nadpis = Label(hlavni, text = "Omezení vstupu", font=("Arial",18))
nadpis.pack()
popisek = Label(hlavni, text = "Vložte pokusný vstup:")
popisek.pack()
vstup=Entry(hlavni,validate="key",validatecommand=(reg_fce,"%P","%i","%d")) #,"%i","%d"
vstup.pack()

mainloop()

"""
Úkol:
1) Vložte do okna 3x Entry i s popisky a nastavte omezení vstupu:
   Entry1 - lze vkládat jen jedničky a nuly (musíme otestovat všechny
            znaky vstupu, nejen poslední vložený)
   Entry2 - lze vkládat jen hexačíslice (to samé)
   Entry3 - lze vkládat jen jen písmena  (řetezec.isalpha())  

Navíc:
   Entry4 - lze vložit desetinné číslo, tečka může být jen jedna!
          - zkuste využít příkaz try: a převodní fci float()
"""



















# def test_hexa(hodnota):
#     for i in hodnota:
#         if i not in "0123456789abcdefABCDEF":
#             return False
#     return True




"""
def test_float2(hodnota):  
    try:
        float(hodnota)
        return True
    except:
        if hodnota == "":
          return True
        else:
          return False    
"""


"""
def test_float1(hodnota, posledni):  
    if (posledni.isdigit() or posledni==".") and hodnota.count(".")<2 or hodnota == "":
        return True
    else:
        return False    

"""