#!/usr/bin/env python3

import os, time, os.path, pygame
from pygame.locals import *
from colorama import Fore, Back, Style

pygame.init()
fenetre = pygame.display.set_mode((800, 600))

wall = pygame.image.load("pics/wall.png").convert() 
floor = pygame.image.load("pics/floor.png").convert()
spike = pygame.image.load("pics/spike.png").convert()
chest = pygame.image.load("pics/chest.png").convert()
perso = pygame.image.load("pics/hero.png").convert()

start = pygame.image.load("pics/start.png").convert()
help = pygame.image.load("pics/help.png").convert()
credits = pygame.image.load("pics/credits.png").convert()
corn = pygame.image.load("pics/corn.png").convert()
saveimg = pygame.image.load("pics/save.png").convert()
jstr = pygame.image.load("pics/jstrenght.png").convert()
gagne = pygame.image.load("pics/gagne.png").convert()

pygame.display.set_icon(perso)
pygame.display.set_caption("SPOOKY BOY")

reponse = ""
pygame.key.set_repeat(400, 100)

while reponse != "5" :
    fenetre.blit(start, (0, 0))
    pygame.display.flip()
    
    for event in pygame.event.get() :
        if event.type == QUIT :
            reponse = 5
            exit(0)
        if event.type == KEYDOWN :
            if event.key == K_KP1 :
                reponse = "1"

            elif event.key == K_KP2 :
                reponse = "2"

            elif event.key == K_KP3 :
                reponse = "3"

            elif event.key == K_KP4 :
                reponse = "4"

            elif event.key == K_KP5 :
                reponse = "5"
                exit(0)

    if reponse == "1" :
        a = True
        while a :
            fenetre.blit(jstr, (0, 0))
            pygame.display.flip()
    
            for event in pygame.event.get() :
                if event.type == QUIT :
                    a = False
                    exit(0)
                if event.type == KEYDOWN :
                    if event.key == K_KP1 :
                        jstrength = 1
                        a = False

                    elif event.key == K_KP2 :
                        jstrength = 2
                        a = False

                    elif event.key == K_KP3 :
                        jstrength = 3
                        a = False

                    elif event.key == K_KP4 :
                        jstrength = 4
                        a = False

                    elif event.key == K_KP5 :
                        jstrength = 5
                        a = False

                    elif event.key == K_KP6 :
                        jstrength = 6
                        a = False

                    elif event.key == K_KP7 :
                        jstrength = 7
                        a = False

                    elif event.key == K_KP8 :
                        jstrength = 8
                        a = False
                        
                    elif event.key == K_KP9 :
                        jstrength = 9
                        a = False       
        
        game = 1
        level = 1
        if os.path.isfile("save") :
            a = True
            while a :
                fenetre.blit(corn, (0, 0))
                pygame.display.flip()
    
                for event in pygame.event.get() :
                    if event.type == QUIT :
                        a = False
                        reponse = 5
                    if event.type == KEYDOWN :
                        if event.key == K_c :
                            saveload = "C"
                            a = False
    
                        elif event.key == K_n :
                            saveload = "N"
                            a = False

            if saveload == "N" :
                level = 1
            else :
                with open("save", "r") as savefile :
                    level = int(savefile.read())
                    savefile.close()
        while game :
            if not os.path.isfile("level" + str(level) + ".txt") :
                
                a = True
                while a :
                    fenetre.blit(gagne, (0, 0))
                    pygame.display.flip()
    
                    for event in pygame.event.get() :
                        if event.type == QUIT :
                            a = False
                            exit(0)
                        if event.type == KEYDOWN :
                            a = False
                            exit(0)

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
            ix = 0
            iy = 0    
            for ligne in structure_niveau :
                for lettre in ligne :
                    if lettre == "@" :
                        fenetre.blit(perso, (ix, iy))

                    elif lettre == "#" :
                        fenetre.blit(floor, (ix, iy))

                    elif lettre == "-" :
                        fenetre.blit(wall, (ix, iy))

                    elif lettre == "A" :
                        fenetre.blit(spike, (ix, iy))

                    elif lettre == "a" :
                        fenetre.blit(chest, (ix, iy))

                    else :
                        fenetre.blit(wall, (ix, iy))
                    ix = ix + 32
                ix = 0
                iy = iy + 32
 
            while continuer :
                evenement = ""
                for event in pygame.event.get() :
                    if event.type == QUIT :
                        continuer = 0
                        game = 0
                    if event.type == KEYDOWN :
                        if event.key == K_z :
                            evenement = "z"

                        elif event.key == K_q :
                            evenement = "q"

                        elif event.key == K_d :
                            evenement = "d"

                        elif event.key == K_c :
                            evenement = "c"

                        elif event.key == K_v :
                            evenement = "v"

                        elif event.key == K_l :
                            evenement = "l"

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
                            ix = 0
                            iy = 0    
                            for ligne in structure_niveau :
                                for lettre in ligne :
                                    if lettre == "@" :
                                        fenetre.blit(perso, (ix, iy))
    
                                    elif lettre == "#" :
                                        fenetre.blit(floor, (ix, iy))

                                    elif lettre == "-" :
                                        fenetre.blit(wall, (ix, iy))

                                    elif lettre == "A" :
                                        fenetre.blit(spike, (ix, iy))

                                    elif lettre == "a" :
                                        fenetre.blit(chest, (ix, iy))

                                    else :
                                        fenetre.blit(wall, (ix, iy))
                                    ix = ix + 32
                                ix = 0
                                iy = iy + 32
                            pygame.display.flip()
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
                            ix = 0
                            iy = 0    
                            for ligne in structure_niveau :
                                for lettre in ligne :
                                    if lettre == "@" :
                                        fenetre.blit(perso, (ix, iy))

                                    elif lettre == "#" :
                                        fenetre.blit(floor, (ix, iy))

                                    elif lettre == "-" :
                                        fenetre.blit(wall, (ix, iy))

                                    elif lettre == "A" :
                                        fenetre.blit(spike, (ix, iy))

                                    elif lettre == "a" :
                                        fenetre.blit(chest, (ix, iy))

                                    else :
                                        fenetre.blit(wall, (ix, iy))
                                    ix = ix + 32
                                ix = 0
                                iy = iy + 32
                            pygame.display.flip()
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
                            ix = 0
                            iy = 0    
                            for ligne in structure_niveau :
                                for lettre in ligne :
                                    if lettre == "@" :
                                        fenetre.blit(perso, (ix, iy))

                                    elif lettre == "#" :
                                        fenetre.blit(floor, (ix, iy))

                                    elif lettre == "-" :
                                        fenetre.blit(wall, (ix, iy))

                                    elif lettre == "A" :
                                        fenetre.blit(spike, (ix, iy))

                                    elif lettre == "a" :
                                        fenetre.blit(chest, (ix, iy))

                                    else :
                                        fenetre.blit(wall, (ix, iy))
                                    ix = ix + 32
                                ix = 0
                                iy = iy + 32
                            pygame.display.flip()
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
                            ix = 0
                            iy = 0    
                            for ligne in structure_niveau :
                                for lettre in ligne :
                                    if lettre == "@" :
                                        fenetre.blit(perso, (ix, iy))

                                    elif lettre == "#" :
                                        fenetre.blit(floor, (ix, iy))

                                    elif lettre == "-" :
                                        fenetre.blit(wall, (ix, iy))

                                    elif lettre == "A" :
                                        fenetre.blit(spike, (ix, iy))
    
                                    elif lettre == "a" :
                                        fenetre.blit(chest, (ix, iy))

                                    else :
                                        fenetre.blit(wall, (ix, iy))
                                    ix = ix + 32
                                ix = 0
                                iy = iy + 32
                            pygame.display.flip()
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
                            ix = 0
                            iy = 0    
                            for ligne in structure_niveau :
                                for lettre in ligne :
                                    if lettre == "@" :
                                        fenetre.blit(perso, (ix, iy))
        
                                    elif lettre == "#" :
                                        fenetre.blit(floor, (ix, iy))

                                    elif lettre == "-" :
                                        fenetre.blit(wall, (ix, iy))

                                    elif lettre == "A" :
                                        fenetre.blit(spike, (ix, iy))

                                    elif lettre == "a" :
                                        fenetre.blit(chest, (ix, iy))

                                    else :
                                        fenetre.blit(wall, (ix, iy))
                                    ix = ix + 32
                                ix = 0
                                iy = iy + 32
                            pygame.display.flip()
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
                        ix = 0
                        iy = 0    
                        for ligne in structure_niveau :
                            for lettre in ligne :
                                if lettre == "@" :
                                    fenetre.blit(perso, (ix, iy))

                                elif lettre == "#" :
                                    fenetre.blit(floor, (ix, iy))
    
                                elif lettre == "-" :
                                    fenetre.blit(wall, (ix, iy))

                                elif lettre == "A" :
                                    fenetre.blit(spike, (ix, iy))

                                elif lettre == "a" :
                                    fenetre.blit(chest, (ix, iy))

                                else :
                                    fenetre.blit(wall, (ix, iy))
                                ix = ix + 32
                            ix = 0
                            iy = iy + 32
                        pygame.display.flip()
                        time.sleep(0.25)
            
                os.system("clear")
                ix = 0
                iy = 0    
                for ligne in structure_niveau :
                    for lettre in ligne :
                        if lettre == "@" :
                            fenetre.blit(perso, (ix, iy))

                        elif lettre == "#" :
                            fenetre.blit(floor, (ix, iy))

                        elif lettre == "-" :
                            fenetre.blit(wall, (ix, iy))

                        elif lettre == "A" :
                            fenetre.blit(spike, (ix, iy))

                        elif lettre == "a" :
                            fenetre.blit(chest, (ix, iy))
    
                        else :
                            fenetre.blit(wall, (ix, iy))
                        ix = ix + 32
                    ix = 0
                    iy = iy + 32
                pygame.display.flip()
        a = True
        while a :            
            fenetre.blit(saveimg, (0, 0))
            pygame.display.flip()
    
            for event in pygame.event.get() :
                if event.type == QUIT :
                    continuer = 0
                if event.type == KEYDOWN :
                    if event.key == K_y :
                        save = "y"
                        a = False

                    elif event.key == K_n :
                        save = "n"
                        a = False

        if save == "y" :
            savefile = open("save", "w")
            savefile.write(str(level))
            savefile.close()

    elif reponse == "2" :
        a = True
        while a :
            fenetre.blit(help, (0, 0))
            pygame.display.flip()
    
            for event in pygame.event.get() :
                if event.type == QUIT :
                    a = False
                    reponse = 5
                if event.type == KEYDOWN :
                    a = False

    elif reponse == "3" :
        os.system('xterm -T "Level editing" -e "nano level1.txt"')

    elif reponse == "4" :
        a = True
        while a :
            fenetre.blit(credits, (0, 0))
            pygame.display.flip()
    
            for event in pygame.event.get() :
                if event.type == QUIT :
                    a = False
                    reponse = 5
                if event.type == KEYDOWN :
                    a = False
    reponse = 0