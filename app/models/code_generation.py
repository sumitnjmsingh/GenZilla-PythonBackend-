from pydantic import BaseModel

class CodeGenerationRequest(BaseModel):
    prompt: str

class CodeGenerationResponse(BaseModel):
    code: str
