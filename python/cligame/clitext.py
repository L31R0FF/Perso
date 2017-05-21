#!/usr/bin/env python

import curses, os
import curses.textpad

os.system("clear")

if len(sys.argv) > 1 :
    if sys.argv[1] == "-v" :
        print("hed version : 1.0")
    else :
        
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

tb = curses.textpad.Textbox(stdscr)
text = tb.edit()

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()
print(text)
filename = raw_input("filename : ")
with open(filename, "w") as fichier :
    fichier.write(text)