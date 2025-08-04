from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

MODEL_PATH = "./stride-finetuned-model"
classifier = pipeline("text-classification", model=MODEL_PATH, return_all_scores=True)

app = FastAPI(
    title="STRIDE Threat Model AI v3 - Fine-Tuned",
    description="API que usa um modelo Transformer especialista, treinado para STRIDE.",
    version="3.0.0"
)

class SystemDescription(BaseModel):
    description: str

@app.post("/analyze")
def analyze_description(data: SystemDescription):
    results = classifier(data.description)
    
    probabilities = {item['label']: round(item['score'], 4) for item in results[0]}
        
    return {
        "input_description": data.description,
        "probabilities": probabilities
    }

@app.get("/")
def read_root():
    return {"status": "API v3 (Fine-Tuned) está rodando!"}