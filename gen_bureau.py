import csv

def generate_bureau_page():
    with open('./sources/membres-bureau-association.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)

        bureau_content = """
        <html>
        <head>
            <title>Bureau de l'association</title>
            <style>
                body { font-family: Arial, sans-serif; }
                h1 { text-align: center; }
                table { width: 80%; margin: 20px auto; border-collapse: collapse; }
                th, td { padding: 10px; border: 1px solid #ddd; text-align: left; }
                th { background-color: #f2f2f2; }
                tr:nth-child(even) { background-color: #f9f9f9; }
                a { text-decoration: none; color: #0066cc; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <h1>Liste des membres du bureau</h1>
            <table>
                <tr>
                    <th>Prénom</th>
                    <th>Nom</th>
                    <th>Email</th>
                    <th>Fonction</th>
                </tr>
        """

        for row in reader:
            prenom, nom, email, fonction = row
            bureau_content += f"""
                <tr>
                    <td>{prenom}</td>
                    <td>{nom}</td>
                    <td><a href="mailto:{email}">{email}</a></td>
                    <td>{fonction}</td>
                </tr>
            """

        bureau_content += """
            </table>
        </body>
        </html>
        """

        with open('./site/bureau.html', 'w', encoding='utf-8') as bureau_file:
            bureau_file.write(bureau_content)

if __name__ == "__main__":
    generate_bureau_page()
