import platform
import time
import pymongo as pym
import getpass
import hashlib
import os
import socket
import msvcrt

# Setting up the title of the console window
if os.name == "nt":
    try:
        import ctypes

        kernel32 = ctypes.windll.kernel32
        kernel32.SetConsoleTitleW("RuV Tools")
    except ImportError:
        pass
else:
    # For Unix-like systems, we can use the `os` module to set the title
    # Note: This may not work in all terminal emulators 
    os.system("echo -ne '\033]0;RuV Tools\007'")

# Setting up the logo
# Using ANSI escape codes for colors
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
                                                                            credits --> @iamrudra69  \033[32;211;23;255;145m                                   
                                                                                           """

# Setting up functions

def cls():
    os.system("cls" if os.name == "nt" else "clear")


def printLogo():
    print(logo)


def getHost_Ip():
    print(f"Hostname : {socket.gethostname()}")
    try:
        # This does not actually connect to the Internet, just determines the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except Exception:
        ip_address = "Unable to determine IP"
    print(f"IP Address : {ip_address}")


def get_CPU_Architecture():
    print(f"CPU Architecture : {platform.machine()}")


def getUsername():
    print(f"User : {getpass.getuser()}")


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def registerUser(address):
    cls()
    printLogo()

    print("--------------------------------------------------")
    userId = input("Enter your user Id : ").lower()
    passW = getpass.getpass("Enter your password: ")
    confirmPass = getpass.getpass("Confirm your password: ")
    print("--------------------------------------------------")

    if passW != confirmPass:
        print("\033[1;31mPasswords do not match!\033[0m")
        time.sleep(2)
        return False

    if len(passW) < 8:
        print("\033[1;31mPassword must be at least 8 characters long!\033[0m")
        time.sleep(2)
        return False

    if not any(char.isdigit() for char in passW):
        print("\033[1;31mPassword must contain at least one digit!\033[0m")
        time.sleep(2)
        return False

    if not userId or not passW:
        print("\033[1;31mUserId and Password cannot be empty!\033[0m")
        time.sleep(2)
        return False

    password = hash_password(passW)

    try:
        client = pym.MongoClient(address)
        database = client["RuVMultitoolv1"]
        collection = database["Auth"]
        document = collection.find_one({"userId": userId})

        if document:
            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(1)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)
            print("\033[1;31mUser already exists!\033[0m")
            time.sleep(1)
            return False
        
        else:
            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(2)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)
            print("\033[32mRegistration successful!\033[0m")
            time.sleep(1)
            collection.insert_one({"userId": userId, "password": password})
            return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def loginUser(address):

    cls()
    printLogo()

    print("--------------------------------------------------")
    userId = input("Enter your user Id : ").lower()
    passW = getpass.getpass("Enter your password: ")
    print("--------------------------------------------------")

    password = hash_password(passW)
    
    try:
        client = pym.MongoClient(address)
        database = client["RuVMultitoolv1"]
        collection = database["Auth"]
        document = collection.find_one({"userId": userId, "password": password})
        
        if document:
            # Simulating a connection delay for user experience
            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(2)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)
            print("\033[32mLogin successful!\033[0m")
            time.sleep(2)
            return True

        else:
            # Simulating a connection delay for user experience
            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(2)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)
            print("\033[1;31mInvalid userId or password.\033[0m")
            return False
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def changePassword(address):
    cls()
    printLogo()
    print("--------------------------------------------------")
    userId = input("Enter your user Id : ").lower()
    oldPass = getpass.getpass("Enter your old password: ")
    print("--------------------------------------------------")
    
    # Validating user input
    if not userId or not oldPass:
        print("\033[1;31mUserId and Password cannot be empty!\033[0m")
        time.sleep(2)
        return False

    oldPasswordHash = hash_password(oldPass)
    try:
        client = pym.MongoClient(address)
        database = client["RuVMultitoolv1"]
        collection = database["Auth"]
        document = collection.find_one({"userId": userId, "password": oldPasswordHash})

        if document:
            
            print("--------------------------------------------------")
            newPass = getpass.getpass("Enter your new password: ")
            confirmPass = getpass.getpass("Confirm your new password: ")
            print("--------------------------------------------------")

            if len(newPass) < 8:
                print("\033[1;31mNew password must be at least 8 characters long!\033[0m")
                time.sleep(2)
                return False

            if not any(char.isdigit() for char in newPass):
                print("\033[1;31mNew password must contain at least one digit!\033[0m")
                time.sleep(2)
                return False

            if newPass != confirmPass:
                print("\033[1;31mNew passwords do not match!\033[0m")
                time.sleep(2)
                return False
            
            oldPasswordHash = hash_password(oldPass)
            newPasswordHash = hash_password(newPass)

            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(1)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)
            print("\033[32mPassword changed successfully!\033[0m")
            time.sleep(1)
            collection.update_one(
                {"userId": userId}, {"$set": {"password": newPasswordHash}}
            )
            return True

        else:
            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(1)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)
            print("\033[1;31mInvalid userId or old password.\033[0m")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


# Starting main function


def main():

    attempts = 3

    while True:

        cls()
        printLogo()
        print("\033[38;5;45mWelcome to RuV Tools!\033[0m")
        print(
            """\n\033[32;211;23;255;145m[1] Login
            \n[2] Register
            \n[3] Change Password
            \n[4] Exit\033[0m"""
        )

        # Taking input
        choiceMain = msvcrt.getch()
        if choiceMain == b"\x1b":  # Escape key
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
        time.sleep(0.5)

        cls()
        printLogo()

        # Setting up conditions

        match (choiceMain):

            case b"1":

                result = loginUser("mongodb://localhost:27017/")

                if result == True:
                    break

                else:
                    attempts -= 1
                    if attempts == 1:
                        print(f"\n\033[1;33mYou have only {attempts} attempt left!\033[0m")
                    else:
                        print(f"\n\033[1;33mYou have only {attempts} attempts left!\033[0m")
                    print("\n\033[38;5;45mPress any key to return to main menu...\033[0m")
                    msvcrt.getch()
                    if attempts == 0:
                        print("\n\033[1;31mToo many failed attempts. Exiting...\033[0m")
                        time.sleep(2)
                        exit(0)
                    else:
                        continue

            case b"2":
                registerUser("mongodb://localhost:27017/")
                print("\n\033[38;5;45mPress any key to return to main menu...\033[0m")
                msvcrt.getch()

            case b"3":
                changePassword("mongodb://localhost:27017/")
                print("\n\033[38;5;45mPress any key to return to main menu...\033[0m")
                msvcrt.getch()

            case b"4":
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

            case _:
                print("\033[1;31mInvalid choice. Try again.\033[0m")
                print("\033[38;5;45mPress any key to return to main menu...\033[0m")
                msvcrt.getch()

    while True:

        # Setting up interface

        cls()
        printLogo()

        print(
            """[1] Get Hostname & IP Address
        \n[2] Get CPU Architecture
        \n[3] Get Current User
        \n[4] Exit"""
        )

        # Taking input
        choice = msvcrt.getch()
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

        time.sleep(0.5)

        cls()
        printLogo()

        # Setting up conditions
        match (choice):

            case b"1":
                getHost_Ip()
                print("\n\033[38;5;45mPress any key to return to main menu...\033[0m")
                msvcrt.getch()

            case b"2":
                get_CPU_Architecture()
                print("\n\033[38;5;45mPress any key to return to main menu...\033[0m")
                msvcrt.getch()

            case b"3":
                getUsername()
                print("\n\033[38;5;45mPress any key to return to main menu...\033[0m")
                msvcrt.getch()

            case b"4":
                for i in range(5, 0, -1):
                    cls()
                    printLogo()
                    print("Thank You for using our multitool")
                    if i == 1:
                        print(f"This program will terminate in {i} second")
                    else:
                        print(f"This program will terminate in {i} seconds")
                    time.sleep(1)
                break

            case _:
                print("Invalid choice. Try again.")
                print("\n\033[38;5;45mPress any key to return to main menu...\033[0m")
                msvcrt.getch()


if __name__ == "__main__":
    main()