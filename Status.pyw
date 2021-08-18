import requests, random, time, json
from colorama import Fore, init

messages = []
counter = 0
lines = []

token   =     input(f'Enter token {Fore.RED}-----------{Fore.RESET}> ')
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
        session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)

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