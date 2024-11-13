#!/usr/bin/env python3
"""! @brief Controllers de recherche de cours du serveur Flask pour l'API de cours."""

import connexion
import six

from swagger_server import util
import json

def search_get(tag):  # noqa: E501
    """!
    @brief Cette fonction permet de rechercher des cours qui contiennent un certain Tag.
    @param tag Tag des cours que l'on recherche.
    @return Un objet JSON qui contient une liste des cours trouvés.
    """
    def load_courses():
        with open('swagger_server/cours.json', 'r') as file:
            return json.load(file)

    courses = load_courses()

    result = []
    for cours in courses:
        if tag in cours['tags']:
            obj = {
                "id": cours["id"],
                "name": cours["name"],
                "discipline": cours["discipline"],
                "tags": cours["tags"]
            }
            result.append(obj)

    return result
