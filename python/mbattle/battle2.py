#!/usr/bin/env python

import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()

fenetre = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF)

pygame.mixer.music.load("dvorak.ogg")

class Perso :
    def __init__(self, nom, direction, sante, spdegats) :
        self.nom = nom
        self.sprite = pygame.image.load(nom + direction + ".png").convert_alpha()
        self.pos = self.sprite.get_rect()
        self.direction = direction
        self.sante = sante
        self.speciale = 0
        self.spdegats = spdegats
        print(self.pos)

    def hurt(self, degats, nom) :
        hit = pygame.mixer.Sound(self.nom + "hit.ogg")
        hit.play()
        self.sante = self.sante - degats
        
        if self.sante <= 0 :
            pygame.mixer.music.stop()
            a = menu(nom + "win.png", nom + "win")
            global continuer
            continuer = 0

    def move(self, x, y) :
        self.pos = self.pos.move(x, y)

    def attack(self, nom, cible) :
        if nom == "punch" and self.direction == "r" :
            self.sprite = pygame.image.load(self.nom + "pr.png").convert_alpha()
            pos = self.sprite.get_rect()
            pos.x = self.pos.x
            pos.y = self.pos.y
            if pos.colliderect(cible.pos) :
                cible.hurt(10, self.nom)
                cible.move(20, 0)
                self.speciale = self.speciale + 25 

        elif nom == "punch" and self.direction == "l" :
            self.sprite = pygame.image.load(self.nom + "pl.png").convert_alpha()
            pos = self.sprite.get_rect()
            pos.x = self.pos.x
            pos.y = self.pos.y
            if pos.colliderect(cible.pos) :
                cible.hurt(10, self.nom)
                cible.move(-20, 0)
                self.speciale = self.speciale + 25 

        elif nom == "kick" and self.direction == "r" :
            self.sprite = pygame.image.load(self.nom + "kr.png").convert_alpha()
            pos = self.sprite.get_rect()
            pos.x = self.pos.x
            pos.y = self.pos.y
            if pos.colliderect(cible.pos) :
                cible.hurt(15, self.nom)
                cible.move(20, 0)
                self.speciale = self.speciale + 25 

        elif nom == "kick" and self.direction == "l" :
            self.sprite = pygame.image.load(self.nom + "kl.png").convert_alpha()
            pos = self.sprite.get_rect()
            pos.x = self.pos.x
            pos.y = self.pos.y
            if pos.colliderect(cible.pos) :
                cible.hurt(15, self.nom)
                cible.move(-20, 0)
                self.speciale = self.speciale + 25

        elif nom == "speciale" and self.direction == "r" :
            if self.speciale >= 100 :
                self.sprite = pygame.image.load(self.nom + "spr.png").convert_alpha()
                pos = self.sprite.get_rect()
                pos.x = self.pos.x
                pos.y = self.pos.y
                self.speciale = 0
                if pos.colliderect(cible.pos) :
                    cible.hurt(self.spdegats, self.nom)
                    cible.move(20, 0)
            else :
                print("nope, speciale level: " + str(self.speciale))

        elif nom == "speciale" and self.direction == "l" :
            if self.speciale >= 100 :
                self.sprite = pygame.image.load(self.nom + "spl.png").convert_alpha()
                pos = self.sprite.get_rect()
                pos.x = self.pos.x
                pos.y = self.pos.y
                self.speciale = 0
                if pos.colliderect(cible.pos) :
                    cible.hurt(self.spdegats, self.nom)
                    cible.move(-20, 0)
            else :
                print("nope, speciale level: " + str(self.speciale))

def menu(image, son) :
    a = True
    sound = pygame.mixer.Sound(son + ".ogg")
    sound.play()
    while a :
        fenetre.blit(pygame.image.load(image).convert(), (0,0))
        pygame.display.flip()
    
        for event in pygame.event.get() :
            if event.type == QUIT :
                exit(0)
            if event.type == KEYDOWN :
                a = False

    return event.key

while 1 :

    while 1 :
        reponse = menu("start.png", "choose1")

        if reponse == K_f :
            perso1 = Perso("felix", "r", 100, 50)
            break

        elif reponse == K_p :
            perso1 = Perso("papa", "r", 100, 50)
            break

    print("2")

    while 1 :
        reponse2 = menu("start.png", "choose2")

        if reponse2 == K_f :
            perso2 = Perso("felix", "l", 100, 50)
            break

        elif reponse2 == K_p :
            perso2 = Perso("papa", "l", 100, 50)
            break

    sound = pygame.mixer.Sound("fight.ogg")
    sound.play()
    perso1.move(0, 300)
    perso2.move(650, 300)
    continuer = 1
    upmode1 = 0
    upmode2 = 0
    pygame.key.set_repeat(400, 100)
    pygame.mixer.music.play()
    while continuer :
        fenetre.blit(pygame.image.load(perso1.nom + "fond.png").convert(), (0,0))
        perso1.sprite = pygame.image.load(perso1.nom + perso1.direction + ".png").convert_alpha()
        perso2.sprite = pygame.image.load(perso2.nom + perso2.direction + ".png").convert_alpha()    

        for event in pygame.event.get():
            if event.type == QUIT :
                musique.stop()
                exit(0)
    
            if event.type == KEYDOWN :
                if event.key == K_LEFT :
                    perso2.direction = "l"
                    perso2.move(-20, 0)
    
                elif event.key == K_RIGHT :
                    perso2.direction = "r"
                    perso2.move(20, 0)
    
                elif event.key == K_UP :
                    if upmode2 == 0 :
                        upmode2 = 1
                        perso2.move(0, -341)
    
                    elif upmode2 == 1 :
                        upmode2 = 0
                        perso2.move(0, 341)
    
                elif event.key == K_KP1 :
                    perso2.attack("punch", perso1)
    
                elif event.key == K_KP2 :
                    perso2.attack("kick", perso1)
    
                elif event.key == K_KP_PLUS :
                    perso2.attack("speciale", perso1)
    
                elif event.key == K_q :
                    perso1.direction = "l"
                    perso1.move(-20, 0)
    
                elif event.key == K_d :
                    perso1.direction = "r"
                    perso1.move(20, 0)
    
                elif event.key == K_z :
                    if upmode1 == 0 :
                        upmode1 = 1
                        perso1.move(0, -341)

                    elif upmode1 == 1 :
                        upmode1 = 0
                        perso1.move(0, 341)

                elif event.key == K_j :
                    perso1.attack("punch", perso2)

                elif event.key == K_k :
                    perso1.attack("kick", perso2)
            
                elif event.key == K_LCTRL :
                    perso1.attack("speciale", perso2)

            fenetre.blit(perso1.sprite, perso1.pos)
            fenetre.blit(perso2.sprite, perso2.pos)

            pygame.display.flip()
