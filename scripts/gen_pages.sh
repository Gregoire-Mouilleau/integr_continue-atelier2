#!/bin/bash

SOURCE_DIR="./sources"
SITE_DIR="../site"

Utilisation de Pandoc pour convertir les fichiers Markdown en HTML
for file in "$SOURCE_DIR"/*.md; do
    if [[ -f "$file" ]]; then
        filename=$(basename "$file" .md)  
        pandoc "$file" -o "$SITE_DIR/$filename.html"
        echo "$filename.html généré."
    else
        echo "Aucun fichier Markdown trouvé dans $SOURCE_DIR."
    fi
done
