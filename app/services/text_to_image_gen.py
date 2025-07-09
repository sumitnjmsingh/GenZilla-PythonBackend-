import logging
import uuid
from huggingface_hub import InferenceClient
import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv
from io import BytesIO
import sys

load_dotenv()

cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET"),
    secure=True
)

os.makedirs("image", exist_ok=True)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)))))
from app.utils.huggingface import hf_login
hf_login()

def generate_image(text: str) -> str:
    try:
        generator = InferenceClient(provider="nebius")
        
        logger.info("Sending text to generator...")
        generated_img = generator.text_to_image(text, model="black-forest-labs/FLUX.1-dev")

        buffer = BytesIO()
        generated_img.save(buffer, format="PNG")
        buffer.seek(0)

        upload_result = cloudinary.uploader.upload(buffer, folder="genzilla", public_id=f"{uuid.uuid4()}")

        return upload_result.get("secure_url")
    
    except Exception as e:
        logger.error(f"Error in Image generation: {e}")
        return None
