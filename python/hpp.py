#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import time
import socket
from colorama import Fore, Back, Style

hote = "localhost"
port = 666

texte = "nope"
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print("Connection on {}".format(port))

texte = socket.recv(99999)

print("Close")
socket.close()

texte = bytes.decode(texte)

os.system("clear")

i = 0
l = 0

for lettre in texte:
    if lettre == "B" :
        print(Fore.BLACK + Back.BLACK + "x" + Style.RESET_ALL, end="")
        i = i + 1

    elif lettre == "r" :
        print(Fore.RED + Back.RED + "x" + Style.RESET_ALL, end="")
        i = i + 1

    elif lettre == "g" :
        print(Fore.GREEN + Back.GREEN + "x" + Style.RESET_ALL, end="")
        i = i + 1

    elif lettre == "y" :
        print(Fore.YELLOW + Back.YELLOW + "x" + Style.RESET_ALL, end="")
        i = i + 1

    elif lettre == "b" :
        print(Fore.BLUE + Back.BLUE + "x" + Style.RESET_ALL, end="")
        i = i + 1

    elif lettre == "m" :
        print(Fore.MAGENTA + Back.MAGENTA + "x" + Style.RESET_ALL, end="")
        i = i + 1

    elif lettre == "c" :
        print(Fore.CYAN + Back.CYAN + "x" + Style.RESET_ALL, end="")
        i = i + 1

    elif lettre == "w" :
        print(Fore.WHITE + Back.WHITE + "x" + Style.RESET_ALL, end="")
        i = i + 1

    if i == 40 :
        sys.stdout.write("\n")
        i = 0
        l = l + 1        

    if l == 15 :
        l = 0
        time.sleep(0.5)
        os.system("clear")