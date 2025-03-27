# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:39:49 2013

@author: Radek
"""
"""
askstring - vstupní řádek, vrací řetězec
askinteger - obdobné, vrací celé číslo
askfloat - obdobné, vrací desetinné číslo
"""

# from tkinter import *
# from tkinter import simpledialog

# hlavni=Tk()

# ret = simpledialog.askstring("Zadávání jména", "Zadej jméno",initialvalue="Jan Novák")
# print(ret)

# mainloop()

"""
Úkol:
1) Pomocí SimpleDialogu načtěte desetinné číslo a vypište
   jej do konzoly zaokrouhlené na celé číslo směrem dolů.
"""   


from tkinter import *
from tkinter import simpledialog

hlavni=Tk()

ret = simpledialog.askfloat("Zadávání čísla", "Zadej desetinné číslo",initialvalue="0.00")
print(int(ret))

mainloop()