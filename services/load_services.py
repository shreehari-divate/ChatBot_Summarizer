from langchain_community.document_loaders import (
    YoutubeLoader,
    UnstructuredURLLoader
)

from config.settings import USER_AGENT

class LoaderService:

    @staticmethod
    def load(url:str):
        
        if "youtube" or "youtu.be" in url:
            return LoaderService._load_youtube(url)


    @staticmethod
    def _load_youtube(url:str):
        loader = YoutubeLoader.from_youtube_url(
            url,
            add_video=False,
            language=["hi","en"]
        )    
        return loader.load()
    
    @staticmethod
    def _load_wensite(url:str):
        loader = UnstructuredURLLoader(
            urls=[url],
            ssl_verify=False,
            headers={"User-Agent":USER_AGENT}
        )    
        return loader.load()