import json

from .estate_manager import (
    MangaEstate,
    MangaSourceEstate
)

def main(params):
    # read source file
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

        estate.synchronize_with_source(
            name=name,
            url=manga['url']
        )
