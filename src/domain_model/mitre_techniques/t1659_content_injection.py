from src.domain_model.model import *
from src.domain_model.enums import *


assets = {
        "browser": Process(
                asset_type= "browser",
                name= "Browser", 
            ),
        "server": Endpoint(
                asset_type = "endpoint",
                name = "some_server"
            ),
        "communication_connection": NetworkConnection(
            asset_type= "network_connection",
            name= "communication_connection",
            source = Process(
                asset_type= "browser",
                name= "Browser", 
            ),
            destination = Endpoint(
                asset_type = "endpoint",
                name = "some_server"
            )
        ),
        "payload": File(
            asset_type= "file",
            name= "PayloadFile",
        ),
        "local_process": Process(
            asset_type = "process",
            name = "local_process"
        ),
        "temp": Directory(
            asset_type = 'directory',
            name="Temp",
            path = "/Temp/"
        ),
        "app_data": Directory(
            asset_type = 'directory',
            name="AppData",
            path = "/%AppData%/"
        )
}

assets["communication_connection"].source = assets.get("browser")
assets["communication_connection"].destination = assets.get("server")

state_conditions = {"connection_active": StateCondition(
        subject = assets.get('communication_connection'),
        subject_state = "active",
        modifiers = None
    ),
    "payload_file_received": StateCondition(
        subject = assets.get('payload'),
        subject_state = "received",
        modifiers = None
    ),
    "local_process_active": StateCondition(
        subject = assets.get('local_process'),
        subject_state = "active",
        modifiers = None
    ),
    "payload_exists_AppData": StateCondition(
        subject = assets.get('payload'),
        subject_state = "exists",
        modifiers = [Modifier(type = ModifierType.LOCATION, value = assets.get('app_data'))]
    ),
    "payload_exists_Temp": StateCondition(
        subject = assets.get('payload'),
        subject_state = "exists",
        modifiers = [Modifier(type = ModifierType.LOCATION, value = assets.get('temp'))]
    ),
    "payload_active": StateCondition(
        subject = assets.get('payload'),
        subject_state = "active",
        modifiers = None
    )
    }

events = [
    Event(
        id = "1",
        name = "Event 1",
        action = Action(
            actor = assets.get('communication_connection').source,
            action_verb = "receives",
            object = assets.get('payload'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('connection_active')],
        precondition_operator = None,
        postconditions = [state_conditions.get('payload_file_received')],
        postcondition_operator = None
    ),
    Event(
        id = "2",
        name = "Event 2",
        action = Action(
            actor = assets.get('communication_connection').source,
            action_verb = "stores",
            object = assets.get('payload'),
            modifiers = [Modifier(type= ModifierType.LOCATION, value=assets.get('app_data'))]
        ),
        preconditions = [state_conditions.get('payload_file_received')],
        precondition_operator = None,
        postconditions = [state_conditions.get('payload_exists_AppData')],
        postcondition_operator = None
    ),
    Event(
        id = "3",
        name = "Event 3",
        action = Action(
            actor = assets.get('communication_connection').source,
            action_verb = "stores",
            object = assets.get('payload'),
            modifiers = [Modifier(type= ModifierType.LOCATION, value=assets.get('temp'))]
        ),
        preconditions = [state_conditions.get('payload_file_received')],
        precondition_operator = None,            
        postconditions = [state_conditions.get('payload_exists_Temp')],
        postcondition_operator = None
    ),
    Event(
        id = "4",
        name = "Event 4",
        action = Action(
            actor = assets.get('local_process'),
            action_verb = "executes",
            object = assets.get('payload'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('payload_exists_AppData'), state_conditions.get('payload_exists_Temp')],
        precondition_operator = LogicalOperatorType.XOR,
        postconditions = [state_conditions.get('payload_active')],
        postcondition_operator = None
    )

]

completion = Completion(
    event_refs= [event for event in events if event.id in ["4"]],
    operator= LogicalOperatorType.XOR
)


content_injection_model = TechniqueModel(
        id= "T1659",
        name= "Content_Injection",
        assets=assets,
        tactics= [Tactic(id="TA0001", name="Initial_Access"), Tactic(id="TA0011", name="Command_and_Control")],
        events= events,
        completion= completion
    )
