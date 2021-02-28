import connexion
import six

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.reaction_emoji import ReactionEmoji  # noqa: E501
from swagger_server.models.utilisateur import Utilisateur  # noqa: E501
from swagger_server import util


def messages_get():  # noqa: E501
    """Retourne la liste des messages

     # noqa: E501


    :rtype: List[Message]
    """
    return 'do some magic!'


def messages_post(body=None):  # noqa: E501
    """Envoie un nouveau message

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def reactions_get(message_id):  # noqa: E501
    """Lister les reactions emojis d&#x27;un message

     # noqa: E501

    :param message_id: Identifiant du message
    :type message_id: int

    :rtype: List[ReactionEmoji]
    """
    return 'do some magic!'


def reactions_post(body=None):  # noqa: E501
    """Réagir avec une emoji à un message

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Body.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def register_post(body=None):  # noqa: E501
    """Inscrire un nouvel utilisateur

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Utilisateur.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
