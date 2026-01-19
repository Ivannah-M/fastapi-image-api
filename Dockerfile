# Image officielle Python
FROM python:3.10-slim

# Installer les dépendances système nécessaires à OpenCV
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libfontconfig1 \
    && rm -rf /var/lib/apt/lists/*

# Créer le dossier de l'app
WORKDIR /app

# Copier requirements et installer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Installer pytest et httpx pour les tests
RUN pip install pytest httpx

# Copier le code
COPY app/ ./app
COPY tests/ ./tests

# Créer le dossier uploads
RUN mkdir uploads

# Définir PYTHONPATH pour que Python trouve le module 'app'
ENV PYTHONPATH=/app

# Exposer le port FastAPI
EXPOSE 8000

# Commande pour lancer l'API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# Commande optionnelle pour tests
# On peut l'exécuter via: docker run --rm images-api pytest
