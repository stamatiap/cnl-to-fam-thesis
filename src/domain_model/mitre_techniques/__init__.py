# techniques/__init__.py
from src.domain_model.model import TechniqueModel
from .t1659_content_injection import content_injection_model

TECHNIQUE_REGISTRY: dict[str, TechniqueModel] = {
    "T1659": content_injection_model
}