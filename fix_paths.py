import os
import re

base_dir = os.getcwd()

# Elenco delle correzioni da applicare
patterns = [
    (r'href="assets/css/', 'href="./assets/css/'),
    (r"href='assets/css/", "href='./assets/css/"),
    (r'src="assets/images/', 'src="./assets/images/'),
    (r"src='assets/images/", "src='./assets/images/"),
    (r'src="assets/js/', 'src="./assets/js/'),
    (r"src='assets/js/", "src='./assets/js/"),
]

# Scansione e correzione dei file HTML
for file in os.listdir(base_dir):
    if file.endswith(".html"):
        path = os.path.join(base_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✔ Corretto: {file}")

print("\n✅ Tutti i percorsi CSS / JS / IMG sono stati sistemati correttamente.")
