import json

from .estate_manager import (
    MangaEstate,
    MangaSourceEstate
)

def main(params):
    source = open(params.source)
    manga_list= json.loads(source.read())
    source.close()

    workspace = params.workspace
    name = params.name

    for manga in manga_list:
        estate = MangaEstate(
            home_directory=workspace,
            manga=manga
        )

        update_source = params.update_source or False
        update_estate = params.update_estate or False

        if update_source:
            estate.update_source(
                name=name,
                url=manga['url'],
                chapters=manga['chapters']
            )

        if update_estate:
            estate.update_estate(
                name=name,
                url=manga['url']
            )

        get_chapters = params.get_chapters or False

        if get_chapters:
            max_mangas = params.max_fetch_mangas
            max_chapters = params.max_fetch_chapters

            estate.get_chapters(
                name=name,
                url=manga['url'],
                max_mangas=max_mangas,
                max_chapters=max_chapters
            )