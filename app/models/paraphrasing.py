from pydantic import BaseModel

class ParaphrasingRequest(BaseModel):
    text: str

class ParaphrasingResponse(BaseModel):
    paraphrased_text: str
