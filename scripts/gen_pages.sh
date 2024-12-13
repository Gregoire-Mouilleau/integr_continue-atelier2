#!/bin/bash

SOURCE_DIR="./sources"
SITE_DIR="./site"

mkdir -p $SITE_DIR

for file in "$SOURCE_DIR"/*.md; do
    if [[ -f "$file" ]]; then
        filename=$(basename "$file" .md)
        echo "Processing $file"
        pandoc "$file" -o "$SITE_DIR/$filename.html"
        echo "$SITE_DIR/$filename.html generated."
    else
        echo "No Markdown files found in $SOURCE_DIR."
    fi
done
