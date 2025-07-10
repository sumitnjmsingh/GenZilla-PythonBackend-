from pydantic import BaseModel

class ContentRequest(BaseModel):
    prompt: str

class ContentResponse(BaseModel):
    content: str
