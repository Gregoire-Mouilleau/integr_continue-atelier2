#!/bin/bash

SOURCE_DIR="./sources"
SITE_DIR="../site"

mkdir -p $SITE_DIR
echo "Génération des pages..."
./gen_pages.sh

echo "Génération de l'index..."
python3 gen_index.py

echo "Génération de la page du bureau..."
python3 gen_bureau.py

echo "Génération terminée."
