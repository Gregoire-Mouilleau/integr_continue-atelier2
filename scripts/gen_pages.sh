#!/bin/bash

# Dossier contenant les fichiers sources (Markdown et CSV)
SOURCE_DIR="../sources"
# Dossier où seront générées les pages HTML
SITE_DIR="../site"

Utilisation de Pandoc pour convertir les fichiers Markdown en HTML
for file in "$SOURCE_DIR"/*.md; do
    if [[ -f "$file" ]]; then
        filename=$(basename "$file" .md)  # Nom du fichier sans l'extension
        pandoc "$file" -o "$SITE_DIR/$filename.html"
        echo "$filename.html généré."
    else
        echo "Aucun fichier Markdown trouvé dans $SOURCE_DIR."
    fi
done