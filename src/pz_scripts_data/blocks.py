from enum import StrEnum

class BlockProperties(StrEnum):
    VERSION = 'version'
    REF_DESC = '#desc'
    REF_FULL = '#ref'
    DEPRECATED = 'deprecated'

    NAME = 'name'
    ID = 'ID'
    SOFT_OVERRIDE = 'softOverride'
    NO_COMMA = 'noComma'
    PATTERN = 'pattern'

    DESCRIPTION = 'description'
    SHORT_DESCRIPTION = 'short_description'

    VARIANT = 'variantOf'
    VARIANTS = 'variants'

    PARENTS = 'parents'
    CHILDREN = 'children'
    NEEDS_CHILDREN = 'needsChildren'
    PARAMETERS = 'parameters'
    PROPERTIES = 'properties'

    IS_ROOT = 'isRoot'

class IDProperties(StrEnum):
    OPTIONAL = 'optional'
    CAN_HAVE_SPACES = 'canHaveSpace'
    FORBIDDEN = 'forbidden'

    VALUES = 'values'
    PARENTS_WITHOUT = 'parentsWithout'
    AS_TYPE = 'asType'

    TRANSLATION = 'translation'

class ParameterProperties(StrEnum):
    REF_DESC = '#desc'
    REF_FULL = '#ref'

    NAME = 'name'
    DESCRIPTION = 'description'

    TYPE = 'type'
    DEFAULT = 'default'
    REQUIRED = 'required'
    CAN_BE_EMPTY = 'canBeEmpty'
    MINIMUM = 'minimum'
    MAXIMUM = 'maximum'
    VALUES = 'values'

    DEPRECATED = 'deprecated'
    IS_USELESS = 'isUseless'
    ALLOW_DUPLICATES = 'allowDuplicates'
    INCOMPATIBLE_WITH = 'incompatibleWith'

    SEE_ALSO = 'seeAlso'

class PropertyData(StrEnum):
    NAME = 'name'
    DESCRIPTION = 'description'
    PROPERTIES = 'properties'