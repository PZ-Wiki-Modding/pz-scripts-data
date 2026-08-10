import os, json, yaml
from pathlib import Path
from typing import TypedDict, Optional, Any

from pz_scripts_data.blocks import BlockProperties


type ScriptsBlock = dict[str, Any]
class Item(TypedDict):
    input: Path
    output: Path
    data: Optional[dict[str, ScriptsBlock]]


items: list[Item] = [
    Item(
        input=Path("data/blocks"),
        output=Path("out/scriptsBlocks.json"),
        data=None,
    ),
    Item(
        input=Path("data/roots"),
        output=Path("out/roots.json"),
        data=None,
    ),
]





## PROCESS ITEM

def fetchBlocks(item: Item):
    # combine all block json files into one
    blocks: dict[str, ScriptsBlock] = {}
    for file_path in item['input'].glob("*.yaml"):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            key = data[BlockProperties.NAME]
            if key in blocks:
                raise ValueError(f"Duplicate block name '{key}' found in '{file_path}'.")
            blocks[key] = data
    return blocks

def process_parameters(data: ScriptsBlock) -> ScriptsBlock:
    # remove unnecessary fields
    data.pop(BlockProperties.VERSION)

    # replace parameters array into dictionary
    # where keys are lowercased parameter names
    parameters_data = data.get(BlockProperties.PARAMETERS, [])
    parameters_new = {}
    for param_data in parameters_data:
        name = param_data[BlockProperties.NAME]
        parameters_new[name.lower()] = param_data
    data[BlockProperties.PARAMETERS] = parameters_new

    # handle properties
    properties_data = data.get(BlockProperties.PROPERTIES, None)
    if properties_data is not None:
        for param_data in properties_data.values():
            # transform into dictionary too
            new_properties = {}
            properties: list = param_data[BlockProperties.PROPERTIES]
            for prop_data in properties:
                prop_name = prop_data[BlockProperties.NAME]
                new_properties[prop_name] = prop_data
            param_data[BlockProperties.PROPERTIES] = new_properties

    return data

# main

def process(item: Item):
    blocks = fetchBlocks(item)
    for key, block in blocks.items():
        blocks[key] = process_parameters(block)

    return blocks



## PREPARE

# relationship and hierarchy

def add_source_ref_to_targets(
        source_name: str, 
        targets_names: list[str], 
        items: list[Item],
        array_type: BlockProperties):
    """
    This is used to add source_name to the targets's array_type.

    For example:
    - source_name -> child_name
    - targets_names -> child_parents
    - array_type -> children (of parent)
    will add source_name in the array stored at key array_type of the targets of targets_names.
    (child_name --append--> array (key: children) of each parents)
    """
    _processed: list[str] = []
    for item in items:
        blocks = item['data']
        assert blocks is not None, "Something went wrong."

        # add children_name ref to every parents
        for parent_name in targets_names:
            parent_block = blocks.get(parent_name, None)
            if parent_block is None:
                continue

            # init if needed
            if array_type not in parent_block:
                parent_block[array_type] = []

            # add name
            children: list[str] = parent_block[array_type]
            if source_name not in children:
                children.append(source_name)
            _processed.append(parent_name)

    # we make sure they were all properly processed
    for parent_name in targets_names:
        if parent_name not in _processed:
            raise ValueError(f"Parent block '{parent_name}' not found for block '{source_name}'.")


def prepare_relationship(block: ScriptsBlock, items: list[Item]):
    """
    This will retrieve the parents of this block and add a reference to itself inside the data,
    of this parent block
    """
    # handle parents
    parents = block.get(BlockProperties.PARENTS, [])
    if parents:
        add_source_ref_to_targets(
            block[BlockProperties.NAME], parents, items,
            BlockProperties.CHILDREN)

    # handle variants
    variant = block.get(BlockProperties.VARIANT, None)
    if variant:
        add_source_ref_to_targets(
            block[BlockProperties.NAME], [variant], items,
            BlockProperties.VARIANTS)


# description and reference

def find_block_in_items(block_name: str, items: list[Item]) -> ScriptsBlock | None:
    for item in items:
        blocks = item['data']
        assert blocks is not None, "Something is wrong."

        if block_name in blocks:
            return blocks[block_name]
    return None


def copy_block_ref(block: ScriptsBlock, items: list[Item]) -> ScriptsBlock:
    """
    #desc copies the description of the source block
    #ref copies every key values of that source block into the block (if not already present)
    """
    # copy #desc
    if BlockProperties.REF_DESC in block:
        desc_source_key: str = block[BlockProperties.REF_DESC]
        desc_source = find_block_in_items(desc_source_key, items)

        if desc_source is not None:
            block[BlockProperties.DESCRIPTION] = desc_source[BlockProperties.DESCRIPTION]

            # copy the short description if available too
            if BlockProperties.SHORT_DESCRIPTION in desc_source:
                block[BlockProperties.SHORT_DESCRIPTION] = desc_source[BlockProperties.SHORT_DESCRIPTION]

    # copy #ref
    if BlockProperties.REF_FULL in block:
        ref_source_key: str = block[BlockProperties.REF_FULL]
        ref_source = find_block_in_items(ref_source_key, items)
        if ref_source is not None:
            # we copy every key-value from the ref_block
            # that doesn't already exist in the block
            for key, value in ref_source.items():
                if key not in block:
                    block[key] = value

    return block


# parameters

def get_source_parameter(ref_key: str, items: list[Item]) -> dict:
    """
    This will return the source parameter data from the ref_key.
    The ref_key is in the format "BlockName/ParameterName"
    """
    # find the source block and parameter
    path = ref_key.split('/')
    assert len(path) == 2, f"Invalid #ref format for '{ref_key}'. Needs to be in format 'BlockName/ParameterName'."
    origin_block = path[0]
    origin_param = path[1].lower()

    origin_block_data = find_block_in_items(origin_block, items)

    # make sure the source block and parameter exist
    if origin_block_data is None:
        raise ValueError(f"Source block '{origin_block}' not found for parameter '{origin_param}'.")
    if BlockProperties.PARAMETERS not in origin_block_data:
        raise ValueError(f"Source block '{origin_block}' has no parameters for parameter '{origin_param}'.")
    if origin_param not in origin_block_data[BlockProperties.PARAMETERS]:
        raise ValueError(f"Source block '{origin_block}' has no parameter '{origin_param}'.")

    return origin_block_data[BlockProperties.PARAMETERS][origin_param]

def copy_parameters_ref(parameters: dict[str, dict], items: list[Item]):
    for param_key, param_data in parameters.items():
        if BlockProperties.REF_FULL in param_data:
            ref_key = param_data[BlockProperties.REF_FULL]
            
            source_param_data = get_source_parameter(ref_key, items)
            assert source_param_data is not None, f"Source parameter '{ref_key}' not found for parameter '{param_key}'."

            # copy every key-value from the source parameter data
            # that doesn't already exist in the parameter data
            for key, value in source_param_data.items():
                if key not in param_data:
                    param_data[key] = value

        if BlockProperties.REF_DESC in param_data:
            desc_key = param_data[BlockProperties.REF_DESC]

            source_param_data = get_source_parameter(desc_key, items)
            assert source_param_data is not None, f"Source parameter '{desc_key}' not found for parameter '{param_key}'."

            # make sure the source parameter has a description
            if BlockProperties.DESCRIPTION not in source_param_data:
                raise ValueError(f"Parameter '{param_key}' has #desc but source has no description.")

            # only copy the description
            param_data[BlockProperties.DESCRIPTION] = source_param_data[BlockProperties.DESCRIPTION]


# main

def prepare(item: Item, items: list[Item]):
    blocks = item['data']
    assert blocks is not None, "Something went wrong."

    for block in blocks.values():
        prepare_relationship(block, items)
        copy_block_ref(block, items)

        parameters = block.get(BlockProperties.PARAMETERS, {})
        copy_parameters_ref(parameters, items)


    return blocks






def main():
    for item in items:
        item['data'] = process(item)
    for item in items:
        item['data'] = prepare(item, items)
    for item in items:
        output_file = item['output']
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(item['data'], f, indent=2, ensure_ascii=False, sort_keys=True)

if __name__ == "__main__":
    main()