import socket
import platform
import getpass

from functions import interface, outputColor, errorColor, line

menuOptions = "[1] Get Hostname & IP Address 🌐\n[2] Get CPU Architecture 🖥️\n[3] Get Current User 👤"

def getHostIp():
    try:
        hostname = socket.gethostname()
        line()
        print(outputColor(f"Hostname : {hostname} 🌐"))

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
        print(outputColor(f"IP Address : {ip_address} 📶"))

    except Exception as e:
        print("\n")
        line()
        print(errorColor(f"❌ Error retrieving IP address: {e}"))

def get_CPU_Architecture():
    try:
        arch = platform.machine()
        line( )
        print(outputColor(f"CPU Architecture : {arch} 🧠"))
    except Exception as e:
        print("\n")
        line( )
        print(errorColor(f"❌ Error retrieving architecture: {e}"))

def getUsername():
    try:
        user = getpass.getuser()
        line()
        print(outputColor(f"User : {user} 👤"))
    except Exception as e:
        print("\n")
        print(errorColor(f"❌ Error retrieving username: {e}"))
        line()

def systemInfoMenu():
    interface("System_Info", menuOptions, getHostIp, get_CPU_Architecture, getUsername)
