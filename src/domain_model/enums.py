from enum import Enum, auto

class ModifierType(Enum):
    LOCATION = auto()
    DESTINATION = auto()

class StateVerbType(Enum):
    PLAIN = auto()
    IS_PASSIVE = auto()
    
class ActionVerbType(Enum):
    ACTIVE = auto()

class LogicalOperatorType(Enum):
    AND = "AND"
    OR = "OR"

class GivenItemType(Enum): 
    STATE_CONDITION = auto()