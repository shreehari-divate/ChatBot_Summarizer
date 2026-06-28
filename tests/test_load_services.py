from unittest.mock import patch

from services.load_services import LoaderService


@patch("services.load_services.LoaderService._load_youtube")
def test_youtube_url_calls_youtube_loader(mock_youtube_loader):
    mock_youtube_loader.return_value=["dummy"]

    LoaderService.load("https://www.youtube.com/watch?v=123")

    mock_youtube_loader.assert_called_once()


@patch("services.load_services.LoaderService._load_website")
def test_website_url_calls_website_loader(mock_website_loader):
    mock_website_loader.return_value = [
        "dummy"
    ]

    LoaderService.load(
        "https://python.org"
    )

    mock_website_loader.assert_called_once()    