from Functions import interface
from Files import fileMenu
from Pranks import prankMenu
from System import systemInfoMenu

menuOptions = "[1] File Operations 📂\n[2] Pranks 🤡\n[3] System Information 💻"


def selectionMenu():
     interface("Selection_Menu", menuOptions, fileMenu, prankMenu, systemInfoMenu)