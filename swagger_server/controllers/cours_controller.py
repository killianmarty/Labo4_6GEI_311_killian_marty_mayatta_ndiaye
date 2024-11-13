#!/usr/bin/env python3
"""! @brief Controllers des cours du serveur Flask pour l'API de cours."""

import connexion
import six

from swagger_server import util
import json
import copy

def cours_get():  # noqa: E501
    """!
    @brief Retourne la liste des cours
    @return Un objet JSON qui contient la liste de tous les cours.

    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    result = []
    for cours in data:
        obj = {
            "id": cours["id"],
            "name": cours["name"],
            "discipline": cours["discipline"],
            "tags": cours["tags"]
        }
        result.append(obj)

    return result


def cours_id_delete(id):  # noqa: E501
    """!
        @brief Cette fonction permet de supprimer un cours.
        @param id L'id du cours à supprimer.
        @return Un message qui indique le résultat de la requête.
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    
    for cours in data:
        if cours['id'] == id:
            data.remove(cours)
            with open('swagger_server/cours.json', 'w') as file:
                json.dump(data, file, indent=4)
            return "Cours deleted"
    
    return "Cours not found", 400


def cours_id_get(id, mode=None):  # noqa: E501
    """!
        @brief Cette fonction permet de lire un cours.
        @param id L'id du cours à lire.
        @param mode Mode ("module"/"semaine") de regroupement des séances dans le cours.
        @return Un objet JSON qui contient le cours.
    """
    # Par défaut le mode est "semaine"

    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    
    for cours in data:
        if cours['id'] == id:
            tmp = copy.deepcopy(cours)
            tmp.pop("fichiers")
            tmp.pop("dossiers")
            tmp["seances"] = {}
            if(mode == "module"):
                for seance in cours["seances"]:
                    if(not seance["thematique"] in tmp["seances"]):
                        tmp["seances"][seance["thematique"]] = []
                    tmp["seances"][seance["thematique"]].append(seance)
            else:
                for seance in cours["seances"]:
                    if(not ("semaine " + str(seance["semaine"])) in tmp["seances"]):
                        tmp["seances"]["semaine " + str(seance["semaine"])] = []
                    tmp["seances"]["semaine " + str(seance["semaine"])].append(seance)

            return tmp
    
    return "Cours not found", 400


def cours_id_post(id):  # noqa: E501
    """!
        @brief Cette fonction permet d'ajouter un cours.
        @param id L'id du cours à ajouter.
        @return Un message qui indique le résultat de la requête.
    """
    body = connexion.request.get_json()
    
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    
    obj = {
        "id": id,
        "name": body["name"],
        "discipline": body["discipline"],
        "tags": body["tags"],
        "seances": [],
        "fichiers": [],
        "dossiers": []
    }

    for cours in data:
        if cours["id"] == id:
            return "Cours already exists", 400
    
    data.append(obj)
    
    with open('swagger_server/cours.json', 'w') as file:
        json.dump(data, file, indent=4)
    
    return "Cours created"
