import streamlit as st
import os

from config.settings import APP_TITLE, APP_ICON 
from utils.validators import validate_url
from utils.logger import logger

from services.llm_services import get_llm 
from services.load_services import LoaderService 
from services.summarizer_serivce import SummarizerService

#1] SET THE PAGE CONFIG
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON
)
st.title=APP_TITLE

#2] SET THE SIDEBAR
with st.sidebar:
    api_key = st.text_input("GROQ API Key", type="password")


#3] MAIN FORM
url = st.text_input("Enter the url either from website or youtube!!")
summarize_btn = st.button("Summarize")

#4] SUMMARIZE THE CONTENT
if summarize_btn:
    try:
        if not api_key:
            st.error("Please provide the GROQ API Key")
            st.stop()

        if not url:
            st.error("Please provide the url")
            st.stop()

        if not validate_url(url):
            st.error("The provided URL is not valid. Stopping the process")
            st.stop()    

        logger.info(f"Processing the given url: {url}")

        with st.spinner("Loading your content....."):
            documents = LoaderService.load(url)
            logger.info(f"Loaded {len(documents)} documents")

        if not documents:
            st.error("No content found")
            st.stop()

        with st.spinner("Intitalising LLM..."):
            llm = get_llm(api_key)

        with st.spinner("Generating Summary....."):
            summary = SummarizerService.summarize(documents=documents,llm=llm) 

        st.subheader("Summary")
        st.write(summary)



    except Exception as e:
        logger.exception(e)

        st.error("Unexpected error occured. Please check the logs!!")