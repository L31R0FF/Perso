#!/usr/bin/env python3
# coding: utf-8

import os
import sys
import time
import socket

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