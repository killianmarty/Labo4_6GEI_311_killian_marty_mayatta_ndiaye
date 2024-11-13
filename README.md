# Documentation Doxygen API système de cours

Mayatta Ndiaye, Killian Marty

## Introduction

Doxygen est un logiciel qui permet de générer automatiquement de la documentation pour un projet informatique. Il supporte de nombreux langages, et peux générer la documentation sous plusieurs formats (HTML, LaTex, etc...).

Doxygen se base sur les commentaires dans le code pour générer la documentation.

## Structure du projet

Le projet est le Laboratoire 3 du cours d'architecture des logiciels. Il s'agit d'un projet complet d'API de cours.

Voici la structure du projet :

* swagger_server : module du serveur Python de l'API
    * controllers
        * contenu_de_cours_controller.py
        * cours_controller.py
        * recherche_de_cours_controller.py
        * seance_controller.py
    * models
        * api_response.py
        * base_model.py
    * test
        * test_api_response.py
        * test_contenu_de_cours_api.py
        * test_cours_api.py
        * test_recherche_de_cours_api.py
        * test_seances_api.py
    * encoder.py
    * util.py
    * __main__.py
* swagger_client : module du client Python de l'API
    * __main__.py
* swagger_client_java : implémentation en Java du client de l'API
    * Main.java

## Explication des commentaires

Dans controller, chaque fonction débute maintenant par des commentaires sous la forme suivante :

```python
"""!
    @brief Description courte de la fonction.

    @param param1 Desription du paramètre param1.
    @param param2 Desription du paramètre param2.
    ...

    @return Expliation de ce qui est retourné par la fonction.
"""
```
Ainsi Doxygen peut documenter chaque fonction facilement.

On peut faire de même pour les classes, et il est possible de définir des commentaires de la même façon en en-tête de fichier pour décrire le fichier.

Par exemple, voici le début du fichier "swagger_server/controllers/contenu_de_cours_controller.py" une fois commenté : 
```python
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
        ...
```

Comme lors du Laboratoire 3, une partie du serveur/client a été généré par un programme, la plupart des fonctions et classes des fichiers générés sont déjà commentées pour permettre la génération de la documentation. C'est le cas des classes de "models", "test" et "encoder" dans "swagger_server".


## Conclusion

En conclusion, Doxygen permet de générer facilement une documentation complète. 

Ce logiciel à plusieurs avantages par rapport à une documentation traditionnelle :
* Il permet de ne pas oublier des sections de la documentation.
* Il permet de faire une documentation propre.
* Il permet de gagner du temps.

Mais il présente aussi des désavantages :

* On n'a pas autant de possibilités de personnalisation que si on rédigeait nous même la documentation.
* Le logiciel peut documenter des choses qu'on ne veut pas documenter, et si on veut éviter cela, il faut entrer dans une configuration avancée et parfois fastidieuse.

Enfin, quelque soit la méthode, il est important d'avoir une documentation du code afin de pouvoir expliquer facilement son code à une personne externe au projet (nouveau développeur, gestionnaire de projet, etc). Mais également comprendre les modifications faites par d'autres membres de l'équipe, et simplifier l'utilisation.