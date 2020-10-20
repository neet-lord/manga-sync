class MangaSourceEstate:
    def __init__(self,
        directory,
        name=None,
        url=None
    ):
        self.__directory = directory
        
        if name is None and url is None:
            self.__read_fs()
        else:
            self.__build_fs()
        
        self.__meta = None
        self.__chapter_index = None

        self.__load_source()

    def __build_fs(self):
        pass

    def __read_fs(self):
        pass

    def __load_source(self):
        pass

    def _update_chapter_index(self):
        pass

    def _get_chapter_index(self):
        pass
