import os
import time
import msvcrt
import ctypes

def setWindowName():
    if os.name == "nt":
        try:
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleTitleW("RuV Tools")
        except ImportError:
            pass
    else:
        os.system("echo -ne '\033]0;RuV Tools\007'")

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def inputColor(text):
    return '\033[1;36m' + text + '\033[0m'

def outputColor(text):
    return '\033[32m' + text + '\033[0m'

def errorColor(text): # Error color or warning color --> red for both
    return '\033[1;31m' + text + '\033[0m'

def menuLine():
    print(f"\033[1;33m=========================\033[0m")

def outputLine():
    print(f"\033[1;95m=========================\033[0m")

def printLogo():
    logo = """\033[38;2;226;255;12m\t▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
\t▐                                                                                                ▌
\t▐                                                                                                ▌
\t▐                                                                                                ▌
\t▐      ███████████              █████   █████    ███████████                   ████              ▌
\t▐     ░░███░░░░░███            ░░███   ░░███    ░█░░░███░░░█                  ░░███              ▌
\t▐      ░███    ░███  █████ ████ ░███    ░███    ░   ░███  ░   ██████   ██████  ░███   █████      ▌
\t▐      ░██████████  ░░███ ░███  ░███    ░███        ░███     ███░░███ ███░░███ ░███  ███░░       ▌
\t▐      ░███░░░░░███  ░███ ░███  ░░███   ███         ░███    ░███ ░███░███ ░███ ░███ ░░█████      ▌
\t▐      ░███    ░███  ░███ ░███   ░░░█████░          ░███    ░███ ░███░███ ░███ ░███  ░░░░███     ▌
\t▐      █████   █████ ░░████████    ░░███            █████   ░░██████ ░░██████  █████ ██████      ▌
\t▐     ░░░░░   ░░░░░   ░░░░░░░░      ░░░            ░░░░░     ░░░░░░   ░░░░░░  ░░░░░ ░░░░░░       ▌
\t▐                                                                                                ▌
\t▐                                                                                                ▌
\t▐                                                                                                ▌
\t▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
\033[32;221;246;255;12m                                                                                           
                                                                            credits --> @VoldRax  \033[32;211;23;255;145m                                   
                                                                                           """
    print(logo)

def checkChoice(choice):

        if choice == b"\x1b":  # Escape key
            for i in range(5, 0, -1):
                cls()
                printLogo()
                print("Thank You for using our multitool")
                if i == 1:
                    print(f"This program will terminate in {i} second")
                else:
                    print(f"This program will terminate in {i} seconds")
                time.sleep(1)
            exit(0)

def confirm(prompt):

    print(f"\033[1;33m{prompt} (y/n):\033[0m ", end='', flush=True)
    while True:
        response = msvcrt.getch().lower()
        if response == b'y':
            return True
        elif response == b'n':
            return False

def exitProgram():
    if confirm("\n\033[1;33mDo you want to exit the tool?\033[0m"):       
        for i in range(5, 0, -1):
            cls()
            printLogo()
            print(f"\033[1;31m[EXIT]\033[0m \033[31mThank you for using our multitool.\033[0m")
            print(f"\033[31mThis program will terminate in {i} second{'s' if i > 1 else ''}...\033[0m")
            time.sleep(1)
        exit(0)
    else:
        print(f"\n\033[1;31m[INFO]\033[0m \033[31mOperation Cancelled by the user.\033[0m")
        msvcrt.getch()

def handleInvalidChoice():

    print(f"\033[1;31m[ERROR]\033[0m \033[31mInvalid choice. Try again.\033[0m")
    print(f"\n\033[38;5;45mPress any key to return to the main menu...\033[0m")
    msvcrt.getch()

def handleBackspace(menuName):

    if menuName.lower() == "selection_menu":
        print(f"\033[1;31m[INFO]\033[0m \033[31mYou are already on the Selection Menu. Cannot go back further.\033[0m")
        time.sleep(2)
        return False  # Don't break the loop

    if menuName.lower() == "auth":
        exitProgram()

    if menuName.lower() == "files" or menuName.lower() == "pranks" or menuName.lower() == "system_info":
        
        if confirm("\n\033[1;33mDo you want to return to the previous menu?\033[0m"):
            print(f"\n\033[1;33m[INFO]\033[0m \033[33mReturning to the previous menu...\033[0m")
            time.sleep(1)
            return True  # Break the loop
    
        else: 
            print(f"\n\033[1;33m[INFO]\033[0m \033[33mStaying in current menu...\033[0m")
            time.sleep(1)
            return False  # Stay in the loop


def interface(menuName, menuOptions, *functions):

    setWindowName()

    while True:

        if not functions:
            print(f"\033[1;31m[ERROR]\033[0m \033[31mNo functions provided for the menu.\033[0m")
            return

        menuNameDisplay  = ""

        match menuName.lower():
            case "auth":
                menuNameDisplay = "RuV Tools"
            case "selection_menu":
                menuNameDisplay = "Selection Menu"
            case "files":
                menuNameDisplay = "Files Operations Menu"
            case "pranks":
                menuNameDisplay = "Pranks Menu"
            case "system_info":
                menuNameDisplay = "System Menu"
            

        cls()
        printLogo()
        print(f"\033[1;33mWelcome to the {menuNameDisplay}!\033[0m")
        if menuName.lower() == "pranks":
            print(f"\033[1;31mDisclaimer : We are not responsible for any loss of data or the system\033[0m")
        menuLine()

        # Print each menu option in green
        for line in menuOptions.strip().split('\n'):
            print(f"{outputColor(line)}")

        menuLine()
        print(f"\033[38;5;208m[INFO]\033[0m {outputColor("Press ESC to exit the program, or Backspace to go back. \033[0m")}")

        choice = msvcrt.getch()

        if choice == b"\x08":  # Backspace
            if handleBackspace(menuName):
                break
            else:
                continue

        elif choice == b"\x1b":  # Escape key
            exitProgram()

        try:
            index = int(choice.decode()) - 1
            if 0 <= index < len(functions):
                cls()
                printLogo()
                print(f"\033[1;32m[SUCCESS]\033[0m \033[32mYou selected option {index + 1}.\033[0m")
                result =  functions[index]()
                if result == "login_success":
                    msvcrt.getch()
                    break
                else:
                    msvcrt.getch()
            else:
                cls()
                printLogo()
                handleInvalidChoice()
        except (ValueError, IndexError):
            cls()
            printLogo()
            handleInvalidChoice()