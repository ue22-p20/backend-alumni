# TP: interagir avec une API de messagerie

## Liens utiles

- URL de la messagerie: http://supermessagerie.tech/messages
- Fichier swagger: [swagger.yaml](https://raw.githubusercontent.com/ue22/backend-alumni/main/private/swagger_complet.yaml)
- Editeur Swagger en ligne: https://editor.swagger.io (instructions ci-dessous)

## Instructions générales

L'objectif, c'est simplement de faire des requêtes 
sur le petit service de messagerie que l'on vous a présenté.

Il y a 3 manières de faire ce TP:
- faire des requêtes en ligne de commande
- faire des requêtes HTTP brut avec Python
- utiliser un client API Python

Chaque approche a son intérêt, n'hésitez pas à varier les plaisirs ;)

**Pour aller plus loin, nous avons rajouté des notions supplémentaires:**
- message "vérifié"
- emojis de réactions aux messages

En faisant une requête supplémentaire d'inscription, 
vous pourrez obtenir le status "vérifié" sur vos messages.

Cette instruction vous pourrait vague ? 
Rien de mieux qu'interagir avec l'API et de regarder ses spécifications
pour mieux comprendre ;)

## Swagger

Allez sur https://editor.swagger.io, puis cliquez sur "File > Import Url" et copiez le lien suivant:
"https://raw.githubusercontent.com/ue22/backend-alumni/main/private/swagger_complet.yaml"

## Faire des requetes via un terminal

Une commande classique pour faire des requetes HTTP: `curl`

```
# Pour faire un get:
curl http://supermessagerie.tech/messages


# Pour faire un post:
curl -d '{"parametre1": "valeur", "parametre2": "valeur2"}' http://supermessagerie.tech/messages

# Remarque: pour afficher les résultats JSON de maniere plus sympa,
# une commande tres utile c'est "jq":
curl http://supermessagerie.tech/messages | jq -r '.'

# et pour pas se faire spammer, on peut utiliser "less"
curl http://supermessagerie.tech/messages | jq -r '.' | less
```

## Faire des requetes via Python (version HTTP brut)

- Exemple pour faire un GET: [request_get.py](requete_get.py)
- Exemple pour faire un POST: [request_post.py](requete_post.py)

## Faire des requetes via Python (version client API)

Instructions & exemples dans le dossier [python-client-generated](python-client-generated). 

