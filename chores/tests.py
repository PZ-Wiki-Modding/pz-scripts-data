import json

BLOCKS_FILE = "out/scriptBlocks.json"
SCHEMA_FILE = "schemas/blocks.json"

def validate_parameter(param_name: str, param_value: dict, block_data: dict, schema: dict):
    # validate the type
    type = param_value.get('type', None)
    if type is not None:
        if 'main' not in type:
            raise ValueError(f"Parameter '{param_name}' in block '{block_data['name']}' is missing 'main' field in 'type'.")
        main_type = type['main']
        if main_type not in ['string', 'number', 'boolean', 'array', 'object']:
            raise ValueError(f"Parameter '{param_name}' in block '{block_data['name']}' has invalid main type '{main_type}'.")
        
        if main_type == 'array':
            if 'array' not in type:
                raise ValueError(f"Parameter '{param_name}' in block '{block_data['name']}' is of type 'array' but is missing 'array' field in 'type'.")
        elif main_type == 'object':
            if 'object' not in type:
                raise ValueError(f"Parameter '{param_name}' in block '{block_data['name']}' is of type 'object' but is missing 'object' field in 'type'.")    

def validate_parameters(block_data: dict, schema: dict):
    parameters = block_data.get('parameters', {})
    for param_name, param_value in parameters.items():
        try:
            validate_parameter(param_name, param_value, block_data, schema)
        except ValueError as e:
            raise ValueError(f"In block '{block_data['name']}', parameter '{param_name}': {e}")        







if __name__ == "__main__":
    with open(BLOCKS_FILE, 'r', encoding='utf-8') as f:
        blocks = json.load(f)

    with open(SCHEMA_FILE, 'r', encoding='utf-8') as f:
        schema = json.load(f)

    for block_key, block_data in blocks.items():
        validate_parameters(block_data, schema)



    