import streamlit as st

from langchain_groq import ChatGroq

from config.settings import (MODEL_NAME,TEMPERATURE)

@st.cache_resource
def get_llm(api_key: str) -> ChatGroq:
    """
    Create and cache Groq LLM.

    Args:
        api_key: Groq API Key

    Returns:
        ChatGroq instance
    """
    return ChatGroq(groq_api_key=api_key,model=MODEL_NAME,temperature=TEMPERATURE)