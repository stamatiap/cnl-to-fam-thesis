from antlr4 import FileStream, CommonTokenStream
from src.cnl.grammar.CNLParser import CNLParser
from src.cnl.grammar.CNLLexer import CNLLexer
from src.translation.visitor import Visitor
from src.domain_model.model import *
from src.domain_model.enums import *
from dataclasses import fields
from src.monitoring import logger, LoguruErrorListener, write_artifact
from pathlib import Path

class Translator:

    def parse_input(self, input_path: str) -> dict:
        logger.info("parsing text in {}", input_path)
        input = FileStream(input_path, encoding="utf-8")
        lexer        = CNLLexer(input)
        stream       = CommonTokenStream(lexer)
        parser       = CNLParser(stream)
        self._parser = parser  # ← keep a handle for toStringTree

        listener = LoguruErrorListener(source=input_path)
        parser.removeErrorListeners()
        parser.addErrorListener(listener)
        
        tree = parser.attack()
        if listener.errors:
            logger.warning("skipped {} — {} syntax error(s)", input_path, len(listener.errors))
            return None
        return tree

    def create_modifier(self, modifier) -> Modifier:
        if modifier[0] == 'location':
            mod_type = ModifierType.LOCATION
        elif modifier[0] == 'destination':
            mod_type = ModifierType.DESTINATION
        elif modifier[0] == 'source':
            mod_type = ModifierType.SOURCE
        elif modifier[0] == 'trigger':
            mod_type = ModifierType.TRIGGER
        
        return Modifier(
            type = mod_type,
            value = self.get_asset(modifier[1])
        )
        
    def build_asset_registry(self, assets_dict: dict) -> dict[str, Asset]:
        registry = {}
        
        for name, info in assets_dict.items():
            asset_type_str = info.get("asset_type")
            properties = info.get("properties") or {}
            
            # check if asset type is known
            class_name = self._to_class_name(asset_type_str)
            cls = globals().get(class_name, Asset)
            
            # in case of "other" warn about generic Asset being used
            if cls == Asset and class_name != "Asset":
                logger.warning(f"Unknown asset type '{asset_type_str}' for asset '{name}' — will be treated as generic Asset.")
            
            # validate properties
            valid_fields = {f.name for f in fields(cls)} - {'asset_type', 'name', 'asset_id'}
            field_types = {f.name: f.type for f in fields(cls)}

            extra = {}
            for k,v in properties.items():
                if k not in valid_fields:
                    continue
                clean_name = v.replace("'", "").replace('"', "") # remove quotes from property values
                t = field_types[k]
                if t is bool:
                    if clean_name.lower() == "true":
                        clean_name = True
                    elif clean_name.lower() == "false":
                        clean_name = False
                    else:
                        logger.warning("Expected bool for {!r} on asset {!r}, got {!r}", k, name, clean_name)
                        clean_name = None
                
                if t is int:
                    try:
                        clean_name = int(clean_name)
                    except ValueError:
                        logger.warning("Expected int for {!r} on asset {!r}, got {!r}", k, name, clean_name)
                        clean_name = None
                
                extra[k] = clean_name

            
            # create objects for Asset types that have other Assets as properties and add to registry
            if asset_type_str == "network_connection":
                if "source" in properties.keys():
                    extra["source"] = Process(asset_type='process', name=properties['source'].replace("'", "").replace('"', ""))
                    registry[extra["source"].name] = extra["source"]
                if "destination" in properties.keys():
                    extra["destination"] = Endpoint(asset_type='endpoint', name=properties['destination'].replace("'", "").replace('"', ""))
                    registry[extra["destination"].name] = extra["destination"]
            elif asset_type_str == "process":
                if "parent_process" in properties.keys():
                    extra["parent_process"] = Process(asset_type="process", name=properties['parent_process'].replace("'", "").replace('"', ""))
                    registry[extra["parent_process"].name] = extra["parent_process"]
            elif asset_type_str == "handle":
                if "target" in properties.keys():
                    target_name = properties['target'].replace("'", "").replace('"', "")
                    # target asset must be declared beforehand
                    if target_name in registry:
                        extra["target"] = registry[target_name]
                    else:
                        logger.error(
                            f"Handle '{name}' references target '{target_name}', which "
                            f"is not declared, or is declared after the handle in the Background."
                        )

            # warn on invalid properties
            for k, v in properties.items(): 
                if k not in valid_fields:
                    if cls != Asset:
                        # only raise for known types
                        logger.error(f"Property '{k}' not a field of {asset_type_str}. Available fields: {valid_fields}")
                    else:
                        # for unknown types, just warn
                        logger.warning(f"Property '{k}' on unknown asset type '{asset_type_str}' — will be ignored")
            
            registry[name] = cls(asset_type=asset_type_str, name=name, **extra)
        
        return registry
    
    def _to_class_name(self, asset_type_str: str) -> str:
        # in case of "network_connection" -> "NetworkConnection"
        parts = asset_type_str.split('_')
        return ''.join(word.capitalize() for word in parts)

    def get_asset(self, asset_name: str) -> Asset:
        asset = self.assets.get(asset_name)
        if asset is None:
            logger.error(f"Asset '{asset_name}' referenced but not declared in Background")
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
            time_value = int(repetition_item[1]) if repetition_item[1] is not None else None,
            time_unit = TIME_UNIT_MAP.get(repetition_item[2], None),
        )
        
    def create_time_period(self, time_period_item) -> TimePeriod | None:
        if time_period_item is None:
            return None
        
        try:
            preposition = TimePeriodPreposition(time_period_item[0].lower())
        except ValueError:
            logger.warning("unknown time period preposition {!r}", time_period_item[0])
            preposition = None
        
        return TimePeriod(preposition=preposition, time_period=time_period_item[1])

    def get_logical_operator(self, clause: dict) -> LogicalOperatorType | None:
        op = clause.get('operator', None)

        if op is not None:
            try: 
                operator = LogicalOperatorType(op.upper())
            except ValueError:
                logger.warning("unknown logical operator {!r}, treating as None", op)
                operator = None
        else: 
            operator = None

        return operator

    def create_event(self, event) -> Event:
        action = self.create_action(event.get('when', {}))
        preconditions = self.create_state_conditions(event.get('given', {}).get('preconditions', []))  # expecting only state conditions as preconditions
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
    
    def create_completion(self, completion, events) -> Completion:
        event_id_refs = completion.get('events', [])
        event_refs = [event for event in events if event.id in event_id_refs]
        operator = self.get_logical_operator(completion)

        return Completion(event_refs= event_refs,
               operator= operator)

    def create_technique_model(self, parsed_data) -> TechniqueModel:
        # background + completion
        self.assets = self.build_asset_registry(parsed_data.get('assets', {}))
        event_objects = [self.create_event(event) for event in parsed_data.get('events', [])]
        completion_data = parsed_data.get('completion')
        completion = self.create_completion(completion_data, event_objects) if completion_data else None
        tactics = [Tactic(id=t["tactic_id"], name=t["tactic_name"]) for t in parsed_data.get("tactics", [])]

        return TechniqueModel(
            id=parsed_data.get("technique_id", ""),
            name=parsed_data.get("technique_name", ""),
            tactics=tactics,
            assets=self.assets,
            events=event_objects,
            completion=completion
        )
    
    def translate(self, cnl_input_path: str) -> TechniqueModel:
        # Parse the CNL input using the grammar
        parsed_data = self.parse_input(cnl_input_path)
        if parsed_data is None:
            logger.error("failed parsing.")
            return None

        logger.info("Visiting parsed text.")
        visitor = Visitor()
        raw_strings = visitor.visitAttack(parsed_data)
        
        # Convert the parsed data into a TechniqueModel
        technique_model = self.create_technique_model(raw_strings)
        # Save TechniqueModel
        out = Path("data/parsed_cnl_models") / f"{technique_model.id.replace(".", "_")}_cnl_{technique_model.name}.json"
        write_artifact(technique_model, out)
        
        logger.info("translated {}: {} assets, {} events. Saved in {}",
                    technique_model.id, len(technique_model.assets), len(technique_model.events), out)
        
        return technique_model