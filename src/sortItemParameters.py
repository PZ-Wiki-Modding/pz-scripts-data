import json

INPUT_FILE = "out/scriptBlocks.json"
OUTPUT_FILE = "out/itemParameters.json"



def get_itemtype_needs(param_data: dict) -> list[str] | None:
    # skip if no needs
    if 'needs' not in param_data:
        return None
    # skip if no need for ItemType
    for need in param_data['needs']:
        if need.get('name', None) == 'ItemType':
            return need.get('values', None)
    return None


# load item ItemTypes available
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    blocks = json.load(f)

item_block = blocks['item']
itemtypes = item_block['parameters']['itemtype']['values']

# initialize dictionary of ItemTypes
type_2_params = {}
for itemtype in itemtypes:
    type_2_params[itemtype] = []


# for each parameter, check if it has a need for ItemType
# if so, it means it specifically is only valid those ItemTypes
for param_key, param_data in item_block['parameters'].items():
    itemtypes = get_itemtype_needs(param_data)
    if itemtypes is not None:
        for itemtype in itemtypes:
            type_2_params[itemtype].append(param_data['name'])


with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    json.dump(type_2_params, f, indent=4)