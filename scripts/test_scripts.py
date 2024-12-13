import os
import re

def test_generate_event_page():
    os.system("bash scripts/gen_pages.sh")
    assert os.path.exists("site/2025-01-18-evenement-1.html")

def test_index_contains_events():
    with open("site/index.html", "r", encoding="utf-8") as file:
        content = file.read()
    assert "2025-01-18-evenement-1.html" in content

def test_bureau_page():
    os.system("python scripts/gen_bureau.py")
    assert os.path.exists("site/bureau.html")

def test_event_page_content():
    with open("site/2025-01-18-evenement-1.html", "r", encoding="utf-8") as file:
        content = file.read()
    assert re.search(r"<h1.*?>", content), "La balise <h1> est absente ou mal formée."

def test_no_empty_files():
    for root, _, files in os.walk("site"):
        for file in files:
            filepath = os.path.join(root, file)
            assert os.path.getsize(filepath) > 0
