from src.domain_model.model import *
from src.domain_model.enums import *
from pprint import pprint


assets = {"communication_connection": NetworkConnection(
                asset_type= "network_connection",
                name= "communication_connection",
                source = Process(
                    asset_type= "browser",
                    name= "Browser", 
                ),
                destination = Endpoint(
                    asset_type = "server",
                    name = "some_server"
                )
            ),
            "payload-1": File(
                asset_type= "file",
                name= "PayloadFile",
                path = "/%AppData%/"
            ),
            "payload-2": File(
                asset_type= "file",
                name= "PayloadFile",
                path = "/Temp/"
            ),
            "local_process": Process(
                asset_type = "process",
                name = "local_process"
            )
            }

state_conditions = {"connection_active": StateCondition(
        subject = assets.get('communication_connection'),
        subject_state = "active",
        modifiers = None
    ),
    "payload1_file_received": StateCondition(
        subject = assets.get('payload-1'),
        subject_state = "received",
        modifiers = None
    ),
    "payload2_file_received": StateCondition(
        subject = assets.get('payload-2'),
        subject_state = "received",
        modifiers = None
    ),
    "local_process_active": StateCondition(
        subject = assets.get('local_process'),
        subject_state = "active",
        modifiers = None
    ),
    "payload_exists_AppData": StateCondition(
        subject = assets.get('payload-1'),
        subject_state = "exists",
        modifiers = None
    ),
    "payload_exists_Temp": StateCondition(
        subject = assets.get('payload-2'),
        subject_state = "exists",
        modifiers = None
    ),
    "payload_1_active": StateCondition(
        subject = assets.get('payload-1'),
        subject_state = "active",
        modifiers = None
    ),
    "payload_2_active": StateCondition(
        subject = assets.get('payload-2'),
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
            object = assets.get('payload-1'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('connection_active')],
        precondition_operator = None,
        postconditions = [state_conditions.get('payload1_file_received'), state_conditions.get('connection_active')],
        postcondition_operator = LogicalOperatorType.AND
    ),
    Event(
        id = "2",
        name = "Event 2",
        action = Action(
            actor = assets.get('communication_connection').source,
            action_verb = "receives",
            object = assets.get('payload-2'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('connection_active')],
        precondition_operator = None,
        postconditions = [state_conditions.get('payload2_file_received'), state_conditions.get('connection_active')],
        postcondition_operator = LogicalOperatorType.AND
    ),
    Event(
        id = "3",
        name = "Event 3",
        action = Action(
            actor = assets.get('communication_connection').source,
            action_verb = "stores",
            object = assets.get('payload-1'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('connection_active'), state_conditions.get('payload1_file_received')],
        precondition_operator = LogicalOperatorType.AND,
        postconditions = [state_conditions.get('payload_exists_AppData'), state_conditions.get('connection_active')],
        postcondition_operator = LogicalOperatorType.AND
    ),
    Event(
        id = "4",
        name = "Event 4",
        action = Action(
            actor = assets.get('communication_connection').source,
            action_verb = "stores",
            object = assets.get('payload-2'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('connection_active'), state_conditions.get('payload2_file_received')],
        precondition_operator = LogicalOperatorType.AND,            
        postconditions = [state_conditions.get('payload_exists_Temp'), state_conditions.get('connection_active')],
        postcondition_operator = LogicalOperatorType.AND
    ),
    Event(
        id = "5",
        name = "Event 5",
        action = Action(
            actor = assets.get('communication_connection').source,
            action_verb = "spawns",
            object = assets.get('local_process'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('connection_active')],
        precondition_operator = None,
        postconditions = [state_conditions.get('local_process_active'), state_conditions.get('connection_active')],
        postcondition_operator = LogicalOperatorType.AND
    ),
    Event(
        id = "6",
        name = "Event 6",
        action = Action(
            actor = assets.get('local_process'),
            action_verb = "executes",
            object = assets.get('payload-1'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('local_process_active'), state_conditions.get('payload_exists_AppData')],
        precondition_operator = [LogicalOperatorType.AND],
        postconditions = [state_conditions.get('payload_1_active')],
        postcondition_operator = None
    ),
    Event(
        id = "7",
        name = "Event 7",
        action = Action(
            actor = assets.get('local_process'),
            action_verb = "executes",
            object = assets.get('payload-2'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('local_process_active'), state_conditions.get('payload_exists_Temp')],
        precondition_operator = LogicalOperatorType.AND,
        postconditions = [state_conditions.get('payload_2_active')],
        postcondition_operator = None
    )

]

detection = Detection(
    event_refs= [event for event in events if event.id in ["6", "7"]],
    operator= LogicalOperatorType.XOR
)


content_injection_model = TechniqueModel(
        id= "T1659",
        name= "Content Injection",
        assets=assets,
        tactics= [Tactic(id="TA0001", name="Initial Access"), Tactic(id="TA0011", name="Command and Control")],
        events= events,
        detection= detection
    )

pprint(content_injection_model)

# from src.petri_net.petri_net_builder import PetriNetBuilder

# petri_net_builder = PetriNetBuilder()
# petri_net_builder.visualize(*petri_net_builder.build(content_injection_model), "domain_content_injection_model")

