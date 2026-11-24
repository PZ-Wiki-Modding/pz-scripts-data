import ruamel.yaml
yaml = ruamel.yaml.YAML()
from pathlib import Path
from pprint import pprint

from pz_scripts_data.schema import BlockDefinition


SOURCE_FILE: str = "data/blocks/item.yaml"
COMPARISON_FILES: list[str] = [
    "data/blocks/item_alarmclock.yaml",
    "data/blocks/item_alarmclockclothing.yaml",
    "data/blocks/item_container.yaml",
    "data/blocks/item_drainable.yaml",
    "data/blocks/item_food.yaml",
    "data/blocks/item_literature.yaml",
    "data/blocks/item_radio.yaml",
    "data/blocks/item_weapon.yaml",
    "data/blocks/item_weaponpart.yaml",
]

# verify exists
assert Path(SOURCE_FILE).exists(), f"Source file not found: {SOURCE_FILE}"
for comparison_file in COMPARISON_FILES:
    if not Path(comparison_file).exists():
        raise FileNotFoundError(f"Comparison file not found: {comparison_file}")

# load source
with open(SOURCE_FILE, "r") as f:
    source_data = yaml.load(f)
source_block = BlockDefinition.model_validate(source_data)
parameters_source = set()
assert source_block.parameters is not None
for param in source_block.parameters:
    parameters_source.add(param.name)

# load comparison files
comparison_blocks = []
for comparison_file in COMPARISON_FILES:
    with open(comparison_file, "r", encoding="utf-8") as f:
        comparison_data = yaml.load(f)
    comparison_blocks.append(BlockDefinition.model_validate(comparison_data))

# verify parameters don't exist in both
for comparison_block in comparison_blocks:

    duplicate_parameters = set()
    assert comparison_block.parameters is not None
    for param in comparison_block.parameters:
        if param.name in parameters_source:
            duplicate_parameters.add(param.name)

    if duplicate_parameters:
        print(f"Duplicate parameters found in {comparison_block.name}")
        pprint(duplicate_parameters)

    # remove duplicate parameters from source
    for param in source_data['parameters']:
        if param['name'] in duplicate_parameters:
            source_data['parameters'].remove(param)

    # update the set of source parameters
    # parameters_source = {param['name'] for param in source_data['parameters']}

# write out source

yaml.indent(sequence=2)
with open(SOURCE_FILE, "w", encoding="utf-8") as f:
    yaml.dump(source_data, f)
