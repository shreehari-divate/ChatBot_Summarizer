from langchain_community.document_loaders import (
    YoutubeLoader,
    WebBaseLoader
)

from config.settings import USER_AGENT


class LoaderService:

    @staticmethod
    def load(url: str):

        if "youtube.com" in url or "youtu.be" in url:
            return LoaderService._load_youtube(url)

        return LoaderService._load_website(url)

    @staticmethod
    def _load_youtube(url: str):

        loader = YoutubeLoader.from_youtube_url(
            url,
            add_video_info=False,
            language=["hi", "en"]
        )

        return loader.load()

    @staticmethod
    def _load_website(url: str):

        loader = WebBaseLoader(
            web_paths=(url,)
        )

        documents = loader.load()

        return documents