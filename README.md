# Intégration Continue - Atelier 1

Ce projet génère un site web statique en HTML contenant des pages d'événements et une page listant les membres du bureau d'une association. Il utilise des fichiers Markdown et un fichier CSV comme sources de données.

## Fonctionnalités

- **Pages d'événements** : Génération de pages HTML pour chaque événement à partir de fichiers Markdown.
- **Index des événements** : Création d'une page d'index avec des liens vers chaque événement et un bouton pour accéder à la page du bureau.
- **Page bureau** : Génération d'une page listant les membres du bureau en lisant un fichier CSV.
- **Styles** : Possibilité d'utiliser Bootstrap 5.3.3 pour styliser les pages, ou un fichier CSS personnalisé.

## Prérequis

- **Python 3.x**
- **Pandoc** : Pour convertir les fichiers Markdown en HTML.
- **Modules Python** : Installables via `pip` avec le fichier `requirements.txt`.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Nico1716/integr_continue-atelier1.git
   cd integr_continue-atelier1
   ```

2.	Installez les dépendances :
`pip install -r requirements.txt`

3.	Assurez-vous que Pandoc est installé. Si ce n’est pas le cas, installez-le selon votre système d’exploitation.

## Structure des dossiers

- `sources/` : Contient les fichiers source, incluant :
  - Fichiers Markdown des événements (ex : `2025-01-18-evenement-1.md`)
  - Images associées aux événements (ex : `evenement-1.webp`)
  - Fichier CSV des membres du bureau (`membres-bureau-association.csv`)
  
- `scripts/` : Contient les scripts pour générer les pages HTML :
  - `gen_index.py` : Génère la page d'index des événements
  - `gen_bureau.py` : Génère la page des membres du bureau
  - `gen_pages.sh` : Script Bash pour générer toutes les pages d'événements avec Pandoc
  - `gen_all.sh` : Script Bash pour exécuter tous les scripts dans l'ordre

- `site/` : Contient les fichiers HTML générés pour le site :
  - Les pages des événements (ex : `evenement-1.html`)
  - La page d'index (`index.html`)
  - La page des membres du bureau (`bureau.html`)
  - Le fichier de style personnalisé (`style.css`), si utilisé

## Utilisation

Pour générer toutes les pages du site, exécutez le script `gen_all.sh` depuis le dossier `scripts` :

```bash
cd scripts
./gen_all.sh
```

## Réalisé par :
Grégoire MOUILLEAU  
Nicolas PUIG
