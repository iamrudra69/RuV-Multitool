import pymongo as pym
import getpass
import hashlib
import time
import string

from Functions import interface, cls, printLogo

menuOptions = "[1] Register User 📝\n[2] Login 🔑\n[3] Change Password 🔄"
dbAddress = "mongodb://localhost:27017/"


def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()


def registerUser():
    print(f"\033[1;33m=========================\033[0m")
    username = input("\033[1;36mEnter your username :  \033[0m").lower()
    passW = getpass.getpass("\033[1;36mEnter your password:  \033[0m")

    if not username or not passW:
        print(f"\033[1;33m=========================\033[0m")
        print("\033[1;31mUsername or Password cannot be empty!\033[0m")
        time.sleep(2)
        return False

    if len(passW) < 8:
        print(f"\033[1;33m=========================\033[0m")
        print("\033[1;31mNew password must be at least 8 characters long!\033[0m")
        time.sleep(2)
        return False

    if not any(char.isdigit() for char in passW):
        print(f"\033[1;33m=========================\033[0m")
        print("\033[1;31mNew password must contain at least one digit!\033[0m")
        time.sleep(2)
        return False

    if not any(char in string.punctuation for char in passW):
        print(f"\033[1;33m=========================\033[0m")
        print(
            "\033[1;31mNew password must contain at least one special character!\033[0m"
        )
        time.sleep(2)
        return False

    if not any(char.isalpha() for char in passW):
        print(f"\033[1;33m=========================\033[0m")
        print(
            "\033[1;31mNew password must contain at least one alphabet character!\033[0m"
        )
        time.sleep(2)
        return False

    confirmPass = getpass.getpass("\033[1;36mConfirm your password:  \033")
    print(f"\033[1;33m=========================\033[0m")

    if passW != confirmPass:
        print("\033[1;31mPasswords do not match!\033[0m")
        time.sleep(2)
        return False

    password = hashPassword(passW)

    try:
        client = pym.MongoClient(dbAddress)
        database = client["RuVMultitoolv1"]
        collection = database["Auth"]
        document = collection.find_one({"username": username})

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
            collection.insert_one({"username": username, "password": password})
            return "1"

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def loginUser():

    print(f"\033[1;33m=========================\033[0m")
    username = input("\033[1;36mEnter your username :  \033[0m").lower()
    passW = getpass.getpass("\033[1;36mEnter your password:  \033[0m")

    if not username or not passW:
        print(f"\033[1;33m=========================\033[0m")
        print("\033[1;31mUsername or Password cannot be empty!\033[0m")
        time.sleep(2)
        return False

    print(f"\033[1;33m=========================\033[0m")

    password = hashPassword(passW)

    try:
        client = pym.MongoClient(dbAddress)
        database = client["RuVMultitoolv1"]
        collection = database["Auth"]
        document = collection.find_one({"username": username, "password": password})

        if document:
            # Simulating a connection delay for user experience
            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(2)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)
            print("\033[32mLogin successful!\033[0m")
            time.sleep(2)
            return "login_success"

        else:
            # Simulating a connection delay for user experience
            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(2)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)
            print("\033[1;31mInvalid username or password.\033[0m")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def changePassword():

    print(f"\033[1;33m=========================\033[0m")
    username = input("\033[1;36mEnter your username:  \033").lower()
    oldPass = getpass.getpass("\033[1;36mEnter your password:  \033")

    # Validating user input
    if not username or not oldPass:
        print(f"\033[1;33m=========================\033[0m")
        print("\033[1;31mUsername or Password cannot be empty!\033[0m")
        time.sleep(2)
        return False

    oldPasswordHash = hashPassword(oldPass)

    try:
        client = pym.MongoClient(dbAddress)
        database = client["RuVMultitoolv1"]
        collection = database["Auth"]
        document = collection.find_one(
            {"username": username, "password": oldPasswordHash}
        )

        if document:
            print(f"\033[1;33m=========================\033[0m")
            newPass = getpass.getpass("\033[1;36mEnter your new password:  \033")

            if len(newPass) < 8:
                print(f"\033[1;33m=========================\033[0m")
                print(
                    "\033[1;31mNew password must be at least 8 characters long!\033[0m"
                )
                time.sleep(2)
                return False

            if not any(char.isdigit() for char in newPass):
                print(f"\033[1;33m=========================\033[0m")
                print("\033[1;31mNew password must contain at least one digit!\033[0m")
                time.sleep(2)
                return False

            if not any(char in string.punctuation for char in newPass):
                print(f"\033[1;33m=========================\033[0m")
                print(
                    "\033[1;31mNew password must contain at least one special character!\033[0m"
                )
                time.sleep(2)
                return False

            if not any(char.isalpha() for char in newPass):
                print(f"\033[1;33m=========================\033[0m")
                print(
                    "\033[1;31mNew password must contain at least one alphabet character!\033[0m"
                )
                time.sleep(2)
                return False

            confirmPass = getpass.getpass("\033[1;36mConfirm your new password:  \033")
            print(f"\033[1;33m=========================\033[0m")

            if newPass != confirmPass:
                print("\033[1;31mNew passwords do not match!\033[0m")
                time.sleep(2)
                return False

            oldPasswordHash = hashPassword(oldPass)
            newPasswordHash = hashPassword(newPass)

            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(1)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)
            print("\033[32mPassword changed successfully!\033[0m")
            time.sleep(1)
            collection.update_one(
                {"username": username}, {"$set": {"password": newPasswordHash}}
            )
            return True

        else:
            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(1)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)
            print("\033[1;31mInvalid username or old password.\033[0m")
            return False

    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def authMenu():
    interface("Auth", menuOptions, registerUser, loginUser, changePassword)