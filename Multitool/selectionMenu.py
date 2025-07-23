from functions import interface
from basicMenu import basicOpsMenu
from files import fileMenu
from pranks import prankMenu
from system import systemInfoMenu

menuOptions = "[1] Basic Operations 💻\n[2] File Operations 📂\n[3] Pranks 🤡\n[4] System Information 💻"


def selectionMenu():
     interface("Selection_Menu",  menuOptions, basicOpsMenu, fileMenu, prankMenu, systemInfoMenu)
