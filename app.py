import time
import streamlit as st

from config.settings import APP_TITLE, APP_ICON
from utils.validators import validate_url
from utils.logger import logger

from services.llm_services import get_llm
from services.load_services import LoaderService
from services.summarizer_serivce import SummarizerService


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON
)

st.title=APP_TITLE


# ==========================================
# SESSION STATE
# ==========================================

if "history" not in st.session_state:
    st.session_state.history = []

if "url_cache" not in st.session_state:
    st.session_state.url_cache = {}


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.header("Configuration")

    api_key = st.text_input(
        "GROQ API Key",
        type="password"
    )

    st.divider()

    st.subheader("Summary History")

    if st.session_state.history:

        for item in reversed(st.session_state.history):

            with st.expander(item["url"]):
                st.write(item["summary"])

    else:
        st.caption("No summaries generated yet.")


# ==========================================
# MAIN UI
# ==========================================

url = st.text_input(
    "Enter a YouTube or Website URL"
)

summarize_btn = st.button("Summarize")


# ==========================================
# PROCESS REQUEST
# ==========================================

if summarize_btn:

    try:

        # --------------------------
        # VALIDATION
        # --------------------------

        if not api_key:
            st.error("Please provide the GROQ API Key.")
            st.stop()

        if not url:
            st.error("Please provide a URL.")
            st.stop()

        if not validate_url(url):
            st.error("The provided URL is not valid.")
            st.stop()

        logger.info(f"Processing URL: {url}")

        start_time = time.time()

        # --------------------------
        # CACHE CHECK
        # --------------------------

        if url in st.session_state.url_cache:

            logger.info(f"Cache HIT for URL: {url}")

            cached_data = st.session_state.url_cache[url]

            summary = cached_data["summary"]
            documents_count = cached_data["documents_count"]
            total_chars = cached_data["total_chars"]

            st.success("Summary loaded from cache.")

        else:

            logger.info(f"Cache MISS for URL: {url}")

            # --------------------------
            # LOAD DOCUMENTS
            # --------------------------

            with st.spinner("Loading content..."):

                documents = LoaderService.load(url)

                logger.info(
                    f"Loaded {len(documents)} document(s)"
                )

            if not documents:
                st.error("No content found.")
                st.stop()

            # --------------------------
            # INITIALIZE LLM
            # --------------------------

            with st.spinner("Initializing LLM..."):

                llm = get_llm(api_key)

            # --------------------------
            # GENERATE SUMMARY
            # --------------------------

            with st.spinner("Generating summary..."):

                summary = SummarizerService.summarize(
                    documents=documents,
                    llm=llm
                )

            documents_count = len(documents)

            total_chars = sum(
                len(doc.page_content)
                for doc in documents
            )

            # --------------------------
            # SAVE TO CACHE
            # --------------------------

            st.session_state.url_cache[url] = {
                "summary": summary,
                "documents_count": documents_count,
                "total_chars": total_chars
            }

        processing_time = round(
            time.time() - start_time,
            2
        )

        # --------------------------
        # DISPLAY SUMMARY
        # --------------------------

        st.subheader("Summary")

        st.write(summary)

        # --------------------------
        # STORE HISTORY
        # --------------------------

        st.session_state.history.append(
            {
                "url": url,
                "summary": summary
            }
        )

        # --------------------------
        # METRICS
        # --------------------------

        st.info(
            f"""
            Documents Loaded: {documents_count}

            Characters Processed: {total_chars}

            Processing Time: {processing_time} sec
            """
        )

        # --------------------------
        # DOWNLOAD BUTTON
        # --------------------------

        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

    except Exception as e:

        logger.exception(
            f"Unexpected error occurred: {e}"
        )

        st.error(
            "Unexpected error occurred. Please check logs."
        )