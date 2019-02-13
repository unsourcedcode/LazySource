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

parser = argparse.ArgumentParser()
parser.add_argument("-L", "--lastest_version", help="show the lastest program version", action="store_true")
parser.add_argument("-U", "--update", help="update the pentesting tools", action="store_true")
args = parser.parse_args()

def install():
    os.system("sudo apt-get update")
    os.system("sudo apt-get upgrade")
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

if args.lastest_version:
    link = "http://www.lazysource.gq/version"
    fvers = urllib.urlopen(link)
    vers = fvers.read()
    print("the lastest program version is" + Fore.GREEN + vers)
    os._exit(1)
elif args.update:
    install()
    print(Fore.GREEN + "Done Updating Pentesting Tools.")
    os._exit(1)

def startup():
    os.system("python setup.py install")
    install()
    os.system("clear")

startup()
print(Fore.BLUE + "\n\n ██╗      █████╗ ███████╗██╗   ██╗███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗")
print(Fore.BLUE + " ██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝")
print(Fore.WHITE + " ██║     ███████║  ███╔╝  ╚████╔╝ ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  ")
print(Fore.WHITE + " ██║     ██╔══██║ ███╔╝    ╚██╔╝  ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  ")
print(Fore.RED + " ███████╗██║  ██║███████╗   ██║   ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗")
print(Fore.RED + " ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝ \n\n")

print(Fore.WHITE + "  Loaded " + Fore.GREEN + "19" + Fore.WHITE + " Tools\n  Version " + Fore.YELLOW + "1.4.5" + Fore.WHITE +"\n  Made By " + Fore.BLUE + "Vaxure" + Fore.WHITE + "\n<---------------------->\n")
print(" 1) Sqlmap")
print(" 2) JSql")
print(" 3) BBQSQL")
print(" 4) Nmap")
print(" 5) Uniscan")
print(" 6) Amap")
print(" 7) Sqlninja")
print(" 8) Sqlsus")
print(" 9) ShellNoob")
print(" 10) CeWL")
print(" 11) Airbase-ng")
print(" 12) Bully")
print(" 13) Nikto")
print(" 14) Doona")
print(" 15) Dnstracer")
print(" 16) Dnswalk")
print(" 17) DotDotPwn")
print(" 18) Enum4linux")
print(" 19) EnumIAX")

text = raw_input(Fore.WHITE + "\n LazySource > ")
if text == "00":
    #os.system('rm -r ' + os.getcwd())
    #os.system('rm -r /home/LazySource')
    filepath = os.path.abspath('')
    shutil.rmtree(filepath)
    git.Repo.clone_from('https://github.com/Vaxure1337/LazySource', filepath)
    print("The file has been installed in the folder home")
elif text == "1":
    os.system("clear")
    os.system("sqlmap")
elif text == "2":
    os.system("clear")
    os.system("jsql")
if text == "3":
    os.system("clear")
    os.system("bbqsql")
elif text == "4":
    os.system("clear")
    os.system("nmap")
elif text == "5":
    os.system("clear")
    os.system("uniscan")
elif text == "6":
    os.system("clear")
    os.system("amap")
elif text == "7":
    os.system("clear")
    os.system("sqlninja -h")
elif text == "8":
    os.system("clear")
    os.system("sqlsus")
elif text == "9":
    os.system("clear")
    os.system("shellnoob -h")
elif text == "10":
    os.system("clear")
    os.system("cewl --help")
elif text == "11":
    os.system("clear")
    os.system("airbase-ng --help")
elif text == "12":
    os.system("clear")
    os.system("bully -h")
elif text == "13":
    os.system("clear")
    os.system("nikto -Help")
elif text == "14":
    os.system("clear")
    os.system("doona -h")
elif text == "15":
    os.system("clear")
    os.system("dnstracer")
elif text == "16":
    os.system("clear")
    os.system("dnswalk --help")
elif text == "17":
    os.system("clear")
    os.system("dotdotpwn.pl")
elif text == "18":
    os.system("clear")
    os.system("enum4linux -h")
elif text == "19":
    os.system("clear")
    os.system("enumiax -h")
else:
    raise SystemExit
