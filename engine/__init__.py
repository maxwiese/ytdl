from engine.search import findVideo 
from engine.download import download

class FindAndDownload:
    def __init__(self, search_txt):
        url = findVideo(search_txt)
        download(url)
            