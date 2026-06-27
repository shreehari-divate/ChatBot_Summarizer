from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from config.prompts import SUMMARY_PROMPT

from utils.helpers import clean_text

class SummarizerService:

    @staticmethod
    def summarize(documents,llm) -> str:
        content = "\n".join(doc.page_content for doc in documents)

        content = clean_text(content)

        prompt = PromptTemplate.from_template(SUMMARY_PROMPT)

        chain = (
            prompt | llm | StrOutputParser()
        )

        summary = chain.invoke(
            {
                "content":content
            }
        )

        return summary