#!/usr/bin/env python3
"""! @brief Controllers des contenus de cours du serveur Flask pour l'API de cours."""


import connexion
import six

from swagger_server import util
import json

def cours_id_dossier_id_dossier_delete(id, idDossier):  # noqa: E501
    """!
        @brief Cette fonction permet de supprimer un dossier dans un cours.
        @param id L'id du cours qui contient le dossier.
        @param idDossier L'id du dossier à supprimer.
        @return Un message qui indique le résultat de la requête.
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    for cours in data:
        if cours['id'] == id:
            for fichier in cours['fichiers']:
                if fichier['idParent'] == idDossier:
                    cours_id_fichier_id_fichier_delete(id, fichier['id'])

            #reload file
            with open('swagger_server/cours.json', 'r') as file:
                data = json.load(file)

            for cours in data:
                if cours['id'] == id:
                    for dossier in cours['dossiers']:
                        if dossier['idParent'] == idDossier:
                            cours_id_dossier_id_dossier_delete(id, dossier['id'])
                    for dossier in cours['dossiers']:
                        if dossier['id'] == idDossier:
                            cours['dossiers'].remove(dossier)

                            with open('swagger_server/cours.json', 'w') as file:
                                json.dump(data, file, indent=4)
                            return 'Directory deleted'
        
        return "Directory not found", 400

    return 'Dossier not found', 400


def cours_id_dossier_id_dossier_get(id, idDossier):  # noqa: E501
    """!
        @brief Cette fonction permet de lire un dossier dans un cours.
        @param id L'id du cours où se trouve le dossier.
        @param idDossier L'id du dossier.
        @return Un objet JSON qui contient le contenu du dossier.
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    
    result = {
        "dossiers": [],
        "fichiers": []
    }
    for cours in data:
        if cours['id'] == id:

            for dossier in cours['dossiers']:
                if dossier['id'] == idDossier:
                    result['propriete'] = dossier
                if(dossier['idParent'] == idDossier):
                    result['dossiers'].append(dossier)

            for fichier in cours['fichiers']:
                if(fichier['idParent']==idDossier):
                    result['fichiers'].append(fichier)

            return result

    return 'Cours not found', 400


def cours_id_dossier_id_dossier_post(id, idDossier):  # noqa: E501

    """!
        @brief Cette fonction permet de créer un dossier dans un cours.
        @param id L'id du cours à l'intérieur duquel créer le dossier.
        @param idDossier L'id du nouveau dossier à créer.
        @return Un message qui indique le résultat de la requête.
    """
    body = connexion.request.get_json()
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    for cours in data:
        if(cours["id"] == id):
            for dossier in cours["dossiers"]:
                if(dossier["id"] == idDossier):
                    return "Directory already exists", 400
            
            obj = {
                "id": idDossier,
                "titre": body["titre"],
                "idParent": body["idParent"]
            }

            error = True
            if(body["idParent"] != 0):
                for dossier in cours["dossiers"]:
                    if(dossier["id"] == body["idParent"]):
                        obj["chemin"] = dossier["chemin"] + "/" + body["titre"]
                        error = False
                        break
                if(error):
                    return "Parent folder does not exists", 400
            else:
                obj["chemin"] = "/" + body["titre"]

            cours["dossiers"].append(obj)

            with open('swagger_server/cours.json', 'w') as file:
                json.dump(data, file, indent=4)
            return 'Directory created'
    
    return "Cours not found", 400


def cours_id_fichier_id_fichier_delete(id, idFichier):  # noqa: E501
    """!
        @brief Cette fonction permet de supprimer un fichier dans un cours.
        @param id L'id du cours qui contient le fichier.
        @param idDossier L'id du dossier à supprimer.
        @return Un message qui indique le résultat de la requête.
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)
    for cours in data:
        if cours['id'] == id:
            
            for fichier in cours['fichiers']:
                if fichier['id'] == idFichier:
                    cours['fichiers'].remove(fichier)

            for seance in cours['seances']:
                if idFichier in seance['fichiers']:
                    seance['fichiers'].remove(idFichier)

            with open('swagger_server/cours.json', 'w') as file:
                json.dump(data, file, indent=4)
            return 'File deleted'

    return 'File not found', 400


def cours_id_fichier_id_fichier_get(id, idFichier):  # noqa: E501
    """!
        @brief Cette fonction permet de lire un fichier dans un cours.
        @param id L'id du cours où se trouve le fichier.
        @param idDossier L'id du fichier.
        @return Un objet JSON qui contient le fichier.
    """
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    for cours in data:
        if cours['id'] == id:
            for fichier in cours['fichiers']:
                if fichier['id'] == idFichier:
                    return fichier

    return "File not found", 400


def cours_id_fichier_id_fichier_post(id, idFichier):  # noqa: E501
    """!
        @brief Cette fonction permet de créer un fichier dans un cours.
        @param id L'id du cours à l'intérieur duquel créer le fichier.
        @param idDossier L'id du nouveau fichier à créer.
        @return Un message qui indique le résultat de la requête.
    """
    body = connexion.request.get_json()
    with open('swagger_server/cours.json', 'r') as file:
        data = json.load(file)

    for cours in data:
        if(cours["id"] == id):
            for fichier in cours["fichiers"]:
                if(fichier["id"] == idFichier):
                    return "File already exists", 400
            
            obj = {
                "id": idFichier,
                "titre": body["titre"],
                "type": body["type"],
                "idParent": body["idParent"]
            }

            if(body["idParent"] != 0):
                for dossier in cours["dossiers"]:
                    if(dossier["id"] == body["idParent"]):
                        obj["chemin"] = dossier["chemin"] + "/" + body["titre"] + "." + body["type"]
                        break
                    return "Parent directory does not exists", 400
            else:
                obj["chemin"] = "/" + body["titre"] + "." + body["type"]

            cours["fichiers"].append(obj)

            with open('swagger_server/cours.json', 'w') as file:
                json.dump(data, file, indent=4)
            return 'File created'
    
    return "Cours not found", 400
