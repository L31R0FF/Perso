#!/usr/bin/env python
# Exactement 118 680 possibilites 

import random

with open("prov", "r") as fichierDebut :
	listeDebut = fichierDebut.read()
	listeDebut = listeDebut.split("\n")

with open("prov2", "r") as fichierFin :
	listeFin = fichierFin.read()
	listeFin = listeFin.split("\n")

print(random.choice(listeDebut) + random.choice(listeFin))