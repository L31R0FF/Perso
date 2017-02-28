#!/usr/bin/env python

import os

with open("niveau.txt", "r") as fichier:
            structure_niveau = []
            for ligne in fichier:
                ligne_niveau = []
                for sprite in ligne:
                    if sprite != '\n':
                        ligne_niveau.append(sprite)
                structure_niveau.append(ligne_niveau)

positionPersoX = 0
positionPersoY = 0

continuer = 1
while continuer :
	evenement = raw_input(": ")
	if evenement == "quit" :
		continuer = 0
	
	elif evenement == "s" :
		if structure_niveau[positionPersoX + 1][positionPersoY] != "#" :
			if structure_niveau[positionPersoX + 1][positionPersoY] == "a" :
				print("GAGNE !")
				continuer = 0
				break
			structure_niveau[positionPersoX][positionPersoY] = "-"
			structure_niveau[positionPersoX + 1][positionPersoY] = "@"
			positionPersoX = positionPersoX + 1
		
	elif evenement == "z" :
		if structure_niveau[positionPersoX - 1][positionPersoY] != "#" :
			if structure_niveau[positionPersoX - 1][positionPersoY] == "a" :
				print("GAGNE !")
				continuer = 0
				break
			structure_niveau[positionPersoX][positionPersoY] = "-"
			structure_niveau[positionPersoX - 1][positionPersoY] = "@"
			positionPersoX = positionPersoX - 1

	elif evenement == "q" :
		if structure_niveau[positionPersoX][positionPersoY - 1] != "#" :
			if structure_niveau[positionPersoX][positionPersoY - 1] == "a" :
				print("GAGNE !")
				continuer = 0
				break
			structure_niveau[positionPersoX][positionPersoY] = "-"
			structure_niveau[positionPersoX][positionPersoY - 1] = "@"
			positionPersoY = positionPersoY - 1
	
	elif evenement == "d" :
		if structure_niveau[positionPersoX][positionPersoY + 1] != "#" :
			if structure_niveau[positionPersoX][positionPersoY + 1] == "a" :
				print("GAGNE !")
				continuer = 0
				break				
			structure_niveau[positionPersoX][positionPersoY] = "-"
			structure_niveau[positionPersoX][positionPersoY + 1] = "@"
			positionPersoY = positionPersoY + 1

	os.system("clear")
	for ligne in structure_niveau :
		print("".join(ligne)) 
