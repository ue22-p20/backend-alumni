# TP: interagir avec une API de messagerie

## Liens utiles

- URL: https://messagerie.tech/messages
- Fichier swagger: [swagger.yaml](swagger.yaml)
- Exemple 

## Visualiser les spécifications

1. Aller sur https://editor.swagger.io/
2. Cliquer sur "Import url"
3. TODO(FIXME) Utilisez l'URL: `https://raw.githubusercontent.com/16pierre/info_1A/main/swagger_simplifie.yaml`


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

