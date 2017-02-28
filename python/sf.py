#!/usr/bin/env python3

import Tkinter
from Tkinter import *
import tkSimpleDialog

fenetre = Tkinter.Tk()
fenetre.geometry("800x600")
fenetre.title("sf")

fonction = tkSimpleDialog.askstring("sf", "fonction : ")
print(fonction)
canvas = Canvas(width=780, height=580, bg="white")
x = 1
y = 1
while y <= 580 :
    canvas.create_line(eval(fonction), y, eval(fonction)+1, y+1, width=2, fill="red")
    x = x + 1
    y = y + 1

canvas.pack()

fenetre.mainloop()