#!/bin/bash

SOURCE_DIR="./sources"
SITE_DIR="./site"

mkdir -p $SITE_DIR

for file in "$SOURCE_DIR"/*.md; do
    if [[ -f "$file" ]]; then
        filename=$(basename "$file" .md)
        pandoc "$file" -o "$SITE_DIR/$filename.html"
    fi
done
