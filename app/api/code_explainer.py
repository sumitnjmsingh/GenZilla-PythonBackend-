from fastapi import APIRouter, HTTPException
from app.models.code_explainer import CodeExplainRequest, CodeExplainResponse
from app.services.code_explainer import explain_code

router = APIRouter()

@router.post("/code-explain", response_model=CodeExplainResponse)
def explain(req: CodeExplainRequest):
    result = explain_code(req.code, req.language)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to generate explanation.")
    return CodeExplainResponse(explanation=result)
