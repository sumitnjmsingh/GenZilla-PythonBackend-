from fastapi import APIRouter, HTTPException
from app.models.question_answering import QARequest, QAResponse
from app.services.question_answering import get_answer

router = APIRouter()

@router.post("/question-answer", response_model=QAResponse)
def question_answering(req: QARequest):
    answer = get_answer(req.question, req.context)
    if not answer:
        raise HTTPException(status_code=500, detail="Failed to get answer.")
    return QAResponse(answer=answer)
