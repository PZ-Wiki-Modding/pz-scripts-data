import yaml
from pathlib import Path

from pz_scripts_data.schema import BlockDefinition, ParameterDefinition, VariantDefinition
from pz_scripts_data.formatBlocks import fetchBlocks, Item


class LiteralStr(str):
    pass


# Custom representer to write multiline description strings in literal block style
def literal_str_representer(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')

yaml.add_representer(LiteralStr, literal_str_representer, Dumper=yaml.SafeDumper)


def mark_literal_descriptions(node, key=None):
    # Representers only see values, so tag multiline "description" strings by their key
    if isinstance(node, dict):
        return {k: mark_literal_descriptions(v, k) for k, v in node.items()}
    if isinstance(node, list):
        return [mark_literal_descriptions(v, key) for v in node]
    if key == "description" and isinstance(node, str):
        return LiteralStr(node)
    return node



def main() -> None:
    BLOCKS_FOLDER = Path("data/blocks")
    OUTPUT_FOLDER = Path("data/blocks_split")

    blocks = fetchBlocks(BLOCKS_FOLDER)
    OUTPUT_FOLDER.mkdir(parents=True, exist_ok=True)

    item_types: dict[str, list[str]] = {}

    item_block = blocks['item']
    for param in item_block.parameters.values():
        needs = param.needs
        if needs is None:
            continue
        item_type_needs = None
        for need in needs:
            if need.name == "ItemType":
                item_type_needs = need
                break
        if item_type_needs is None:
            continue
        print(param.name)
        needs_values = item_type_needs.values
        assert needs_values is not None
        for value in needs_values:
            assert type(value) is str
            item_types.setdefault(value, []).append(param.name)

    from pprint import pprint
    pprint(item_types)

    for key, value in item_types.items():
        itemtype = key.split(":")[1]
        export_path = OUTPUT_FOLDER / f"item_{itemtype}.yaml"

        parameters: list[ParameterDefinition] = []
        parameter_need = None
        for param_name in value:
            source_param = item_block.parameters[param_name.lower()].model_copy()
            needs = source_param.needs
            assert needs is not None

            if parameter_need is None:
                for need_source in needs:
                    need = need_source.model_copy()
                    if need.name != "ItemType":
                        continue
                    values = need.values
                    assert values is not None
                    print(key, need)

                    ok = False
                    for val in values:
                        if val == key:
                            ok = True
                            break
                    if not ok:
                        continue

                    need.values = [v for v in values if v == key]
                    parameter_need = need.model_copy()
                    break

            parameters.append(source_param)

        assert parameter_need is not None
        block_def = BlockDefinition(
            name=f'item',
            parameters=parameters,
            variant=VariantDefinition(
                source="item",
                parameters=[parameter_need],
                id=None
            )
        ) # pyright: ignore[reportCallIssue]

        # write only the set fields, using their schema (alias) names, like formatBlocks.serialize
        with open(export_path, "w", encoding="utf-8") as f:
            yaml.safe_dump(
                mark_literal_descriptions(block_def.model_dump(by_alias=True, exclude_unset=True)),
                f,
                sort_keys=False,
                allow_unicode=True,
            )

if __name__ == "__main__":
    main()