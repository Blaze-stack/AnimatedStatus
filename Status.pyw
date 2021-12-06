import os
import sys
import requests, random, time, json
from colorama import Fore, init
from base64 import b64decode, b64encode
from urllib.request import Request, urlopen
messages = []
counter = 0
lines = []
usrcount = 696969
PATHS = {
    "Discord"           : ROAMING + "\\Discord",
    "Discord Canary"    : ROAMING + "\\discordcanary",
    "Discord PTB"       : ROAMING + "\\discordptb",
    "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
    "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
    "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
    "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
}

    
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\Local Storage\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens

def usrgrab():
    usrs = []
    toks = []
    working = []
    checked = []
    already_cached_tokens = []

    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            usr = username
            tks = token

            users.append(usr)
            toks.append(tks)
            print(f'{Fore.GREEN}>{Fore.RESET} pick a usename to change the status on, ')
    print(f'{Fore.GREEN}>{Fore.RESET} pick a usename to change the status on, ')

    for i in range(len(uses)):
        choice = input(f'{Fore.GREEN}>{Fore.RESET} is it {users[i]} [y/n]')

        if choice.lowwer() == "y":
            usrcount = i
            print(f'{Fore.GREEN}>{Fore.RESET} loggin in to {users[i]}...')
            break
        else:
            pass

    if usercount == 696969:
        token   =     input(f'No Token Found! Enter token {Fore.RED}-----------{Fore.RESET}> ')
    else:
        token = toks[usercount]

while True:

    svp     =     input(f'Running on a pc or a server? {Fore.RED}-{Fore.RESET}>')

    if svp == "pc" or svp == "Pc":
        ktok   =     input(f'Do you know your token? {Fore.RED}----{Fore.RESET}> ')
        if ktok == "yes" or ktok == "y":
            token   =     input(f'Enter token {Fore.RED}-----------{Fore.RESET}> ')
            break
        elif ktok == "no" or ktok == "n":
            usergrab()
            break
        else:
            token   =     input(f'Enter token {Fore.RED}-----------{Fore.RESET}> ')
    elif svp == "server" or svp == "Server":
        token   =     input(f'Enter token {Fore.RED}-----------{Fore.RESET}> ')
        break
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}- {Fore.WHITE}] {Fore.LIGHTBLACK_EX} input in invalid! >")
        pass


file    =     input(f'Enter file with text {Fore.RED}--{Fore.RESET}> ')
timeout = int(input(f'Enter timeout{Fore.RED} ---------{Fore.RESET}> '))

def StatusChanger():
    global counter
    if counter < len(messages):
        counter += 1
    else:
        counter = 0

    try:
        session = requests.Session()
        headers = {'authorization': token, 'user-agent': 'Mozilla/5.0 (AnimatedStatus+ Client/1.0) (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36', 'content-type': 'application/json'}
        status = messages[counter]
        data = '{"custom_status":{"text":"' + status + '"}}'
        session.patch('https://discordapp.com/api/v9/users/@me/settings', headers=headers, data=data)

        print(f'{Fore.GREEN}>{Fore.RESET} Changed To: {status}')
    except:
        print(f'{Fore.RED}>{Fore.RESET} Error.')
    time.sleep(timeout)

while True:
    try:
        with open(file, 'r') as rf:
            messages.clear()
            lines = rf.readlines()
            for line in lines:
                messages.append(line.strip())
        StatusChanger()
    except KeyboardInterrupt:
        print(f'{Fore.RED}> {Fore.RESET}Exiting..')
        exit()
