from fastapi import APIRouter, HTTPException
from app.models.content_generation import ContentRequest, ContentResponse
from app.services.content_generator import generate_content

router = APIRouter()

@router.post("/generate-content", response_model=ContentResponse)
def generate_content_api(req: ContentRequest):
    result = generate_content(req.prompt)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to generate content.")
    return ContentResponse(content=result)
