import argparse

parser = argparse.ArgumentParser(
    prog='manga-sync',
    description='Module for downloading and uploading manga fetched through the manga-indexer package.'
)

parser.add_argument(
    '-s',
    '--source',
    type=str,
    dest='source',
    help=(
        'Source file for the manga.'
        'The program assumes it is a json file by default.'
    )
)

parser.add_argument(
    '-n',
    '--name',
    type=str,
    required=True,
    dest='name',
    help=(
        'The name of the manga source to be used for estate management. '
        'Typically uses the website from which the source file was generated. '
        'If your source is mangakakalot.com, just use "-n mangakakalot.com."'
    )
)

parser.add_argument(
    '-t',
    '--type',
    dest='source_type',
    default='json',
    choices=[
        'json', 'xml', 'csv'
    ],
    help=(
        'Source file type. The default is json.'
    )
)

parser.add_argument(
    '-w',
    '--workspace',
    type=str,
    dest='workspace',
    default='./Manga/',
    help=(
        'The directory for staging the whole synchronization process.'
    )
)

parser.add_argument(
    '-d',
    '--destination',
    type=str,
    dest='destination',
    default='./Manga',
    help=(
        'The destination folder.'
    )
)

parser.add_argument(
    '--update-estate',
    action='store_true',
    dest='update_estate',
    help=(
        'Update the manga estate by synchronizing it with a given source. '
        'If the tool fails to find a healthy and functional estate, it forces this option.'
    )
)

parser.add_argument(
    '--update-source',
    action='store_true',
    dest='update_source',
    help=(
        'Update the manga\'s estate source. It requires the -n option and an existing estate.'
    )
)

parser.add_argument(
    '--g',
    '--get-chapters',
    action='store_true',
    dest='get_chapters',
    help=(
        'Actually download the chapters from the estate to the destination folder.'
    )
)

parser.add_argument(
    '-c',
    '--max-fetch-chapters',
    type=int,
    dest='max_fetch_chapters',
    default=-2,
    help=(
        'Maximum number of chapters to actually fetch from source and download.'
    )
)

parser.add_argument(
    '-m',
    '--max-fetch-manga',
    type=int,
    dest='max_fetch_manga',
    default=-2,
    help=(
        'Maximum number of mangas to fetch.'
    )
)
