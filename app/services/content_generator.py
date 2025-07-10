import os
import sys
import logging
from huggingface_hub import InferenceClient
from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)))))

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from app.utils.huggingface import hf_login
hf_login()

client = InferenceClient(
    provider="fireworks-ai",
)

def generate_content(prompt: str) -> str:
    try:
        logger.info(f"Generating content for prompt: {prompt}")
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content if completion.choices else "No content generated."
    except Exception as e:
        logger.error(f"Error during content generation: {e}")
        return None
