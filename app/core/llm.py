"""
LLM Manager

Responsible for creating and returning the Gemini LLM instance.

All agents should import get_llm() from this file.
"""

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import MODEL_NAME, TEMPERATURE

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please check your .env file."
    )


_llm = ChatGoogleGenerativeAI(
    model=MODEL_NAME,
    google_api_key=API_KEY,
    temperature=TEMPERATURE,
)


def get_llm():
    """
    Returns the shared Gemini LLM instance.
    """
    return _llm