#!/usr/bin/env python3

import os
import sys
import time

texte = ""
os.system("clear")

with open("line", "r") as fichier:
    texte = fichier.read()
    fichier.close()

i = 0
l = 0

for lettre in texte:
    if lettre == "0" :
        sys.stdout.write("-")
        i = i + 1

    elif lettre == "1" :
        sys.stdout.write("#")
        i = i + 1

    if i == 40 :
        sys.stdout.write("\n")
        i = 0
        l = l + 1
        time.sleep(0.02)        

    if l == 15 :
        l = 0
        os.system("clear")

    