import os, re

base = os.getcwd()
assets_dir = os.path.join(base, "assets")

# --- 1. Rinomina tutte le sottocartelle e file in minuscolo ---
for root, dirs, files in os.walk(assets_dir, topdown=False):
    for name in dirs:
        new_name = name.lower()
        old_path = os.path.join(root, name)
        new_path = os.path.join(root, new_name)
        if old_path != new_path and not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"📁 Cartella rinominata: {old_path} -> {new_path}")
    for name in files:
        new_name = name.lower().replace(" ", "_")
        old_path = os.path.join(root, name)
        new_path = os.path.join(root, new_name)
        if old_path != new_path and not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"🗂️ File rinominato: {old_path} -> {new_path}")

# --- 2. Corregge i percorsi dentro i file HTML ---
for file in os.listdir(base):
    if file.endswith(".html"):
        html_path = os.path.join(base, file)
        with open(html_path, "r", encoding="utf-8") as f:
            html = f.read()

        original = html
        html = re.sub(r'Assets', 'assets', html)
        html = re.sub(r'Images', 'images', html)
        html = re.sub(r'IMG', 'images', html)
        html = re.sub(r'Css', 'css', html)
        html = re.sub(r'JS', 'js', html)
        html = re.sub(r'Js', 'js', html)

        if html != original:
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"✏️ Percorsi aggiornati in: {file}")

print("\n✅ Tutti i nomi e percorsi sono stati normalizzati con successo.")
