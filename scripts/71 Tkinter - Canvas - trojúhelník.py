# -*- coding: utf-8 -*-
"""
Created on Tue Apr 02 12:04:24 2013

@author: Radek
"""

from tkinter import *
import random

hlavni = Tk()

platno = Canvas(hlavni,width=500, height=500)
platno.pack()

bod_x = -1
bod_y = -1
pocatek_x = -1
pocatek_y = -1

# def trojuhelnik(udalost):
#     if len(body) == 0:
#         body.append(udalost.x)
#         body.append(udalost.y)
#     elif len(body) == 0:    

# platno.bind("<1>",trojuhelnik)

def cara(udalost):
    global bod_x
    global bod_y
    global pocatek_x
    global pocatek_y
    if bod_x != -1:
        platno.create_line(bod_x,bod_y,udalost.x,udalost.y)
    if pocatek_x == -1:
        pocatek_x = udalost.x
        pocatek_y = udalost.y
    bod_x = udalost.x
    bod_y = udalost.y

def uzavrit(udalost):
    global bod_x
    global bod_y
    global pocatek_x
    global pocatek_y
    platno.create_line(bod_x,bod_y,pocatek_x,pocatek_y)
    bod_x = -1
    bod_y = -1
    pocatek_x = -1
    pocatek_y = -1

platno.bind("<1>",cara)
platno.bind("<3>",uzavrit)

mainloop()