# app/api/summarization.py
from fastapi import APIRouter, HTTPException
from app.models.summarization import SummarizationRequest, SummarizationResponse
from app.services.summarizer import summarize_text

router = APIRouter()

@router.post("/summarize", response_model=SummarizationResponse)
def summarize(payload: SummarizationRequest):
    summary = summarize_text(payload.text)
    if summary is None:
        raise HTTPException(status_code=500, detail="Failed to generate summary.")
    return SummarizationResponse(summary=summary)


