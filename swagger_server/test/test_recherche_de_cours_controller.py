# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestRechercheDeCoursController(BaseTestCase):
    """RechercheDeCoursController integration test stubs"""

    def test_search_tag_get(self):
        """Test case for search_tag_get

        Recherche de cours par tag
        """
        query_string = [('mode', None)]
        response = self.client.open(
            '/search/{tag}'.format(tag=None),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
