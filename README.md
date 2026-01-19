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

## Installation & Docker

Pour lancer l’API avec Docker et sauvegarder les images sur votre machine :

```bash
docker build -t images-api .
docker run -d -p 8000:8000 -v /chemin/vers/uploads:/app/uploads --name images-api-container images-api

