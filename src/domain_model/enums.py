from enum import Enum, auto

class ModifierType(Enum):
    LOCATION = "in"
    DESTINATION = "to"
    SOURCE_BY = "by"
    SOURCE_FROM = "from"
    TIMING = "during"
    GEOLOCATION = "located_at"

class LogicalOperatorType(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"