#!/bin/bash

SOURCE_DIR="./sources"
SITE_DIR="./site"

mkdir -p $SITE_DIR

./gen_pages.sh
python3 gen_index.py
python3 gen_bureau.py
