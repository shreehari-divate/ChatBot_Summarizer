from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config.prompts import SUMMARY_PROMPT
from config.settings import (CHUNK_OVERLAP,CHUNK_SIZE)

from utils.helpers import clean_text

class SummarizerService:

    @staticmethod
    def summarize(documents,llm) -> str:
        content = "\n".join(doc.page_content for doc in documents)

        content = clean_text(content)
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )

        chunks = splitter.split_text(content)

        

        prompt = PromptTemplate.from_template(SUMMARY_PROMPT)

        chain = (
            prompt | llm | StrOutputParser()
        )

        chunk_summaries = []
        for chunk in chunks:
            chunk_summary = chain.invoke(
                {
                    "content":chunk
                }
            )
            chunk_summaries.append(chunk_summary)


        combined_summary = "\n".join(
        chunk_summaries
        )    

        final_summary = chain.invoke(
            {
                "content": combined_summary
            }
        )

        return final_summary