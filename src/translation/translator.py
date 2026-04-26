from antlr4 import FileStream, CommonTokenStream
from src.cnl.grammar.CNLParser import CNLParser
from src.cnl.grammar.CNLLexer import CNLLexer
from src.translation.visitor import Visitor
from src.domain_model.model import TechniqueModel
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

    def translate(self, cnl_input_path: str) -> TechniqueModel:
        # Parse the CNL input using the grammar
        parsed_data = self.parse_input(cnl_input_path)
        visitor = Visitor()
        raw_strings = visitor.visitAttack(parsed_data)
        pprint(raw_strings)

        # Convert the parsed data into a TechniqueModel
        technique_model = self.convert_to_technique_model(raw_strings)
        return technique_model

    def convert_to_technique_model(self, parsed_data) -> TechniqueModel:
        # This is a placeholder implementation. The actual conversion logic will depend on the structure of parsed_data.
        return TechniqueModel(
            id=parsed_data.get('id', 'default_id'),
            name=parsed_data.get('name', 'default_name'),
            tactic=parsed_data.get('tactic', 'default_tactic'),
            tactic_id=parsed_data.get('tactic_id', 'default_tactic_id'),
            events=parsed_data.get('events', [])
        )
    
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
