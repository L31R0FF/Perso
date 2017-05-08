#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, random, os
from pygame.locals import *

pygame.init()
pygame.mixer.init()

fenetre = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF)
pygame.mouse.set_visible(False)

i = 0
tempsActuel = 0
tempsPrecedent = 0
i2 = 0
tempsActuel2 = 0
tempsPrecedent2 = 0
enemyListe = []
deadListe = []
level = 0 

class Gun :
    """Classe définissant une arme caractérisée par :
    - Son nom
    - Son son
    - Son son de recharge
    - Ses dégats
    - Ses munitions"""

    def __init__(self, nom):
        with open(nom, "r") as fichier :
            texte = fichier.read()
            texte = texte.split("\n")

        self.mire = pygame.image.load(texte[0]).convert_alpha()
        self.nom = texte[1]
        self.son = pygame.mixer.Sound("sound/" + self.nom + ".ogg")
        self.reloadson = pygame.mixer.Sound("sound/" + self.nom + "load.ogg")
        self.degats = int(texte[2])
        self.munitions = int(texte[3])
        self.hitboxL = int(texte[4])
        self.hitboxH = int(texte[5])

class Enemy :
    """Classe définissant un ennemi caractérisé par:
    - Sa position courante X
    - Sa position courante Y
    - Sa liste de position et d'images
    - Sa liste d'images de mort
    - Son cri
    - Sa fonction animer
    - Sa fonction death
    - Sa fonction hit"""

    def __init__(self, nom):
        with open(nom, "r") as fichier :
            texte = fichier.read()
            texte = texte.split("\n")
        
            self.posX = int(texte[0])
            self.posY = int(texte[1])
            self.posListe = eval(texte[2])
            self.deathListe = eval(texte[3])
            self.cri = pygame.mixer.Sound(texte[4])
            self.health = int(texte[5])

    def animer(self):
        global tempsActuel, tempsPrecedent, i
        tempsActuel = pygame.time.get_ticks()

        if len(self.posListe) >= i + 1:    
            if tempsActuel - tempsPrecedent > random.randrange(100,200):
                fenetre.blit(pygame.image.load(self.posListe[i][0]), (self.posListe[i][1],self.posListe[i][2]))    
                tempsPrecedent = tempsActuel
                self.posX = self.posListe[i][1]
                self.posY = self.posListe[i][2]
                i = i + 1
            else :
                fenetre.blit(pygame.image.load(self.posListe[i][0]), (self.posX, self.posY))
        else: 
            i = 0

    def death(self):
        self.cri.play()
        enemyListe.remove(self)
        deadListe.append([self.deathListe, self.posX, self.posY, 1])

    def hit(self, degats):
        self.health = self.health - degats
    
class Perso:
    """Classe définissant le joueur caractérisé par:
    - Son sprite
    - Sa position X
    - Sa position Y
    - Son arme
    - Sa fonction tir
    - Sa fonction recharger"""

    def __init__(self, arme):
        self.posX = 0
        self.posY = 0
        self.arme = Gun(arme)
        self.sprite = self.arme.mire

    def tir(self):
        if self.arme.munitions > 0 :
            self.arme.son.play()
            self.arme.munitions = self.arme.munitions - 1
            global enemyListe
            for enemy in enemyListe :
                if (self.posX <= enemy.posX + self.arme.hitboxL and self.posX >= enemy.posX - self.arme.hitboxL) and (self.posY <= enemy.posY + self.arme.hitboxH and self.posY >= enemy.posY - self.arme.hitboxL) :
                    enemy.hit(self.arme.degats)
                    
                    if enemy.health <= 0 :
                        enemy.death()
                    else :
                        hit = pygame.mixer.Sound("sound/hit.ogg")
                        hit.play()
                            

        else :
            nobullet = pygame.mixer.Sound("sound/nobullet.ogg")
            nobullet.play()

    def recharger(self):
        self.arme.reloadson.play()
        self.arme.munitions = self.arme.munitions + 1

def deadBlit() :
    i3 = 0
    while i3 < len(deadListe) :
        global tempsActuel2, tempsPrecedent2, i2
        tempsActuel2 = pygame.time.get_ticks()
        if deadListe[i3][3] == 1 :
            if len(deadListe[i3][0]) >= i2 + 1:    
                if tempsActuel2 - tempsPrecedent2 >= random.randrange(400, 500):
                    fenetre.blit(pygame.image.load(deadListe[i3][0][i2]), (deadListe[i3][1],deadListe[i3][2]))    
                    i2 = i2 + 1
                    tempsPrecedent2 = tempsActuel2
                else :
                    fenetre.blit(pygame.image.load(deadListe[i3][0][i2]), (deadListe[i3][1], deadListe[i3][2]))
            else: 
                fenetre.blit(pygame.image.load(deadListe[i3][0][len(deadListe[i3][0]) - 1]), (deadListe[i3][1],deadListe[i3][2]))
                deadListe[i3][3] = 0
                i2 = 0
        else :
            fenetre.blit(pygame.image.load(deadListe[i3][0][len(deadListe[i3][0]) - 1]), (deadListe[i3][1],deadListe[i3][2]))
        i3 = i3 + 1

            

def enemyBlit() :
    for enemy in enemyListe :
        enemy.animer()

def next() :
    global level, fond, enemyListe, mire, deadListe, fore
    enemyListe = []
    deadListe = []
    level = level + 1
    if not os.path.isfile("pics/fond" + str(level) + ".png") :
        print("GAGNE")
        exit(0)

    fond = pygame.image.load("pics/fond" + str(level) + ".png").convert()
    fore = pygame.image.load("pics/fore" + str(level) + ".png").convert_alpha()   
    
    i = 1

    while os.path.isfile("enemy/enemy" + str(level) + str(i) + ".txt") :
        enemy = Enemy("enemy/enemy" + str(level) + str(i) + ".txt")
        enemyListe.append(enemy)
        i = i + 1

    mire = Perso("arme/bazooka.txt")

continuer = 1
next()

while continuer :
    fenetre.blit(fond, (0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0

        elif event.type == MOUSEMOTION :
            mire.posX = event.pos[0]
            mire.posY = event.pos[1]

        elif event.type == MOUSEBUTTONDOWN and event.button == 1 :
            mire.tir()

        elif event.type == MOUSEBUTTONDOWN and event.button == 3 :
            mire.recharger() 

    deadBlit()

    enemyBlit()

    fenetre.blit(fore, (0,0))
    fenetre.blit(mire.sprite, (mire.posX - 35, mire.posY - 35))
    pygame.display.flip()

    if enemyListe == [] :
        next()
