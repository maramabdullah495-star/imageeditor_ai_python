from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np


app = FastAPI(
    title="AI Image Processing API"
)


@app.get("/")
def home():
    return {
        "message": "AI Image Processing API is running"
    }


@app.post("/process-image")
async def process_image(file: UploadFile = File(...)):

    contents = await file.read()

    np_image = np.frombuffer(
        contents,
        np.uint8
    )

    img = cv2.imdecode(
        np_image,
        cv2.IMREAD_COLOR
    )

    height, width, _ = img.shape

    return {
        "filename": file.filename,
        "width": width,
        "height": height,
        "status": "image received"
    }
