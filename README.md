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

+ Load an index file in JSON format and use it to initiate source tracking.
  
```
./manga-sync.py -d Manga -s /path/to/index/file.json -n source-website.url --update-sources
```

+ After the source has been created or updated for that particular manga, we synchronize the source with the estate.

```
./manga-sync.py -d Manga -n source.website.url --update-estate
```

+ After synchronizing the source with the estate, we can then fetch manga from the estate. The following example fetches 10 chapters each from 100 manga, depending on how they are ordered in the estate:

```
./manga-sync.py -d Manga -n source.website.url --get-chapters -m 100 -c 10
```