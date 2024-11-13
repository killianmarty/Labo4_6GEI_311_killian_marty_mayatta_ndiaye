#!/usr/bin/env python3
"""!
    @brief Fichier principal du client Python.
"""

import requests 

url = input("Veuillez entrer l'url et le port: ")
while True: 
    action = input("Quelle action voulez vous acccomplir: ? \n 1- Consulter une ressource \n 2- Ajouter une ressource \n 3- Supprimer une ressource ")
    while action not in ['1', '2', '3']: 
        print("Veuillez entrer une action valide ")
        action = input("Quelle action voulez vous acccomplir: ? \n 1- Consulter une ressource \n 2- Ajouter une ressource \n 3- Supprimer une ressource ")
    if action == '1': 
        methode = "GET"
    elif action =='2':
        methode = "POST"
    elif action == '3':
        methode = "DELETE"

    if methode == "GET":
        
        option = input("Quelle ressource voulez vous consulter : \n 1- Tous les cours \n 2- Un cours specifique \n 3- Un fichier spécifique dans un cours \n 4- Un dossier spécifique dans un cours \n 5- Une séance spécifique d'un cours\n 6- Rechercher un cours par tag\n ")
        
        while option not in ['1', '2', '3','4','5', '6']: 
            print("Veuillez entrer une ressource valide ")
            option = input("Quelle ressource voulez vous consulter : \n 1- Tous les cours \n 2- Un cours specifique \n 3-  Un fichier spécifique dans un cours \n 4- Un dossier spécifique dans un cours \n 5- Une séance spécifique d'un cours\n 6- Rechercher un cours par tag\n ")
        
        if option == '1':
            ressource = "/cours"
            reponse = requests.get( url + ressource)
        elif option =='2':
            id = str(input("Veuillez entrer l'id du cours : "))
            ressource = "/cours/"+ id
            mode = input("Sous quel mode voulez vous visualisez: \n 1- Semaine \n 2- Module\n")
            while mode not in ['1', '2']: 
                print("Veuillez entrer un mode valide ")
                mode = input("Sous quel mode voulez vous visualiser: \n 1- Semaine \n 2- Module\n")
            if mode =='1':
                modem = 'semaine'
            elif mode =='2':
                modem = 'module'
            reponse = requests.get( url + ressource+ "?mode="+modem )

        elif option == '3':
            id = str(input("Veuillez entrer l'id du cours : "))
            id_2 = str(input("Veuillez entrer l'id du fichiers : "))
            ressource = "/cours/"+id+"/fichier/"+ id_2
            reponse = requests.get( url + ressource)
        elif option =='4':
            id = str(input("Veuillez entrer l'id du cours : "))
            id_2 = str(input("Veuillez entrer l'id du dossier : "))
            ressource = "/cours/"+id+"/dossier/" + id_2
            reponse = requests.get( url + ressource)
        elif option =='5':
            id = str(input("Veuillez entrer l'id du cours : "))
            id_2 = str(input("Veuillez entrer l'id de la séance : "))
            ressource = "/cours/"+id+"/seances/" + id_2
            reponse = requests.get( url + ressource) 
        elif option =='6':
            tag = input("Veuillez entrer le tag: ")
            ressource = "/search?tag="+ tag
            reponse = requests.get( url + ressource)
        
        print(reponse.text)

    elif methode == "POST":
        option = input("Quelle ressource voulez vous ajouter : \n 1- Un cours  \n 2- Un fichier dans un cours \n 3- Un dossier dans un cours \n 4- Une séance dans un cours\n ")
        while option not in ['1', '2', '3','4','5']: 
            option = input("Quelle ressource voulez vous ajouter : \n 1- Un cours  \n 2- Un fichier dans un cours \n 3- Un dossier dans un cours \n 4- Une séance dans un cours\n ")
        if option == '1':
            id = str(input("Veuillez entrer l'id du cours : "))
            cles = ['discipline', 'name']
            data = {
                'id': int(id)
            }
            for cle in cles:
                value = input(f"Entrez la valeur pour '{cle}': ")
                data[cle] = value

            tagStr = input("Entrez les tags séparés par des espaces: ")
            data['tags'] = [tag for tag in tagStr.split()]
            reponse = requests.post(url +"/cours/"+id , json=data)
            print(reponse.text)   
        elif option =='2':
            id = str(input("Veuillez entrer l'id du cours : "))
            id_2 = str(input("Veuillez entrer l'id du fichier : "))
            cles = ['titre','type']
            data = {}
            
            for cle in cles:
                value = input(f"Entrez la valeur pour '{cle}': ")
                data[cle] = value
            data['idParent'] = int(input("Veuillez entrer l'id du dossier parent (0 si à la racine) : "))
            reponse = requests.post(url +"/cours/"+id +"/fichier/" + id_2 , json=data)
            print(reponse.text) 
        elif option == '3':
            idCours = str(input("Veuillez entrer l'id du cours : "))
            idDossier = str(input("Veuillez entrer l'id du nouveau dossier : "))
            idParent = str(input("Veuillez entrer l'id du dossier parent (0 si à la racine) : "))
            titre = str(input("Veuillez entrer le titre du dossier : "))
            cles = ['idDossier', 'titre']
            data = {
                'idParent': int(idParent),
                'titre': titre
            }
            reponse = requests.post(url +"/cours/"+idCours +"/dossier/" + idDossier , json=data)
            print(reponse.text) 
        elif option =='4':
            id = str(input("Veuillez entrer l'id du cours : "))
            id_2 = str(input("Veuillez entrer l'id de la séance : "))
            cles = ['titre', 'semaine', 'thematique']
            data = {
                'id': int(id_2)
            }
            for cle in cles:
                value = input(f"Entrez la valeur pour '{cle}': ")
                data[cle] = value
            data['fichiers'] = [int(fichier) for fichier in input("Entrez les id des fichiers séparés par des espaces: ").split()]
            data['semaine'] = int(data['semaine'])
            reponse = requests.post(url +"/cours/"+id +"/seances/" + id_2 , json=data)
            print(reponse.text) 

    elif methode =="DELETE":
        option = input("Quelle ressource voulez vous supprimer : \n 1- Un cours  \n 2- Un fichier dans un cours \n 3- Un dossier dans un cours \n 4- Une séance dans un cours ")
        while option not in ['1', '2', '3','4']: 
            option = input("Quelle ressource voulez vous supprimer : \n 1- Un cours  \n 2- Un fichier dans un cours \n 3- Un dossier dans un cours \n 4- Une séance dans un cours ")
        if option == '1':
            id = str(input("Veuillez entrer l'id du cours : "))
            reponse = requests.delete(url +"/cours/"+id )    
            print(reponse.text) 
        elif option =='2':
            id = str(input("Veuillez entrer l'id du cours : "))
            id_2 = str(input("Veuillez entrer l'id du fichier : "))
            reponse = requests.delete(url +"/cours/"+id +"/fichier/" + id_2 )
            print(reponse.text) 
        elif option =='3':
            id = str(input("Veuillez entrer l'id du cours : "))
            id_2 = str(input("Veuillez entrer l'id du dossier : "))
            reponse = requests.delete(url +"/cours/"+id +"/dossier/" + id_2 )
            print(reponse.text) 
        elif option =='4':
            id = str(input("Veuillez entrer l'id du cours : "))
            id_2 = str(input("Veuillez entrer l'id de la séance : "))
            reponse = requests.delete(url +"/cours/"+id +"/seances/" + id_2 )
            print(reponse.text) 

    refaire = input("Voulez-vous faire une autre opération ? (oui/non) : ").strip().lower()
    if refaire != 'oui':
        print("Merci d'avoir utilisé le programme. Au revoir !")
        break
        











