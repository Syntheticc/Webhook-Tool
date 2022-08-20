import os
import sys
import time
from colorama import Fore
import dhooks
import requests 
import requests
import os
import json
import ctypes
import webbrowser as wb
from colorama import Fore, init
from discord_webhook import DiscordEmbed, DiscordWebhook
import requests
import os
import colorama
import sys
import time

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./10)
slowprint(Fore.RED + "Welcome to Synful Spammer!")
slowprint(Fore.RED + "We are happy to have you back")
time.sleep(1)
print(chr(27)+'[2j')
print('\033c')
print('\x1bc')

def spammer():
    webhook = input(Fore.BLUE + "[+] Enter your webhook > ")
    message = input(Fore.BLUE + "[+] Enter The Message: ")
    try:
        while True:
            try:
                time.sleep(0.3)
                data = requests.post(webhook, json={"content" : message})
                if data.status_code == 204:
                    print("[+] Sent [" + message +"]")
            except:
                print("Error")
                time.sleep(5)
                main()
    except KeyboardInterrupt:
        print("Succesfully Spammed The Webhook")
        time.sleep(2)
        sys.exit

def delete():
    webhook = input(Fore.RED + "[+] Enter Webhook Link > ")
    deletehook = requests.delete(webhook)
    the = requests.get(webhook)
    if the.status_code == 404:
      print(Fore.GREEN + "[+] Webhook Deleted")

def info():
   webhook= input(Fore.BLUE + "[+] Enter Webhook > ")
   r = requests.get(webhook)
   if r.status_code == 200:
    print(Fore.GREEN + "Webhook Is Working")
    time.sleep(2)
    
   else:
        input(Fore.RED + 'Webhook Is Not Working.')
        time.sleep(2)

def insta():
    os.system('cls')
    print("""
    \033[35m
    █░░ █▀█ █▀▀ █ █▄░█
    █▄▄ █▄█ █▄█ █ █░▀█
    """)
    token = input('\nINSERT YOUR TOKEN :  ')
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get('https://discord.com/login')
    js = 'function login(token) {setInterval(() => {document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`}, 50);setTimeout(() => {location.reload();}, 500);}'
    driver.execute_script(js + f'login("{token}")')

print(Fore.MAGENTA + '''
            .▄▄ ·  ▄· ▄▌ ▐ ▄ ·▄▄▄▄• ▄▌▄▄▌  
            ▐█ ▀. ▐█▪██▌•█▌▐█▐▄▄·█▪██▌██•  
            ▄▀▀▀█▄▐█▌▐█▪▐█▐▐▌██▪ █▌▐█▌██▪  
            ▐█▄▪▐█ ▐█▀·.██▐█▌██▌.▐█▄█▌▐█▌▐▌
             ▀▀▀▀   ▀ • ▀▀ █▪▀▀▀  ▀▀▀ .▀▀▀
                [1] webhook Spammer
                [2] webhook Deleter
                [3] webhook Checker
                [4] login with token
''')
choices = input(Fore.RED + "[+] Enter Your Choice > ")

if choices == '1':
   spammer()
if choices == '2':
   delete()
if choices == '3':
   info()
if choices == '4':
   insta()
if choices == '10':
   sys.exit

  

