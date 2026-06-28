from utils.helpers import clean_text


def test_remove_empty_lines():

    text = """
Hello

World

"""

    result = clean_text(text)

    assert result == "Hello\nWorld"


def test_remove_duplicate_lines():

    text = """
Python
Python
AI
AI
"""

    result = clean_text(text)

    assert result == "Python\nAI"


def test_empty_string():

    result = clean_text("")

    assert result == ""


def test_single_line():

    result = clean_text("LangChain")

    assert result == "LangChain"