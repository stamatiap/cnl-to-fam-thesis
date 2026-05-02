from antlr4 import FileStream, CommonTokenStream
from src.cnl.grammar.CNLParser import CNLParser
from src.cnl.grammar.CNLLexer import CNLLexer
from src.translation.visitor import Visitor
from src.domain_model.model import *
from src.domain_model.enums import *
from src.domain_model.asset_registry import ASSET_TYPE_MAP
import sys
from pprint import pprint


class Translator:

    def parse_input(self, input_path: str) -> dict:
        input = FileStream(input_path, encoding="utf-8")
        lexer        = CNLLexer(input)
        stream       = CommonTokenStream(lexer)
        parser       = CNLParser(stream)
        tree         = parser.attack()
        print(tree.toStringTree(recog=parser))
        return tree

    def create_modifier(self, modifier) -> Modifier:
        if modifier[0] == 'location':
            mod_type = ModifierType.LOCATION
        elif modifier[0] == 'destination':
            mod_type = ModifierType.DESTINATION
        elif modifier[0] == 'source_by':
            mod_type = ModifierType.SOURCE_BY
        elif modifier[0] == 'source_from':
            mod_type = ModifierType.SOURCE_FROM
        
        return Modifier(
            type = mod_type,
            value = self.create_asset(modifier[1])
        )

    def create_asset(self, asset_name: str) -> Asset:
        asset_type_str = self.assets.get(asset_name, None)
        cls = ASSET_TYPE_MAP.get(asset_type_str.lower(), Asset)
        return cls(type=asset_type_str, name=asset_name)

    def create_state_conditions(self, conditions: list) -> list[StateCondition]:
        return [self.create_state_condition(c) for c in conditions]

    def create_state_condition(self, condition: dict) -> StateCondition:
        subject = self.create_asset(condition["object"])
        modifiers = [self.create_modifier(m) for m in condition.get("modifiers", [])]
        return StateCondition(
            subject=subject,
            subject_state=condition["verb"],
            modifiers=modifiers
        )

    def create_action(self, action) -> Action:
        actor = self.create_asset(action.get('actor', None))
        object = self.create_asset(action.get('object', None))
        modifiers = [self.create_modifier(m) for m in action.get('modifiers', [])]
        return Action(
            action_verb = action.get('action_verb', None),
            actor = actor,
            object = object,
            modifiers= modifiers
        )
    
    def get_logical_operators(self, clause: dict) -> list:
        op_refs = clause.get('operators', [])
        operators = []
        for op in op_refs:
            if op == LogicalOperatorType.AND.value:
                operators.append(LogicalOperatorType.AND)
            elif op == LogicalOperatorType.OR.value:
                operators.append(LogicalOperatorType.OR)
            else:
                operators.append(None)

        return operators


    def create_event(self, event) -> Event:
        action = self.create_action(event.get('when', {}))
        preconditions = self.create_state_conditions(event.get('given', {}).get('preconditions', []))
        precondition_operators = self.get_logical_operators(event.get('given', {}))
        postconditions = self.create_state_conditions(event.get('then', {}).get('postconditions', []))
        postcondition_operators = self.get_logical_operators(event.get('then', {}))

        return Event(
            id = event.get('event_number', None),
            name = "Event" + event.get('event_number', None),
            action = action,
            preconditions = preconditions,
            precondition_operators = precondition_operators,
            postconditions = postconditions,
            postcondition_operators = postcondition_operators,

        )
    
    def create_detection(self, detection, events) -> Detection:
        event_id_refs = detection.get('events', [])
        event_refs = [event for event in events if event.id in event_id_refs]
        operators = self.get_logical_operators(detection)

        return{'event_refs': event_refs,
               'operators': operators}

    def create_technique_model(self, parsed_data) -> TechniqueModel:
        # background + detection
        self.assets = parsed_data.get('assets', {})
        event_objects = [self.create_event(event) for event in parsed_data.get('events', [])]
        detection = self.create_detection(parsed_data.get('detection', []), event_objects)
        return TechniqueModel(
            id=parsed_data.get("technique_id", ""),
            name=parsed_data.get("technique_name", ""),
            tactic=parsed_data.get("tactic_name", ""),
            tactic_id=parsed_data.get("tactic_id", ""),
            events= event_objects,
            detection=detection
        )
    
    def translate(self, cnl_input_path: str) -> TechniqueModel:
        # Parse the CNL input using the grammar
        parsed_data = self.parse_input(cnl_input_path)
        visitor = Visitor()
        raw_strings = visitor.visitAttack(parsed_data)
        pprint(raw_strings)

        # Convert the parsed data into a TechniqueModel
        technique_model = self.create_technique_model(raw_strings)
        return technique_model
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_description.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    input_path = "data/example_descriptions/" + input_file
    translator = Translator()
    model = translator.translate(input_path)
    pprint(model)

if __name__ == "__main__":
    main()
