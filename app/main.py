# app/main.py
import sys
import os
from fastapi.middleware.cors import CORSMiddleware
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import uvicorn
from fastapi import FastAPI
from app.api import summarization, translation, text_to_image

app = FastAPI(title="GenAI Services API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(summarization.router, prefix="/api")
app.include_router(translation.router, prefix="/api")
app.include_router(text_to_image.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the GenAI Backend!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
