# run_api.ps1
# Script PowerShell pour build, tester et lancer l'API Docker

# Arrêter et supprimer le conteneur s'il existe déjà
$existing = docker ps -a --filter "name=images-api-container" --format "{{.ID}}"
if ($existing) {
    Write-Host "Arrêt et suppression du conteneur existant..."
    docker stop images-api-container
    docker rm images-api-container
}

# Build de l'image Docker
Write-Host "Build de l'image Docker..."
docker build -t images-api .

# Lancer les tests pytest dans un conteneur temporaire
Write-Host "Lancement des tests automatisés..."
docker run --rm -v ${PWD}/tests:/app/tests -w /app images-api pytest tests/

# Lancer l'API dans un conteneur détaché
Write-Host "Lancement de l'API..."
docker run -d -p 8000:8000 -v ${PWD}/uploads:/app/uploads --name images-api-container images-api

Write-Host "API lancée ! Accédez à http://127.0.0.1:8000/docs"
