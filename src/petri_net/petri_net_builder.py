from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.petri_net.utils import petri_utils
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.visualization.petri_net.variants import wo_decoration
from src.domain_model.model import TechniqueModel, Event, StateCondition, Modifier, Detection
from src.domain_model.enums import ModifierType, LogicalOperatorType
from itertools import permutations

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

    def _add_modifier_to_name(self, name: str, modifier: Modifier) -> str:
        if modifier.type == ModifierType.LOCATION:
            return f"{name}_in_{modifier.value.name}"
        elif modifier.type == ModifierType.DESTINATION:
            return f"{name}_to_{modifier.value.name}"
        elif modifier.type == ModifierType.SOURCE:
            return f"{name}_from_{modifier.value.name}"
        elif modifier.type == ModifierType.TRIGGER:
            return f"{name}_by_{modifier.value.name}"
        else:
            return name

    def _add_event(self, event: Event) -> None:
        transition_name = f"{event.action.actor.name}_{event.action.action_verb}_{event.action.object.name}"
        for modifier in event.action.modifiers or []:
            transition_name = self._add_modifier_to_name(transition_name, modifier)
        
        transition = self._get_or_create_transition(transition_name)

        if event.precondition_operator == LogicalOperatorType.OR :
            #OR - get all transitions that produce the precondition places
            previous_transitions = []
            for condition in event.preconditions:
                place_name = self._get_place_name(condition)
                place = self._get_or_create_place(place_name)
                if not self._arc_exists(place, transition):
                    petri_utils.add_arc_from_to(place, transition, self.net)
                
                incoming_transitions = [arc.source for arc in place.in_arcs]
                for t in incoming_transitions:
                    previous_transitions.append(t)

            # permutations of all transitions included in the OR
            transition_permutations = permutations(previous_transitions)

            # keep original transitions and clone them as many times as the permutations
            all_transitions = []
            for k, perm in enumerate(transition_permutations):
                if k>0:
                    perm_transitions = []
                    for t in perm:
                        new_transition = self._get_or_create_transition(t.name+f"_{k}")
                        for out in t.out_arcs:
                            if not self._arc_exists(new_transition, out.target):
                                            petri_utils.add_arc_from_to(new_transition, out.target, self.net)
                        perm_transitions.append(new_transition)
                else: 
                    perm_transitions = list(perm)
                all_transitions.append(perm_transitions)
                # create final OR place that connects all final OR transitions
                final_or_place = self._get_or_create_place(f"final_or_place")
            
            for k, perm in enumerate(all_transitions):
                for j, t in enumerate(perm):
                    # if first transition, find incoming arcs and add them to it
                    if j == 0:
                        if not t.in_arcs:
                            # find cloned transition and connect arcs
                            for trans in self.transitions.values():
                                if trans.in_arcs and trans.name == "_".join(t.name.split("_")[:-1]):
                                    for arc in trans.in_arcs:
                                        if not self._arc_exists(arc.source, t) and "intermediate" not in arc.source.name.split("_"):
                                            petri_utils.add_arc_from_to(arc.source, t, self.net)

                    # if last transition, find outgoing arcs and add them to it
                    if j==len(perm)-1:
                        if not t.out_arcs:
                            # find original transition and connect outgoing arcs to this one
                            for trans in self.transitions.values():
                                if trans.out_arcs and trans.name == "_".join(t.name.split("_")[:-1]):
                                    for arc in trans.out_arcs:
                                        if not self._arc_exists(t, arc.target) and "intermediate" not in arc.target.name.split("_"):
                                            petri_utils.add_arc_from_to(t, arc.target, self.net)

                        # add silent transition between found outgoing places and final OR place
                        for out_arc in t.out_arcs:
                            out_place = out_arc.target
                            silent = self._get_or_create_transition(f"τ_{out_place.name}", label=None)
                            if not self._arc_exists(out_place,silent):
                                petri_utils.add_arc_from_to(out_place, silent, self.net)
                            if not self._arc_exists(silent, out_place):
                                petri_utils.add_arc_from_to(silent, final_or_place, self.net)

                            # their old outgoing arcs get deleted and the or_final_place gets connected to outgoing transitions
                            arcs_to_be_deleted = []
                            for place_out_arc in out_place.out_arcs:
                                out_transition = place_out_arc.target
            
                                if not self._arc_exists(final_or_place, out_transition) and "τ" not in out_transition.name.split("_"):
                                    petri_utils.add_arc_from_to(final_or_place, out_transition, self.net)
                                print(place_out_arc)
                                if "τ" not in out_transition.name.split("_"):
                                    print("GOT IN", place_out_arc)
                                    arcs_to_be_deleted.append(place_out_arc)
                            
                            for arc in arcs_to_be_deleted:
                                petri_utils.remove_arc(self.net, arc)

                    # if not at last transition of the permutation
                    else:
                        # create intermediate place and connect to final or place
                        inter_place = self._get_or_create_place(f"intermediate_place_{k}{j}")
                        if not self._arc_exists(t,inter_place):
                            petri_utils.add_arc_from_to(t, inter_place, self.net)
                        silent = self._get_or_create_transition(f"τ_{inter_place.name}", label=None)
                        if not self._arc_exists(inter_place,silent):
                            petri_utils.add_arc_from_to(inter_place, silent, self.net)
                        if not self._arc_exists(silent,final_or_place):
                            petri_utils.add_arc_from_to(silent, final_or_place, self.net)
                        # add arc to next transition in the permutation
                        if not self._arc_exists(inter_place,perm[j+1]):
                            petri_utils.add_arc_from_to(inter_place, perm[j+1], self.net)
            
            #print(all_transitions[0])
            # arcs_to_be_deleted = []
            # places_to_be_deleted = []
            # for t in all_transitions[0]:
            #     for out in t.out_arcs:
            #         if "intermediate" not in out.target.name.split("_"):
            #             arcs_to_be_deleted.append(out)
            #             places_to_be_deleted.append(out.target)
            # for arc in arcs_to_be_deleted:
            #     petri_utils.remove_arc(self.net, arc)
            # for place in places_to_be_deleted:
            #     petri_utils.remove_place(self.net, place)
                    
           
        elif event.precondition_operator == LogicalOperatorType.XOR:
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
        if detection.operator == LogicalOperatorType.XOR:
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
            name = self._add_modifier_to_name(name, modifier)
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