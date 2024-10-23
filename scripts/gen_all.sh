#!/bin/bash

# Dossier contenant les fichiers sources (Markdown et CSV)
SOURCE_DIR="../sources"
# Dossier où seront générées les pages HTML
SITE_DIR="../site"

# 1. Exécution du script Bash pour générer les pages des événements
echo "Génération des pages..."
./gen_pages.sh

# 2. Exécution du script Python pour générer l'index des événements
echo "Génération de l'index..."
python3 gen_index.py

# 3. Exécution du script Python pour générer la page du bureau
echo "Génération de la page du bureau..."
python3 gen_bureau.py

echo "Génération terminée."