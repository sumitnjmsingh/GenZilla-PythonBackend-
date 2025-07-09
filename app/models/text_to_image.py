from pydantic import BaseModel

class TextToImageRequest(BaseModel):
    prompt: str

class TextToImageResponse(BaseModel):
    image_url: str
