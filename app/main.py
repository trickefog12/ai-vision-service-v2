from fastapi import FastAPI, UploadFile, File, HTTPException
from google.cloud import vision
from typing import List
import os

app = FastAPI(
    title="AI Vision Professional API",
    description="Multi-functional Image Analysis API using Google Cloud Vision",
    version="2.0.0"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "message": "Welcome to the AI Vision API",
        "documentation": "/docs",
        "endpoints": {
            "health": "/health",
            "single_analyze": "/analyze",
            "multiple_analyze": "/analyze-multiple"
        }
    }

@app.get("/health")
def health():
    return {"status": "ok", "environment": "production" if os.getenv("K_SERVICE") else "local"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if file.content_type not in {"image/jpeg", "image/png", "image/webp"}:
        raise HTTPException(status_code=400, detail=f"File {file.filename} is not a supported image type")
    
    return await process_vision_data(file)

@app.post("/analyze-multiple")
async def analyze_multiple(files: List[UploadFile] = File(...)):
    results = []
    for file in files:
        if file.content_type in {"image/jpeg", "image/png", "image/webp"}:
            data = await process_vision_data(file)
            results.append(data)
        else:
            results.append({"filename": file.filename, "error": "Unsupported type"})
    return {"results": results}

async def process_vision_data(file: UploadFile):
    content = await file.read()
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)

    # Label Detection
    label_resp = client.label_detection(image=image)
    labels = [{"description": l.description, "score": round(l.score, 2)} for l in label_resp.label_annotations]

    # Text Detection
    text_resp = client.text_detection(image=image)
    texts = [t.description for t in text_resp.text_annotations]

    return {
        "filename": file.filename,
        "labels": labels[:5],
        "extracted_text": texts[0] if texts else "No text found"
    }