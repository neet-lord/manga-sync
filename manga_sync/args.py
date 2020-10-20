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