from pydantic import BaseModel

class CodeExplainRequest(BaseModel):
    code: str
    language: str

class CodeExplainResponse(BaseModel):
    explanation: str
