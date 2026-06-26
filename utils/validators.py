import validators

def validate_url(url:str)->bool:
    """
    Validate whether the provided string is a valid URL.

    Args:
        url: URL entered by the user.

    Returns:
        True if valid, False otherwise.
    """
    return validators.url(url)