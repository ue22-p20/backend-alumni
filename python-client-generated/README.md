# Client HTTP Python

## Installation

```
git clone git@github.com:ue22/backend-alumni.git
cd backend-alumni/python-client-generated
python3 -m pip install -r requirements.txt
```

## Utilisation

1. Editer "main.py"
2. `python3 main.py`

## Remarques

1. Cette manière de versionner le code du client HTTP n'est pas propre: normalement, la librairie auto-générée par Swagger se trouve dans un package indépendant, ou mieux, est re-générée automatiquement et se fait `gitignore`. Cela ne sert à rien de versionner le code auto-généré, seul le fichier de configuration devrait être versionné.
