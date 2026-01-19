import numpy as np
import cv2
from fastapi import UploadFile
import os

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def read_image(file: UploadFile):
    contents = file.file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    if img is None:
        raise ValueError("Impossible de lire l'image")
    return img

def save_image(img, prefix, filename):
    output_path = os.path.join(UPLOAD_FOLDER, f"{prefix}_{filename}")
    cv2.imwrite(output_path, img)
    return output_path