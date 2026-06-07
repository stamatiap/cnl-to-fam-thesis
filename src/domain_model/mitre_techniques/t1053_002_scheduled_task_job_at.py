from src.domain_model.model import *
from src.domain_model.enums import *
from pprint import pprint



assets = {"at_exe": Process(
                asset_type = "process",
                name = "at.exe"
            ),
            "WMI_Win32_ScheduledJob": Process(
                asset_type = "process",
                name = "WMI_Win32_ScheduledJob"
            ),
            "anomalous_job": Process(
                asset_type = "process",
                name = "AnomalousJob"
            ),
            "svchost_process": Process(
                asset_type = "process",
                name = "svchost_exe", 
                command_line = "svchost.exe"
            ),
            "taskeng_process": Process(
                asset_type = "process",
                name = "taskeng_exe",
                command_line = "taskeng.exe"
            )
            }

state_conditions = {"at_exe_active": StateCondition(
            subject = assets.get('at_exe'),
            subject_state = "active",
            modifiers = None
        ),
        "WMI_Win32_ScheduledJob_active": StateCondition(
            subject = assets.get('WMI_Win32_ScheduledJob'),
            subject_state = "active",
            modifiers = None
        ),
        "anomalous_job_created": StateCondition(
            subject = assets.get('anomalous_job'),
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
        "anomalous_job_active": StateCondition(
            subject = assets.get('anomalous_job'),
            subject_state = "active",
            modifiers = None
        ),
        }

events = [
    Event(
        id = "1",
        name = "Event 1",
        action = Action(
            actor = assets.get('at_exe'),
            action_verb = "creates",
            object = assets.get('anomalous_job'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('at_exe_active')],
        precondition_operator = None,
        postconditions = [state_conditions.get('anomalous_job_created')],
        postcondition_operator = None
    ),
    Event(
        id = "2",
        name = "Event 2",
        action = Action(
            actor = assets.get('WMI_Win32_ScheduledJob'),
            action_verb = "creates",
            object = assets.get('anomalous_job'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('WMI_Win32_ScheduledJob_active')],
        precondition_operator = None,
        postconditions = [state_conditions.get('anomalous_job_created')],
        postcondition_operator = None
    ),
    Event(
        id = "3",
        name = "Event 3",
        action = Action(
            actor = assets.get('svchost_process'),
            action_verb = "executes",
            object = assets.get('anomalous_job'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('anomalous_job_created'), state_conditions.get('svchost_process_active')],
        precondition_operator = LogicalOperatorType.AND,
        postconditions = [state_conditions.get('anomalous_job_active')],
        postcondition_operator = None
    ),
    Event(
        id = "4",
        name = "Event 4",
        action = Action(
            actor = assets.get('taskeng_process'),
            action_verb = "executes",
            object = assets.get('anomalous_job'),
            modifiers = None
        ),
        preconditions = [state_conditions.get('anomalous_job_created'), state_conditions.get('taskeng_process_active')],
        precondition_operator = LogicalOperatorType.AND,
        postconditions = [state_conditions.get('anomalous_job_active')],
        postcondition_operator = None
    ),
]

completion = Completion(
    event_refs= [event for event in events if event.id in ["3", "4"]],
    operator= LogicalOperatorType.XOR
)


scheduled_task_at_model = TechniqueModel(
        id= "T1053.002",
        name= "Scheduled_Task_Job_At",
        tactics= [Tactic(id="TA0002", name="Execution"), Tactic(id="TA0003", name="Persistence"), Tactic(id="TA0004", name="Privilege_Escalation")],
        assets= assets,
        events= events,
        completion= completion
    )

# pprint(scheduled_task_at_model)

# from src.petri_net.petri_net_builder import PetriNetBuilder

# petri_net_builder = PetriNetBuilder()
# petri_net_builder.visualize(*petri_net_builder.build(scheduled_task_at_model), "domain_scheduled_task_at_model")
