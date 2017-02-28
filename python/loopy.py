#!/usr/bin/env python  
# -*- coding: utf-8 -*-

cmd = ""
memListe = []

while cmd != "quit" :
	cmd = raw_input("> ")
	cmdListe = cmd.split()

	if cmdListe[0] == "mem+" :
		memListe.append(cmdListe[1])

	elif cmdListe[0] == "mem-" :
		memListe.pop()

	elif cmdListe[0] == "pmem" :
		print(memListe)

	elif cmdListe[0] == "puts" :
		print(cmdListe[1])

	elif cmdListe[0] == "pvar" :
		print(memListe[int(cmdListe[1])])

	elif cmdListe[0] == "text" :
		ListeLignes = []
		ligne = ""
		while ligne != "exit" :
			ligne = raw_input("texte > ")
			ListeLignes.append(ligne)
		memListe.append(ListeLignes)

	elif cmdListe[0] == "calc" :
		print(int(cmdListe[1]))