from dataclasses import dataclass
from src.domain_model.enums import ModifierType, LogicalOperatorType

@dataclass
class Asset:
    type: str
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
    object: Asset
    modifiers: list[Modifier]


@dataclass
class Event:
    id: str
    name: str
    action: Action
    preconditions: list[StateCondition]
    precondition_operators: list[LogicalOperatorType]
    postconditions: list[StateCondition]
    postcondition_operators: list[LogicalOperatorType]

@dataclass
class Detection:
    event_refs: list[Event]
    operators: list[LogicalOperatorType]

@dataclass
class TechniqueModel:
    id: str
    name: str
    tactic: str
    tactic_id: str
    events: list[Event]
    detection: Detection

    def get_all_assets(self) -> dict[str, list[Asset]]:
        assets: dict[str, list[Asset]] = {}
        seen_names = set()
        
        for event in self.events:
            for asset in self._extract_assets_from_event(event):
                if asset.name not in seen_names:
                    seen_names.add(asset.name)
                    asset_type = type(asset).__name__
                    if asset_type not in assets:
                        assets[asset_type] = []
                    assets[asset_type].append(asset)
        
        return assets
    
    def _extract_assets_from_event(self, event: Event) -> list[Asset]:
        assets = []
        assets.append(event.action.actor)
        assets.append(event.action.object)
        for modifier in event.action.modifiers or []:
            assets.append(modifier.value)
        for condition in event.preconditions or []:
            assets.append(condition.subject)
            for modifier in condition.modifiers or []:
                assets.append(modifier.value)
        for condition in event.postconditions or []:
            assets.append(condition.subject)
            for modifier in condition.modifiers or []:
                assets.append(modifier.value)
        return assets

# --------------------------

@dataclass
class Process(Asset):
    process_id: str = None
    parent_process: str = None
    started_at: str = None
    status: str = None

@dataclass
class File(Asset):
    path: str = None
    size: int = None

@dataclass
class Message(Asset):
    data: str = None

@dataclass
class Account(Asset):
    username: str = None
    password: str = None
    access_level: str = None

@dataclass
class Device(Asset):
    device_type: str = None
    ip_address: str = None

@dataclass
class Session(Asset):
    session_id: str = None
    start_time: str = None
    end_time: str = None
    duration: int = None

@dataclass
class Endpoint(Asset):
    protocol: str = None
    port: str = None
    ip_address: str = None
    identifier_path: str = None

@dataclass
class NetworkConnection(Asset):
    source: Process = None
    destination: Endpoint = None
    source_ip: str = None
    destination_ip: str = None
    transport_protocol: str = None
    started_at: str = None
    status: str = None

@dataclass
class Directory(Asset):
    path: str = None