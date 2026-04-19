import os, yaml

BLOCKS_DIR = "data/blocks"

# Custom representer to preserve multiline strings in literal block style
def str_representer(dumper, data):
    if '\n' in data:
        # Use literal block style (|-) for multiline strings
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_representer, Dumper=yaml.SafeDumper)

# combine all block json files into one
blocks = {}
for filename in os.listdir(BLOCKS_DIR):
    if filename.endswith('.yaml'):
        key = os.path.splitext(filename)[0]
        file_path = os.path.join(BLOCKS_DIR, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            blocks[file_path] = yaml.safe_load(f)



for file_path, block in blocks.items():
    print(block['name'])
    parameters = block.get('parameters', [])
    
    # fix type format
    for param in parameters:
        originalType = param.get('type', None)
        blockType = block.get('blockType', None)
        if originalType is None:
            if blockType is not None:
                print(f"Block '{block['name']}' parameter '{param['name']}' has no type defined, skipping.")
            continue

        newType = {
            'main': originalType # string, array, boolean etc
        }

        if blockType is not None:
            newType['block'] = {
                'name': blockType['block'],
                'fullType': blockType.get('fullType', False)
            }

        arrayType = param.get('arrayType', None)
        if arrayType is not None:
            newType['array'] = {
                'type': arrayType,
                'separator': param.get('separator', ';')
            }

            if param.get('separator', None) is None:
                print(f"Block '{block['name']}' parameter '{param['name']}' has no separator for array")

        object = param.get('object', None)
        if object is not None:
            object['keyValueSeparator'] = param.get('separator', ':')
            object['pairsSeparator'] = param['separator']
            newType['object'] = object

        if param.get('separator', None) is not None:
            param.pop('separator')
        if param.get('arrayType', None) is not None:
            param.pop('arrayType')
        if param.get('object', None) is not None:
            param.pop('object')
        if param.get('blockType', None) is not None:
            param.pop('blockType')

        param['type'] = newType

    with open(file_path, 'w', encoding='utf-8') as f:
        yaml.dump(block, f, sort_keys=False, Dumper=yaml.SafeDumper)
