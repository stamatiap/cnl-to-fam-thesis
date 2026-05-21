from src.domain_model.model import *
from src.domain_model.enums import *
from pprint import pprint


assets = {"communication_connection": NetworkConnection(
                type= "network_connection",
                name= "communication_connection",
                source = Process(
                    type= "browser",
                    name= "Browser", 
                ),
                destination = Endpoint(
                    type = "server",
                    name = "some_server"
                ),
                status = "active"
            ),
            "payload": File(
                type= "file",
                name= "PayloadFile"
            ),
            "%AppData%": Directory(type = "folder",
                                name = "AppData"),
            "Temp": Directory(type = "folder",
                            name = "Temp"),
            "local_process": Process(
                type = "process",
                name = "local_process"
            )
            }

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
        modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('%AppData%'))]
    ),
    "payload_exists_Temp": StateCondition(
        subject = assets.get('payload'),
        subject_state = "exists",
        modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('Temp'))]
    ),
    "payload_active": StateCondition(
        subject = assets.get('payload'),
        subject_state = "active",
        modifiers = None
    )}

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
        precondition_operators = None,
        postconditions = [state_conditions.get('payload_file_received'), state_conditions.get('connection_active')],
        postcondition_operators = [LogicalOperatorType.AND]
    ),
    Event(
        id = "2",
        name = "Event 2",
        action = Action(
            actor = assets.get('communication_connection').source,
            action_verb = "stores",
            object = assets.get('payload'),
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('%AppData%'))]
        ),
        preconditions = [state_conditions.get('connection_active'), state_conditions.get('payload_file_received')],
        precondition_operators = [LogicalOperatorType.AND],
        postconditions = [state_conditions.get('payload_exists_AppData'), state_conditions.get('connection_active')],
        postcondition_operators = [LogicalOperatorType.AND]
    ),
    Event(
        id = "3",
        name = "Event 3",
        action = Action(
            actor = assets.get('communication_connection').source,
            action_verb = "stores",
            object = assets.get('payload'),
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('Temp'))]
        ),
        preconditions = [state_conditions.get('connection_active'), state_conditions.get('payload_file_received')],
        precondition_operators = [LogicalOperatorType.AND],            
        postconditions = [state_conditions.get('payload_exists_Temp'), state_conditions.get('connection_active')],
        postcondition_operators = [LogicalOperatorType.AND]
    ),
    Event(
        id = "4",
        name = "Event 4",
        action = Action(
            actor = assets.get('local_process'),
            action_verb = "executes",
            object = assets.get('payload'),
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('%AppData%'))]
        ),
        preconditions = [state_conditions.get('local_process_active'), state_conditions.get('payload_exists_AppData')],
        precondition_operators = [LogicalOperatorType.AND],
        postconditions = [state_conditions.get('payload_active')],
        postcondition_operators = None
    ),
    Event(
        id = "5",
        name = "Event 5",
        action = Action(
            actor = assets.get('local_process'),
            action_verb = "executes",
            object = assets.get('payload'),
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('Temp'))]
        ),
        preconditions = [state_conditions.get('local_process_active'), state_conditions.get('payload_exists_Temp')],
        precondition_operators = [LogicalOperatorType.AND],
        postconditions = [state_conditions.get('payload_active')],
        postcondition_operators = None
    ),
    Event(
        id = "6",
        name = "Event 6",
        action = Action(
            actor = assets.get('communication_connection').source,
            action_verb = "spawns",
            object = assets.get('local_process'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('connection_active')],
        precondition_operators = None,
        postconditions = [state_conditions.get('local_process_active'), state_conditions.get('connection_active')],
        postcondition_operators = [LogicalOperatorType.AND]
    )

]

detection = Detection(
    event_refs= [event for event in events if event.id in ["4", "5"]],
    operators= [LogicalOperatorType.XOR]
)


content_injection_model = TechniqueModel(
        id= "T1659",
        name= "Content Injection",
        tactics= [Tactic(id="TA0001", name="Initial Access"), Tactic(id="TA0011", name="Command and Control")],
        events= events,
        detection= detection
    )

# pprint(content_injection_model)

# from src.petri_net.petri_net_builder import PetriNetBuilder

# petri_net_builder = PetriNetBuilder()
# petri_net_builder.visualize(*petri_net_builder.build(content_injection_model), "domain_content_injection_model")

