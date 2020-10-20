#!venv/bin/python3

from manga_sync import args
from manga_sync.utils import main

def __main__():
    params = args.parser.parse_args()
    main(params)

if __name__=='__main__':
    __main__()

