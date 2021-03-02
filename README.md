# TP: interagir avec une API de messagerie

## Liens utiles

- URL de la messagerie: https://messagerie.tech/messages
- Fichier swagger: [swagger.yaml](https://raw.githubusercontent.com/ue22/backend-alumni/main/private/swagger_simplifie.yaml)
- Editeur Swagger en ligne: https://swagger.messagerie.tech/

## Instructions générales

L'objectif, c'est simplement de faire des requêtes 
sur le petit service de messagerie que l'on vous a présenté.

Il y a 3 manières de faire ce TP:
- faire des requêtes en ligne de commande
- faire des requêtes HTTP brut avec Python
- utiliser un client API Python

Chaque approche a son intérêt, n'hésitez pas à varier les plaisirs ;)

**Pour aller plus loin:** nous avons rajouté la notion de message "vérifié".

En faisant une requête supplémentaire d'inscription, 
vous pourrez obtenir le status "vérifié" sur vos messages.

Cette instruction vous pourrait vague ? 
Rien de mieux qu'interagir avec l'API et de regarder ses spécifications
pour mieux comprendre ;)

## Visualiser les spécifications

Aller sur https://swagger.messagerie.tech

## Faire des requetes via Python (version HTTP brut)

- Exemple pour faire un GET: [request_get.py](requete_get.py)
- Exemple pour faire un POST: [request_post.py](requete_post.py)

## Faire des requetes via Python (version client API)

Instructions & exemples dans le dossier [python-client-generated](python-client-generated). 

## Faire des requetes via un terminal

Une commande classique pour faire des requetes HTTP: `curl`

```
# Pour faire un get:
curl https://messageries.tech/messages


# Pour faire un post:
curl -d '{"parametre1": "valeur", "parametre2": "valeur2"}' https://messageries.tech/messages

# Remarque: pour afficher les résultats JSON de maniere plus sympa,
# une commande tres utile c'est "jq":
curl https://messageries.tech/messages | jq -r '.'

# et pour pas se faire spammer, on peut utiliser "less"
curl https://messageries.tech/messages | jq -r '.' | less
```

