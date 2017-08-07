#!/usr/bin/env python

import os, sys

texte = str()
nom = ""
ligne = ""

os.system("clear")

if len(sys.argv) > 1 :
    nom = sys.argv[1]

    if os.path.isfile(sys.argv[1]) :
        with open(sys.argv[1], "r") as fichier :
            texte = fichier.read()


while ligne != ":q" :
    os.system("clear")

    texte = texte.split("\n")
    i = 0    

    while i < len(texte) - 1 :
        if i < 10 :
            print(str(i + 1) + " : " + texte[i])

        else :
            print(str(i + 1) + ": " +texte[i])

        i = i + 1

    myi = i + 1
    texte = "\n".join(texte)      

    if myi < 10 :
        ligne = raw_input(str(myi) + " > ")

    else :
        ligne = raw_input(str(myi) + "> ") 

    ligne = ligne.replace(":N", "\033[0m")
    ligne = ligne.replace(":Bl", "\033[5m")
    ligne = ligne.replace(":In", "\033[7m")
    ligne = ligne.replace(":B", "\033[1m")
    ligne = ligne.replace(":D", "\033[2m")
    ligne = ligne.replace(":I", "\033[3m")
    ligne = ligne.replace(":U", "\033[4m")

    ligne = ligne.replace(":fB", "\033[30m")
    ligne = ligne.replace(":fr", "\033[31m")
    ligne = ligne.replace(":fg", "\033[32m")
    ligne = ligne.replace(":fy", "\033[33m")
    ligne = ligne.replace(":fb", "\033[34m")
    ligne = ligne.replace(":fm", "\033[35m")
    ligne = ligne.replace(":fc", "\033[36m")
    ligne = ligne.replace(":flg", "\033[37m")

    ligne = ligne.replace(":flB", "\033[90m")
    ligne = ligne.replace(":flr", "\033[91m")
    ligne = ligne.replace(":flg", "\033[92m")
    ligne = ligne.replace(":fly", "\033[93m")
    ligne = ligne.replace(":flb", "\033[94m")
    ligne = ligne.replace(":flm", "\033[95m")
    ligne = ligne.replace(":flc", "\033[96m")
    ligne = ligne.replace(":fw", "\033[97m")

    ligne = ligne.replace(":bB", "\033[40m")
    ligne = ligne.replace(":br", "\033[41m")
    ligne = ligne.replace(":bg", "\033[42m")
    ligne = ligne.replace(":by", "\033[43m")
    ligne = ligne.replace(":bb", "\033[44m")
    ligne = ligne.replace(":bm", "\033[45m")
    ligne = ligne.replace(":bc", "\033[46m")
    ligne = ligne.replace(":blg", "\033[47m")

    ligne = ligne.replace(":blB", "\033[100m")
    ligne = ligne.replace(":blr", "\033[101m")
    ligne = ligne.replace(":blg", "\033[102m")
    ligne = ligne.replace(":bly", "\033[103m")
    ligne = ligne.replace(":blb", "\033[104m")
    ligne = ligne.replace(":blm", "\033[105m")
    ligne = ligne.replace(":blc", "\033[106m")
    ligne = ligne.replace(":bw", "\033[107m")

    sligne = ligne.split(" ")

    if sligne[0] == ":l" :
        texte = texte.split("\n")
        texte[int(sligne[1])-1] = sligne[2].replace("_", " ")
        texte = "\n".join(texte)

    elif sligne[0] == ":lw" :
        texte = texte.split("\n")
        texte[int(sligne[1])-1] = texte[int(sligne[1])-1].split(" ")
        texte[int(sligne[1])-1][int(sligne[2])-1] = sligne[3].replace("_", " ")
        texte[int(sligne[1])-1] = " ".join(texte[int(sligne[1])-1])
        texte = "\n".join(texte)

    elif ligne == ":q" :
        a = 1    

    else :
        texte = texte + ligne + "\n"

rep = raw_input("Sauvegarder ? (O/n) : ")

if rep == "n" :
    exit(0)

else :
    fnom = raw_input("nom : " + nom + " ")

    if fnom != "" :
        nom = fnom

    with open(nom, "w") as fichier :
        fichier.write(texte)

