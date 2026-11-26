"""Pydantic models defining the structure of block definition files.

``BlockDefinition`` is the root model. Its JSON Schema is exported to
``schemas/blocks.json`` by running ``python -m pz_scripts_data.schema``.
"""

import json
import sys
from pathlib import Path
from typing import Annotated, Any, Literal, Self, TypeVar, Generic
from deprecated.sphinx import deprecated

from pydantic import BaseModel, ConfigDict, Field, WithJsonSchema, model_validator
from pydantic.json_schema import GenerateJsonSchema, JsonSchemaValue
from pydantic_core import core_schema

DEFAULT_SCHEMA_OUTPUT = Path(__file__).resolve().parents[2] / "schemas" / "blocks.json"

StringType = Literal["string"]
FloatType = Literal["float"]
BooleanType = Literal["boolean"]
IntegerType = Literal["integer"]
ScalarType = (
    StringType 
    | FloatType 
    | BooleanType 
    | IntegerType
)
TranslationType = Literal["translation"]
CallBackType = Literal["callback"]
BlockType = Literal["block"]
ObjectType = Literal["object"]
ArrayType = Literal["array"]
FileType = Literal["file"]
ParameterMainType = (
    ScalarType 
    | TranslationType 
    | CallBackType 
    | BlockType 
    | ObjectType 
    | ArrayType
    | FileType
)


# Accepts whole numbers as int so they are not widened to float on output. The JSON Schema stays "number".
Number = Annotated[int | float, WithJsonSchema({"type": "number"})]


class SchemaModel(BaseModel):
    """Base model. Unknown keys are rejected and no value may be null."""

    model_config = ConfigDict(
        extra="forbid",
        strict=True,
        validate_by_name=True,
        use_attribute_docstrings=True,
    )

    @model_validator(mode="before")
    @classmethod
    def _reject_null(cls, data: Any) -> Any:
        if isinstance(data, dict) and any(value is None for value in data.values()):
            raise ValueError("null is not allowed; omit the key instead")
        return data


class BlockReference(SchemaModel):
    """If the parameter is of type 'block', this can be used to provide 
    a description of the expected format of the block."""

    name: str
    """The name of the block type that this parameter references to."""
    full_type: bool = Field(
        True,
        alias="fullType",
    )
    """Indicates whether the parameter's value can match the module and 
    block name, for example 'module.block'."""
    no_auto_import: bool = Field(
        False,
        alias="noAutoImport",
    )
    """Indicates whenever this parameter can automatically check its own 
    parent block module when fullType is set to true. If false, this 
    means that the module won't be automatically imported."""


class TranslationDefinition(SchemaModel):
    """If the parameter is of type 'translation', this can be used to provide 
    a description of the expected format of the translation. For script blocks, 
    this is associated to the ID of the block."""

    key_pattern: str = Field(
        alias="keyPattern",
    )
    """A regex pattern that the translation key in the source must match. The 
    '{value}' placeholder is replaced by the ID of the block or value of the 
    parameter. '{module}' is replaced by the module of the block."""
    source_file: str = Field(
        alias="sourceFile",
    )
    """The source file where the translation key is defined (without the 
    .json extension)."""


class BlockID(SchemaModel):
    """Defines the ID properties for this block type. If not specified, the 
    block type does not have an ID."""

    parents_without: list[str] | None = Field(
        None,
        alias="parentsWithout",
    )
    """A list of block names that cannot be parents if this block has an ID."""
    values: list[str] | None = Field(
        None,
    )
    """A list of allowed ID values for this block. If not given, any value is 
    allowed."""
    deprecated_as_type: bool | None = Field(
        None,
        alias="asType",
    )
    """Specifies if the ID of the block should count as the block type. For 
    example, components have specific definitions based on their ID. This means 
    a script block needs to be defined with the name 'component <componentID>' 
    as well as 'component' to cover all component types available with the 
    'values' attribute."""
    @property
    @deprecated(
        reason="as_type is deprecated, use deprecated_as_type instead.",
        version="1.4.0",
    )
    def as_type(self) -> bool | None:
        return self.deprecated_as_type
    optional: list[str] | None = None
    """A list of ID values that are optional for this block type."""
    can_have_space: bool | None = Field(
        None,
        alias="canHaveSpace",
    )
    """Indicates whether the ID of the block can contain spaces. If false or not 
    specified, the ID cannot contain spaces."""
    forbidden: list[str] | None = None
    """A list of forbidden ID values for this block. If not provided, no values 
    are forbidden."""
    translation: TranslationDefinition | None = None


class BlockDeprecation(SchemaModel):
    """Indicates whether the block type is deprecated."""

    replaced_by: str | None = Field(
        None,
        alias="replacedBy",
    )
    """The name of the block type that replaces this deprecated block type."""
    description: str | None = None
    """A brief description of why the block type is deprecated and any additional 
    information about the deprecation."""

class FileDefinition(SchemaModel):
    """Describes the expected format of a file parameter."""

    relative_to: str = Field(
        alias="relativeTo",
    )
    """The relative path of the file, relative to version and common folders."""
    prefix: str | None = None
    """An optional prefix for the file path."""
    extension: str
    """The file extension for the file parameter."""


class _ArrayBase(SchemaModel):
    separator: str
    """Specifies the separator used to split the string into array items."""
    min_items: Number | None = Field(
        None,
        alias="min",
    )
    """The minimum number of items required in the array."""
    max_items: Number | None = Field(
        None,
        alias="max",
    )
    """The maximum number of items allowed in the array."""
    soft_override: bool | None = Field(
        None,
        alias="softOverride",
    )
    """If true, a soft override of this property will add its content to the 
    previously already existing array. Thus adding the old entries is not 
    necessary and should be avoided to prevent duplicates."""


class ScalarArrayDefinition(_ArrayBase):
    item_type: ScalarType = Field(alias="type")
    """Specifies the data type of the items in the array."""


class BlockArrayDefinition(_ArrayBase):
    item_type: Literal["block"] = Field(alias="type")
    """Specifies the data type of the items in the array."""
    block: BlockReference
    """The block type of the items in the array."""


ArrayDefinition = ScalarArrayDefinition | BlockArrayDefinition


class _ObjectBase(SchemaModel):
    key_value_separator: str = Field(
        alias="keyValueSeparator",
    )
    """Specifies the separator used to split the key and the value in the 
    key-value pairs. The parameter 'pairsSeparator' is used to split the pairs 
    from each others."""
    pairs_separator: str = Field(
        alias="pairsSeparator",
    )
    """Specifies the separator used to split the pairs from each others. 
    The parameter 'keyValueSeparator' is used to split the keys and values."""
    soft_override: bool | None = Field(
        None,
        alias="softOverride",
    )
    """If true, a soft override of this property will add its content to 
    the previously already existing array. Thus adding the old entries is 
    not necessary and should be avoided to prevent duplicates."""


class ScalarKeyScalarValueObject(_ObjectBase):
    key_type: ScalarType = Field(alias="keyType")
    """Specifies the data type of the keys in the object."""
    value_type: ScalarType = Field(alias="valueType")
    """Specifies the data type of the values in the object."""


class BlockKeyBlockValueObject(_ObjectBase):
    key_type: Literal["block"] = Field(alias="keyType")
    """Specifies the data type of the keys in the object."""
    key_block: BlockReference = Field(alias="keyBlock")
    """The block type of the keys in the object."""
    value_type: Literal["block"] = Field(alias="valueType")
    """Specifies the data type of the values in the object."""
    value_block: BlockReference = Field(alias="valueBlock")
    """The block type of the values in the object."""


class BlockKeyScalarValueObject(_ObjectBase):
    key_type: Literal["block"] = Field(alias="keyType")
    """Specifies the data type of the keys in the object."""
    key_block: BlockReference = Field(alias="keyBlock")
    """The block type of the keys in the object."""
    value_type: ScalarType = Field(alias="valueType")
    """Specifies the data type of the values in the object."""


class ScalarKeyBlockValueObject(_ObjectBase):
    key_type: ScalarType = Field(alias="keyType")
    """Specifies the data type of the keys in the object."""
    value_type: Literal["block"] = Field(alias="valueType")
    """Specifies the data type of the values in the object."""
    value_block: BlockReference = Field(alias="valueBlock")
    """The block type of the values in the object."""


ObjectDefinition = (
    ScalarKeyScalarValueObject
    | BlockKeyBlockValueObject
    | BlockKeyScalarValueObject
    | ScalarKeyBlockValueObject
)


class CallbackParameter(SchemaModel):
    name: str
    """The name of the parameter."""
    param_type: str = Field(alias="type")
    """The type of the parameter."""
    is_java: bool = Field(
        False,
        alias="isJava",
    )
    """Indicates whether the parameter is a Java object."""


class CallbackDefinition(SchemaModel):
    """Indicates whether the parameter is a callback function."""

    parameters: list[CallbackParameter]
    """A list of parameters that the callback function takes."""
    returns: str | None = None
    """The return type of the callback function."""


T = TypeVar('T')
class ParameterType(SchemaModel, Generic[T]):
    """Represents the type of a parameter."""
    main: T
    """The main data type of the parameter."""


class ArrayParameterType(ParameterType[ArrayType]):
    main: ArrayType
    """The main data type of the parameter."""
    array: ArrayDefinition
    """If the parameter is of type 'array', this can be used to provide 
    a description of the expected format of the array."""


class ObjectParameterType(ParameterType[ObjectType]):
    main: ObjectType
    """The main data type of the parameter."""
    object: ObjectDefinition = Field(
        alias="object",
    )
    """If the parameter is of type 'object', this can be used to provide 
    a description of the expected format of the object."""


class BlockParameterType(ParameterType[BlockType]):
    main: BlockType
    """The main data type of the parameter."""
    block: BlockReference
    """If the parameter is of type 'block', this can be used to provide 
    a description of the expected format of the block."""


class CallbackParameterType(ParameterType[CallBackType]):
    main: CallBackType
    """The main data type of the parameter."""
    callback: CallbackDefinition
    """Indicates whether the parameter is a callback function."""


class TranslationParameterType(ParameterType[TranslationType]):
    main: TranslationType
    """The main data type of the parameter."""
    translation: TranslationDefinition
    """If the parameter is of type 'translation', this can be used to provide 
    a description of the expected format of the translation."""

class FileParameterType(ParameterType[FileType]):
    main: FileType
    """The main data type of the parameter."""
    file: FileDefinition
    """If the parameter is of type 'file', this can be used to provide a 
    description of the expected format of the file."""


class ScalarParameterType(ParameterType[ScalarType]):
    main: ScalarType
    """The main data type of the parameter."""


ParameterTypeUnion = (
    ArrayParameterType
    | ObjectParameterType
    | BlockParameterType
    | CallbackParameterType
    | TranslationParameterType
    | FileParameterType
    | ScalarParameterType
)


class ParameterDeprecation(SchemaModel):
    """Indicates whether the parameter is deprecated."""

    replaced_by: str | None = Field(
        None,
        alias="replacedBy",
    )
    """The name of the parameter that replaces this deprecated parameter."""
    description: str | None = None
    """A brief description of why the parameter is deprecated and any additional 
    information about the deprecation."""
    version: str | None = None
    """The version(s) in which the parameter is deprecated."""


class Need(SchemaModel):
    """A condition on another parameter that must be met for this parameter to 
    be valid."""

    parameter: str | None = Field(None, alias='name')
    """The name of the parameter that this condition depends on."""
    # TODO: mark parameter as required when `forbidden_parameter` is not None
    forbidden_parameter: bool | None = Field(None, alias='forbiddenParameter')
    """Whenever the provided `parameter` is forbidden from being present."""
    values: list[str | Number | bool] | None = None
    """The values of the dependent parameter that must be met for this parameter 
    to be valid."""
    deprecated_value_to_type: dict[str, str] | None = Field(
        None,
        alias="valueToType",
        examples=[{"integer": "float", "double": "float", "boolean": "boolean", "string": "string"}],
    )
    """A mapping of values of the dependent parameter to the expected type 
    of this parameter. For example, if the dependent parameter is 'type' 
    and it has a value 'integer', then this parameter should be of type 'float'. 
    The key is the value of the dependent parameter, and the value is the 
    expected type of this parameter when the dependent parameter has that value."""
    @property
    @deprecated(
        reason="Use 'deprecated_value_to_type' instead.",
        version="1.4.0",
    )
    def value_to_type(self) -> dict[str, str] | None:
        return self.deprecated_value_to_type
    minimum: Number | None = None
    """The minimum value for the provided parameter when the dependent parameter 
    has a specific value. Requires the target parameter to be of type 'float' 
    or 'integer'."""
    maximum: Number | None = None
    """The maximum value for the provided parameter when the dependent parameter 
    has a specific value. Requires the target parameter to be of type 'float' 
    or 'integer'."""
    children: list[str] | None = None
    """A list of child blocks that must be present."""
    parents: list[str] | None = None
    """A list of parent blocks that must be present."""
    id: list[str] | None = None
    """A list of IDs the script block must have."""


class ParameterDefinition(SchemaModel):
    """A parameter available for a block type."""

    name: str
    """The name of the parameter."""
    any_name: bool | None = Field(
        None,
        alias="anyName",
    )
    """A parameter with `anyName` can have any name."""
    ref: str | None = Field(None, alias="#ref")
    """A reference to another block parameter."""
    ref_desc: str | None = Field(
        None,
        alias="#desc",
    )
    """A reference to the description of another block parameter. This 
    allows sharing the same description between multiple parameters without 
    using #ref, which would also share other properties."""
    description: str | None = None
    """A brief description of what the parameter does."""
    allowed_duplicate: bool | None = Field(
        None,
        alias="allowedDuplicate",
    )
    """Indicates whether the parameter can be duplicated."""
    can_be_empty: bool | None = Field(
        None,
        alias="canBeEmpty",
    )
    """Indicates whether the parameter can be empty."""
    item_types: list[str] | None = Field(
        None,
        alias="itemTypes",
    )
    """DEPRECATED: Specifies the type of item the parameter is associated 
    with (e.g., 'vehicle', 'item', etc.). Only for item scripts."""
    parents_only: list[str] | None = Field(
        None,
        alias="parentsOnly",
    )
    """DEPRECATED: A list of parent block types for which this parameter 
    is applicable."""
    required: bool | None = None
    """Indicates whether the parameter is required."""
    default_value: str | Number | bool | list[Any] | dict[str, Any] | None = Field(
        None,
        alias="default",
    )
    """The default value for the parameter if not specified."""
    minimum: Number | None = None
    """The minimum value for the parameter if it is a number. Needs 
    type.main to be 'float' or 'integer' to be applicable."""
    maximum: Number | None = None
    """The maximum value for the parameter if it is a number. Needs 
    type.main to be 'float' or 'integer' to be applicable."""
    data_type: ParameterTypeUnion | None = Field(
        None,
        alias="type",
    )
    """The data type of the parameter."""
    values: list[str | Number] | None = None
    """A list of allowed values for the parameter."""
    deprecated: ParameterDeprecation | None = None
    needs: list[Need] | None = None
    """A list of conditions of other parameters that must be met for this 
    parameter to be valid."""
    incompatible_with: list[str] | None = Field(
        None,
        alias="incompatibleWith",
    )
    """List of other parameters which are incompatible with this one."""
    is_useless: bool = Field(
        False,
        alias="isUseless",
    )
    """Indicates whether the parameter is considered useless or not. 
    This can be used to flag parameters that have no effect in the game. 
    Not to be confused with deprecated which indicates a parameter that 
    previously worked but no longer does."""
    see_also: list[str] | None = Field(
        None,
        alias="seeAlso",
    )
    """A list of other parameters that are related to this one."""

class VariantDefinition(SchemaModel):
    """Schema for defining a variant of a block type."""

    source: str
    """The source block type that this variant is based on."""
    needs: list[Need] | None = None
    """A list of parameters that must be met for this variant to be valid."""


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
    )
    """A reference to the description of another block type. This allows 
    sharing the same description between multiple block types without 
    using #ref, which would also share other properties."""
    ref: str | None = Field(
        None,
        alias="#ref",
    )
    variant_of_deprecated: str | None = Field(
        None,
        alias="variantOf",
    )
    @property
    @deprecated(
        reason="Accessing the variant source through the `variant_of` property is deprecated. Use `get_variant_source` instead.",
        version="1.4.0"
    )
    def variant_of(self) -> str | None:
        return self.get_variant_source()
    variant: VariantDefinition | None = None
    """Defines a variant of this block type."""
    name: str
    """The name of the block type."""
    any_name: bool | None = Field(
        None,
        alias="anyName",
    )
    """A block with `anyName` can have any name. This requires strict 
    placement in parent blocks to correctly validate the block parameters."""
    short_description: str | None = Field(
        None,
        alias="shortDescription",
    )
    """A brief description of the block type, used for quick reference in completion items."""
    description: str | None = None
    """A brief description of the block type."""
    block_id: BlockID | None = Field(None, alias="ID")
    parents: list[str] | None = None
    """A list of valid parent block types."""
    needs_children: list[str] | None = Field(
        None,
        alias="needsChildren",
    )
    """A list of required child block types."""
    soft_override: bool | None = Field(
        None,
        alias="softOverride",
    )
    """Indicates whether the block can be soft overridden in scripts."""
    is_root: bool | None = Field(
        None,
        alias="isRoot",
    )
    """Indicates whether the block is a root document."""
    pattern: list[str] | None = None
    """A list of regex patterns that can be used to match this root file. 
    Required when 'isRoot' is true."""
    no_comma: bool | None = Field(
        None,
        alias="noComma",
    )
    """Indicates whether the block parameters should not be followed 
    by a comma."""
    deprecated: BlockDeprecation | None = None
    parameters: list[ParameterDefinition] | None = None
    """A list of parameters available for this block type."""
    properties: dict[str, Any] | None = None
    """Custom additional properties for the block type."""

    @model_validator(mode="after")
    def _root_requires_pattern(self) -> Self:
        if self.is_root is True and self.pattern is None:
            raise ValueError("'pattern' is required when 'isRoot' is true")
        return self

    def get_variant_source(self) -> str | None:
        variant = self.variant
        if variant is not None:
            return variant.source
        variant_of_deprecated = self.variant_of_deprecated
        if variant_of_deprecated is not None:
            @deprecated(
                reason="The variant_of property is deprecated. It has now been replaced with `variant.source`.",
                version="1.4.0"
            )
            def _get_deprecated_variant_of() -> str | None:
                return variant_of_deprecated
            return _get_deprecated_variant_of()
        return None

class _BlocksJsonSchemaGenerator(GenerateJsonSchema):
    """Draft-07 output without null members, titles or `default: null` 
    entries, matching the hand-written schema."""

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


class ScriptsBlock(BlockDefinition):
    """Block used by the pipeline: parameters are keyed by lowercase name and relations are filled in during preparation."""

    # we change the parameters field structure from list to a dictionary
    def_id: str = Field(..., alias="def_id")
    parameters: dict[str, ParameterDefinition] = Field(default_factory=dict) # pyright: ignore[reportIncompatibleVariableOverride]
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



def build_json_schema() -> dict[str, Any]:
    return BlockDefinition.model_json_schema(by_alias=True, schema_generator=_BlocksJsonSchemaGenerator)

def output_json_schema(output: Path | str = DEFAULT_SCHEMA_OUTPUT) -> None:
    output_path = Path(output)
    output_path.write_text(json.dumps(build_json_schema(), indent=2), encoding="utf-8")
    print(f"Wrote {output_path}")


def main(argv: list[str]) -> int:
    output = Path(argv[0]) if argv else DEFAULT_SCHEMA_OUTPUT
    output_json_schema(output)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
