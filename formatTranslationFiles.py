import os, json, yaml

SCRIPT_DIR = os.path.join(os.path.dirname(__file__))

TRANSLATION_FILES_DIR = os.path.join(SCRIPT_DIR, 'data', 'translation_files')
OUTPUT_FILE = os.path.join(SCRIPT_DIR, 'data', 'translationFiles.json')

translation_files = {}
for filename in os.listdir(TRANSLATION_FILES_DIR):
    if filename.endswith('.yaml'):
        key = os.path.splitext(filename)[0]
        file_path = os.path.join(TRANSLATION_FILES_DIR, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            translation_files[key] = yaml.safe_load(f)

for file_key, file_data in translation_files.items():
    # remove unnecessary fields
    file_data.pop('version', None)

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(translation_files, f, indent=2, ensure_ascii=False)