#!/usr/bin/env python
# coding: utf-8
from colorama import Fore
from pathlib import Path
import time
import os
import shutil
import git
import argparse
import urllib

Pversion = "1.4.8"

parser = argparse.ArgumentParser()
parser.add_argument("-L", "--lastest_version", help="show the lastest program version", action="store_true")
parser.add_argument("-U", "--update", help="update the pentesting tools", action="store_true")
parser.add_argument("-I", "--installation", help="install the pentesting tools", action="store_true")
args = parser.parse_args()
clear = lambda: os.system('clear')

link = "https://pastebin.com/raw/JN9RC4Wj"
fvers = urllib.urlopen(link)
vers = fvers.read()

def install():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
    print("Installing gitpython")
    os.system("sudo pip install gitpython")
    print("Installing colorama")
    os.system("sudo pip install colorama")
    print("Installing pathlib")
    os.system("sudo pip install pathlib")
    print("Installing argparse")
    os.system("sudo pip isntall argparse")
    print("Installing Sqlmap")
    os.system("sudo apt install sqlmap")
    print("Installing jsql")
    os.system("sudo apt install jsql")
    print("Installing bbqsql")
    os.system("sudo apt install bbqsql")
    print("Installing nmap")
    os.system("sudo apt install nmap")
    print("Installing uniscan")
    os.system("sudo apt install uniscan")
    print("Installing Amap")
    os.system("sudo apt install amap")
    print("Installing Sqlninja")
    os.system("sudo apt install sqlninja")
    print("Installing sqlsus")
    os.system("sudo apt install sqlsus")
    print("Installing ShellNoob")
    os.system("sudo apt install shellnoob")
    print("Installing cewl")
    os.system("sudo apt install cewl")
    print("Installing airbase-ng")
    os.system("sudo apt install airbase-ng")
    print("Installing bully")
    os.system("sudo apt install bully")
    print("Installing nikto")
    os.system("sudo apt install nikto")
    print("Installing doona")
    os.system("sudo apt install doona")
    print("Inatlling dnstracer")
    os.system("sudo apt install dnstracer")
    print("Installing dnswalk")
    os.system("sudo apt install dnswalk")
    print("Installing dotdotpwn.pl")
    os.system("sudo apt install dotdotpwn")
    print("Installing enum4linux")
    os.system("sudo apt install enum4linux")
    print("Installing enumiax")
    os.system("sudo apt install enumiax")
    print("Installing eyewitness")
    os.system("sudo apt install eyewitness")
    print("Installing faraday")
    os.system("sudo apt install faraday")
    print("Installing fierce")
    os.system("sudo apt install fierce")
    print("Installing firewalk")
    os.system("sudo apt install firewalk")
    print("Installing fragroute")
    os.system("sudo apt install fragroute")
    print("Installing fragrouter")
    os.system("sudo apt install fragrouter")
    print("Installing ghost-phisher")
    os.system("sudo apt install ghost-phisher")
    print("Installing ohrwurm")
    os.system("sudo apt install ohrwurm")
    print("Installing oscanner")
    os.system("sudo apt install oscanner")
    print("Installing powerfuzzer")
    os.system("sudo apt install powerfuzzer")
    print("Installing sfuzz")
    os.system("sudo apt install sfuzz")
    print("Installing sidguess")
    os.system("sudo apt install sidguess")
    print("installing siparmyknife")
    os.system("sudo apt install siparmyknife")
    print("Installing tnscmd10g")
    os.system("sudo apt install tnscmd10g")
    print("Installing unix-privesc-check")
    os.system("sudo apt install unix-privesc-check")
    print("Installing yersinia")
    os.system("sudo apt install yersinia")

if args.lastest_version:
    link = "https://pastebin.com/raw/JN9RC4Wj"
    fvers = urllib.urlopen(link)
    vers = fvers.read()
    print("the lastest program version is" + Fore.GREEN + vers)
    print("your program version is" + Fore.GREEN + Pversion)
    os._exit(1)
elif args.update:
    install()
    print(Fore.GREEN + "Done Updating Pentesting Tools.")
    os._exit(1)
elif args.installation:
    install()
    print(Fore.GREEN + "Done Installing Pentesting Tools.")
    os._exit(1)

def startup():
    os.system("sudo pip install -r requirements.txt")
    os.system("python setup.py install")
    install()
    clear()

startup()
print(Fore.BLUE + "\n\n ██╗      █████╗ ███████╗██╗   ██╗███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗")
print(Fore.BLUE + " ██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝")
print(Fore.WHITE + " ██║     ███████║  ███╔╝  ╚████╔╝ ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  ")
print(Fore.WHITE + " ██║     ██╔══██║ ███╔╝    ╚██╔╝  ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  ")
print(Fore.RED + " ███████╗██║  ██║███████╗   ██║   ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗")
print(Fore.RED + " ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝ \n\n")

print(Fore.WHITE + "  Loaded " + Fore.GREEN + "35" + Fore.WHITE + " Tools\n  Your Version " + Fore.YELLOW + Pversion +" - Pre-Release\n" + Fore.WHITE + "  Last Version " + Fore.YELLOW + vers + Fore.WHITE + "\n  Try python LazySource" + Fore.YELLOW + " -h" + Fore.WHITE + "\n  Made By " + Fore.BLUE + "Vaxure" + Fore.WHITE + "\n  <---------------------->\n")
print(" 1) Sqlmap          2) JSql")
print(" 3) BBQSQL          4) Nmap")
print(" 5) Uniscan         6) Amap")
print(" 7) Sqlninja        8) Sqlsus")
print(" 9) ShellNoob       10) CeWL")
print(" 11) Airbase-ng     12) Bully")
print(" 13) Nikto          14) Doona")
print(" 15) Dnstracer      16) Dnswalk")
print(" 17) DotDotPwn      18) Enum4linux")
print(" 19) EnumIAX        20) EyeWitness")
print(" 21) Faraday        22) Fierce")
print(" 23) Firewalk       24) Fragroute")
print(" 25) Fragrouter     26) Ghost Phisher")
print(" 27) Ohrwurm        28) Oscanner")
print(" 29) Powerfuzzer    30) Sfuzz")
print(" 31) SidGuesser     32) SIPArmyKnife")
print(" 33) Tnscmd10g      34) Unix-Privesc-Check")
print(" 35) Yersinia")

text = raw_input(Fore.WHITE + "\n LazySource > ")
if text == "1":
    clear()
    os.system("sqlmap")
elif text == "2":
    clear()
    os.system("jsql")
if text == "3":
    clear()
    os.system("bbqsql")
elif text == "4":
    clear()
    os.system("nmap")
elif text == "5":
    clear()
    os.system("uniscan")
elif text == "6":
    clear()
    os.system("amap")
elif text == "7":
    clear()
    os.system("sqlninja -h")
elif text == "8":
    clear()
    os.system("sqlsus")
elif text == "9":
    clear()
    os.system("shellnoob -h")
elif text == "10":
    clear()
    os.system("cewl --help")
elif text == "11":
    clear()
    os.system("airbase-ng --help")
elif text == "12":
    clear()
    os.system("bully -h")
elif text == "13":
    clear()
    os.system("nikto -Help")
elif text == "14":
    clear()
    os.system("doona -h")
elif text == "15":
    clear()
    os.system("dnstracer")
elif text == "16":
    clear()
    os.system("dnswalk --help")
elif text == "17":
    clear()
    os.system("dotdotpwn.pl")
elif text == "18":
    clear()
    os.system("enum4linux -h")
elif text == "19":
    clear()
    os.system("enumiax -h")
elif text == "20":
    clear()
    os.system("eyewitness -h")
elif text == "21":
    clear()
    os.system("python-faraday -h")
elif text == "22":
    clear()
    os.system("fierce -h")
elif text == "23":
    clear()
    os.system("firewalk -h")
elif text == "24":
    clear()
    os.system("fragroute")
elif text == "25":
    clear()
    os.system("fragrouter")
elif text == "26":
    clear()
    os.system("ghost-phisher")
elif text == "27":
    clear()
    os.system("ohrwurm")
elif text == "28":
    clear()
    os.system("oscanner")
elif text == "29":
    clear()
    os.system("powerfuzzer")
elif text == "30":
    clear()
    os.system("sfuzz -h")
elif text == "31":
    clear()
    os.system("sidguess")
elif text == "32":
    clear()
    os.system("siparmyknife")
elif text == "33":
    clear()
    os.system("tnscmd10g")
elif text == "34":
    clear()
    os.system("unix-privesc-check")
elif text == "35":
    clear()
    os.system("yersinia -h")
else:
    raise SystemExit
