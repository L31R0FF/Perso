import os
from colorama import Fore, Back, Style
os.system("clear")

i = 0
i2 = 0

def blit(text, posX, posY, surface) :
    i = posY
    i2 = posX
    i3 = 0
    i4 = 0
    text = text.split("\n")
    while i3 < len(text) :
        while i4 < len(text[i3]) :
            surface[i][i2] = text[i3][i4]
            i4 = i4 + 1
            i2 = i2 + 1
        i2 = posX
        i4 = 0
        i = i + 1
        i3 = i3 + 1
    return surface

def render(surface) :
    for ligne in surface :
        for lettre in ligne:
            if lettre == "n" :
                print(Fore.BLACK + Back.BLACK + "x" + Style.RESET_ALL, end="")

            elif lettre == "r" :
                print(Fore.RED + Back.RED + "x" + Style.RESET_ALL, end="")

            elif lettre == "g" :
                print(Fore.GREEN + Back.GREEN + "x" + Style.RESET_ALL, end="")

            elif lettre == "y" :
                print(Fore.YELLOW + Back.YELLOW + "x" + Style.RESET_ALL, end="")
    
            elif lettre == "b" :
                print(Fore.BLUE + Back.BLUE + "x" + Style.RESET_ALL, end="")

            elif lettre == "m" :
                print(Fore.MAGENTA + Back.MAGENTA + "x" + Style.RESET_ALL, end="")

            elif lettre == "c" :
                print(Fore.CYAN + Back.CYAN + "x" + Style.RESET_ALL, end="")

            elif lettre == "w" :
                print(Fore.WHITE + Back.WHITE + "x" + Style.RESET_ALL, end="")

            else :
                print(lettre, end="")
        print()

def openback(filename) :
    with open(filename, "r") as fichier:
        structure_niveau = []
        for ligne in fichier:
            ligne_niveau = []
            for sprite in ligne:
                if sprite != '\n':
                    ligne_niveau.append(sprite)
            structure_niveau.append(ligne_niveau)
    return structure_niveau

structure_niveau = openback("screen.txt")
perso = """wwwrwww
wwr rww
wrr rrw
r     r
rr   rr
rr r rr
wrrwrrw
wrrwrrw
wrrwrrw"""

screen2 = blit(perso, 50, 20, structure_niveau)
render(screen2)