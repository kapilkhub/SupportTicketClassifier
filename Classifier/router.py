from fastapi import APIRouter
from transformers import pipeline
from pydantic import BaseModel


router = APIRouter()


classifier = pipeline('zero-shot-classification', model='cross-encoder/nli-MiniLM2-L6-H768', device=-1)
classifier('warm up', ['a', 'b', 'c'])

@router.get("/")
async def read_root():
    return {"message": "Welcome to the Support Ticket Classifier API"}

@router.get("/health")
async def health_check():
    return {"status": "OK"}



class ClassifyRequest(BaseModel):
    text: str
    ticket_labels: list[str]

@router.post("/classify")
def classify_text(item: ClassifyRequest) -> str:
    result = classifier(item.text, item.ticket_labels)
    return result['labels'][0]