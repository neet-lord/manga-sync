import argparse

parser = argparse.ArgumentParser(
    prog='manga-sync',
    description='Module for downloading and uploading manga fetched through the manga-indexer package.'
)

parser.add_argument(
    '-s',
    '--source',
    type=str,
    required=True,
    dest='source',
    help=(
        'Source file for the manga.'
        'The program assumes it is a json file by default.'
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
    '--temp',
    type=str,
    default='./Manga/.tmp',
    help=(
        'The tmp directory for staging manga.'
    )
)

parser.add_argument(
    '-d',
    '--destination',
    type=str,
    default='./Manga',
    help=(
        'The destination folder.'
    )
)