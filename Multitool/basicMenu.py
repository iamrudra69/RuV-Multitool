import requests as r
import random 
import msvcrt
import time 
from pyfiglet import Figlet
import os
import sys
import pygame
import shutil

from functions import interface ,inputColor, outputColor, errorColor, line, cls


menuOptions = "[1] Get currency exchange rate 💱\n[2] Generate a password 🔐\n[3] Use Timer ⏰"

def fetchExchangeRates(currencyCode):
    url = f"https://v6.exchangerate-api.com/v6/ac60b2859a97d9cdf969f829/latest/{currencyCode}"

    try:
        response = r.get(url, timeout=10)
        if not response:
            return False
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx or 5xx)
        data = response.json()       # Convert JSON response to Python dict
        return data

    except r.exceptions.HTTPError as http_err:
        print(f"{errorColor("Currency code not found in the database ❌ ")}")
    except r.exceptions.ConnectionError:
        print(f"{errorColor(f"[ERROR] Connection failed.")}")
    except r.exceptions.Timeout:
        print(f"{errorColor(f"[ERROR] Request timed out.")}")
    except r.exceptions.RequestException as err:
        print(f"{errorColor(f"[REQUEST ERROR] {err}")}")
    except Exception as e:
        print(f"{errorColor(f"[UNKNOWN ERROR] {e}")}")

def getCurrencyRates():

    line()
    currCode = input(inputColor(f"Enter the currency code 💵 : ")).upper()

    
    exchangeData = fetchExchangeRates(currCode)

    if exchangeData == False:
        line()
        print(errorColor("Currency code not found in the database ❌ "))
    else:
        converstionRates = exchangeData["conversion_rates"]

        if exchangeData:

            print(outputColor("Exchange rate data received successfuly ✅"))
            
            line()
            currCodeforExchange = input(inputColor(f"{currCode} to ? 💵 : ")).upper()
            amount = int(input(inputColor("Enter the amount : ")))
            
            if currCodeforExchange in converstionRates:
                line()
                print(outputColor(f"1 {currCode} = {converstionRates[currCodeforExchange]} {currCodeforExchange}"))
                print(outputColor(f"{amount} {currCode} = {(converstionRates[currCodeforExchange])*amount} {currCodeforExchange}"))
            else:
                line()
                print(errorColor(f"{currCodeforExchange} does't exist in the data base ! ❌"))

def passwordGenerator():

    characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&-_1234567890")
    
    try:
        line()
        passLen = int(input(inputColor("Enter the password length (8 characters by default) 🔐 : "))) or 8
        password = ""

        for i in range(passLen):
            password += random.choice(characters)
        line()
        
        print(inputColor("Press y to save password in a file or any key to cancel"))
        saveAsFile = msvcrt.getch().lower()
    
        if saveAsFile == b'y':
            try:
                line()
                with open("password.txt", "w+") as f:
                    f.write(f"password : {password}")
                    print(outputColor(f"password : {password}"))
                    print(outputColor("File written successfully!"))
            except Exception as e:
                print(errorColor(f"An Error Occured writing file ! : {e}"))
            
        
    except Exception as e:
        print(errorColor(f"An Error Occured ! : {e}"))

def resource_path(relative_path):
    # Works whether it's a script or a bundled .exe
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

def playSound():
    try:
        # print(errorColor("This prank will play different sounds to disturb the people. 🎧"))
        line()

        pygame.mixer.init()
        assets = resource_path("assets")

        if not os.path.isdir(assets):
            print(errorColor(f"❌ Asset folder '{assets}' not found. 📁"))
            line()
            return

        sound_files = [f for f in os.listdir(assets) if f.endswith((".mp3", ".wav"))]

        if not sound_files:
            print(errorColor("⚠️ No sound files found in the specified folder. 📭"))
            line()
            return

        # Optional: Extract all sounds to working directory for debug or reuse
        extract_dir = os.path.join(os.getcwd(), "extracted_sounds")
        os.makedirs(extract_dir, exist_ok=True)
        for f in sound_files:
            shutil.copyfile(os.path.join(assets, f), os.path.join(extract_dir, f))

        while True:
            try:
                sound = random.choice(sound_files)
                full_path = os.path.join(assets, sound)
                pygame.mixer.music.load(full_path)
                pygame.mixer.music.play()

                print(outputColor(f"🔊 Playing: {sound} 🎶"))

                while pygame.mixer.music.get_busy():
                    time.sleep(1)

                time.sleep(random.randint(1, 5))

            except Exception as e:
                print(errorColor(f"❌ Error playing sound: {e} 💥"))
                line()
                time.sleep(2)

    except KeyboardInterrupt:
        print("\n")
        line()
        print(errorColor("⛔ Sound playback interrupted by user (Ctrl+C). 🛑"))
        pygame.mixer.music.stop()
        time.sleep(1)

    except Exception as e:
        print("\n")
        line()
        print(errorColor(f"❌ Initialization failed: {e} 🚨"))

def timer():

    line()
    hours = int(input(inputColor(f"Enter the time in hours : ")))
    minutes = int(input(inputColor(f"Enter the time in minutes : ")))
    seconds = int(input(inputColor(f"Enter the time in seconds : ")))
    line()
    f = Figlet(font='big')

    if seconds >= 60:
        minutes += seconds // 60
        seconds %= 60   

    if minutes >= 60:
        hours += minutes // 60
        minutes %= 60   

    totalTime = (hours * 3600) + (minutes * 60) + seconds
    try :
        while totalTime > -1:
            
            if seconds == -1:
                minutes -= 1
                seconds = 59
            if minutes == -1:
                hours -= 1
                minutes = 59

            cls()
            
            formattedTime = f.renderText(f"{hours} : {minutes} : {seconds}")
            print(outputColor(formattedTime))

            totalTime -= 1 
            seconds -= 1
            time.sleep(1)

        print(errorColor("Press (Ctrl+C) on the Keyboard to Stop. 🛑"))
        playSound()

    except Exception as e:
        print(errorColor(e))

    except KeyboardInterrupt:
        print(errorColor("⛔ Keyboard interrupted by user (Ctrl+C). 🛑"))

def basicOpsMenu():
    interface("Basic_Operations" ,menuOptions, getCurrencyRates, passwordGenerator, timer)