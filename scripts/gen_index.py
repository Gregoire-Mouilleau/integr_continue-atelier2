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
            md_filepath = os.path.join('./sources', filename)
            html_filename = filename.replace('.md', '.html')
            with open(md_filepath, 'r', encoding='utf-8') as file:
                md_content = file.read()
                title = extract_title(md_content)
            index_content += f"""
            <div class="col-md-4 mb-4">
                <div class="card">
                    <div class="card-body">
                        <h5 class="card-title">{title}</h5>
                        <a href="{html_filename}" class="btn btn-primary">Voir l'événement</a>
                    </div>
                </div>
            </div>
            """

    index_content += """
            </div>
        </div>
    </body>
    </html>
    """

    with open('./site/index.html', 'w', encoding='utf-8') as index_file:
        index_file.write(index_content)

if __name__ == "__main__":
    generate_index_page()
