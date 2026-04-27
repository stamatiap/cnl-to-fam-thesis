# asset_registry.py
from src.domain_model.model import *

ASSET_TYPE_MAP = {
    "browser": Process,
    "process": Process,
    "file": File,
    "folder": Directory,
    "account": Account,
    "endpoint": Endpoint,
    "session": Session,
    "device": Device,
    "message": Message,
    "credentials": Message,
    "user": Process,
    "registry": File,
    "network_connection": NetworkConnection

}