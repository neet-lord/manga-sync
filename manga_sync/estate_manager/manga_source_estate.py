import os, pathlib, json

class MangaSourceEstate:
    def __init__(self,
        directory: str,
        name=None,
        url=None
    ):
        assert isinstance(directory, str)

        self.__directory = directory
        self.__meta = {
            'name': name,
            'url': url
        }

        if self.__meta['name'] is None:
            try:
                self.__read_fs()
            except FileNotFoundError:
                raise ValueError(
                    'Could not load the meta file. It doesn\'t exist. '
                    'Please provide the name and url to build the estate.' 
                )
        else:
            self.__build_fs()

        self.__chapter_index = None

    def __build_fs(self):
        path = self.__get_estate_path()
        
        if not os.path.isdir(path):
            os.makedirs(path)

        meta_path = self.__get_meta_path()

        if not os.path.isfile(meta_path):
            pathlib.Path(meta_path).touch()

        self.__dump_meta()

    def __dump_meta(self):
        path = self.__get_meta_path()

        meta = open(path, 'w+')

        meta.write(
            json.dumps(
                self.__meta,
                indent=4
            )
        )

        meta.close()

    def __read_fs(self):
        meta_path = self.__get_meta_path()
        meta = open(meta_path, 'r')
        
        self.__meta = json.loads(
            meta.read()
        )
        meta.close()

    def __get_estate_path(self):
        return self.__directory

    def __get_meta_path(self):
        return os.path.join(
            self.__get_estate_path(),
            'meta.json'
        )
    
    def _get_name(self):
        return self.__meta['name']
    
    def __update_chapter_index(self):
        print('updating the chapter index')
        # Get specify a new chapter index.
        # The chapter index only contains the chapter index,
        # and name.
        # It is used solely to know how many chapters we have.

    def _get_chapter_index(self, update_estate):
        if update_estate:
            self.__update_chapter_index()

        print('fetching chapter index')
        return ''


