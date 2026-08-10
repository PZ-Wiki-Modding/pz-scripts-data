from enum import StrEnum

class BlockProperties(StrEnum):
    REF_DESC = '#desc'
    REF_FULL = '#ref'

    VERSION = 'version'
    NAME = 'name'

    DESCRIPTION = 'description'
    SHORT_DESCRIPTION = 'short_descrition'

    VARIANT = 'variantOf'
    VARIANTS = 'variants'

    PARENTS = 'parents'
    CHILDREN = 'children'
    PARAMETERS = 'parameters'
    PROPERTIES = 'properties'

    SEE_ALSO = 'seeAlso'