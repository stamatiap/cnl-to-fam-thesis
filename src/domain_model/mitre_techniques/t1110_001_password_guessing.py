from src.domain_model.model import *
from src.domain_model.enums import *
from pprint import pprint



assets = {"accountA": Account(
                type = "account",
                name = "accountA"
            ),
            "authentication": Process(
                type = "authentication",
                name = "authentication_process"
            ),
            "correct_credentials": Message(
                type = "credentials",
                name = "CorrectCredentials",
                data = ["username", "guess_password"]
            ),
            "incorrect_credentials": Message(
                type = "credentials",
                name = "IncorrectCredentials",
                data = ["username", "guess_password"]
            )
            }

state_conditions = {"authentication_active": StateCondition(
            subject = assets.get('authentication'),
            subject_state = "active",
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
        "account_login": StateCondition(
            subject = assets.get('accountA'),
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
        preconditions = [state_conditions.get('authentication_active')],
        precondition_operators = None,
        postconditions = [state_conditions.get('credentials_rejected'), state_conditions.get('authentication_active')],
        postcondition_operators = [LogicalOperatorType.AND]
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
        preconditions = [state_conditions.get('authentication_active')],
        precondition_operators = None,
        postconditions = [state_conditions.get('credentials_accepted'), state_conditions.get('account_login')],
        postcondition_operators = [LogicalOperatorType.AND]
    )
]

detection = Detection(
    event_refs= [event for event in events if event.id in ["2"]],
    operators= None
)


password_guessing_model = TechniqueModel(
        id= "T1110.001",
        name= "Brute_Force_Password_Guessing",
        tactics= [Tactic(id="TA0006", name="Credential_Access")],
        events= events,
        detection= detection
    )

# pprint(password_guessing_model)

# from src.petri_net.petri_net_builder import PetriNetBuilder

# petri_net_builder = PetriNetBuilder()
# petri_net_builder.visualize(*petri_net_builder.build(password_guessing_model), "domain_password_guessing_model")
