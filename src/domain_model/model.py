from dataclasses import dataclass, field
from src.domain_model.enums import *
from typing import Self
import uuid

@dataclass
class Asset:
    asset_type: str
    name: str
    asset_id: str = field(default_factory=lambda: str(uuid.uuid4()))

@dataclass
class Modifier:
    type: ModifierType
    value: Asset

@dataclass
class StateCondition:
    subject: Asset
    subject_state: str
    modifiers: list[Modifier]

@dataclass
class Action:
    action_verb: str
    actor: Asset
    object: Asset
    modifiers: list[Modifier]

@dataclass
class Repetition:
    occurrences: int
    time_value: int
    time_unit: TimeUnit

@dataclass 
class Timing:
    preposition: TimePeriodPreposition
    time_period: str

@dataclass
class Event:
    id: str
    name: str
    action: Action
    preconditions: list[StateCondition]
    precondition_operator: LogicalOperatorType
    postconditions: list[StateCondition]
    postcondition_operator: LogicalOperatorType
    repetition: Repetition = None
    timing: Timing = None

@dataclass
class Completion:
    event_refs: list[Event]
    operator: LogicalOperatorType

@dataclass
class Tactic:
    id: str
    name: str

@dataclass
class TechniqueModel:
    id: str
    name: str
    tactics: list[Tactic]
    assets: dict[str, Asset]
    events: list[Event]
    completion: Completion

# --------------------------
@dataclass
class Handle(Asset):
    hexadecimal_number: str = None
    target: Asset = None

@dataclass
class Process(Asset):
    signed: bool = None
    command_line: str = None
    parent_process: Self = None

@dataclass
class File(Asset):
    path: str = None
    signed: bool = None

@dataclass
class Registry(Asset):
    path: str = None

@dataclass
class Endpoint(Asset):
    port: str = None
    protocol: str = None
    ip_address: str = None

@dataclass
class NetworkConnection(Asset):
    destination: Endpoint = None
    source: Process = None
    transport_protocol: str = None

@dataclass
class Driver(Asset):
    signed: bool = None

@dataclass
class Module(Asset):
    path: str = None
    signed: bool = None

@dataclass
class Device(Asset):
    device_type: str = None

@dataclass
class Volume(Asset):
    path: str = None

@dataclass
class Account(Asset):
    scope: str = None

@dataclass
class Session(Asset):
    access_level: str = None

@dataclass
class Message(Asset):
    data: str = None

@dataclass
class Directory(Asset):
    path: str = None