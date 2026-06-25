from src.monitoring import setup_logging
from src.run_pipeline import run_pipeline
import sys
import argparse


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Translate a single input file.")
    parser.add_argument("input_file", help="Name of the file in data/example_descriptions/ to translate.",)
    parser.add_argument("--validate", action="store_true", help="Perform validation step.",)
    parser.add_argument("--build_domain", action="store_true", help="Build corresponding domain model, if it exists")
    args = parser.parse_args()

    input_path = "data/example_descriptions/" + args.input_file

    result = run_pipeline(input_path, validate=args.validate, build_domain=args.build_domain)
    if not result.ok:
        sys.exit(1)


if __name__ == "__main__":
    main()