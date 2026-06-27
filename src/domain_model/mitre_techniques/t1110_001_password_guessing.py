from src.domain_model.model import *
from src.domain_model.enums import *


assets = {"accountA": Account(
                asset_type = "account",
                name = "accountA"
            ),
            "authentication": Process(
                asset_type = "authentication",
                name = "authentication_process"
            ),
            "correct_credentials": Message(
                asset_type = "credentials",
                name = "CorrectCredentials",
                data = "guess_correct_password"
            ),
            "incorrect_credentials": Message(
                asset_type = "credentials",
                name = "IncorrectCredentials",
                data = "guess_random_password"
            ),
            "user": Session(
                asset_type = "session",
                name = "user"
            )
            }

state_conditions = {"authentication_awaiting_input": StateCondition(
            subject = assets.get('authentication'),
            subject_state = "awaiting_input",
            modifiers = None
        ),
        "credentials_rejected": StateCondition(
            subject = assets.get('incorrect_credentials'),
            subject_state = "rejected",
            modifiers = None
        ),
        "credentials_accepted": StateCondition(
            subject = assets.get('correct_credentials'),
            subject_state = "accepted",
            modifiers = None
        ),
        "user_logged_in": StateCondition(
            subject = assets.get('user'),
            subject_state = "logged_in",
            modifiers = None
        )}

events = [
    Event(
        id = "1",
        name = "Event 1",
        action = Action(
            actor = assets.get('authentication'),
            action_verb = "receives",
            object = assets.get('incorrect_credentials'),
            modifiers = [Modifier(type = ModifierType.DESTINATION, value = assets.get('accountA'))]
        ),
        preconditions = [state_conditions.get('authentication_awaiting_input')],
        precondition_operator = None,
        postconditions = [state_conditions.get('credentials_rejected')],
        postcondition_operator = None,
        repetition = Repetition(occurrences=5, time_value=1, time_unit=TimeUnit.SECOND)
    ),
    Event(
        id = "2",
        name = "Event 2",
        action = Action(
            actor = assets.get('authentication'),
            action_verb = "receives",
            object = assets.get('correct_credentials'),
            modifiers = [Modifier(type = ModifierType.DESTINATION, value = assets.get('accountA'))]
        ),
        preconditions = [state_conditions.get('credentials_rejected')],
        precondition_operator = None,
        postconditions = [state_conditions.get('credentials_accepted'), state_conditions.get('user_logged_in')],
        postcondition_operator = LogicalOperatorType.AND
    )
]

completion = Completion(
    event_refs= [event for event in events if event.id in ["2"]],
    operator= None
)


password_guessing_model = TechniqueModel(
        id= "T1110.001",
        name= "Brute_Force_Password_Guessing",
        tactics= [Tactic(id="TA0006", name="Credential_Access")],
        assets=assets,
        events= events,
        completion= completion
    )
