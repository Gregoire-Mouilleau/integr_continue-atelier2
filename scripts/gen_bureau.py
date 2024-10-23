import csv
import os

def generate_bureau_page():
    # Ouverture du fichier CSV
    with open('../sources/membres-bureau-association.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)  # Lire la première ligne comme en-tête

        # Début du contenu HTML
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

        # Pour chaque ligne du fichier CSV, ajouter une ligne dans le tableau HTML
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

        # Fin du contenu HTML
        bureau_content += """
            </table>
        </body>
        </html>
        """

        # Sauvegarde du fichier HTML dans le dossier 'site/'
        with open('../site/bureau.html', 'w', encoding='utf-8') as bureau_file:
            bureau_file.write(bureau_content)
        
        print("bureau.html has been created.")

if __name__ == "__main__":
    generate_bureau_page()