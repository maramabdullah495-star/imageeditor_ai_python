from fastapi import FastAPI

app = FastAPI(
    title="AI Image Processing API"
)


@app.get("/")
def home():
    return {
        "message": "AI Image Processing API is running"
    }
