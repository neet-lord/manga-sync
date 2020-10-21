Manga Sync
==========

This is a repository that works with manga-indexer (https://github.com/neet-lord/manga-indexer.git) to create a localized manga estate based on the indices fetched by the indexer.

To make it simple, it downloads manga, and keeps track of chapters based on a scraped index.

Installation
============
```
git clone https://github.com/neet-lord/manga-sync.git

cd manga-sync

python3 -m venv venv

source venv/bin/activate

python3 -m pip install -r requirements.txt
```
Basic Usage:
============

+ Load an index file in JSON format, update the chapter index, and use the index to download manga to a localized chapter directory 'Manga'.
  
```
./manga-sync.py -d Manga -s /path/to/index/file.json -n source-website.url --update-sources
```