# coding: utf-8
from colorama import Fore

print(Fore.BLUE + "\n\n ██╗      █████╗ ███████╗██╗   ██╗███████╗ ██████╗ ██╗   ██╗██████╗  ██████╗███████╗")
print(Fore.BLUE + " ██║     ██╔══██╗╚══███╔╝╚██╗ ██╔╝██╔════╝██╔═══██╗██║   ██║██╔══██╗██╔════╝██╔════╝")
print(Fore.WHITE + " ██║     ███████║  ███╔╝  ╚████╔╝ ███████╗██║   ██║██║   ██║██████╔╝██║     █████╗  ")
print(Fore.WHITE + " ██║     ██╔══██║ ███╔╝    ╚██╔╝  ╚════██║██║   ██║██║   ██║██╔══██╗██║     ██╔══╝  ")
print(Fore.RED + " ███████╗██║  ██║███████╗   ██║   ███████║╚██████╔╝╚██████╔╝██║  ██║╚██████╗███████╗")
print(Fore.RED + " ╚══════╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝ \n\n")

print(Fore.WHITE + "  Loaded " + Fore.GREEN + "6" + Fore.WHITE + " Tools\n  Version " + Fore.YELLOW + "1.2" + Fore.WHITE +"\n  Made By " + Fore.BLUE + "Vaxure" + Fore.WHITE + "\n<---------------------->\n")
print(" 1) Sqlmap")
print(" 2) JSql")
print(" 3) BBQSQL")
print(" 4) Nmap")
print(" 5) Uniscan")
print(" 6) Bitcoin Price")

text = input(Fore.WHITE + " LazySource > ")
if text == "2":
    # Sqlmap
else:
    raise SystemExit
if text == "2":
    # JSql
else:
    raise SystemExit
if text == "3":
    # BBQSQL
else:
    raise SystemExit
if text == "4":
    # Nmap
else:
    raise SystemExit
if text == "5":
    # Uniscan
else:
    raise SystemExit
if text == "6":
    bitfinex.get_current_price()
else:
    raise SystemExit


