

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