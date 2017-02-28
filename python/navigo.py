#!/usr/bin/env python  
# -*- coding: utf-8 -*-

import pygtk
import gtk  
import gobject  
import webkit

# Fonction appelée lorsqu'on appuie sur enter dans la barre d'adresse
def browse(widget):
  # On affiche l'URL contenue dans la barre d'adresse
  browser.open(barre.get_text()) 

gobject.threads_init()

# Création de la fenêtre
window = gtk.Window()
# On définit sa taille par défaut
window.maximize()
# Exécute gtk.main_quit() quand on clique sur la croix
window.connect("destroy", lambda a: gtk.main_quit()) 

# La barre d'adresse et la zone où s'affiche la page internet
# sont placées dans une boîte verticale
vbox = gtk.VBox(False, 0)
window.add(vbox)
hbox = gtk.HBox(False, 1)
vbox.pack_start(hbox, False, False, 0)
barre = gtk.Entry()
chercher = gtk.Button("Rechercher")
fenetre = gtk.ScrolledWindow()
# la fonction browse est appelée quand on tape sur Enter
barre.connect("activate", browse)
chercher.connect("clicked", browse)
hbox.pack_start(barre, True, True, 0)
hbox.pack_start(chercher, False, False)

# Initialisation de l'objet webkit
browser = webkit.WebView()
browser.open("http://google.com")
vbox.pack_start(fenetre, True, True)
fenetre.add(browser)

window.show_all()  
gtk.main()  

