from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import cv2
import numpy as np

from src.object_detection import detect_objects


app = FastAPI(
    title="AI Image Processing API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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


    result = detect_objects(img)


    return {
        "filename": file.filename,
        "result": result
    }
