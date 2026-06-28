from unittest.mock import patch

from langchain_core.documents import Document

from services.summarizer_serivce import (
    SummarizerService
)


@patch.object(
    SummarizerService,
    "generate_summary"
)
def test_summarizer_returns_summary(
    mock_generate_summary
):

    mock_generate_summary.return_value = (
        "Mock Summary"
    )

    documents = [
        Document(
            page_content=
            "Python is a programming language"
        )
    ]

    result = SummarizerService.summarize(
        documents=documents,
        llm=None
    )

    assert result == "Mock Summary"