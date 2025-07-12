from functions import interface
from files import fileMenu
from pranks import prankMenu
from system import systemInfoMenu

menuOptions = "[1] File Operations 📂\n[2] Pranks 🤡\n[3] System Information 💻"


def selectionMenu():
     interface("Selection_Menu", menuOptions, fileMenu, prankMenu, systemInfoMenu)
