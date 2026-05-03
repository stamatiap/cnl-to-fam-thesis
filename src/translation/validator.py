from src.domain_model.model import *
from src.domain_model.enums import *
from src.domain_model.mitre_techniques import TECHNIQUE_REGISTRY
from pprint import pprint

class Validator():
    def __init__(self):
        self.errors: list[str] = [] 

    def fetch_domain_model(self, technique_id) -> TechniqueModel:
        domain_model = TECHNIQUE_REGISTRY.get(technique_id)
        return domain_model
    

    def validate_model_structure(self, cnl_model: TechniqueModel, domain_model: TechniqueModel) -> bool:

        # check No. of Assets
        cnl_assets = cnl_model.get_all_assets()
        domain_assets = domain_model.get_all_assets()
        if len(cnl_assets) != len(domain_assets):
            self.errors.append(f"Total asset count mismatch. Expected {len(domain_assets)}, got {len(cnl_assets)}")
        
        # check asset type categories exist
        for asset_type, domain_list in domain_assets.items():
            cnl_list = cnl_assets.get(asset_type, [])
            
            if len(cnl_list) != len(domain_list):
                self.errors.append(
                    f"Asset count mismatch for {asset_type}: "
                    f"expected {len(domain_list)}, got {len(cnl_list)}"
                )
        
        # check no extra asset types in parsed that aren't in domain
        for asset_type in cnl_assets:
            if asset_type not in domain_assets:
                self.errors.append(f"Unexpected asset type in description: {asset_type}")
            

        # check No. of Events
        cnl_events = cnl_model.events
        domain_events = domain_model.events
        if len(cnl_events) != len(domain_events):
            self.errors.append(f"Total event count mismatch. Expected {len(domain_events)}, got {len(cnl_events)}")
        
        pprint(cnl_model.get_all_assets())
        pprint(domain_model.get_all_assets())

        if not self.errors:
            return True
        else:
            print(self.errors)
            return False

    def validate_asset_contents(self, cnl_model: TechniqueModel, domain: TechniqueModel) -> bool:
        
        cnl_assets = cnl_model.get_all_assets()
        domain_assets = domain.get_all_assets()
        
        for asset_type, domain_list in domain_assets.items():
            parsed_list = cnl_assets.get(asset_type, [])
            
            # sort both lists by type string for consistent comparison
            domain_sorted = sorted(domain_list, key=lambda a: a.type)
            parsed_sorted = sorted(parsed_list, key=lambda a: a.type)
            
            for domain_asset, parsed_asset in zip(domain_sorted, parsed_sorted):
                # check type string matches
                if parsed_asset.type != domain_asset.type:
                    self.errors.append(
                        f"{asset_type} type mismatch: "
                        f"expected '{domain_asset.type}', got '{parsed_asset.type}'"
                    )
                
                # check name only for directories
                if asset_type == "Directory":
                    if parsed_asset.name != domain_asset.name:
                        self.errors.append(
                            f"Directory name mismatch: "
                            f"expected '{domain_asset.name}', got '{parsed_asset.name}'"
                        )

        if not self.errors:
            return True
        else:
            print(self.errors)
            return False
        
    def validate_events(self, cnl_model: TechniqueModel, domain_model: TechniqueModel) -> bool:
        cnl_events = cnl_model.events
        domain_events = domain_model.events

        for cnl_event, domain_event in zip(cnl_events, domain_events):
            self._validate_event(cnl_event, domain_event)

        if not self.errors:
            return True
        else:
            print(self.errors)
            return False

    def _validate_event(self, cnl_event: Event, domain_event: Event) -> None:
        self._validate_action(cnl_event.action, domain_event.action, cnl_event.id)
        self._validate_conditions(cnl_event.preconditions, domain_event.preconditions, cnl_event.id, "precondition")
        # self._validate_conditions(cnl_event.postconditions, domain_event.postconditions, cnl_event.id, "postcondition")

    def _validate_action(self, cnl_action: Action, domain_action: Action, event_id: str) -> None:
        if type(cnl_action.actor) != type(domain_action.actor):
            self.errors.append(
                f"Event {event_id} actor type mismatch: "
                f"expected {type(domain_action.actor).__name__}, got {type(cnl_action.actor).__name__}"
            )
        if type(cnl_action.object) != type(domain_action.object):
            self.errors.append(
                f"Event {event_id} object type mismatch: "
                f"expected {type(domain_action.object).__name__}, got {type(cnl_action.object).__name__}"
            )


    def _validate_conditions(self, cnl_conditions: list, domain_conditions: list, event_id: str, label: str) -> None:
        if len(cnl_conditions) != len(domain_conditions):
            self.errors.append(
                f"Event {event_id} {label} count mismatch: "
                f"expected {len(domain_conditions)}, got {len(cnl_conditions)}"
            )
            return

        # for cnl_cond, domain_cond in zip(cnl_conditions, domain_conditions):
        #     if type(cnl_cond.subject) != type(domain_cond.subject):
        #         self.errors.append(
        #             f"Event {event_id} {label} subject type mismatch: "
        #             f"expected {type(domain_cond.subject).__name__}, got {type(cnl_cond.subject).__name__}"
        #         )


    def validate_string(self, cnl_model: TechniqueModel, domain_model: TechniqueModel):
        # for each event in cnl model, check if the string representation of the event matches the string representation of the corresponding event in the domain model
        pass

    def validate_model(self, cnl_model: TechniqueModel) -> bool:
        domain_model = self.fetch_domain_model(cnl_model.id)
        if not domain_model:
            print(f"No domain model found for technique ID {cnl_model.id}")
            return False
        
        # validate structure
        if not self.validate_model_structure(cnl_model, domain_model):
            print("Model structure validation failed.")
            return False
        
        # validate types
        if not self.validate_asset_contents(cnl_model, domain_model):
            print("Asset content validation failed.")
            return False

        if not self.validate_events(cnl_model, domain_model):
            print("Event validation failed.")
            return False

        # validate string representation
        # self.validate_string(cnl_model, domain_model)

        print("Model validation successful.")
        return True


  