from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from swagger_client.api.default_api import DefaultApi
from swagger_client.models.message import Message


# Un peu de configuration, pas besoin de toucher

config = Configuration()
config.host = 'http://supermessagerie.tech/'
client = ApiClient(configuration=config)
api = DefaultApi(api_client=client)

# Code pour envoyer des requetes
message = Message(contenu="Hello world", emetteur="Anonyme")
api.messages_post(body=message)

messages = api.messages_get()
for msg in messages:
    print(msg)
