from enum import Enum, auto

class ModifierType(Enum):
    LOCATION = "in"
    DESTINATION = "to"
    SOURCE_BY = "by"
    SOURCE_FROM = "from"

class LogicalOperatorType(Enum):
    AND = "AND"
    OR = "OR"