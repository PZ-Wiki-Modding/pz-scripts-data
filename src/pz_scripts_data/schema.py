"""Pydantic models defining the structure of block definition files.

``BlockDefinition`` is the root model. Its JSON Schema is exported to
``schemas/blocks.json`` by running ``python -m pz_scripts_data.schema``.
"""

import json
import sys
from pathlib import Path
from typing import Annotated, Any, Literal, Self

from pydantic import BaseModel, ConfigDict, Field, WithJsonSchema, model_validator
from pydantic.json_schema import GenerateJsonSchema, JsonSchemaValue
from pydantic_core import core_schema

DEFAULT_OUTPUT = Path(__file__).resolve().parents[2] / "schemas" / "blocks.json"

ScalarType = Literal["string", "float", "boolean", "integer"]

# Accepts whole numbers as int so they are not widened to float on output. The JSON Schema stays "number".
Number = Annotated[int | float, WithJsonSchema({"type": "number"})]


class SchemaModel(BaseModel):
    """Base model. Unknown keys are rejected and no value may be null."""

    model_config = ConfigDict(extra="forbid", strict=True, validate_by_name=True)

    @model_validator(mode="before")
    @classmethod
    def _reject_null(cls, data: Any) -> Any:
        if isinstance(data, dict) and any(value is None for value in data.values()):
            raise ValueError("null is not allowed; omit the key instead")
        return data


class BlockReference(SchemaModel):
    """If the parameter is of type 'block', this can be used to provide a description of the expected format of the block."""

    name: str = Field(description="The name of the block type that this parameter references to.")
    full_type: bool = Field(
        True,
        alias="fullType",
        description="Indicates whether the parameter's value can match the module and block name, for example 'module.block'.",
    )
    no_auto_import: bool = Field(
        False,
        alias="noAutoImport",
        description="Indicates whenever this parameter can automatically check its own parent block module when fullType is set to true. If false, this means that the module won't be automatically imported.",
    )


class TranslationDefinition(SchemaModel):
    """If the parameter is of type 'translation', this can be used to provide a description of the expected format of the translation. For script blocks, this is associated to the ID of the block."""

    key_pattern: str = Field(
        alias="keyPattern",
        description="A regex pattern that the translation key in the source must match. The '{value}' placeholder is replaced by the ID of the block or value of the parameter. '{module}' is replaced by the module of the block.",
    )
    source_file: str = Field(
        alias="sourceFile",
        description="The source file where the translation key is defined (without the .json extension).",
    )


class BlockID(SchemaModel):
    """Defines the ID properties for this block type. If not specified, the block type does not have an ID."""

    parents_without: list[str] | None = Field(
        None,
        alias="parentsWithout",
        description="A list of block names that cannot be parents if this block has an ID.",
    )
    values: list[str] | None = Field(
        None,
        description="A list of allowed ID values for this block. If not given, any value is allowed.",
    )
    as_type: bool | None = Field(
        None,
        alias="asType",
        description="Specifies if the ID of the block should count as the block type. For example, components have specific definitions based on their ID. This means a script block needs to be defined with the name 'component <componentID>' as well as 'component' to cover all component types available with the 'values' attribute.",
    )
    optional: list[str] | None = Field(
        None,
        description="A list of ID values that are optional for this block type.",
    )
    can_have_space: bool | None = Field(
        None,
        alias="canHaveSpace",
        description="Indicates whether the ID of the block can contain spaces. If false or not specified, the ID cannot contain spaces.",
    )
    forbidden: list[str] | None = Field(
        None,
        description="A list of forbidden ID values for this block. If not provided, no values are forbidden.",
    )
    translation: TranslationDefinition | None = None


class BlockDeprecation(SchemaModel):
    """Indicates whether the block type is deprecated."""

    replaced_by: str | None = Field(
        None,
        alias="replacedBy",
        description="The name of the block type that replaces this deprecated block type.",
    )
    description: str | None = Field(
        None,
        description="A brief description of why the block type is deprecated and any additional information about the deprecation.",
    )


class _ArrayBase(SchemaModel):
    separator: str = Field(description="Specifies the separator used to split the string into array items.")
    min_items: Number | None = Field(
        None,
        alias="min",
        description="The minimum number of items required in the array.",
    )
    max_items: Number | None = Field(
        None,
        alias="max",
        description="The maximum number of items allowed in the array.",
    )
    soft_override: bool | None = Field(
        None,
        alias="softOverride",
        description="If true, a soft override of this property will add its content to the previously already existing array. Thus adding the old entries is not necessary and should be avoided to prevent duplicates.",
    )


class ScalarArrayDefinition(_ArrayBase):
    item_type: ScalarType = Field(alias="type", description="Specifies the data type of the items in the array.")


class BlockArrayDefinition(_ArrayBase):
    item_type: Literal["block"] = Field(alias="type", description="Specifies the data type of the items in the array.")
    block: BlockReference = Field(description="The block type of the items in the array.")


ArrayDefinition = ScalarArrayDefinition | BlockArrayDefinition


class _ObjectBase(SchemaModel):
    key_value_separator: str = Field(
        alias="keyValueSeparator",
        description="Specifies the separator used to split the key and the value in the key-value pairs. The parameter 'pairsSeparator' is used to split the pairs from each others.",
    )
    pairs_separator: str = Field(
        alias="pairsSeparator",
        description="Specifies the separator used to split the pairs from each others. The parameter 'keyValueSeparator' is used to split the keys and values.",
    )
    soft_override: bool | None = Field(
        None,
        alias="softOverride",
        description="If true, a soft override of this property will add its content to the previously already existing array. Thus adding the old entries is not necessary and should be avoided to prevent duplicates.",
    )


class ScalarKeyScalarValueObject(_ObjectBase):
    key_type: ScalarType = Field(alias="keyType", description="Specifies the data type of the keys in the object.")
    value_type: ScalarType = Field(alias="valueType", description="Specifies the data type of the values in the object.")


class BlockKeyBlockValueObject(_ObjectBase):
    key_type: Literal["block"] = Field(alias="keyType", description="Specifies the data type of the keys in the object.")
    key_block: BlockReference = Field(alias="keyBlock", description="The block type of the keys in the object.")
    value_type: Literal["block"] = Field(alias="valueType", description="Specifies the data type of the values in the object.")
    value_block: BlockReference = Field(alias="valueBlock", description="The block type of the values in the object.")


class BlockKeyScalarValueObject(_ObjectBase):
    key_type: Literal["block"] = Field(alias="keyType", description="Specifies the data type of the keys in the object.")
    key_block: BlockReference = Field(alias="keyBlock", description="The block type of the keys in the object.")
    value_type: ScalarType = Field(alias="valueType", description="Specifies the data type of the values in the object.")


class ScalarKeyBlockValueObject(_ObjectBase):
    key_type: ScalarType = Field(alias="keyType", description="Specifies the data type of the keys in the object.")
    value_type: Literal["block"] = Field(alias="valueType", description="Specifies the data type of the values in the object.")
    value_block: BlockReference = Field(alias="valueBlock", description="The block type of the values in the object.")


ObjectDefinition = (
    ScalarKeyScalarValueObject
    | BlockKeyBlockValueObject
    | BlockKeyScalarValueObject
    | ScalarKeyBlockValueObject
)


class CallbackParameter(SchemaModel):
    name: str = Field(description="The name of the parameter.")
    param_type: str = Field(alias="type", description="The type of the parameter.")
    is_java: bool = Field(
        False,
        alias="isJava",
        description="Indicates whether the parameter is a Java object.",
    )


class CallbackDefinition(SchemaModel):
    """Indicates whether the parameter is a callback function."""

    parameters: list[CallbackParameter] = Field(description="A list of parameters that the callback function takes.")
    returns: str | None = Field(None, description="The return type of the callback function.")


class ArrayParameterType(SchemaModel):
    main: Literal["array"] = Field(description="The main data type of the parameter.")
    array: ArrayDefinition = Field(
        description="If the parameter is of type 'array', this can be used to provide a description of the expected format of the array.",
    )


class ObjectParameterType(SchemaModel):
    main: Literal["object"] = Field(description="The main data type of the parameter.")
    object_: ObjectDefinition = Field(
        alias="object",
        description="If the parameter is of type 'object', this can be used to provide a description of the expected format of the object.",
    )


class BlockParameterType(SchemaModel):
    main: Literal["block"] = Field(description="The main data type of the parameter.")
    block: BlockReference = Field(
        description="If the parameter is of type 'block', this can be used to provide a description of the expected format of the block.",
    )


class CallbackParameterType(SchemaModel):
    main: Literal["callback"] = Field(description="The main data type of the parameter.")
    callback: CallbackDefinition = Field(description="Indicates whether the parameter is a callback function.")


class TranslationParameterType(SchemaModel):
    main: Literal["translation"] = Field(description="The main data type of the parameter.")
    translation: TranslationDefinition = Field(
        description="If the parameter is of type 'translation', this can be used to provide a description of the expected format of the translation.",
    )


class ScalarParameterType(SchemaModel):
    main: ScalarType = Field(description="The main data type of the parameter.")


ParameterType = (
    ArrayParameterType
    | ObjectParameterType
    | BlockParameterType
    | CallbackParameterType
    | TranslationParameterType
    | ScalarParameterType
)


class ParameterDeprecation(SchemaModel):
    """Indicates whether the parameter is deprecated."""

    replaced_by: str | None = Field(
        None,
        alias="replacedBy",
        description="The name of the parameter that replaces this deprecated parameter.",
    )
    description: str | None = Field(
        None,
        description="A brief description of why the parameter is deprecated and any additional information about the deprecation.",
    )
    version: str | None = Field(None, description="The version(s) in which the parameter is deprecated.")


class ParameterNeed(SchemaModel):
    """A condition on another parameter that must be met for this parameter to be valid."""

    name: str | None = Field(None, description="The name of the parameter that this condition depends on.")
    values: list[str | Number | bool] | None = Field(
        None,
        description="The values of the dependent parameter that must be met for this parameter to be valid.",
    )
    value_to_type: dict[str, str] | None = Field(
        None,
        alias="valueToType",
        description="A mapping of values of the dependent parameter to the expected type of this parameter. For example, if the dependent parameter is 'type' and it has a value 'integer', then this parameter should be of type 'float'. The key is the value of the dependent parameter, and the value is the expected type of this parameter when the dependent parameter has that value.",
        examples=[{"integer": "float", "double": "float", "boolean": "boolean", "string": "string"}],
    )
    minimum: Number | None = Field(
        None,
        description="The minimum value for this parameter when the dependent parameter has a specific value. Requires the target parameter to be of type 'float' or 'integer'.",
    )
    maximum: Number | None = Field(
        None,
        description="The maximum value for this parameter when the dependent parameter has a specific value. Requires the target parameter to be of type 'float' or 'integer'.",
    )
    children: list[str] | None = Field(
        None,
        description="A list of child blocks that must be present for this parameter to be valid.",
    )
    parents: list[str] | None = Field(
        None,
        description="A list of parent blocks that must be present for this parameter to be valid.",
    )


class ParameterDefinition(SchemaModel):
    """A parameter available for a block type."""

    name: str | None = Field(None, description="The name of the parameter.")
    any_name: bool | None = Field(
        None,
        alias="anyName",
        description="A parameter with `anyName` can have any name.",
    )
    ref: str | None = Field(None, alias="#ref", description="A reference to another block parameter.")
    ref_desc: str | None = Field(
        None,
        alias="#desc",
        description="A reference to the description of another block parameter. This allows sharing the same description between multiple parameters without using #ref, which would also share other properties.",
    )
    description: str | None = Field(None, description="A brief description of what the parameter does.")
    allowed_duplicate: bool | None = Field(
        None,
        alias="allowedDuplicate",
        description="Indicates whether the parameter can be duplicated.",
    )
    can_be_empty: bool | None = Field(
        None,
        alias="canBeEmpty",
        description="Indicates whether the parameter can be empty.",
    )
    item_types: list[str] | None = Field(
        None,
        alias="itemTypes",
        description="DEPRECATED: Specifies the type of item the parameter is associated with (e.g., 'vehicle', 'item', etc.). Only for item scripts.",
    )
    parents_only: list[str] | None = Field(
        None,
        alias="parentsOnly",
        description="DEPRECATED: A list of parent block types for which this parameter is applicable.",
    )
    required: bool | None = Field(None, description="Indicates whether the parameter is required.")
    default_value: str | Number | bool | list[Any] | dict[str, Any] | None = Field(
        None,
        alias="default",
        description="The default value for the parameter if not specified.",
    )
    minimum: Number | None = Field(
        None,
        description="The minimum value for the parameter if it is a number. Needs type.main to be 'float' or 'integer' to be applicable.",
    )
    maximum: Number | None = Field(
        None,
        description="The maximum value for the parameter if it is a number. Needs type.main to be 'float' or 'integer' to be applicable.",
    )
    data_type: ParameterType | None = Field(
        None,
        alias="type",
        description="The data type of the parameter.",
    )
    values: list[str | Number] | None = Field(None, description="A list of allowed values for the parameter.")
    deprecated: ParameterDeprecation | None = None
    needs: list[ParameterNeed] | None = Field(
        None,
        description="A list of conditions of other parameters that must be met for this parameter to be valid.",
    )
    incompatible_with: list[str] | None = Field(
        None,
        alias="incompatibleWith",
        description="List of other parameters which are incompatible with this one.",
    )
    is_useless: bool = Field(
        False,
        alias="isUseless",
        description="Indicates whether the parameter is considered useless or not. This can be used to flag parameters that have no effect in the game. Not to be confused with deprecated which indicates a parameter that previously worked but no longer does.",
    )
    see_also: list[str] | None = Field(
        None,
        alias="seeAlso",
        description="A list of other parameters that are related to this one.",
    )


class BlockDefinition(SchemaModel):
    """Schema of a block definition file."""

    model_config = ConfigDict(
        title="Blocks Folder General Schema",
        json_schema_extra=lambda schema: schema.update(
            allOf=[
                {
                    "if": {"required": ["isRoot"], "properties": {"isRoot": {"const": True}}},
                    "then": {"required": ["pattern"]},
                }
            ]
        ),
    )

    version: float | str | None = None
    ref_desc: str | None = Field(
        None,
        alias="#desc",
        description="A reference to the description of another block type. This allows sharing the same description between multiple block types without using #ref, which would also share other properties.",
    )
    ref: str | None = Field(
        None,
        alias="#ref",
        description="A reference to another block type. This allows sharing the same properties between multiple block types.",
    )
    variant_of: str | None = Field(
        None,
        alias="variantOf",
        description="Indicates whether this block type is a variant of another block type. The value corresponds to the block type it is a variant of.",
    )
    name: str = Field(description="The name of the block type.")
    any_name: bool | None = Field(
        None,
        alias="anyName",
        description="A block with `anyName` can have any name. This requires strict placement in parent blocks to correctly validate the block parameters.",
    )
    short_description: str | None = Field(
        None,
        alias="shortDescription",
        description="A brief description of the block type, used for quick reference in completion items.",
    )
    description: str | None = Field(None, description="A brief description of the block type.")
    block_id: BlockID | None = Field(None, alias="ID")
    parents: list[str] | None = Field(None, description="A list of valid parent block types.")
    needs_children: list[str] | None = Field(
        None,
        alias="needsChildren",
        description="A list of required child block types.",
    )
    soft_override: bool | None = Field(
        None,
        alias="softOverride",
        description="Indicates whether the block can be soft overridden in scripts.",
    )
    is_root: bool | None = Field(
        None,
        alias="isRoot",
        description="Indicates whether the block is a root document.",
    )
    pattern: list[str] | None = Field(
        None,
        description="A list of regex patterns that can be used to match this root file. Required when 'isRoot' is true.",
    )
    no_comma: bool | None = Field(
        None,
        alias="noComma",
        description="Indicates whether the block parameters should not be followed by a comma.",
    )
    deprecated: BlockDeprecation | None = None
    parameters: list[ParameterDefinition] | None = Field(
        None,
        description="A list of parameters available for this block type.",
    )
    properties: dict[str, Any] | None = Field(
        None,
        description="Custom additional properties for the block type.",
    )

    @model_validator(mode="after")
    def _root_requires_pattern(self) -> Self:
        if self.is_root is True and self.pattern is None:
            raise ValueError("'pattern' is required when 'isRoot' is true")
        return self


class _BlocksJsonSchemaGenerator(GenerateJsonSchema):
    """Draft-07 output without null members, titles or `default: null` entries, matching the hand-written schema."""

    schema_dialect = "http://json-schema.org/draft-07/schema#"

    def field_title_should_be_set(self, schema: Any) -> bool:
        return False

    def model_schema(self, schema: core_schema.ModelSchema) -> JsonSchemaValue:
        json_schema = super().model_schema(schema)
        if schema["cls"] is not BlockDefinition:
            json_schema.pop("title", None)
        return json_schema

    def nullable_schema(self, schema: core_schema.NullableSchema) -> JsonSchemaValue:
        return self.generate_inner(schema["schema"])

    def default_schema(self, schema: core_schema.WithDefaultSchema) -> JsonSchemaValue:
        if schema.get("default") is None:
            return self.generate_inner(schema["schema"])
        return super().default_schema(schema)


def build_json_schema() -> dict[str, Any]:
    return BlockDefinition.model_json_schema(by_alias=True, schema_generator=_BlocksJsonSchemaGenerator)


def main(argv: list[str]) -> int:
    output = Path(argv[0]) if argv else DEFAULT_OUTPUT
    output.write_text(json.dumps(build_json_schema(), indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {output}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
