from src.monitoring import setup_logging, logger
import sys
from src.run_pipeline import run_pipeline


def main():
    setup_logging()

    if len(sys.argv) < 2:
        logger.error("Usage: python -m src.main <input_file>")
        sys.exit(1)
    elif len(sys.argv) > 2:
        logger.error("Too many parameters used! Only one file can be translated at a time.")
        logger.warning("First input file used: {}", sys.argv[1])

    input_file = sys.argv[1]
    input_path = "data/example_descriptions/" + input_file

    result = run_pipeline(input_path)
    if not result.ok:
        sys.exit(1)


if __name__ == "__main__":
    main()