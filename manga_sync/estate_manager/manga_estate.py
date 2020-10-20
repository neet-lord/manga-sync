from . import MangaSource

class MangaEstate:
    def __init__(
        self,
        home_directory,
        manga,
        chapters
    ):
        self.__home_directory = home_directory
        self.__manga = manga
        self.__chapter_index = self._get_chapter_index()
        self.__sources = list(MangaSource)

    def __build_chapter_index(self):
        pass

    def _get_chapter_index(self):
        return self.__chapter_index

    def get_sources(self):
        pass

    def add_source(self):
        pass

    def remove_source(self):
        pass

    def synchronize_with_source(self, source: MangaSource):
        pass


