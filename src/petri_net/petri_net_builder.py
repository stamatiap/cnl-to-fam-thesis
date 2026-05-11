from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.petri_net.utils import petri_utils
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.visualization.petri_net.variants import wo_decoration
from src.domain_model.model import TechniqueModel, Event, StateCondition, Modifier, Detection
from src.domain_model.enums import ModifierType, LogicalOperatorType


class PetriNetBuilder:

    def __init__(self):
        self.net = None
        self.places = {}
        self.transitions = {}
        self.event_postcondition_places: dict[str, list[PetriNet.Place]] = {}

    def build(self, model: TechniqueModel) -> tuple[PetriNet, Marking, Marking]:
        self.net = PetriNet(name=model.name)
        self.places = {}
        self.transitions = {}
        self.event_postcondition_places = {}  # reset here too

        for event in model.events:
            self._add_event(event)

        # create final place
        final_place = self._get_or_create_place("end")

        # connect final transitions based on detection block
        if model.detection:
            self._add_detection(model.detection, final_place)

        # initial marking
        initial_marking = Marking()
        first_event = model.events[0]
        for condition in first_event.preconditions:
            place_name = self._get_place_name(condition)
            place = self.places.get(place_name)

        # final marking
        final_marking = Marking()
        #final_marking[final_place] = 1

        return self.net, initial_marking, final_marking
    
    def _arc_exists(self, source, target) -> bool:
        for arc in self.net.arcs:
            if arc.source == source and arc.target == target:
                return True
        return False

    def _add_event(self, event: Event) -> None:
        transition_name = f"{event.action.actor.name}_{event.action.action_verb}_{event.action.object.name}"
        for modifier in event.action.modifiers or []:
            if modifier.type == ModifierType.LOCATION:
                transition_name += f"_in_{modifier.value.name}"
        transition = self._get_or_create_transition(transition_name)

        if event.precondition_operators and all(op == LogicalOperatorType.XOR for op in event.precondition_operators):
            # XOR — create silent transitions and shared xor_place
            xor_key = "xor_" + "_".join(sorted(self._get_place_name(c) for c in event.preconditions))
            xor_place = self._get_or_create_place(xor_key)
            # xor_place = self._get_or_create_place(f"xor_input_{transition_name}")
            petri_utils.add_arc_from_to(xor_place, transition, self.net)
            
            for condition in event.preconditions:
                place_name = self._get_place_name(condition)
                place = self._get_or_create_place(place_name)
                silent = self._get_or_create_transition(f"τ_{place_name}", label=None)
                
                if not self._arc_exists(place, silent):
                    petri_utils.add_arc_from_to(place, silent, self.net)
                if not self._arc_exists(silent, xor_place):
                    petri_utils.add_arc_from_to(silent, xor_place, self.net)
        else:
            # AND — connect all places directly to transition
            for condition in event.preconditions:
                place_name = self._get_place_name(condition)
                place = self._get_or_create_place(place_name)
                petri_utils.add_arc_from_to(place, transition, self.net)

        # postconditions
        post_places = []
        for condition in event.postconditions:
            place_name = self._get_place_name(condition)
            place = self._get_or_create_place(place_name)
            petri_utils.add_arc_from_to(transition, place, self.net)
            post_places.append(place)

        self.event_postcondition_places[event.id] = post_places

    def _add_detection(self, detection: Detection, final_place: PetriNet.Place) -> None:
        if detection.operators and all(op == LogicalOperatorType.XOR for op in detection.operators):
            # XOR — each postcondition place gets its own silent transition to final place
            for event_ref in detection.event_refs:
                post_places = self._get_postcondition_place(event_ref.id)
                for post_place in post_places:
                    silent = self._get_or_create_transition(f"τ_detect_{post_place.name}", label=None)
                    if not self._arc_exists(post_place, silent):
                        petri_utils.add_arc_from_to(post_place, silent, self.net)
                    if not self._arc_exists(silent, final_place):
                        petri_utils.add_arc_from_to(silent, final_place, self.net)
        else:
            # AND (or single event) — all postcondition places feed into one shared silent transition
            silent = self._get_or_create_transition("τ_detect_and", label=None)
            for event_ref in detection.event_refs:
                post_places = self._get_postcondition_place(event_ref.id)
                for post_place in post_places:
                    if not self._arc_exists(post_place, silent):
                        petri_utils.add_arc_from_to(post_place, silent, self.net)
            if not self._arc_exists(silent, final_place):
                petri_utils.add_arc_from_to(silent, final_place, self.net)

    def _get_postcondition_place(self, event_id: str) -> list[PetriNet.Place]:
        return self.event_postcondition_places.get(event_id, [])

    def _get_place_name(self, condition: StateCondition) -> str:
        name = f"{condition.subject.name}_{condition.subject_state}"
        for modifier in condition.modifiers or []:
            if modifier.type == ModifierType.LOCATION:
                name += f"_in_{modifier.value.name}"
        return name

    def _get_or_create_place(self, name: str) -> PetriNet.Place:
        if name not in self.places:
            place = PetriNet.Place(name)
            self.net.places.add(place)
            self.places[name] = place
        return self.places[name]

    def _get_or_create_transition(self, name: str, label: str = "") -> PetriNet.Transition:
        if name not in self.transitions:
            # label=None means silent transition (rendered as black box)
            transition = PetriNet.Transition(name, label=None if label is None else name)
            self.net.transitions.add(transition)
            self.transitions[name] = transition
        return self.transitions[name]

    def visualize(self, net: PetriNet, initial_marking: Marking, final_marking: Marking, output_path: str = "petri_net") -> None:
        decorations = {}
        for place in net.places:
            decorations[place] = {
                "label": place.name,
                "color": "white"
            }

        parameters = {
            "decorations": decorations,
            "format": "png"
        }

        gviz = pn_visualizer.apply(
            net,
            initial_marking,
            final_marking,
            parameters=parameters,
            variant=wo_decoration
        )
        pn_visualizer.save(gviz, f"{output_path}.png")
        print(f"Petri net saved to {output_path}.png")