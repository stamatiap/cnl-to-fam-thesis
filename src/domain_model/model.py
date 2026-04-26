from dataclasses import dataclass
from src.domain_model.enums import ModifierType, LogicalOperatorType

@dataclass
class Asset:
    type:str
    name: str

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
    target: Asset
    modifiers: list[Modifier]


@dataclass
class Event:
    id: str
    name: str
    action: Action
    preconditions: list[StateCondition]
    operator: list[LogicalOperatorType]
    postconditions: list[StateCondition]

@dataclass
class TechniqueModel:
    id: str
    name: str
    tactic: str
    tactic_id: str
    events: list[Event]


# --------------------------

@dataclass
class Process(Asset):
    process_id: str
    parent_process: str
    started_at: str
    status: str

@dataclass
class File(Asset):
    path: str
    size: int

@dataclass
class Message(Asset):
    data: str

@dataclass
class Account(Asset):
    username: str
    password: str
    access_level: str

@dataclass
class Device(Asset):
    device_type: str
    ip_address: str

@dataclass
class Session(Asset):
    session_id: str
    start_time: str
    end_time: str
    duration: int

@dataclass
class Endpoint(Asset):
    protocol: str
    port: str
    ip_address: str
    identifier_path: str

@dataclass
class NetworkConnection(Asset):
    source: Process 
    destination: Endpoint
    source_ip: str
    destination_ip: str
    transport_protocol: str
    started_at: str
    status: str