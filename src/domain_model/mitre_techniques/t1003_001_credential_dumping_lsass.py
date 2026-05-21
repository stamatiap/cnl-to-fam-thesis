from src.domain_model.model import *
from src.domain_model.enums import *
from pprint import pprint



assets = {"user": Account(
                type = "user",
                name = "User",
                access_level = "Low"
            ),
            "authentication": Process(
                type = "authentication",
                name = "authentication_process"
            ),
            "lsass": Process(
                type = "process",
                name = "lsass_exe"
            ),
            "credentials":  Message(
                type = "credentials",
                name = "credentials",
                data = ["username", "password"]
            ),
            "administrator": Account(
                type = "process",
                name = "Administrator",
                access_level = "High"
            ),
            "system_user": Account(
                type = "process",
                name = "SYSTEM_User",
                access_level = "High"
            ),
            "lsass_memory": File(
                type = "file",
                name = "lsass_memory"
            ),
            "memory_dump": File(
                type = "file",
                name = "Memory_dump"
            ),
            "registry_keys": File(
                type = "registry",
                name = "Registry_Keys"
            )
            }

state_conditions = {"authentication_active": StateCondition(
            subject = assets.get('authentication'),
            subject_state = "active",
            modifiers = None
        ),
        "user_active": StateCondition(
            subject = assets.get('user'),
            subject_state = "active",
            modifiers = None
        ),
        "lsass_active": StateCondition(
            subject = assets.get('lsass'),
            subject_state = "active",
            modifiers = None
        ),
        "credentials_stored": StateCondition(
            subject = assets.get('credentials'),
            subject_state = "stored",
            modifiers = [Modifier(
                type = ModifierType.LOCATION, 
                value = assets.get("lsass_memory")
            )]
        ),
        "administrator_active": StateCondition(
            subject = assets.get('administrator'),
            subject_state = "active",
            modifiers = None
        ),
        "system_user_active": StateCondition(
            subject = assets.get('system_user'),
            subject_state = "active",
            modifiers = None
        ),
        "system_user_lsass_access": StateCondition(
            subject = assets.get('system_user'),
            subject_state = "has_access",
            modifiers = [Modifier(
                type = ModifierType.DESTINATION,
                value = assets.get('lsass_memory')
            )]
        ),
        "administrator_lsass_access": StateCondition(
            subject = assets.get('administrator'),
            subject_state = "has_access",
            modifiers = [Modifier(
                type = ModifierType.DESTINATION,
                value = assets.get('lsass_memory')
            )]
        ),
        "memory_dump_exists": StateCondition(
            subject = assets.get('memory_dump'),
            subject_state = "exists",
            modifiers = None
        ),
        "registry_keys_exists": StateCondition(
            subject = assets.get('registry_keys'),
            subject_state = "exists",
            modifiers = None
        ),
        "registry_keys_modified": StateCondition(
            subject = assets.get('registry_keys'),
            subject_state = "modified",
            modifiers = None
        )}

events = [
    Event(
        id = "1",
        name = "Event 1",
        action = Action(
            actor = assets.get('user'),
            action_verb = "sends",
            object = assets.get('credentials'),
            modifiers = [Modifier(type = ModifierType.DESTINATION, value= assets.get('authentication'))]
        ),
        preconditions = [state_conditions.get('authentication_active')],
        precondition_operators = None,
        postconditions = [state_conditions.get('user_active')],
        postcondition_operators = None
    ),
    Event(
        id = "2",
        name = "Event 2",
        action = Action(
            actor = assets.get('lsass'),
            action_verb = "stores",
            object = assets.get('credentials'),
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('lsass_memory'))]
        ),
        preconditions = [state_conditions.get('lsass_active'), state_conditions.get('user_active')],
        precondition_operators = [LogicalOperatorType.AND],
        postconditions = [state_conditions.get('credentials_stored')],
        postcondition_operators = None
    ),
    Event(
        id = "3",
        name = "Event 3",
        action = Action(
            actor = assets.get('administrator'),
            action_verb = "creates",
            object = assets.get('memory_dump'),
            modifiers = [Modifier(
                type = ModifierType.SOURCE_FROM,
                value = assets.get('lsass_memory'))]
        ),
        preconditions = [state_conditions.get('administrator_active'), state_conditions.get('administrator_lsass_access'), state_conditions.get('credentials_stored')],
        precondition_operators = [LogicalOperatorType.AND],            
        postconditions = [state_conditions.get('memory_dump_exists'), state_conditions.get('administrator_active')],
        postcondition_operators = [LogicalOperatorType.AND]
    ),
    Event(
        id = "4",
        name = "Event 4",
        action = Action(
            actor = assets.get('system_user'),
            action_verb = "creates",
            object = assets.get('memory_dump'),
            modifiers = [Modifier(
                type = ModifierType.SOURCE_FROM,
                value = assets.get('lsass_memory'))]
        ),
        preconditions = [state_conditions.get('system_user_active'), state_conditions.get('system_user_lsass_access'), state_conditions.get('credentials_stored')],
        precondition_operators = [LogicalOperatorType.AND],            
        postconditions = [state_conditions.get('memory_dump_exists'), state_conditions.get('system_user_active')],
        postcondition_operators = [LogicalOperatorType.AND]
    ),
    Event(
        id = "5",
        name = "Event 5",
        action = Action(
            actor = assets.get('administrator'),
            action_verb = "modifies",
            object = assets.get('registry_keys'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('memory_dump_exists'),  state_conditions.get('registry_keys_exists'), state_conditions.get('administrator_active')],
        precondition_operators = [LogicalOperatorType.AND],            
        postconditions = [state_conditions.get('registry_keys_modified')],
        postcondition_operators = None
    ),
    Event(
        id = "6",
        name = "Event 6",
        action = Action(
            actor = assets.get('system_user'),
            action_verb = "modifies",
            object = assets.get('registry_keys'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('memory_dump_exists'), state_conditions.get('registry_keys_exists'), state_conditions.get('system_user_active')],
        precondition_operators = [LogicalOperatorType.AND],            
        postconditions = [state_conditions.get('registry_keys_modified')],
        postcondition_operators = None
    ),

]

detection = Detection(
    event_refs= [event for event in events if event.id in ["3", "4", "5", "6"]],
    operators= [LogicalOperatorType.XOR]
)


lsass_dumping_model = TechniqueModel(
        id= "T1003.001",
        name= "OS_Credential_Dumping_LSASS_Memory",
        tactics= [Tactic(id="TA0006", name="Credential_Access")],
        events= events,
        detection= detection
    )

# pprint(lsass_dumping_model)

# from src.petri_net.petri_net_builder import PetriNetBuilder

# petri_net_builder = PetriNetBuilder()
# petri_net_builder.visualize(*petri_net_builder.build(lsass_dumping_model), "domain_lsass_dumping_model")
