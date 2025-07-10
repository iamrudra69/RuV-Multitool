import socket
import platform
import getpass

from Functions import interface

menuOptions = "[1] Get Hostname & IP Address 🌐\n[2] Get CPU Architecture 🖥️\n[3] Get Current User 👤"


def getHostIp():
    print(f"\033[92mHostname : {socket.gethostname()}\033[0m")
    try:
        # This does not actually connect to the Internet, just determines the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_address = s.getsockname()[0]
        s.close()
    except Exception:
        ip_address = "Unable to determine IP"
    print(f"\033[92mIP Address : {ip_address}\033[0m")


def get_CPU_Architecture():
    print(f"\033[92mCPU Architecture : {platform.machine()}\033[0m")


def getUsername():
    print(f"\033[92mUser : {getpass.getuser()}\033[0m")


def systemInfoMenu():
    interface("System_Info", menuOptions, getHostIp, get_CPU_Architecture, getUsername)