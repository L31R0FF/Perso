from cursesmenu import *
from cursesmenu.items import *

# Create the main menu
menu = CursesMenu("Mini interface", "Commandes : ")

# Create sub menu "editors"
editors = CursesMenu("Editors")

cmdEmacs = CommandItem("Emacs", "emacs")
cmdNano = CommandItem("Nano",  "nano")

editors.append_item(cmdEmacs)
editors.append_item(cmdNano)

editors_item = SubmenuItem("Editors", editors, menu)

# Create sub menu "developing"
developing = CursesMenu("Developing")

cmdPython = CommandItem("Python",  "python")

developing.append_item(cmdPython)

developing_item = SubmenuItem("Developing", developing, menu)

# Once we're done creating them, we just add the items to the menu
menu.append_item(editors_item)
menu.append_item(developing_item)

# Finally, we call show to show the menu and allow the user to interact
menu.show()
