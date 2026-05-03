from src.domain_model.model import *
from src.domain_model.enums import *


assets = {"browserA": Process(
                type= "browser",
                name= "browserA",
                process_id = "some process_id",
                status = "active"
            ),
            "processB": Process(
                type= "process",
                name= "processB"
            ),
            "payload":  File(
                type= "file",
                name= "fileC"
            ),
            "%AppData%": Directory(type = "folder",
                                    name = "AppData"),
            "Temp": Directory(type = "folder",
                                    name = "Temp"),
            }

events = [
    Event(
        id = "1",
        name = "Event 1",
        action = Action(
            action_verb = "spawns",
            actor = assets.get('browserA'),
            object = assets.get('processB'),
            modifiers = None
        ),
        preconditions = [StateCondition(
            subject = assets.get('browserA'),
            subject_state = "active",
            modifiers = None
        )],
        precondition_operators = None,
        postconditions = [StateCondition(
            subject = assets.get('processB'),
            subject_state = "spawned",
            modifiers = None
        ), StateCondition(
            subject = assets.get('processB'),
            subject_state = "active",
            modifiers = None
        )],
        postcondition_operators = None
    ),
    Event(
        id = "2",
        name = "Event 2",
        action = Action(
            action_verb = "creates",
            actor = assets.get('processB'),
            object = assets.get('payload'),
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('%AppData%'))]
        ),
        preconditions = [StateCondition(
            subject = assets.get('processB'),
            subject_state = "active",
            modifiers = None
        )],
        precondition_operators = None,
        postconditions = [StateCondition(
            subject = assets.get('payload'),
            subject_state = "exists",
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('%AppData%'))]
        )],
        postcondition_operators = None
    ),
    Event(
        id = "3",
        name = "Event 3",
        action = Action(
            action_verb = "creates",
            actor = assets.get('processB'),
            object = assets.get('payload'),
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('Temp'))]
        ),
        preconditions = [StateCondition(
            subject = assets.get('processB'),
            subject_state = "active",
            modifiers = None
        )],
        precondition_operators = None,            
        postconditions = [StateCondition(
            subject = assets.get('payload'),
            subject_state = "exists",
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('Temp'))]
        )],
        postcondition_operators = None
    ),
    Event(
        id = "4",
        name = "Event 4",
        action = Action(
            action_verb = "executes",
            actor = assets.get('processB'),
            object = assets.get('payload'),
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('%AppData%'))]
        ),
        preconditions = [StateCondition(
            subject = assets.get('processB'),
            subject_state = "active",
            modifiers = None
        ), StateCondition(
            subject = assets.get('payload'),
            subject_state = "exists",
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('%AppData%'))]
        )],
        precondition_operators = [LogicalOperatorType.AND],
        postconditions = [StateCondition(
            subject = assets.get('payload'),
            subject_state = "active",
            modifiers = None
        )],
        postcondition_operators = None
    ),
    Event(
        id = "5",
        name = "Event 5",
        action = Action(
            action_verb = "executes",
            actor = assets.get('processB'),
            object = assets.get('payload'),
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('Temp'))]
        ),
        preconditions = [StateCondition(
            subject = assets.get('processB'),
            subject_state = "active",
            modifiers = None
        ), StateCondition(
            subject = assets.get('payload'),
            subject_state = "exists",
            modifiers = [Modifier(
                type = ModifierType.LOCATION,
                value = assets.get('Temp'))]
        )],
        precondition_operators = [LogicalOperatorType.AND],
        postconditions = [StateCondition(
            subject = assets.get('payload'),
            subject_state = "active",
            modifiers = None
        )],
        postcondition_operators = None
    )

]

detection = Detection(
    event_refs= [event for event in events if event.id in ["4", "5"]],
    operators= [LogicalOperatorType.OR]
)


content_injection_model = TechniqueModel(
        id= "T1659",
        name= "Content Injection",
        tactic= "Initial Access",
        tactic_id= "TA0001",
        events= events,
        detection= detection
    )

