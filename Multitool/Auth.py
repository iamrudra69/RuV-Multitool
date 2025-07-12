import pymongo as pym 
import getpass
import hashlib
import time
import string

from functions import interface, inputColor, outputColor, errorColor, outputLine

menuOptions = "[1] Register User 📝\n[2] Login 🔑\n[3] Change Password 🔄"
dbAddress   = "mongodb://localhost:27017/"

def hashPassword(password):
    return hashlib.sha256(password.encode()).hexdigest()

def registerUser():
    try:
        outputLine()
        username = input(inputColor("Enter your username 🧑‍💻 : ")).lower()
        passW    = getpass.getpass(inputColor("Enter your password 🔒 : "))

        if not username or not passW:
            outputLine()
            print(errorColor("Username or Password cannot be empty ❗"))
            time.sleep(2)
            return False

        if len(passW) < 8:
            outputLine()
            print(errorColor("New password must be at least 8 characters long ⚠️"))
            time.sleep(2)
            return False

        if not any(char.isdigit() for char in passW):
            outputLine()
            print(errorColor("New password must contain at least one digit 🔢"))
            time.sleep(2)
            return False

        if not any(char in string.punctuation for char in passW):
            outputLine()
            print(errorColor("New password must contain at least one special character ❗"))
            time.sleep(2)
            return False

        if not any(char.isalpha() for char in passW):
            outputLine()
            print(errorColor("New password must contain at least one alphabet character 🔠"))
            time.sleep(2)
            return False

        confirmPass = getpass.getpass(inputColor("Confirm your password ✅ : "))
        outputLine()

        if passW != confirmPass:
            print(errorColor("Passwords do not match ❌"))
            time.sleep(2)
            return False

        password = hashPassword(passW)

        try:
            client     = pym.MongoClient(dbAddress)
            database   = client["RuVMultitoolv1"]
            collection = database["Auth"]
            document   = collection.find_one({"username": username})

            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(2)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)

            if document:
                print(errorColor("User already exists ❗"))
                return False

            collection.insert_one({"username": username, "password": password})
            print(outputColor("Registration successful ✅"))
            return True

        except Exception as e:
            print(errorColor(f"An error occurred: {e} ❌"))
            return False

    except KeyboardInterrupt:
        print("\n")
        outputLine()
        print(errorColor("⛔ Operation cancelled by user (Ctrl+C)"))
        return False

def loginUser():
    try:
        outputLine()
        username = input(inputColor("Enter your username 🧑‍💻 : ")).lower()
        passW    = getpass.getpass(inputColor("Enter your password 🔒 : "))

        if not username or not passW:
            outputLine()
            print(errorColor("Username or Password cannot be empty ❗"))
            time.sleep(2)
            return False

        outputLine()
        password = hashPassword(passW)

        try:
            client     = pym.MongoClient(dbAddress)
            database   = client["RuVMultitoolv1"]
            collection = database["Auth"]
            document   = collection.find_one({"username": username, "password": password})

            print("\033[38;5;27mConnecting to the Server !\033[0m")
            time.sleep(2)
            print("\033[38;5;45mConnection successful!\033[0m")
            time.sleep(1)

            if document:
                print(outputColor("Login successful 🔓"))
                time.sleep(0.5)
                return "login_success"
            else:
                print(errorColor("Invalid username or password ❌"))
                return False

        except Exception as e:
            print(errorColor(f"An error occurred: {e} ❌"))
            return False

    except KeyboardInterrupt:
        print("\n")
        outputLine()
        print(errorColor("⛔ Operation cancelled by user (Ctrl+C)"))
        return False

def changePassword():
    try:
        outputLine()
        username = input(inputColor("Enter your username 🧑‍💻 : ")).lower()
        oldPass  = getpass.getpass(inputColor("Enter your password 🔒 : "))

        if not username or not oldPass:
            outputLine()
            print(errorColor("Username or Password cannot be empty ❗"))
            time.sleep(2)
            return False

        oldPasswordHash = hashPassword(oldPass)

        try:
            client     = pym.MongoClient(dbAddress)
            database   = client["RuVMultitoolv1"]
            collection = database["Auth"]
            document   = collection.find_one({"username": username, "password": oldPasswordHash})

            if document:
                outputLine()
                newPass = getpass.getpass(inputColor("Enter your new password 🔐 : "))

                if len(newPass) < 8:
                    outputLine()
                    print(errorColor("New password must be at least 8 characters long ⚠️"))
                    time.sleep(2)
                    return False

                if not any(char.isdigit() for char in newPass):
                    outputLine()
                    print(errorColor("New password must contain at least one digit 🔢"))
                    time.sleep(2)
                    return False

                if not any(char in string.punctuation for char in newPass):
                    outputLine()
                    print(errorColor("New password must contain at least one special character ❗"))
                    time.sleep(2)
                    return False

                if not any(char.isalpha() for char in newPass):
                    outputLine()
                    print(errorColor("New password must contain at least one alphabet character 🔠"))
                    time.sleep(2)
                    return False

                confirmPass = getpass.getpass(inputColor("Confirm your new password ✅ : "))
                outputLine()

                if newPass != confirmPass:
                    print(errorColor("New passwords do not match ❌"))
                    time.sleep(2)
                    return False

                newPasswordHash = hashPassword(newPass)

                print("\033[38;5;27mConnecting to the Server !\033[0m")
                time.sleep(1)
                print("\033[38;5;45mConnection successful!\033[0m")
                time.sleep(1)
                print(outputColor("Password changed successfully 🔁"))
                time.sleep(1)
                collection.update_one({"username": username}, {"$set": {"password": newPasswordHash}})
                return True

            else:
                print("\033[38;5;27mConnecting to the Server !\033[0m")
                time.sleep(1)
                print("\033[38;5;45mConnection successful!\033[0m")
                time.sleep(1)
                print(errorColor("Invalid username or old password ❌"))
                return False

        except Exception as e:
            print(errorColor(f"An error occurred: {e} ❌"))
            return False

    except KeyboardInterrupt:
        print("\n")
        outputLine()
        print(errorColor("⛔ Operation cancelled by user (Ctrl+C)"))
        return False

def authMenu():
    interface("Auth", menuOptions, registerUser, loginUser, changePassword)