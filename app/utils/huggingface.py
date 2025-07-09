import os
from dotenv import load_dotenv
from huggingface_hub import login

load_dotenv()

def hf_login():
    hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
    if not hf_token:
        raise EnvironmentError("HUGGINGFACEHUB_ACCESS_TOKEN is not set.")
    login(hf_token)