# coding: utf-8
from colorama import Fore
import time
import os
from pathlib import Path
from git import RemoteProgress
#import exchanges

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
    mypath = Path().absolute()
    os.system('rm -r ' + mypath)
    os.system('cd ..')
    git.Repo.clone_from('https://github.com/Vaxure1337/LazySource', '/home/')
    print("The file has been installed in the folder home")
elif text == "1":
    # Sqlmap
    print("Sqlmap")
elif text == "2":
    # JSql
    print("JSql")
if text == "3":
    # BBQSQL
    print("BBQSQL")
elif text == "4":
    # Nmap
    print("Nmap")
elif text == "5":
    # Uniscan
    print("Uniscan")
elif text == "6":
    print("Bitcoin")
    #exchanges.bitfinex.get_current_price()
else:
    raise SystemExit


