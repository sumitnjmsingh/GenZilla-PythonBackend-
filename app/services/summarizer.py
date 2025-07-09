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

def summarize_text(text: str) -> str:
    try:
        summarizer = InferenceClient(
          provider="hf-inference",
        )
        
        logger.info("Sending text to summarizer...")
        summary = (summarizer.summarization(text,model="tuner007/pegasus_summarizer")).get('summary_text')
        return summary if summary else "Unable to summarize the text."
    except Exception as e:
        logger.error(f"Error in summarization: {e}")
        return None
