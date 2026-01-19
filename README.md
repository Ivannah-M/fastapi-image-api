# FastAPI Image Processing API

Une API FastAPI pour traiter des images (grayscale, blur, resize) avec OpenCV, containerisée avec Docker.  


## Features

- Upload d’images via `/docs` (Swagger UI)
- Traitements disponibles :
  - `grayscale` : conversion en niveaux de gris
  - `blur` : flou gaussien, paramètre `blur_strength`
  - `resize` : redimensionnement proportionnel, paramètre `ratio`
- Stockage des images traitées dans le dossier `uploads`
- Documentation interactive Swagger disponible via `/docs`

## Stack technique

- Python 3.10
- FastAPI
- OpenCV (headless)
- Docker
- Uvicorn
- Pytest + HTTPX pour tests automatisés

## Installation & Docker

Pour lancer l’API avec Docker et sauvegarder les images sur votre machine :

1. Build de l'image Docker :
```bash
docker build -t images-api .
```

2. Lancer les tests
```bash
docker run --rm -v ${PWD}/tests:/app/tests -w /app images-api pytest tests/
```

 3. Lancer l'API
 ```bash
docker run -d -p 8000:8000 -v ${PWD}/uploads:/app/uploads --name images-api-container images-api
```

4. Lancer l’API + tests avec PowerShell (Windows)

Si vous êtes sous Windows, vous pouvez tout faire en une seule commande grâce au script run_api.ps1 :
 ```bash
.\run_api.ps1
```
Ce script :

- Arrête et supprime le conteneur existant s’il y en a un
- Build l’image Docker
- Lance les tests pytest
- Démarre l’API dans un conteneur détaché
- Monte le dossier uploads pour sauvegarder les images générées

L’API sera disponible sur : http://127.0.0.1:8000/docs

## Commandes Docker utiles

Arrêter le conteneur :
 ```bash
docker stop images-api-container
```

Redémarrer le conteneur :
 ```bash
docker start images-api-container
```

Supprimer le conteneur :
 ```bash
docker rm images-api-container
```

## Tests automatisés

Les tests sont dans tests/test_main.py
Placez une image de test nommée `test_image.jpg` dans le dossier `tests/` pour exécuter les tests.


Ils vérifient que les endpoints grayscale, blur et resize renvoient bien des images