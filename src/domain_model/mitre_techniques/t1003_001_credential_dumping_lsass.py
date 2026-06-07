from src.domain_model.model import *
from src.domain_model.enums import *
from pprint import pprint



assets = {"lsass": Process(
                asset_type = "process",
                name = "lsass",
                command_line = "lsass.exe",
                signed = True
            ),
            "attacker_process": Process(
                asset_type = "process",
                name = "attacker_process",
                signed = False
            ),
            "lsass_handle": Handle(
                asset_type = "handle",
                name = "lsass_handle",
                hexadecimal_number = "0x1F0FFF"
            ),
            "lsass_memory_dump": File(
                asset_type = "file",
                name = "lsass_memory_dump"
            ),
            "registry": Registry(
                asset_type = "registry",
                name = "registry_keys"
            )
            }

state_conditions = {"lsass_active": StateCondition(
            subject = assets.get('lsass'),
            subject_state = "active",
            modifiers = None
        ),
        "attacker_process_active": StateCondition(
            subject = assets.get('attacker_process'),
            subject_state = "active",
            modifiers = None
        ),
        "lsass_memory_dump_created": StateCondition(
            subject = assets.get('lsass_memory_dump'),
            subject_state = "created",
            modifiers = None
        ),
        "handle_obtained": StateCondition(
            subject = assets.get('lsass_handle'),
            subject_state = "obtained",
            modifiers = [Modifier(
                type = ModifierType.TRIGGER,
                value = assets.get('attacker_process')
            )]
        ),
        "memory_dump_created": StateCondition(
            subject = assets.get('lsass_memory_dump'),
            subject_state = "created",
            modifiers = None
        ),
        "registry_keys_modified": StateCondition(
            subject = assets.get('registry'),
            subject_state = "modified",
            modifiers = None
        )}

events = [
    Event(
        id = "1",
        name = "Event 1",
        action = Action(
            actor = assets.get('attacker_process'),
            action_verb = "requests",
            object = assets.get('lsass_handle'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('attacker_process_active'),  state_conditions.get('lsass_active')],
        precondition_operator = LogicalOperatorType.AND,
        postconditions = [state_conditions.get('handle_obtained')],
        postcondition_operator = None
    ),
    Event(
        id = "2",
        name = "Event 2",
        action = Action(
            actor = assets.get('attacker_process'),
            action_verb = "requests",
            object = assets.get('lsass_memory_dump'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('handle_obtained')],
        precondition_operator = None,
        postconditions = [state_conditions.get('memory_dump_created')],
        postcondition_operator = None
    ),
    Event(
        id = "3",
        name = "Event 3",
        action = Action(
            actor = assets.get('attacker_process'),
            action_verb = "modifies",
            object = assets.get('registry'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('memory_dump_created')],
        precondition_operator = None,          
        postconditions = [state_conditions.get('registry_keys_modified')],
        postcondition_operator = None
    )

]

completion = Completion(
    event_refs= [event for event in events if event.id in ["2", "3"]],
    operator= LogicalOperatorType.XOR
)


lsass_dumping_model = TechniqueModel(
        id= "T1003.001",
        name= "OS_Credential_Dumping_LSASS_Memory",
        tactics= [Tactic(id="TA0006", name="Credential_Access")],
        assets=assets,
        events= events,
        completion= completion
    )

# pprint(lsass_dumping_model)

# from src.petri_net.petri_net_builder import PetriNetBuilder

# petri_net_builder = PetriNetBuilder()
# petri_net_builder.visualize(*petri_net_builder.build(lsass_dumping_model), "domain_lsass_dumping_model")
