import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configure the Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_code(instruction: str) -> str:
    try:
        logger.info(f"Generating code for instruction: {instruction}")

        CODE_GEN_PROMPT_TEMPLATE = """
        You are an expert programmer.

        Generate clean, readable, and well-commented code based on the following instruction:

        Instruction:
        {instruction}

        Make sure the code:
        - Uses best practices.
        - Is beginner-friendly (if applicable).
        - Includes brief comments for clarity.
        - Is written in an appropriate programming language.
        - Only outputs code, no explanation.

        Begin generating code now.
        """

        prompt = CODE_GEN_PROMPT_TEMPLATE.format(instruction=instruction)
        response = model.generate_content(prompt)

        return response.text.strip() if response and response.text else "No code generated."
    except Exception as e:
        logger.error(f"Code generation failed: {e}")
        return "Error during code generation."

