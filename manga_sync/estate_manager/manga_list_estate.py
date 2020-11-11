import os, json, pathlib

from json.decoder import JSONDecodeError

from . import MangaSourceEstate


class MangaEstate:
    def __init__(
        self,
        home_directory:str=None
    ):
        if not isinstance(home_directory, str):
            raise ValueError(
                'Home directory must be a string representing a file path.'
            )

        self.__home_directory = home_directory
        self.__manga_index = None
        
        self.__manga_estates = list()

        self.__load_estate()

    def __load_estate(self):
        try:
            self.__read_estate_fs()
        except EnvironmentError:
            self.__build_estate_fs()
        except JSONDecodeError:
            self.__build_estate_fs()
    
    def __get_manga_index_path(self):
        return os.path.join(
            self.__home_directory,
            'manga_list.json'
        )

    def __build_estate_fs(self):
        if not os.path.exists(self.__home_directory):
            os.makedirs(self.__home_directory)

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
                    directory=os.path.join(
                        sources_directory,
                        source_dir
                    )
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
            if source._get_name() == name:
                return source
        return None

    def __add_source(self, name: str, url: str):

        base_directory = self.__get_sources_directory()

        directory = os.path.join(
            base_directory,
            name
        )

        MangaSourceEstate(
            directory=directory,
            name=name,
            url=url
        )

        self.__load_sources()

    def update_estate(self, name: str, url: str):
        source = self.__get_source(
            name
        )

        if source == None:
            raise EnvironmentError('The source \'{0}\' hasn\'t been setup in the file system properly. Run --update-source first.'.format(name))

        config_file = self.__get_config_path()

        config = open(config_file, 'w')

        config_dict = {
            'source': source.get_meta()
        }

        config.write(
            json.dumps(
                config_dict,
                indent=4
            )
        )

        config.close()
        
        chapters = source.get_chapters()

        self.__chapter_index = chapters

        chapters_path = self.__get_chapters_path()
        chapters_file = open(chapters_path, 'w')

        chapters_file.write(
            json.dumps(chapters, indent=4)
        )

        chapters_file.close()

    def update_source(self, name: str, url: str, chapters: list):
        source = self.__get_source(
            name
        )

        if source == None:
            self.__add_source(name, url)
            
            source = self.__get_source(
                name
            )

            source.synchronize_with_chapters(
                chapters
            )

    def get_chapters(self, name: str, url: str, max_mangas: int, max_chapters: int):
        pass
