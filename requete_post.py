import requests

payload = {'emetteur': 'quentin', 'contenu': 'Hello world'}
req = requests.post("https://messagerie.tech/messages", json=payload)

print("Reponse du serveur:")
print(req.content)

