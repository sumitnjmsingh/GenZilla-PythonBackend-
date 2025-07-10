import os
import logging
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def explain_code(code: str, language: str) -> str:
    try:
        logger.info("Explaining code...")

        CODE_EXPLANATION_PROMPT_TEMPLATE = """
        You are an expert software engineer.

        Your task is to explain the following code in simple, understandable language. Highlight what the code does, why it's written this way, and any important concepts (e.g., loops, conditions, data structures).

        Code:
        ```{language}
        {code}
        ```

        Make the explanation:
        - Beginner-friendly.
        - Line-by-line or section-wise if helpful.
        - Clear and concise.
        - Free of unnecessary technical jargon.

        Begin your explanation now.
        """

        prompt = CODE_EXPLANATION_PROMPT_TEMPLATE.format(code=code, language=language)
        response = model.generate_content(prompt)

        return response.text.strip() if response and response.text else "No explanation generated."
    except Exception as e:
        logger.error(f"Code explanation failed: {e}")
        return "Error during code explanation."