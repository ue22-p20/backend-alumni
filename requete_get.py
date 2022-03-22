import requests
import json

req = requests.get("http://supermessagerie.tech/messages")

print("Contenu brut: ")
print(req.content)

print("\nUn peu plus joli (parsed json):")
print(json.dumps(json.loads(req.content), indent=4))
