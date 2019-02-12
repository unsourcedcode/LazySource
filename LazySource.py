#!/usr/bin/env python
# coding: utf-8
from colorama import Fore
import time
import os
import shutil
from pathlib import Path
import git
#import exchanges

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

print(Fore.WHITE + "  Loaded " + Fore.GREEN + "6" + Fore.WHITE + " Tools\n  Version " + Fore.YELLOW + "1.4" + Fore.WHITE +"\n  Made By " + Fore.BLUE + "Vaxure" + Fore.WHITE + "\n<---------------------->\n")
print(" 1) Sqlmap")
print(" 2) JSql")
print(" 3) BBQSQL")
print(" 4) Nmap")
print(" 5) Uniscan")
print(" 6) Bitcoin Price")
print(" 00) Update")

text = raw_input(Fore.WHITE + " LazySource > ")
if text == "00":
    #os.system('rm -r ' + os.getcwd())  
    #os.system('rm -r /home/LazySource')
    filepath = os.path.abspath('')
    shutil.rmtree(filepath)
    git.Repo.clone_from('https://github.com/Vaxure1337/LazySource', filepath)
    print("The file has been installed in the folder home")
elif text == "1":
    os.system("sqlmap")
elif text == "2":
    os.system("jsql")
if text == "3":
    os.system("bbqsql")
elif text == "4":
    os.system("nmap")
elif text == "5":
    os.system("uniscan")
elif text == "6":
    print("Bitcoin")
    #exchanges.bitfinex.get_current_price()
else:
    raise SystemExit


