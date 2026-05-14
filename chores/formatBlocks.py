import os, json, yaml

BLOCKS_DIR = "data/blocks"
OUTPUT_FILE = "out/scriptBlocks.json"

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

# copy #ref and #desc
for block_key, block_data in blocks.items():
    parameter = block_data.get('parameters', {})

    # copy #desc of other block
    if "#desc" in block_data:
        desc_key = block_data['#desc']
        block_data['description'] = blocks[desc_key]['description']

    # copy #ref of other block
    if "#ref" in block_data:
        ref_key = block_data['#ref']
        ref_block = blocks[ref_key]
        for key, value in ref_block.items():
            if key not in block_data:
                block_data[key] = value

    # copy #ref and #desc of parameters
    for param_key, param_data in parameter.items():
        if '#ref' in param_data:
            original_name = param_data['name']
            ref_key = param_data['#ref']
            path = ref_key.split('/')
            assert len(path) == 2, f"Invalid #ref format for '{ref_key}' in block '{block_key}' parameter '{param_key}'. Needs to be in format 'BlockName/ParameterName'."
            origin_block = path[0]
            origin_param = path[1].lower()

            new_param_data = blocks[origin_block]['parameters'][origin_param].copy()
            parameter[param_key] = new_param_data

            # restore original name and #ref
            parameter[param_key]['name'] = original_name
            parameter[param_key]['#ref'] = ref_key

            # param_data.pop('#ref')

        if '#desc' in param_data:
            original_name = param_data['name']
            desc_key = param_data['#desc']
            path = desc_key.split('/')
            assert len(path) == 2, f"Invalid #desc format for '{desc_key}' in block '{block_key}' parameter '{param_key}'. Needs to be in format 'BlockName/ParameterName'."
            origin_block = path[0]
            origin_param = path[1].lower()

            # only copy description
            param_data['description'] = blocks[origin_block]['parameters'][origin_param]['description']

os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(blocks, f, indent=2, ensure_ascii=False)

os.system(f'git add {OUTPUT_FILE}')

# print(f"Combined JSON written to {OUTPUT_FILE}")