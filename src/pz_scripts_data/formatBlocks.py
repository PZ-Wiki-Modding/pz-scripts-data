import json
from pathlib import Path
from typing import Any, Literal, Optional, TypedDict

import yaml
from pydantic import BaseModel, Field, ValidationError, model_validator

from pz_scripts_data.blocks import PropertyData
from pz_scripts_data.schema import BlockDefinition, ParameterDefinition


class ScriptsBlock(BlockDefinition):
    """Block used by the pipeline: parameters are keyed by lowercase name and relations are filled in during preparation."""

    parameters: dict[str, ParameterDefinition] = Field(default_factory=dict) # type: ignore
    children: list[str] | None = None
    variants: list[str] | None = None

    @model_validator(mode="before")
    @classmethod
    def _key_parameters_by_name(cls, data: Any) -> Any:
        if not isinstance(data, dict):
            return data
        parameters = data.get("parameters", [])
        if not isinstance(parameters, list):
            return data

        keyed: dict[str, Any] = {}
        for param in parameters:
            name = param.get("name") if isinstance(param, dict) else None
            if not isinstance(name, str):
                raise ValueError("every parameter must have a 'name' to be referenced")
            keyed[name.lower()] = param
        return {**data, "parameters": keyed}


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
    # combine all block yaml files into one, validating each against the schema
    blocks: dict[str, ScriptsBlock] = {}
    for file_path in item['input'].glob("*.yaml"):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        try:
            block = ScriptsBlock.model_validate(data)
        except ValidationError as exc:
            raise ValueError(f"Invalid block definition in '{file_path}':\n{exc}") from exc
        if block.name.lower() in blocks:
            raise ValueError(f"Duplicate block name '{block.name}' found in '{file_path}'.")
        blocks[block.name.lower()] = block
    return blocks

def process_properties(block: ScriptsBlock) -> ScriptsBlock:
    # transform each property group's list into a dictionary keyed by property name
    if block.properties is None:
        return block
    for property_data in block.properties.values():
        properties: list = property_data[PropertyData.PROPERTIES]
        property_data[PropertyData.PROPERTIES] = {prop[PropertyData.NAME]: prop for prop in properties}
    return block

# main

def process(item: Item):
    blocks = fetchBlocks(item)
    for block in blocks.values():
        process_properties(block)

    return blocks



## PREPARE

# relationship and hierarchy

def add_source_ref_to_targets(
        source_name: str, 
        targets_names: list[str], 
        items: list[Item],
        array_type: Literal["children", "variants"]):
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
            parent_block = blocks.get(parent_name.lower(), None)
            if parent_block is None:
                continue

            # init if needed
            if getattr(parent_block, array_type) is None:
                setattr(parent_block, array_type, [])

            # add name
            children: list[str] = getattr(parent_block, array_type)
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
    parents = block.parents
    if parents:
        add_source_ref_to_targets(block.name, parents, items, "children")

    # handle variants
    variant = block.variant_of
    if variant:
        add_source_ref_to_targets(block.name, [variant], items, "variants")


# description and reference

def find_block_in_items(block_name: str, items: list[Item]) -> ScriptsBlock | None:
    for item in items:
        blocks = item['data']
        assert blocks is not None, "Something is wrong."

        if block_name.lower() in blocks:
            return blocks[block_name.lower()]
    return None


def copy_missing_fields(target: BaseModel, source: BaseModel) -> None:
    """Copies every field explicitly set on source that isn't already set on target."""
    for field_name in source.model_fields_set:
        if field_name not in target.model_fields_set:
            setattr(target, field_name, getattr(source, field_name))

def copy_block_ref(block: ScriptsBlock, items: list[Item]) -> ScriptsBlock:
    """
    #desc copies the description of the source block
    #ref copies every field of that source block into the block (if not already present)
    """
    # copy #desc
    if block.ref_desc is not None:
        desc_source = find_block_in_items(block.ref_desc, items)

        if desc_source is not None:
            if desc_source.description is None:
                raise ValueError(f"Block '{block.name}' has #desc but source has no description.")
            block.description = desc_source.description

            # copy the short description if available too
            if desc_source.short_description is not None:
                block.short_description = desc_source.short_description

    # copy #ref
    if block.ref is not None:
        ref_source = find_block_in_items(block.ref, items)
        if ref_source is not None:
            copy_missing_fields(block, ref_source)

    return block


# parameters

def get_source_parameter(ref_key: str, items: list[Item]) -> ParameterDefinition:
    """
    This will return the source parameter from the ref_key.
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
    if origin_param not in origin_block_data.parameters:
        raise ValueError(f"Source block '{origin_block}' has no parameter '{origin_param}'.")

    return origin_block_data.parameters[origin_param]

def copy_parameters_ref(parameters: dict[str, ParameterDefinition], items: list[Item]):
    for param_key, param in parameters.items():
        if param.ref is not None:
            source_param = get_source_parameter(param.ref, items)

            # copy every field from the source parameter
            # that isn't already set on the parameter
            copy_missing_fields(param, source_param)

        if param.ref_desc is not None:
            source_param = get_source_parameter(param.ref_desc, items)

            # make sure the source parameter has a description
            if source_param.description is None:
                raise ValueError(f"Parameter '{param_key}' has #desc but source has no description.")

            # only copy the description
            param.description = source_param.description


# main

def prepare(item: Item, items: list[Item]):
    blocks = item['data']
    assert blocks is not None, "Something went wrong."

    for block in blocks.values():
        prepare_relationship(block, items)
        copy_block_ref(block, items)
        copy_parameters_ref(block.parameters, items)


    return blocks


# serialization

def serialize(blocks: dict[str, ScriptsBlock]) -> dict[str, dict[str, Any]]:
    # only write the fields that were set, using their schema (alias) names
    # the version is only used for validation, so it is not written
    return {
        name: block.model_dump(by_alias=True, exclude_unset=True, exclude={"version"})
        for name, block in blocks.items()
    }


def main():
    for item in items:
        item['data'] = process(item)
    for item in items:
        item['data'] = prepare(item, items)
    for item in items:
        output_file = item['output']
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            assert item['data'] is not None
            json.dump(serialize(item['data']), f, indent=2, 
                      ensure_ascii=False, sort_keys=True)

if __name__ == "__main__":
    main()