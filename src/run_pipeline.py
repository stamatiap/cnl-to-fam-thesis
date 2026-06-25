from dataclasses import dataclass, field
from pathlib import Path

from src.translation.translator import Translator
from src.validation.validator import Validator
from src.petri_net.petri_net_builder import PetriNetBuilder
from src.domain_model.mitre_techniques import TECHNIQUE_REGISTRY
from src.monitoring import logger


@dataclass
class PipelineResult:
    translated: bool = False
    cnl_svg_path: Path | None = None
    grammar_errors: list[dict] = field(default_factory=list)
    translation_errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return self.translated and not self.translation_errors

def run_pipeline(input_path, validate: bool = False, build_domain: bool = False, petri_net_dir: Path = "data/generated_petri_nets", 
                 parsed_prefix: str = "parsed_",  domain_prefix: str = "domain_") -> PipelineResult:
    """Run the CNL -> Petri net pipeline on a CNL description file.

    This is where the pipeline is run. Both the CLI (``src.main``) and the 
    Streamlit web app (``web_app.py``) call it.

    input_path:     CNL description file to translate
    validate:       Compare the parsed model against its domain model
    build_domain:   Also build/visualize the domain model's Petri net
    pnml_dir:       Directory for the pnml files produced
    svg_dir:        Directory for the svg files produced
    parsed_prefix:  Filename prefix for the parsed artifacts
    domain_prefix:  Filename prefix for the domain artifacts
    """
    input_path = str(input_path)
    petri_net_dir = Path(petri_net_dir)
    result = PipelineResult()

    # translate CNL text into a TechniqueModel
    logger.info("Translating {}", input_path)
    translator = Translator()
    model = None

    captured_errors: list[str] = []
    sink_id = logger.add(lambda m: captured_errors.append(m.record["message"]), level="ERROR")

    try:
        model = translator.translate(input_path)
    except Exception as e:
        logger.exception("Translation interrupted with error: {} - {}", type(e).__name__, e)
    finally:
        logger.remove(sink_id)

    # get any grammar/syntax errors the parser caught
    result.grammar_errors = list(getattr(translator, "parse_errors", []))
    if not result.grammar_errors:
        result.translation_errors = list(dict.fromkeys(captured_errors))

    if model is None:
        logger.error("Failed translation.")
        return result
    result.translated = True
    logger.info("Successful translation!")

    # fetch matching domain model for validation and buildimg the domain net
    domain_model = None
    if validate or build_domain:
        try:
            domain_model = TECHNIQUE_REGISTRY.get(model.id)
            if domain_model is not None:
                logger.info("Domain model found!")
        except Exception as e:
            logger.exception("Fetching Domain Model interrupted: {} - {}", type(e).__name__, e)

    # validate the parsed model against the domain model
    if validate:
        logger.info("Comparing the structure of Technique Model against Domain Model structure")
        is_valid = False
        try:
            is_valid = Validator().validate_model(model, domain_model)
        except Exception as e:
            logger.exception("Comparison was interrupted: {} - {}", type(e).__name__, e)
        if is_valid:
            logger.info("Successful validation!")
        else:
            logger.error("Failed validation.")

    # build + visualize the Petri net for the parsed model
    builder = PetriNetBuilder()
    logger.info("Building Petri Net of Technique Model")
    cnl_net = None
    try:
        cnl_net = builder.build(model, str(petri_net_dir / f"{parsed_prefix}{model.name}"))
    except Exception as e:
        logger.exception("PN Building was interrupted: {} - {}", type(e).__name__, e)

    if cnl_net is not None:
        try:
            out = petri_net_dir / f"{parsed_prefix}{model.name}"
            builder.visualize(*cnl_net, str(out))
            result.cnl_svg_path = Path(f"{out}.svg")
        except Exception as e:
            logger.exception("Visualization was interrupted: {} - {}", type(e).__name__, e)

    # build + visualize the Petri net for the domain model
    if build_domain and domain_model is not None:
        logger.info("Building Petri Net of Domain Model")
        dom_net = None
        try:
            dom_net = builder.build(domain_model, str(petri_net_dir / f"{domain_prefix}{domain_model.name}"))
        except Exception as e:
            logger.exception("PN Building was interrupted: {} - {}", type(e).__name__, e)

        if dom_net is not None:
            logger.info("Visualizing Petri Net of Domain Model")
            try:
                out = petri_net_dir / f"{domain_prefix}{domain_model.name}"
                builder.visualize(*dom_net, str(out))
                logger.info("Petri net saved to {}.svg", out)
            except Exception as e:
                logger.exception("Visualization was interrupted: {} - {}", type(e).__name__, e)

    return result