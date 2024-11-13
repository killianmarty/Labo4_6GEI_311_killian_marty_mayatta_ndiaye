#!/usr/bin/env python3
"""! @brief Controllers des séances du serveur Flask pour l'API de cours."""

import connexion
import six

from swagger_server import util
import json

def cours_id_seances_id_seance_delete(id, idSeance):  # noqa: E501
    """!
        @brief Cette fonction permet de supprimer une séance dans un cours.
        @param id L'id du cours qui contient la séance.
        @param idDossier L'id de la séance à supprimer.
        @return Un message qui indique le résultat de la requête.
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    for cours in data:
        if(cours["id"] == id):
            for seance in cours["seances"]:
                if(seance["id"] == idSeance):
                    cours["seances"].remove(seance)
                    with open('swagger_server/cours.json', 'w') as file:
                        json.dump(data, file, indent=4)
                    return "Seance deleted"
    return "Seance not found", 400


def cours_id_seances_id_seance_get(id, idSeance):  # noqa: E501
    """!
        @brief Cette fonction permet de lire une séance dans un cours.
        @param id L'id du cours où se trouve la séance.
        @param idDossier L'id de la séance.
        @return Un objet JSON qui contient le contenu de la séance.
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    for cours in data:
        if(cours["id"] == id):
            for seance in cours["seances"]:
                if(seance["id"] == idSeance):
                    return seance
    return "Seance not found", 400


def cours_id_seances_id_seance_post(id, idSeance):  # noqa: E501
    """!
        @brief Cette fonction permet de créer une séance dans un cours.
        @param id L'id du cours à l'intérieur duquel créer la séance.
        @param idDossier L'id de la nouvelle séance à créer.
        @return Un message qui indique le résultat de la requête.
    """
    body = connexion.request.get_json()
    
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    
    obj = {
        "id": idSeance,
        "semaine": body["semaine"],
        "titre": body["titre"],
        "thematique": body["thematique"],
        "fichiers": body["fichiers"]
    }

    for cours in data:
        if cours["id"] == id:
            for seance in cours["seances"]:
                if seance["id"] == idSeance:
                    return "Seance already exists", 400
            cours["seances"].append(obj)
            with open('swagger_server/cours.json', 'w') as file:
                json.dump(data, file, indent=4)
            return "Seance created"
    return "Cours not found", 400
    
