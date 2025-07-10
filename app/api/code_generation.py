from fastapi import APIRouter, HTTPException
from app.models.code_generation import CodeGenerationRequest, CodeGenerationResponse
from app.services.code_generator import generate_code

router = APIRouter()

@router.post("/code-generation", response_model=CodeGenerationResponse)
def code_generation(req: CodeGenerationRequest):
    result = generate_code(req.prompt)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to generate code.")
    return CodeGenerationResponse(code=result)
