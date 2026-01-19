from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from app.processing import grayscale, blur, resize
from app.utils import read_image, save_image

from enum import Enum

class ProcessType(str, Enum):
    grayscale = "grayscale"
    blur = "blur"
    resize = "resize"

app = FastAPI(title="Image Processing API")

@app.post("/process")
async def process_image(
    file: UploadFile = File(...), 
    type: ProcessType = Form(...),
    ratio: float = Form(0.5),
    blur_strength: int = Form(15)
):
    if not file.content_type.startswith("image/"):
        return {"error": "Le fichier n'est pas une image"}

    try:
        img = read_image(file)
    except ValueError as e:
        return {"error": str(e)}

    if type == ProcessType.grayscale:
        img_out = grayscale(img)
        prefix = "grayscale"

    elif type == ProcessType.blur:
        if blur_strength % 2 == 0: #strength doit être un nombre impair
            blur_strength += 1
        img_out = blur(img, strength=blur_strength)
        prefix = "blur"

    elif type == ProcessType.resize:
        img_out = resize(img, ratio=ratio)
        prefix = "resize"

    else:
        return {"error": "Type de traitement inconnu"}

    output_path = save_image(img_out, prefix, file.filename)
    return FileResponse(output_path)
