from utils.validators import validate_url

def test_validate_http_url():
    assert validate_url("https://www.google.com")


def test_valid_https_url():
    assert validate_url("https://python.org")


def test_invalid_url():
    assert not validate_url("invalid_url")

def test_empty_url():
    assert not validate_url("")    