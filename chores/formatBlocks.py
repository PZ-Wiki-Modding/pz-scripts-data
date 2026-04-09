import os, json, yaml

SCRIPT_DIR = os.path.join(os.path.dirname(__file__))

BLOCKS_DIR = os.path.join(SCRIPT_DIR, 'data', 'blocks')
OUTPUT_FILE = os.path.join(SCRIPT_DIR, 'out', 'scriptBlocks.json')

def prepare_parameters(data: dict) -> dict:
    # remove unnecessary fields
    data.pop('version')

    # for each parameters, make an easy access by name (case insensitive)
    parameters_data = data.get('parameters', [])
    parameters_new = {}
    for param_data in parameters_data:
        name = param_data['name']
        parameters_new[name.lower()] = param_data
    data['parameters'] = parameters_new

    # handle properties
    properties_data = data.get('properties', None)
    if properties_data is not None:
        for param_data in properties_data.values():
            new_properties = {}
            properties = param_data["properties"]
            for prop_data in properties:
                prop_name = prop_data['name']
                new_properties[prop_name] = prop_data
            param_data['properties'] = new_properties
    return data

# combine all block json files into one
blocks = {}
for filename in os.listdir(BLOCKS_DIR):
    if filename.endswith('.yaml'):
        key = os.path.splitext(filename)[0]
        file_path = os.path.join(BLOCKS_DIR, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            blocks[key] = prepare_parameters(yaml.safe_load(f))

# copy #ref of parameters
for block_key, block_data in blocks.items():
    parameter = block_data.get('parameters', {})
    for param_key, param_data in parameter.items():
        if '#ref' in param_data:
            ref_key = param_data['#ref']
            path = ref_key.split('/')
            origin_block = path[0]
            origin_param = path[1].lower()

            new_param_data = blocks[origin_block]['parameters'][origin_param].copy()
            parameter[param_key] = new_param_data

            param_data.pop('#ref')

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(blocks, f, indent=2, ensure_ascii=False)

os.system(f'git add {OUTPUT_FILE}')

# print(f"Combined JSON written to {OUTPUT_FILE}")