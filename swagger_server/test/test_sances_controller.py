# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestSancesController(BaseTestCase):
    """SancesController integration test stubs"""

    def test_cours_seances_id_delete(self):
        """Test case for cours_seances_id_delete

        Supprime une séance
        """
        response = self.client.open(
            '/cours/seances/{id}'.format(id=None),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_seances_id_get(self):
        """Test case for cours_seances_id_get

        Retourne les infos sur la séance
        """
        response = self.client.open(
            '/cours/seances/{id}'.format(id=None),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_seances_id_post(self):
        """Test case for cours_seances_id_post

        Crée une nouvelle séance
        """
        response = self.client.open(
            '/cours/seances/{id}'.format(id=None),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
