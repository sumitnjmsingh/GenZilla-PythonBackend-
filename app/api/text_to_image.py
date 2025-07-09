from fastapi import APIRouter, HTTPException
from app.models.text_to_image import TextToImageRequest, TextToImageResponse
from app.services.text_to_image_gen import generate_image

router = APIRouter()

@router.post("/text-to-image", response_model=TextToImageResponse)
def text_to_image(req: TextToImageRequest):
    image_path = generate_image(req.prompt)
    if not image_path:
        raise HTTPException(status_code=500, detail="Failed to generate image.")
    return TextToImageResponse(image_url=image_path)
