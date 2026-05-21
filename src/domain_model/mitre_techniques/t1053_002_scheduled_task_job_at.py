from src.domain_model.model import *
from src.domain_model.enums import *
from pprint import pprint



assets = {"scheduler": Process(
                type = "process",
                name = "at.exe"
            ),
            "at_job": Process(
                type = "job",
                name = "WMI_Win32_ScheduledJob"
            ),
            "scheduled_task": Process(
                type = "process",
                name = "ScheduledTask"
            ),
            "svchost_process": Process(
                type = "process",
                name = "svchost_exe"
            ),
            "taskeng_process": Process(
                type = "process",
                name = "taskeng_exe"
            ),
            "anomalous_process": Process(
                type = "process",
                name = "AnomalousProcess"
            ),
            }

state_conditions = {"scheduler_active": StateCondition(
            subject = assets.get('scheduler'),
            subject_state = "active",
            modifiers = None
        ),
        "at_job_active": StateCondition(
            subject = assets.get('at_job'),
            subject_state = "active",
            modifiers = None
        ),
        "scheduled_task_created": StateCondition(
            subject = assets.get('scheduled_task'),
            subject_state = "created",
            modifiers = None
        ),
        "svchost_process_active": StateCondition(
            subject = assets.get('svchost_process'),
            subject_state = "active",
            modifiers = None
        ),
        "taskeng_process_active": StateCondition(
            subject = assets.get('taskeng_process'),
            subject_state = "active",
            modifiers = None
        ),
        "anomalous_process_active": StateCondition(
            subject = assets.get('anomalous_process'),
            subject_state = "active",
            modifiers = None
        ),
        }

events = [
    Event(
        id = "1",
        name = "Event 1",
        action = Action(
            actor = assets.get('scheduler'),
            action_verb = "creates",
            object = assets.get('scheduled_task'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('scheduler_active')],
        precondition_operators = None,
        postconditions = [state_conditions.get('scheduled_task_created')],
        postcondition_operators = None
    ),
    Event(
        id = "2",
        name = "Event 2",
        action = Action(
            actor = assets.get('at_job'),
            action_verb = "creates",
            object = assets.get('scheduled_task'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('at_job_active')],
        precondition_operators = None,
        postconditions = [state_conditions.get('scheduled_task_created')],
        postcondition_operators = None
    ),
    Event(
        id = "3",
        name = "Event 3",
        action = Action(
            actor = assets.get('svchost_process'),
            action_verb = "executes",
            object = assets.get('anomalous_process'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('scheduled_task_created'), state_conditions.get('svchost_process_active')],
        precondition_operators = [LogicalOperatorType.AND],
        postconditions = [state_conditions.get('anomalous_process_active')],
        postcondition_operators = None
    ),
    Event(
        id = "4",
        name = "Event 4",
        action = Action(
            actor = assets.get('taskeng_process'),
            action_verb = "executes",
            object = assets.get('anomalous_process'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('scheduled_task_created'), state_conditions.get('taskeng_process_active')],
        precondition_operators = [LogicalOperatorType.AND],
        postconditions = [state_conditions.get('anomalous_process_active')],
        postcondition_operators = None
    ),
]

detection = Detection(
    event_refs= [event for event in events if event.id in ["3", "4"]],
    operators= [LogicalOperatorType.XOR]
)


scheduled_task_at_model = TechniqueModel(
        id= "T1053.002",
        name= "Scheduled_Task_Job_At",
        tactics= [Tactic(id="TA0002", name="Execution"), Tactic(id="TA0003", name="Persistence"), Tactic(id="TA0004", name="Privilege_Escalation")],
        events= events,
        detection= detection
    )

# pprint(scheduled_task_at_model)

# from src.petri_net.petri_net_builder import PetriNetBuilder

# petri_net_builder = PetriNetBuilder()
# petri_net_builder.visualize(*petri_net_builder.build(scheduled_task_at_model), "domain_scheduled_task_at_model")
