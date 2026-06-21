from src.translation.translator import Translator
from src.validation.validator import Validator
from src.petri_net.petri_net_builder import PetriNetBuilder
from src.domain_model.mitre_techniques import TECHNIQUE_REGISTRY
from src.monitoring import setup_logging, logger
import sys


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
    logger.info("Translating {}", input_path)
    model = None
    try:
        translator = Translator()
        model = translator.translate(input_path)
    except Exception as e:
        logger.exception("Translation interrupted with error: {} - {}", type(e).__name__, e)

    if model is None:
        logger.error("Failed translation.")
    else:
        logger.info("Successful translation!")
        
        # simple validation on the model structure
        logger.info("Comparing the structure of Technique Model against Domain Model structure")
        domain_model = None
        try:
            domain_model = TECHNIQUE_REGISTRY.get(model.id)
            logger.info("Domain model found!")
        except Exception as e:
            logger.exception("Fetching Domain Model interrupted: {} - {}", type(e).__name__, e)

        is_valid = False
        try:
            validator = Validator()
            is_valid = validator.validate_model(model, domain_model)
        except Exception as e:
            logger.exception("Comparison was interrupted: {} - {}", type(e).__name__, e)
        
        if not is_valid:
            logger.error("Failed validation.")
        else:
            logger.info("Successful validation!")

        # CNL Model Petri Net Build and Visualization
        logger.info("Buidling Petri Net of Technique Model")
        cnl_petri_net = None
        petri_net_builder = PetriNetBuilder()
        try:
            output_path = "data/petri_net_models/parsed_" + model.name
            cnl_petri_net = petri_net_builder.build(model, output_path)
        except Exception as e:
            logger.exception("PN Building was interrupted: {} - {}", type(e).__name__, e)

        if cnl_petri_net is not None:
            try:
                output_path = f"./data/generated_petri_nets/parsed_{model.name}"
                petri_net_builder.visualize(*cnl_petri_net, output_path)
            except Exception as e:
                logger.exception("Visualization was interrupted: {} - {}", type(e).__name__, e)

        if domain_model is not None:
            # Domain Model Petri Net Build and Visualization
            logger.info("Buidling Petri Net of Domain Model")
            try:
                output_path = "data/petri_net_models/domain_" + domain_model.name
                dom_petri_net = petri_net_builder.build(domain_model, output_path)
            except Exception as e:
                logger.exception("PN Building was interrupted: {} - {}", type(e).__name__, e)

            if dom_petri_net:
                logger.info("Visualizing Petri Net of Domain Model")
                try:
                    output_path = f"./data/generated_petri_nets/domain_{domain_model.name}"
                    petri_net_builder.visualize(*dom_petri_net, output_path)
                    logger.info("Petri net saved to {}.svg", output_path)
                except Exception as e:
                    logger.exception("Visualization was interrupted: {} - {}", type(e).__name__, e)


if __name__ == "__main__":
    main()