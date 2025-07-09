# app/services/summarization.py
import logging
from huggingface_hub import InferenceClient
import sys
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)))))

from app.utils.huggingface import hf_login
hf_login()

def translate_text(text: str) -> str:
    try:
        translator = InferenceClient(
          provider="hf-inference",
        )
        
        logger.info("Sending text to translator...")
        translated_text = (translator.translation(text,model="Helsinki-NLP/opus-mt-en-ar")).get('translation_text')
        return translated_text if translated_text else "Unable to translate the text."
    except Exception as e:
        logger.error(f"Error in translation: {e}")
        return None
