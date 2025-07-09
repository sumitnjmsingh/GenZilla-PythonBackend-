import os
import sys
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import logging
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(__file__)))))

load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
from app.utils.huggingface import hf_login
hf_login()

def get_answer(question: str, context: str) -> str:
    try:
        client = InferenceClient(
            provider="hf-inference",
        )
        response = client.question_answering(
            question=question,
            context=context,
            model="deepset/roberta-base-squad2"
        )
        logger.info(f"Received response: {response}")
        return response.get("answer", "No answer found.")
    except Exception as e:
        logger.error(f"Error in question answering: {e}")
        return "Unable to find an answer."
