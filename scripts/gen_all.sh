#!/bin/bash

SOURCE_DIR="./sources"
SITE_DIR="./site"

mkdir -p $SITE_DIR

bash ./scripts/gen_pages.sh
python3 ./scripts/gen_index.py
python3 ./scripts/gen_bureau.py
