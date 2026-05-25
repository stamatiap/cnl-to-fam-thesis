# asset_registry.py
from src.domain_model.model import *

ASSET_TYPE_MAP = {
    "browser": Process,
    "process": Process,
    "file": File,
    "account": Account,
    "endpoint": Endpoint,
    "device": Device,
    "message": Message,
    "credentials": Message,
    "user": Process,
    "registry": File,
    "network_connection": NetworkConnection,
    "operating_system": Process,
    "volume": Device,
    "input": Message,
    "driver": Device,
    "server": Endpoint,
    "interface": Device,
    "administrative_account": Account,
    "system_account": Account,
    "authentication_service": Process

}