DOCKER-COMPOSE
Assurez-vous que Docker compose est installé sur votre système.

Allez dans le dossier contenant le projet et se placer là où il y manage.py

sourcez l'environnement virtuel (sur windows en tapant "env\Scripts\activate")
lancez le server par la commande "docker-compose up"

Pour la suite, assurez vous que le server est  lancé, et que l'environnement virtuel est sourcé
le projet est accessible depuis votre localhost port 8000 (localhost:8000)

MODELS
Les models :
Questionnaire : pour la liste des questionnaires
Question : pour la liste des questions, assicié au Questionnaire
Réponse : en liaison avec Question, contient la liste des réponses
ReponseUser : contient la liste de réponse de chaque utilisateur
Note : contient le note en pourcentage , associé au Users et Question

lancez "docker-compose exec web python manage.py makemigrations"
lancer "docker-compose exec web python manage.py migrate"

DATABASE
pour seeder la base de données
soit en allant dans la page admin est cliquer sur le boutons dédiés.
soit "docker-compose exec web python manage.py seed questionnaires --number=15"
on peut mettre le nombre qu'on souhaite, ici j'ai utilisé 15



COMPTE ADMIN
lancer le commande qui suit
python manage.py createsuperuser --email suleman.prisc@gmail.com --username admin
si jamais ça donne une erreur mettez :
docker-compose exec web python manage.py createsuperuser --email suleman.prisc@gmail.com --username admin
lancez "docker-compose exec web python manage.py makemigrations"
lancer "docker-compose exec web python manage.py migrate"
lancer "docker-compose build"


API
les liens des deux api sont sur la page d'accueil du projet.
Les deux api sont accéssible pour les utilisateurs authentifiés.

"http://localhost:8000/api/reponse-user/"
Pour que l'utilisateur puisse répondre aux questions, méthode POST

"http://localhost:8000/api/note/" qui affiche si une question a eu la bonne réponse.
pour l'api note, ça ne renvoi pas vraiment ce qui a été demandé, je me suis documenté. je sais comment je vais procéder mais ça me revoi une erreur que je cherche à comment y remédier. La raison où je ne mis la réponse actuelle.


sur Postman, il faut insérer dans le cookies votre sessionid avec sa valeur (à récupérer depuis le navigateur)



