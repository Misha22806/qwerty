import requests
import os
 
 
class Client:
    def __init__(self, username: str, address: str):
        self.address = address
        self.username = username
        response = requests.get(self.address).text
        if response != "true":
            raise ValueError("Could not connect to server")
 
    def sendMessage(self, message):
        requests.get(self.address + "message?text=" + f"{self.username}: {message}")
 
    def getMessages(self):
        messages = requests.get(self.address + "history").json()
        os.system("cls")
        for message in messages:
            print(message)
 
 
client = Client("burger king shit", "https://bf7d-87-76-244-215.eu.ngrok.io/")
while True:
    client.sendMessage(input("Enter message: "))
    client.getMessages()
 