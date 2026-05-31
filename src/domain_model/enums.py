from enum import Enum, auto

class ModifierType(Enum):
    LOCATION = "in"
    DESTINATION = "to"
    SOURCE = "from"
    TRIGGER = "by"

class LogicalOperatorType(Enum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"

class TimePeriodPreposition(Enum):
    DURING = "during"
    OUTSIDE = "outside"

class TimeUnit(Enum):
    MILLISECOND = "millisecond"
    SECOND = "second"
    MINUTE = "minute"
    HOUR = "hour"


TIME_UNIT_MAP = {
    "sec": TimeUnit.SECOND,
    "seconds": TimeUnit.SECOND,
    "min": TimeUnit.MINUTE,
    "minutes": TimeUnit.MINUTE,
    "ms": TimeUnit.MILLISECOND,
    "milliseconds": TimeUnit.MILLISECOND,
    "hours": TimeUnit.HOUR,
}