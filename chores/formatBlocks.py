import os, json, yaml
from pathlib import Path

BLOCKS_DIR = Path("data/blocks")
OUTPUT_FILE = Path("out/scriptBlocks.json")

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
block_name_to_id = {}
for file_path in BLOCKS_DIR.glob("*.yaml"):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = prepare_parameters(yaml.safe_load(f))
        key = data['name']
        if key in blocks:
            raise ValueError(f"Duplicate block name '{key}' found in '{file_path}'.")
        blocks[key] = data

# copy #ref and #desc
for block_key, block_data in blocks.items():
    parameter = block_data.get('parameters', {})

    # store ref to this block into parent block as a potential children
    for parent in block_data.get("parents", []):
        if parent not in blocks:
            raise ValueError(f"Parent block '{parent}' not found for block '{block_key}'.")
        parent_block = blocks[parent]
        if "children" not in parent_block:
            parent_block["children"] = []
        if block_key not in parent_block["children"]:
            parent_block["children"].append(block_key)

    # store ref to variant blocks into original block as a potential variants
    if "isVariant" in block_data and block_data["isVariant"]:
        source_block = block_data["isVariant"]
        if source_block not in blocks:
            raise ValueError(f"Source block '{source_block}' not found for variant block '{block_key}'.")
        source_block_data = blocks[source_block]
        if "variants" not in source_block_data:
            source_block_data["variants"] = []
        if block_key not in source_block_data["variants"]:
            source_block_data["variants"].append(block_key)

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

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(blocks, f, indent=2, ensure_ascii=False)

os.system(f'git add {OUTPUT_FILE}')

# print(f"Combined JSON written to {OUTPUT_FILE}")