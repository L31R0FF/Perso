#!/usr/bin/env python

import os, time, os.path

reponse = ""
start = """@####################################
------------------------------------#
--------------1 : Play--------------a
######--------2 : Help--------#######
--------------3 : Level Editing-----#
-----######---4 : Credits-----------# 
--------------5 : Quit-----##-------#
--######----##----------------------#        
------------------------------------#
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA#
#####################################
"""
help = """@####################################
Use (q) and (d) to go left and right#
@<-@->@                       @^    #
Use (z) to make a static jump @|    a
                                    #
                              @@    #
Use (c) to make a left jump  @<-@   #
                                    #
                              @@    #
Use (v) to make a right jump @->@   #
############### Help ################
"""
credits = """@####################################
# This game was created by Felix    #
# Foriel, the original concept was  #
# found when I was sick, it is      #
# based on a labyrinth project and  #
# it was coded in a day.            #
# This game was tested by me and my #
# friend Joshua and all the levels  #
# are finishable                    #
#                                   #
############## Credits ##############
"""
while reponse != "5" :
    os.system("clear")
    print(start)
    reponse = raw_input(": ")

    if reponse == "1" :
        jstrength = raw_input("Jump strength (integer) : ")
        jstrength = int(jstrength)
        game = 1
        level = 1
        if os.path.isfile("save") :
            saveload = raw_input("(C)ontinue or (N)ew game : ")
            if saveload == "N" :
                level = 1
            else :
                with open("save", "r") as savefile :
                    level = int(savefile.read())
                    savefile.close()
        while game :
            if not os.path.isfile("level" + str(level) + ".txt") :
                print("GAGNE !")
                game = 0
                break
            with open("level" + str(level) + ".txt", "r") as fichier:
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
            os.system("clear")
            for ligne in structure_niveau :
                print("".join(ligne)) 
            while continuer :
                evenement = raw_input(": ")
                if evenement == "l" :
                    continuer = 0
                    game = 0
        
            
                elif evenement == "z" :
                    i = 0
                    while i != jstrength :
                        if structure_niveau[positionPersoX - 1][positionPersoY] != "#" :
                            if structure_niveau[positionPersoX - 1][positionPersoY] == "a" :
                                level = level + 1
                                continuer = 0
                                break
                            if structure_niveau[positionPersoX - 1][positionPersoY] == "A" :
                                print("PERDU !")
                                continuer = 0
                                game = 0
                                break
                            structure_niveau[positionPersoX][positionPersoY] = "-"
                            structure_niveau[positionPersoX - 1][positionPersoY] = "@"
                            positionPersoX = positionPersoX - 1
                            os.system("clear")
                            for ligne in structure_niveau :
                                print("".join(ligne))
                            time.sleep(0.25)
                            i = i + 1
                        else :
                            break
    
                elif evenement == "c" :
                    i = 0
                    while i != jstrength :
                        if structure_niveau[positionPersoX - 1][positionPersoY - 1] != "#" :
                            if structure_niveau[positionPersoX - 1][positionPersoY - 1] == "a" :
                                level = level + 1
                                continuer = 0
                                break
                            if structure_niveau[positionPersoX - 1][positionPersoY - 1] == "A" :
                                print("PERDU !")
                                continuer = 0
                                game = 0
                                break
                            structure_niveau[positionPersoX][positionPersoY] = "-"
                            structure_niveau[positionPersoX - 1][positionPersoY - 1] = "@"
                            positionPersoX = positionPersoX - 1
                            positionPersoY = positionPersoY - 1
                            os.system("clear")
                            for ligne in structure_niveau :
                                print("".join(ligne))
                            time.sleep(0.25)
                            i = i + 1
                        else :
                            break
            
                    i = 0
                    while i !=jstrength :
                        if structure_niveau[positionPersoX + 1][positionPersoY - 1] != "#" :
                            if structure_niveau[positionPersoX + 1][positionPersoY - 1] == "a" :
                                level = level + 1
                                continuer = 0
                                break
                            if structure_niveau[positionPersoX + 1][positionPersoY - 1] == "A" :
                                print("PERDU !")
                                continuer = 0
                                game = 0
                                break
                            structure_niveau[positionPersoX][positionPersoY] = "-"
                            structure_niveau[positionPersoX + 1][positionPersoY - 1] = "@"
                            positionPersoX = positionPersoX + 1
                            positionPersoY = positionPersoY - 1
                            os.system("clear")
                            for ligne in structure_niveau :
                                print("".join(ligne))
                            time.sleep(0.25)
                            i = i + 1
                        else :
                            break
            
                elif evenement == "v" :
                    i = 0
                    while i != jstrength :
                        if structure_niveau[positionPersoX - 1][positionPersoY + 1] != "#" :
                            if structure_niveau[positionPersoX - 1][positionPersoY - 1] == "a" :
                                level = level + 1
                                continuer = 0
                                break
                            if structure_niveau[positionPersoX - 1][positionPersoY + 1] == "A" :
                                print("PERDU !")
                                continuer = 0
                                game = 0
                                break
                            structure_niveau[positionPersoX][positionPersoY] = "-"
                            structure_niveau[positionPersoX - 1][positionPersoY + 1] = "@"
                            positionPersoX = positionPersoX - 1
                            positionPersoY = positionPersoY + 1
                            os.system("clear")
                            for ligne in structure_niveau :
                                print("".join(ligne))
                            time.sleep(0.25)
                            i = i + 1
                        else :
                            break
            
                    i = 0
                    while i != jstrength :
                        if structure_niveau[positionPersoX + 1][positionPersoY + 1] != "#" :
                            if structure_niveau[positionPersoX + 1][positionPersoY + 1] == "a" :
                                level = level + 1
                                continuer = 0
                                break
                            if structure_niveau[positionPersoX + 1][positionPersoY + 1] == "A" :
                                print("PERDU !")
                                continuer = 0
                                game = 0
                                break
                            structure_niveau[positionPersoX][positionPersoY] = "-"
                            structure_niveau[positionPersoX + 1][positionPersoY + 1] = "@"
                            positionPersoX = positionPersoX + 1
                            positionPersoY = positionPersoY + 1
                            os.system("clear")
                            for ligne in structure_niveau :
                                print("".join(ligne))
                            time.sleep(0.25)
                            i = i + 1
                        else :
                            break
                    
    
                elif evenement == "q" :
                    if structure_niveau[positionPersoX][positionPersoY - 1] != "#" :
                        if structure_niveau[positionPersoX][positionPersoY - 1] == "a" :
                            level = level + 1
                            continuer = 0
                            break
                        if structure_niveau[positionPersoX][positionPersoY - 1] == "A" :
                            print("PERDU !")
                            continuer = 0
                            game = 0
                            break
                        structure_niveau[positionPersoX][positionPersoY] = "-"
                        structure_niveau[positionPersoX][positionPersoY - 1] = "@"
                        positionPersoY = positionPersoY - 1
                
                elif evenement == "d" :
                    if structure_niveau[positionPersoX][positionPersoY + 1] != "#" :
                        if structure_niveau[positionPersoX][positionPersoY + 1] == "a" :
                            level = level + 1
                            continuer = 0
                            break           
                        if structure_niveau[positionPersoX][positionPersoY + 1] == "A" :
                            print("PERDU !")
                            continuer = 0
                            game = 0
                            break           
                        structure_niveau[positionPersoX][positionPersoY] = "-"
                        structure_niveau[positionPersoX][positionPersoY + 1] = "@"
                        positionPersoY = positionPersoY + 1
            
                if structure_niveau[positionPersoX + 1][positionPersoY] != "#" :
                    while structure_niveau[positionPersoX + 1][positionPersoY] != "#" :
                        if structure_niveau[positionPersoX + 1][positionPersoY] == "a" :
                            level = level + 1
                            continuer = 0
                            break
                        if structure_niveau[positionPersoX + 1][positionPersoY] == "A" :
                            print("PERDU !")
                            continuer = 0
                            game = 0
                            break
                        structure_niveau[positionPersoX][positionPersoY] = "-"
                        structure_niveau[positionPersoX + 1][positionPersoY] = "@"
                        positionPersoX = positionPersoX + 1
                        os.system("clear")
                        for ligne in structure_niveau :
                            print("".join(ligne))
                        time.sleep(0.25)
            
                os.system("clear")
                for ligne in structure_niveau :
                    print("".join(ligne)) 
        save = raw_input("save (y/n) : ")
        if save == "y" :
            savefile = open("save", "w")
            savefile.write(str(level))
            savefile.close()

    elif reponse == "2" :
        os.system("clear")
        print(help)
        raw_input(": ") 

    elif reponse == "3" :
        os.system("clear")
        print("You can edit here the first level, type :quit to quit")
        print("")
        with open("level1.txt", "r") as lfichier :
            print(lfichier.read())

        print("")
        efichier = open("level1.txt", "w")
        continuer = 1

        while continuer :
            ligne = raw_input("> ")
            if ligne == ":quit" :
                continuer = 0
                break
            efichier.write(ligne)
            efichier.write("\n")

        efichier.close()

    elif reponse == "4" :
        os.system("clear")
        print(credits)
        raw_input(": ") 
