from fastapi import FastAPI, UploadFile, File, HTTPException
from google.cloud import vision
import os

app = FastAPI(title="AI Vision Professional API")

@app.get("/health")
def health():
    return {"status": "ok", "service": "Vision API v2"}

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if file.content_type not in {"image/jpeg", "image/png", "image/webp"}:
        raise HTTPException(status_code=400, detail="Unsupported file type")

    content = await file.read()
    client = vision.ImageAnnotatorClient()
    image = vision.Image(content=content)

    # 1. Label Detection (Τι δείχνει η φωτό)
    label_resp = client.label_detection(image=image)
    labels = [{"description": l.description, "score": float(l.score)} for l in label_resp.label_annotations]

    # 2. Text Detection (Τι γράφει η φωτό)
    text_resp = client.text_detection(image=image)
    texts = [t.description for t in text_resp.text_annotations]

    return {
        "filename": file.filename,
        "labels": labels[:5],  # Top 5 labels
        "extracted_text": texts[0] if texts else "No text found" # Το πλήρες κείμενο
    }