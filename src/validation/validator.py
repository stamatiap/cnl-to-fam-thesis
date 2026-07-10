from src.domain_model.model import *
from src.domain_model.enums import *
from dataclasses import is_dataclass, fields
from enum import Enum
from src.monitoring import logger, write_artifact
from pathlib import Path

class Validator():
    def __init__(self):
        self.errors: int = 0 

    def _group_by_type(self, assets: dict) -> dict:
        """Group dict[name, Asset] by Python subclass name -> list[Asset]."""
        grouped: dict = {}
        for asset in assets.values():
            grouped.setdefault(type(asset).__name__, []).append(asset)
        return grouped

    def validate_model_structure(self, cnl_model: TechniqueModel, domain_model: TechniqueModel) -> bool:
        cnl_grouped = self._group_by_type(cnl_model.assets)
        domain_grouped = self._group_by_type(domain_model.assets)

        # check no. of assets per asset type
        for asset_type, domain_list in domain_grouped.items():
            cnl_list = cnl_grouped.get(asset_type, [])
            if len(cnl_list) != len(domain_list):
                logger.warning(
                    f"Asset count mismatch for {asset_type}: "
                    f"expected {len(domain_list)}, got {len(cnl_list)}"
                )
                self.errors += 1

        # check unexpected asset types used
        for asset_type in cnl_grouped:
            if asset_type not in domain_grouped:
                logger.warning(f"Unexpected asset type in description: {asset_type}")
                self.errors += 1

        # check no. of events
        if len(cnl_model.events) != len(domain_model.events):
            logger.warning(
                f"Total event count mismatch. Expected {len(domain_model.events)}, "
                f"got {len(cnl_model.events)}"
            )
            self.errors += 1

        # check no. of actions
        cnl_actions = [e.action for e in cnl_model.events if e.action is not None]
        domain_actions = [e.action for e in domain_model.events if e.action is not None]
        if len(cnl_actions) != len(domain_actions):
            logger.warning(
                f"Total action count mismatch. Expected {len(domain_actions)}, "
                f"got {len(cnl_actions)}"
            )
            self.errors += 1

        if self.errors == 0:
            return True
        return False


    def validate_events(self, cnl_model: TechniqueModel, domain_model: TechniqueModel) -> bool:
        for cnl_event, domain_event in zip(cnl_model.events, domain_model.events):
            self._validate_event(cnl_event, domain_event)

        if not self.errors:
            return True
        return False

    def _validate_event(self, cnl_event: Event, domain_event: Event) -> None:
        self._validate_action(cnl_event.action, domain_event.action, cnl_event.id)

    def _validate_action(self, cnl_action: Action, domain_action: Action, event_id: str) -> None:
        if type(cnl_action.actor) != type(domain_action.actor):
            logger.warning(
                f"Event {event_id} actor type mismatch: "
                f"expected {type(domain_action.actor).__name__}, "
                f"got {type(cnl_action.actor).__name__}"
            )
            self.errors += 1
        if type(cnl_action.object) != type(domain_action.object):
            logger.warning(
                f"Event {event_id} object type mismatch: "
                f"expected {type(domain_action.object).__name__}, "
                f"got {type(cnl_action.object).__name__}"
            )
            self.errors += 1

    def validate_model(self, cnl_model: TechniqueModel, domain_model: TechniqueModel) -> bool:

        if domain_model is None:
            logger.warning(f"No domain model found for technique ID {cnl_model.id}")
            return False
        else:
            # Save domain model 
            out = Path("data/technique_models") / f"domain_{domain_model.id.replace(".", "_")}_{domain_model.name}.json"
            write_artifact(domain_model, out)

        if not self.validate_model_structure(cnl_model, domain_model):
            logger.warning("failed model structure validation.")
            return False

        if not self.validate_events(cnl_model, domain_model):
            logger.warning("failed Event validation.")
            return False

        return True


  