from antlr4 import FileStream, CommonTokenStream
from src.cnl.grammar.CNLParser import CNLParser
from src.cnl.grammar.CNLLexer import CNLLexer
from src.translation.visitor import Visitor
from src.domain_model.model import *
from src.domain_model.enums import *
from src.domain_model.asset_registry import ASSET_TYPE_MAP
from dataclasses import fields


class Translator:

    def parse_input(self, input_path: str) -> dict:
        input = FileStream(input_path, encoding="utf-8")
        lexer        = CNLLexer(input)
        stream       = CommonTokenStream(lexer)
        parser       = CNLParser(stream)
        tree         = parser.attack()
        return tree

    def create_modifier(self, modifier) -> Modifier:
        if modifier[0] == 'location':
            mod_type = ModifierType.LOCATION
        elif modifier[0] == 'destination':
            mod_type = ModifierType.DESTINATION
        elif modifier[0] == 'source':
            mod_type = ModifierType.SOURCE
        elif modifier[0] == 'geolocation':
            mod_type = ModifierType.GEOLOCATION
        
        if modifier[0] in ['location', 'destination', 'source']:
            # modifier references an Asset
            return Modifier(
                type = mod_type,
                value = self.get_asset(modifier[1])
            )
        else:
            # modifier does not reference an Asset
            return Modifier(
                type = mod_type,
                value = modifier[1]
            )
        
    def build_asset_registry(self, assets_dict: dict) -> dict[str, Asset]:
        registry = {}
        for name, info in assets_dict.items():
            asset_type_str = info.get("asset_type")
            properties = info.get("properties") or {}
            cls = ASSET_TYPE_MAP.get(asset_type_str.lower(), Asset) if asset_type_str else Asset
            # add all valid properties described
            valid_fields = {f.name for f in fields(cls)} - {'asset_type', 'name', 'asset_id'}
            extra = {k: v.replace("'", "").replace('"', "") for k, v in properties.items() if k in valid_fields}
            # warning for incorrect properties 
            for k, v in properties.items(): 
                if k not in valid_fields:
                    raise ValueError(f"Property '{k}' not a field of {cls}. Available fields: {valid_fields}")

            registry[name] = cls(asset_type=asset_type_str, name=name, **extra)
        return registry

    def get_asset(self, asset_name: str) -> Asset:
        asset = self.assets.get(asset_name)
        if asset is None:
            raise ValueError(f"Asset '{asset_name}' referenced but not declared in Background")
        return asset

    def create_state_conditions(self, conditions: list) -> list[StateCondition]:
        return [self.create_state_condition(c) for c in conditions]

    def create_state_condition(self, condition: dict) -> StateCondition:
        subject = self.get_asset(condition["object"])
        modifiers = [self.create_modifier(m) for m in condition.get("modifiers", [])]
        return StateCondition(
            subject=subject,
            subject_state=condition["verb"],
            modifiers=modifiers
        )

    def create_action(self, action) -> Action:
        actor = self.get_asset(action.get('actor', None))
        object = self.get_asset(action.get('object', None))
        modifiers = [self.create_modifier(m) for m in action.get('modifiers', [])]
        return Action(
            action_verb = action.get('action_verb', None),
            actor = actor,
            object = object,
            modifiers= modifiers
        )
    
    def create_repetition(self, repetition_item) -> Repetition | None:
        if repetition_item is None: 
            return None

        return Repetition(
            frequency = repetition_item[0],
            time_value = repetition_item[1],
            time_unit = TIME_UNIT_MAP.get(repetition_item[2], None),
        )
        
    def create_time_period(self, time_period_item) -> TimePeriod | None:
        if time_period_item is None:
            return None
        
        try:
            preposition = TimePeriodPreposition(time_period_item[0].lower())
        except ValueError:
            preposition = None
        
        return TimePeriod(preposition=preposition, time_period=time_period_item[1])

    def get_logical_operator(self, clause: dict) -> LogicalOperatorType | None:
        op = clause.get('operator', None)

        if op is not None:
            try: 
                operator = LogicalOperatorType(op.upper())
            except ValueError:
                operator = None
        else: 
            operator = None

        return operator


    def create_event(self, event) -> Event:
        action = self.create_action(event.get('when', {}))
        preconditions = self.create_state_conditions(event.get('given', {}).get('preconditions', []))  # currently expecting only state conditions as preconditions
        precondition_operator = self.get_logical_operator(event.get('given', {}))
        postconditions = self.create_state_conditions(event.get('then', {}).get('postconditions', []))
        postcondition_operator = self.get_logical_operator(event.get('then', {}))
        repetition = self.create_repetition(event.get('repetition', None))
        time_period = self.create_time_period(event.get('time_period', None))

        return Event(
            id = event.get('event_number', None),
            name = f"Event{event.get('event_number', None)}",
            action = action,
            preconditions = preconditions,
            precondition_operator = precondition_operator,
            postconditions = postconditions,
            postcondition_operator = postcondition_operator,
            time_period = time_period,
            repetition = repetition

        )
    
    def create_detection(self, detection, events) -> Detection:
        event_id_refs = detection.get('events', [])
        event_refs = [event for event in events if event.id in event_id_refs]
        operator = self.get_logical_operator(detection)

        return Detection(event_refs= event_refs,
               operator= operator)

    def create_technique_model(self, parsed_data) -> TechniqueModel:
        # background + detection
        self.assets = self.build_asset_registry(parsed_data.get('assets', {}))
        event_objects = [self.create_event(event) for event in parsed_data.get('events', [])]
        detection_data = parsed_data.get('detection')
        detection = self.create_detection(detection_data, event_objects) if detection_data else None
        tactics = [Tactic(id=t["tactic_id"], name=t["tactic_name"]) for t in parsed_data.get("tactics", [])]

        return TechniqueModel(
            id=parsed_data.get("technique_id", ""),
            name=parsed_data.get("technique_name", ""),
            tactics=tactics,
            assets=self.assets,
            events=event_objects,
            detection=detection
        )
    
    def translate(self, cnl_input_path: str) -> TechniqueModel:
        # Parse the CNL input using the grammar
        parsed_data = self.parse_input(cnl_input_path)
        visitor = Visitor()
        raw_strings = visitor.visitAttack(parsed_data)
        
        # Convert the parsed data into a TechniqueModel
        technique_model = self.create_technique_model(raw_strings)
        return technique_model