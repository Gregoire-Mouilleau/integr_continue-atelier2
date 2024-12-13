import os

def extract_title(md_content):
    for line in md_content.splitlines():
        if line.startswith('# '):
            return line.lstrip('# ').strip()
    return "Sans titre"

def generate_index_page():
    if not os.path.exists('./site'):
        os.makedirs('./site')

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

    for filename in os.listdir('./sources'):
        if filename.endswith('.md'):
            event_name = filename.split('-', 3)[-1].replace('.md', '')
            md_filepath = os.path.join('./sources', filename)
            image_filepath = os.path.join('./sources', f'{event_name}.webp')

            with open(md_filepath, 'r', encoding='utf-8') as file:
                md_content = file.read()
                title = extract_title(md_content)

            html_filename = f"{filename.replace('.md', '.html')}"

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

    index_content += """
            </div>
            <div class="text-center mt-5">
                <a href="bureau.html" class="btn btn-secondary">Voir le bureau</a>
            </div>
        </div>
    </body>
    </html>
    """

    with open('./site/index.html', 'w', encoding='utf-8') as index_file:
        index_file.write(index_content)

if __name__ == "__main__":
    generate_index_page()
