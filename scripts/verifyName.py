import yaml, os

BLOCKS_DIR = "data/blocks"

blocks = {}
for filename in os.listdir(BLOCKS_DIR):
    if filename.endswith('.yaml'):
        key = os.path.splitext(filename)[0]
        file_path = os.path.join(BLOCKS_DIR, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            blocks[key] = yaml.safe_load(f)

for key, block in blocks.items():
    if key != block['name']:
        print(key)