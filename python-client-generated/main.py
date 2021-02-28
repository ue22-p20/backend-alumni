from swagger_client.api_client import ApiClient
from swagger_client.configuration import Configuration
from swagger_client.api.default_api import DefaultApi
from swagger_client.models.message import Message


config = Configuration(host="localhost")
client = ApiClient(configuration=config)
api = DefaultApi(api_client=client)


message = Message(contenu="Hello world", emetteur="Quentin")
api.messages_post(body=message)

messages = api.messages_get()
print(messages)
