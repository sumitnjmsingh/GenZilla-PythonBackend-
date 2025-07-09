# app/services/summarization.py
import logging
import uuid
from huggingface_hub import InferenceClient
import sys
import os

os.makedirs("image", exist_ok=True)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)))))

from app.utils.huggingface import hf_login
hf_login()

def generate_image(text: str) -> str:
    try:
        generator = InferenceClient(
          provider="nebius",
        )
        
        logger.info("Sending text to generator...")
        filename = f"{uuid.uuid4()}.png"
        output_path = os.path.join("image", filename)

        generated_url = generator.text_to_image(text,model="black-forest-labs/FLUX.1-dev")
        generated_url.save(output_path, format="PNG")

        return output_path
    except Exception as e:
        logger.error(f"Error in Image generation: {e}")
        return None
