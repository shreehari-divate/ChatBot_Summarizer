import tiktoken


def clean_text(text:str) -> str:
    lines = text.splitlines()

    unique = list(
        dict.fromkeys(
            line.strip()
            for line in lines
            if line.strip()
        )
    )

    return "\n".join(unique)



def count_tokens(text: str) -> int:
    """
    Count tokens using tiktoken.
    """

    encoding = tiktoken.get_encoding(
        "cl100k_base"
    )

    return len(encoding.encode(text))