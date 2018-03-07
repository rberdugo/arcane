# arcane REST API 

CONTEXTE :
Dans le cadre d’un projet de création d’une application web de gestion immobilière, on nous demande de créer un ensemble de microservices. Ces microservices doivent permettre à un utilisateur de renseigner un bien immobilier avec les caractéristiques suivantes : nom, description, type de bien, ville, pièces, caractéristiques des pièces, propriétaire.


FONCTIONNALITES : 

  1) Un utilisateur peut modifier les caractéristiques d’un bien 
  2) Les utilisateurs peuvent renseigner/ modifier leurs informations personnelles sur la plateforme
  3) Les utilisateurs peuvent consulter uniquement les biens d’une ville particulière
  4) Un propriétaire ne peut modifier que les caractéristiques de son bien sans avoir accès à l’édition des autres biens.
  
  
INSTALLATION DE L'ENVIRONNEMENT : 

  1) Sur bash : pip install flask flask-jsonpify flask-sqlalchemy flask-restful
  2) Créer/Choisir un dossier en local "d" dans lequel cloner le git 
  3) Sur bash dans ce dossier : 
        virtualenv venv
        export FLASK_APP=yourapplication
        export FLASK_DEBUG=true
        pip install -e .
        source venv/bin/activate 
        flask run
  4) Changer de console (si nécessaire) et ouvrir le dossier example.py et faire les tests 
