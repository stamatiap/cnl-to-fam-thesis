from src.translation.translator import Translator
from src.translation.validator import Validator
from src.petri_net.petri_net_builder import PetriNetBuilder
import sys
from pprint import pprint


def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_description.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    input_path = "data/example_descriptions/" + input_file
    translator = Translator()
    model = translator.translate(input_path)
    pprint(model)

    validator = Validator()
    is_valid = validator.validate_model(model)
    print(is_valid)


if __name__ == "__main__":
    main()