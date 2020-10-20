import os, json, pathlib

from . import MangaSourceEstate

class MangaEstate:
    def __init__(
        self,
        home_directory:str=None,
        manga:dict=None
    ):
        if not isinstance(home_directory, str):
            raise ValueError(
                'Home directory must be a string representing a file path.'
            )

        if not isinstance(manga, dict):
            raise ValueError(
                'Manga must be a dict that follows the standard.'
            )

        self.__verify_meta(
            manga
        )

        self.__home_directory = home_directory
        self.__manga = manga

        self.__estate = None

        self.__meta = None
        self.__chapter_index = None
        self.__sources = list()

        self.__load_estate()

    def __load_estate(self):
        try:
            self.__read_estate_fs()
        except EnvironmentError:
            self.__build_estate_fs()
        except AttributeError:
            self.__build_estate_fs()
        except TypeError:
            self.__build_estate_fs()
        
    def __get_estate_directory(self):
        return os.path.join(
            self.__home_directory,
            self.__manga['title']
        )
    
    def __get_sources_directory(self):
        return os.path.join(
            self.__estate,
            '.sources'
        )

    def __get_meta_path(self):
        return os.path.join(
            self.__estate,
            'meta.json'
        )


    def __build_estate_fs(self):
        self.__estate = os.path.join(
            self.__home_directory,
            self.__manga['title']
        )

        estate_path = self.__get_estate_directory()
        meta_path = self.__get_meta_path()
        sources_path = self.__get_sources_directory()

        for path in [ estate_path, sources_path ]:
            if not os.path.isdir(path):
                os.makedirs(path)

        if not os.path.isfile(meta_path):
            pathlib.Path(meta_path).touch()
        
        self.__dump_meta(meta_path)

    def __read_estate_fs(self):
        meta_path = self.__get_meta_path()

        with open(meta_path) as meta:
            self.__meta = json.loads(
                meta.read()
            )

        self.__verify_meta(
            self.__meta
        )

        self.__load_sources()

    def __verify_meta(self, obj: dict):
        keys = obj.keys()

        for item in [
            'title',
            'description',
            'status',
            'tags',
            'authors',
            'alternate_names',
            'url'
        ]:
            if item not in keys:
                raise EnvironmentError(
                    'Manga meta data is not properly defined.'
                )

    def __load_sources(self):
        sources_directory = self.__get_sources_directory()

        if not os.path.isdir(sources_directory):
            os.makedirs(sources_directory)
            return
        
        source_dirs = os.listdir(sources_directory)

        for source_dir in source_dirs:
            try:
                source = MangaSourceEstate(
                    directory=source_dir
                )

                self.__sources.append(source)
            except EnvironmentError:
                continue


    def __dump_meta(self, path):
        estate = open(path, 'w+')

        estate.write(
            json.dumps(
                self.__manga,
                indent=4
            )
        )

        estate.close()
    
    def _get_chapter_index(self):
        return self.__chapter_index

    def get_sources(self):
        return [ source.name for source in self.__sources ]

    def __get_source(self, name):
        for source in self.__sources:
            if source.name == name:
                return source
        return None

    def __add_source(self, name: str, url: str):

        base_directory = self.__get_sources_directory()
        directory = os.path.join(
            base_directory,
            name
        )

        source = MangaSourceEstate(
            directory=directory,
            name=name,
            url=url
        )

    def synchronize_with_source(self, name: str, url: str):
        source = self.__get_source(
            name
        )

        if source == None:
            self.__add_source(name, url)
            #self.synchronize_with_source(name, url)

        print('synchronizing with source')

    def get_home_directory(self):
        pass

