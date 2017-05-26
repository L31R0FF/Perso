#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()
fenetre = pygame.display.set_mode((800, 600))

class Sprite :
    def __init__(self, nom, centerX, centerY, hurtboxH1, hurtboxH2, hurtboxL1, hurtboxL2, hitboxH1, hitboxH2, hitboxL1, hitboxL2)
        self.sprite = pygame.image.load(nom).convert_alpha() 
        self.centerX = centerX
        self.centerY = centerY
        self.hurtboxH1 = hurtboxH1
        self.hurtboxH2 = hurtboxH2
        self.hurtboxL1 = hurtboxL1
        self.hurtboxL2 = hurtboxL2
        self.hitboxH1 = hitboxH1
        self.hitboxH2 = hitboxH2
        self.hitboxL1 = hitboxL1
        self.hitboxL2 = hitboxL2


class Perso :
    def __init__(self, direction) :
        self.sprite = Sprite("perso.png", 75, 150, 41, 299, 49, 95, 0, 0, 0, 0)
        self.posX = 0
        self.posY = 341
        self.direction = direction

    def attack(self, nom) :
        if nom == "punch" and self.direction == "l" :
            self.sprite = Sprite("persopl.png", 75, 150, 41, 299, 49, 95, 193, 207, 0, 64)

        