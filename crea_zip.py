{\rtf1}import os
import re
import zipfile

zip_filename = "elite_solutions_final.zip"
base_dir = os.getcwd()

patterns = [
    (r'href="assets/', 'href="./assets/'),
    (r"href='assets/", "href='./assets/"),
    (r'src="assets/', 'src="./assets/'),
    (r"src='assets/", "src='./assets/"),
    (r'href="favicon.ico"', 'href="./favicon.ico"'),
    (r"href='favicon.ico'", "href='./favicon.ico'")
]

for file in os.listdir(base_dir):
    if file.endswith(".html"):
        path = os.path.join(base_dir, file)
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        original = content
        for pattern, replacement in patterns:
            content = re.sub(pattern, replacement, content)
        if content != original:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✔ Corretto: {file}")
        else:
            print(f"= Nessuna correzione necessaria: {file}")

with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(base_dir):
        if zip_filename in files:
            files.remove(zip_filename)
        for file in files:
            if file.endswith((".html", ".xml", ".md")) or "assets" in root:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, base_dir)
                zipf.write(file_path, arcname)
                print(f"Aggiunto: {arcname}")

print(f"\n✅ File ZIP creato con successo: {zip_filename}")
print("📦 Tutti i percorsi corretti e archivio pronto per il deploy.")
