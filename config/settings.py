#APLLICATION CONFIGURATION

import os
from dotenv import load_dotenv

load_dotenv()

#1] LLM CONFIG
MODEL_NAME = "llama-3.3-70b-versatile"
TEMPERATURE = 0
MAX_SUMMARY_WORDS = 300
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#2] APPLICATION (STREAMLIT)
APP_TITLE = "AI CONTENT SUMMARIZER"
APP_ICON = "🤖"
SUPPORTED_LANGUAGES = ["en","hi"]
REQUEST_TIMEOUT = 30
USER_AGENT = (
    "Mozilla/5.0",
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/138.0 Safari/537.36"
)

#3] CHUNK
CHUNK_SIZE = 3000
CHUNK_OVERLAP = 300
