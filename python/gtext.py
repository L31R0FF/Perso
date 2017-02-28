#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import pygtk 
import gtk  
import gobject # Bibliothèques à importer 

def save(widget): # Fonction de sauvegarde du fichier créé
	debut = tampon.get_start_iter() # Obtenir le debut de la zone de texte
        fin = tampon.get_end_iter() # Obtenir la fin de la zone de texte
        txt = tampon.get_text(debut, fin, True) # Obtenir le texte entre le debut et la fin de la zone de texte
	monfichier = open(name.get_text(), "w") # Ouverture du fichier
	monfichier.write(txt) # Écriture du texte dans le fichier
	monfichier.close() # Fermeture du fichier

def ouverture(widget):
	fichier = open(name.get_text(), "r") # Ouverture du fichier
	texteliste = fichier.readlines()
        texte = ''.join(texteliste)      
	tampon.set_text(texte) # Lecture du texte du fichier
	fichier.close() # Fermeture du fichier 		

gobject.threads_init() # Initialisation de gobject
window = gtk.Window() # Création de la fenêtre principale
window.set_default_size(800, 600) # Paramétrage des dimensions de la fenêtre
window.connect("destroy", lambda a: gtk.main_quit())  # Connexion de la croix de la fenêtre à la fonction quitter de gtk

vbox = gtk.VBox() # Création de la boîte verticale vbox
window.add(vbox) # Ajout de vbox à la fenêtre principale
hbox = gtk.HBox() # Création de la boîte verticale hbox
name = gtk.Entry() # Création de la zone de texte mono-ligne
sauver = gtk.Button("Enregistrer") # Création du bouton sauver
sauver.connect("clicked", save) # Connexion du bouton sauver à la fonction save
ouvrir = gtk.Button("Ouvrir") # Création du bouton ouvrir
ouvrir.connect("clicked", ouverture) # Connexion du bouton ouvrir à la fonction ouverture
fenetre = gtk.ScrolledWindow() # Crétion de la fenetre à barre de défilement
texte = gtk.TextView() # Création de la zone de texte multi-lignes
tampon = texte.get_buffer() # Obtenir le tampon de la zone de texte

vbox.pack_start(hbox, False, False, 0) # Ajout d'hbox à vbox
hbox.pack_start(name, True, True, 0) # Ajout de name à hbox
hbox.pack_start(sauver, False, False) # Ajout de sauver à hbox
hbox.pack_start(ouvrir, False, False) # Ajout d'ouvrir à hbox
vbox.pack_start(fenetre, True, True) # Ajout de fenetre à vbox
fenetre.add(texte)

window.show_all() # On voit tous les widgets de la fenêtre  
gtk.main() # On fait tourner gtk
