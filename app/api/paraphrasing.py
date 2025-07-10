from fastapi import APIRouter, HTTPException
from app.models.paraphrasing import ParaphrasingRequest, ParaphrasingResponse
from app.services.paraphrasing_service import paraphrase_text

router = APIRouter()

@router.post("/paraphrase", response_model=ParaphrasingResponse)
def paraphrase(req: ParaphrasingRequest):
    result = paraphrase_text(req.text)
    if not result or "Error" in result:
        raise HTTPException(status_code=500, detail="Failed to paraphrase.")
    return ParaphrasingResponse(paraphrased_text=result)
