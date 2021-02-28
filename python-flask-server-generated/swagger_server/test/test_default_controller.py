# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.body import Body  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server.models.reaction_emoji import ReactionEmoji  # noqa: E501
from swagger_server.models.utilisateur import Utilisateur  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_messages_get(self):
        """Test case for messages_get

        Retourne la liste des messages
        """
        response = self.client.open(
            '/messages',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_messages_post(self):
        """Test case for messages_post

        Envoie un nouveau message
        """
        body = None
        response = self.client.open(
            '/messages',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reactions_get(self):
        """Test case for reactions_get

        Lister les reactions emojis d'un message
        """
        query_string = [('message_id', 56)]
        response = self.client.open(
            '/reactions',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reactions_post(self):
        """Test case for reactions_post

        Réagir avec une emoji à un message
        """
        body = Body()
        response = self.client.open(
            '/reactions',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_register_post(self):
        """Test case for register_post

        Inscrire un nouvel utilisateur
        """
        body = Utilisateur()
        response = self.client.open(
            '/register',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
