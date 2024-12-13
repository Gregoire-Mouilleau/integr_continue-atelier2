import csv
import os

def generate_bureau_page():
    if not os.path.exists('./site'):
        os.makedirs('./site')

    with open('./sources/membres-bureau-association.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        bureau_content = """
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Bureau de l'association</title>
        </head>
        <body>
            <h1>Liste des membres du bureau</h1>
            <table border="1">
                <tr>
        """
        for header in headers:
            bureau_content += f"<th>{header}</th>"
        bureau_content += "</tr>"

        for row in reader:
            bureau_content += "<tr>"
            for cell in row:
                bureau_content += f"<td>{cell}</td>"
            bureau_content += "</tr>"

        bureau_content += """
            </table>
        </body>
        </html>
        """

        with open('./site/bureau.html', 'w', encoding='utf-8') as bureau_file:
            bureau_file.write(bureau_content)

if __name__ == "__main__":
    generate_bureau_page()
