import os, json, yaml

SCRIPT_DIR = os.path.join(os.path.dirname(__file__))

LANGUAGE_CODES_DIR = os.path.join(SCRIPT_DIR, 'data', 'language_codes')
OUTPUT_FILE = os.path.join(SCRIPT_DIR, 'data', 'languageCodes.json')

language_codes = {}
for filename in os.listdir(LANGUAGE_CODES_DIR):
    if filename.endswith('.yaml'):
        key = os.path.splitext(filename)[0]
        file_path = os.path.join(LANGUAGE_CODES_DIR, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            language_codes[key] = yaml.safe_load(f)

for file_key, file_data in language_codes.items():
    # remove unnecessary fields
    file_data.pop('version', None)

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(language_codes, f, indent=2, ensure_ascii=False)