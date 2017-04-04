#!/usr/bin/env python3
# coding: utf-8

import sys
import socket

if len(sys.argv) < 2 :
    sys.exit(0)

texte = ""

with open(sys.argv[1], "r") as fichier:
    texte = fichier.read()
    fichier.close()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 666))

while True:
        socket.listen(5)
        client, address = socket.accept()
        print("{} connected".format( address ))
        client.send(texte.encode())

print("Close")
client.close()
stock.close()