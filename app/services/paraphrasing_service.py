import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

def paraphrase_text(text: str) -> str:
    try:
        logger.info(f"Paraphrasing input: {text}")
        prompt = (
            "Paraphrase the following sentence to make it sound natural and fluent:\n\n"
            f"{text}"
        )
        response = model.generate_content(prompt)
        return response.text.strip() if response and response.text else "No paraphrased result."
    except Exception as e:
        logger.error(f"Paraphrasing failed: {e}")
        return "Error during paraphrasing."
