import pytest
from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

# Chemin vers l'image de test
TEST_IMAGE_PATH = "tests/test_image.jpg"

# Vérifie que l'image de test existe
assert os.path.exists(TEST_IMAGE_PATH), f"Placez une image de test à {TEST_IMAGE_PATH}"

# Liste des types de traitement à tester
TEST_TYPES = [
    {"type": "grayscale"},
    {"type": "blur", "blur_strength": "15"},  # string car c'est envoyé via Form
    {"type": "resize", "ratio": "0.5"}        # string pour le même motif
]

@pytest.mark.parametrize("params", TEST_TYPES)
def test_process_endpoint(params):
    """
    Test de l'endpoint /process pour différents types de traitement.
    Vérifie que le code HTTP est 200 et que le type de contenu est une image.
    """
    with open(TEST_IMAGE_PATH, "rb") as f:
        files = {"file": ("test_image.jpg", f, "image/jpeg")}
        response = client.post("/process", files=files, data=params)

    assert response.status_code == 200, f"Erreur pour type={params}"
    assert response.headers["content-type"].startswith("image/"), \
        f"La réponse n'est pas une image pour type={params}"
