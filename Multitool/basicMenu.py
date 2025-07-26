import requests as r
import random 
import msvcrt
import time 
from pyfiglet import Figlet
import tempfile
import subprocess

from functions import interface ,inputColor, outputColor, errorColor, line, cls

menuOptions = "[1] Get currency exchange rate 💱\n[2] Generate a password 🔐\n[3] Use Timer ⏰"

asciiDigits = {
    "0": [" ██████ ", "██    ██", "██    ██", "██    ██", " ██████ "],
    "1": ["   ██   ", " ████   ", "   ██   ", "   ██   ", " ██████ "],
    "2": [" ██████ ", "     ██ ", " ██████ ", "██      ", "███████ "],
    "3": [" ██████ ", "     ██ ", " ██████ ", "     ██ ", " ██████ "],
    "4": ["██   ██ ", "██   ██ ", "███████ ", "     ██ ", "     ██ "],
    "5": ["███████ ", "██      ", "██████  ", "     ██ ", "██████  "],
    "6": [" ██████ ", "██      ", "██████  ", "██   ██ ", " ██████ "],
    "7": ["███████ ", "     ██ ", "    ██  ", "   ██   ", "  ██    "],
    "8": [" ██████ ", "██   ██ ", " ██████ ", "██   ██ ", " ██████ "],
    "9": [" ██████ ", "██   ██ ", " ██████ ", "     ██ ", " ██████ "],
    ":": ["        ", "   ██   ", "        ", "   ██   ", "        "]
}

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

    characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%=+*><&-_1234567890")
    
    try:

        line()  
        passLen = int(input(inputColor("Enter the password length (8 characters by default) 🔐 : "))) or 8
        password = ""
       
        if passLen > 256:
            line()
            print(errorColor("❌ Password length could not be more than 256 characters !!!"))

        else:
            for i in range(passLen):
                password += random.choice(characters)
            
            line()
            print(outputColor(f"password : {password}"))
            
            line()
            print(inputColor("Press y to save password in a file or any key to cancel"))
            
            saveAsFile = msvcrt.getch().lower()
        
            if saveAsFile == b'y':
                try:
                    line()
                    with open("password.txt", "w+") as f:
                        f.write(f"password : {password}")
                        print(outputColor("File written successfully!"))
                except Exception as e:
                    print(errorColor(f"❌ An Error Occured writing file ! : {e}"))
            else:
                print(outputColor("❌ Password not written in the file !"))    
    
    except ValueError:
            line()
            print(errorColor(f"❌ Invalid input the given input is not an integer!"))

    except Exception as e:
        line()
        print(errorColor(f"❌ An Error Occured ! : {e}"))

def printAsciiTime(h, m, s):
    time_str = f"{h:02}:{m:02}:{s:02}"
    rows = [""] * 5
    for ch in time_str:
        for i in range(5):
            rows[i] += asciiDigits[ch][i] + "  "
    for row in rows:
        print(outputColor(row))

def timer():

    line()
    hours = int(input(inputColor(f"Enter the time in hours : ")))
    minutes = int(input(inputColor(f"Enter the time in minutes : ")))
    seconds = int(input(inputColor(f"Enter the time in seconds : ")))
    line()

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
            
            printAsciiTime(f"{hours:02}", f"{minutes:02}", f"{seconds:02}")

            totalTime -= 1 
            seconds -= 1
            time.sleep(1)

        line()
        print(errorColor("Press (Ctrl+C) on the Keyboard to Stop. 🛑"))
        line()
        
        writeAbleText = "🆃🅸🅼🅴 🅵🅸🅽🅸🆂🅷🅴🅳"

        while True:

            with tempfile.NamedTemporaryFile(delete=False, suffix=".txt", mode='w', encoding='utf-8') as temp_file:
                temp_file.write(writeAbleText)
                temp_path = temp_file.name

            subprocess.Popen(["notepad.exe", temp_path])
            print(outputColor("It will open again in 10 seconds !"))
            time.sleep(10)


    except Exception as e:
        line()
        print(errorColor(e))

    except KeyboardInterrupt:
        line()
        print(errorColor("⛔ Keyboard interrupted by user (Ctrl+C). 🛑"))

def basicOpsMenu():
    interface("Basic_Operations" ,menuOptions, getCurrencyRates, passwordGenerator, timer)