from src.domain_model.model import TechniqueModel
from .t1659_content_injection import content_injection_model
from .t1003_001_credential_dumping_lsass import lsass_dumping_model
from .t1053_002_scheduled_task_job_at import scheduled_task_at_model
from .t1110_001_password_guessing import password_guessing_model

TECHNIQUE_REGISTRY: dict[str, TechniqueModel] = {
    "T1659": content_injection_model,
    "T1003.001": lsass_dumping_model,
    "T1053.002": scheduled_task_at_model,
    "T1110.001": password_guessing_model
}