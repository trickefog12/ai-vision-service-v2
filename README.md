# 👁️ AI Vision Professional API

A production-ready microservice built with **FastAPI** and **Google Cloud Vision API**, containerized with **Docker**, and deployed on **Google Cloud Run**.

## 🚀 Live Demo
- **Base URL:** [https://ai-vision-api-544647878540.europe-west3.run.app/health]
- **Interactive Documentation (Swagger):** [https://ai-vision-api-544647878540.europe-west3.run.app/docs]

## 🛠️ Tech Stack
- **Backend:** Python, FastAPI, Uvicorn
- **AI Engine:** Google Cloud Vision API (Label & OCR detection)
- **DevOps:** Docker (Multi-platform build), Google Artifact Registry
- **Cloud:** Google Cloud Run (Serverless), IAM Service Accounts

## ✨ Key Features
- **Asynchronous Processing:** High-performance image analysis.
- **OCR & Object Detection:** Extract labels and text simultaneously.
- **Multi-File Support:** Analyze multiple images in a single request.
- **Serverless Infrastructure:** Fully scalable deployment on GCP.
- **Professional IAM:** Implements 'Least Privilege' using dedicated Service Accounts.

## 📝 API Endpoints
- `GET /`: Service status and navigation.
- `GET /health`: Health check for monitoring.
- `POST /analyze`: Analysis of a single image.
- `POST /analyze-multiple`: Batch analysis for multiple images.

## ⚙️ Local Development
1. Clone the repo.
2. Install dependencies: `pip install -r requirements.txt`.
3. Set up GCP credentials.
4. Run locally: `uvicorn app.main:app --reload`.
