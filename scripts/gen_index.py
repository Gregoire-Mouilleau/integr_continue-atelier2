import os
import markdown

def extract_title(md_content):
    """Extracts the title from the Markdown content (first header)"""
    for line in md_content.splitlines():
        if line.startswith('# '):  # Assuming the title is the first H1 (#)
            return line.lstrip('# ').strip()
    return "Sans titre"

def generate_index_page():
    index_content = """
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Index des événements</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container my-5">
            <h1 class="text-center mb-5">Liste des événements</h1>
            <div class="row">
    """

    # Parcours des fichiers Markdown
    for filename in os.listdir('../sources'):
        if filename.endswith('.md'):
            event_name = filename.split('-', 3)[-1].replace('.md', '')  # Extrait "evenement-X"
            md_filepath = os.path.join('../sources', filename)
            image_filepath = os.path.join('../sources', f'{event_name}.webp')

            # Lecture du fichier Markdown pour extraire le titre
            with open(md_filepath, 'r', encoding='utf-8') as file:
                md_content = file.read()
                title = extract_title(md_content)

            # Génération du chemin du fichier HTML correspondant
            html_filename = f"{filename.replace('.md', '.html')}"

            # Ajout du titre et de l'image dans l'index
            index_content += """
            <div class="col-md-4 mb-4">
                <div class="card">
            """
            if os.path.exists(image_filepath):
                index_content += f'<img src="{image_filepath}" class="card-img-top" alt="{title}">'
            index_content += f"""
                    <div class="card-body">
                        <h5 class="card-title">{title}</h5>
                        <a href="{html_filename}" class="btn btn-primary">Voir l'événement</a>
                    </div>
                </div>
            </div>
            """

    # Ajout d'un bouton pour accéder à la page du bureau
    index_content += """
            </div> <!-- row -->
            <div class="text-center mt-5">
                <a href="bureau.html" class="btn btn-secondary">Voir le bureau</a>
            </div>
        </div> <!-- container -->
    </body>
    </html>
    """

    # Sauvegarde du fichier index.html dans le dossier 'site/'
    with open('../site/index.html', 'w', encoding='utf-8') as index_file:
        index_file.write(index_content)

    print("index.html has been created.")

if __name__ == "__main__":
    generate_index_page()