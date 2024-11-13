# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestContenuDeCoursController(BaseTestCase):
    """ContenuDeCoursController integration test stubs"""

    def test_cours_id_dossier_delete(self):
        """Test case for cours_id_dossier_delete

        Supprime un dossier du cours
        """
        query_string = [('dossier', None)]
        response = self.client.open(
            '/cours/{id}/dossier'.format(id=None),
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_id_dossier_get(self):
        """Test case for cours_id_dossier_get

        Retourne un JSON du contenu du dossier
        """
        query_string = [('dossier', None)]
        response = self.client.open(
            '/cours/{id}/dossier'.format(id=None),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_id_dossier_post(self):
        """Test case for cours_id_dossier_post

        Crée un nouveau dossier pour le cours
        """
        response = self.client.open(
            '/cours/{id}/dossier'.format(id=None),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_id_fichier_delete(self):
        """Test case for cours_id_fichier_delete

        Supprime un fichier du cours
        """
        query_string = [('chemin', None)]
        response = self.client.open(
            '/cours/{id}/fichier'.format(id=None),
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_id_fichier_get(self):
        """Test case for cours_id_fichier_get

        Retourne un fichier selon le chemin spécifié
        """
        query_string = [('chemin', None)]
        response = self.client.open(
            '/cours/{id}/fichier'.format(id=None),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_cours_id_fichier_post(self):
        """Test case for cours_id_fichier_post

        Télécharge un fichier pour le cours
        """
        response = self.client.open(
            '/cours/{id}/fichier'.format(id=None),
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
