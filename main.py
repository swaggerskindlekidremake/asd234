import requests

webhook_url = "https://discord.com/api/webhooks/1453986777634308156/ZZXxeiiV5hbFCs1TOwaFoLFPV5Ixe_5BN4qqTOgI-l4VdlmTvlV-REIgZ0RVrdVN1k7A"

data = {
    "content": "bazinga"
}

response = requests.post(webhook_url, json=data)

if response.status_code == 204:
    print("Message sent successfully")
else:
    print("Failed to send message:", response.status_code, response.text)
