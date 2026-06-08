from pm4py.objects.petri_net.obj import PetriNet, Marking
from pm4py.objects.petri_net.utils import petri_utils
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.visualization.petri_net.variants import wo_decoration
from src.domain_model.model import TechniqueModel, Event, StateCondition, Modifier, Completion
from src.domain_model.enums import ModifierType, LogicalOperatorType
from itertools import permutations
from src.monitoring import logger

class PetriNetBuilder:

    def __init__(self):
        self.net = None
        self.places = {}
        self.transitions = {}
        self.event_postcondition_places: dict[str, list[PetriNet.Place]] = {}
        self._arc_index: set[tuple[str, str]] = set()

    def build(self, model: TechniqueModel) -> tuple[PetriNet, Marking, Marking]:
        logger.info("building petri net for {}", model.name)

        self.net = PetriNet(name=model.name)
        self.places = {}
        self.transitions = {}
        self.event_postcondition_places = {}  # reset 
        self._arc_index = set() # reset 

        for event in model.events:
            self._add_event(event)

        # create final place
        final_place = self._get_or_create_place("end") # synthetic end place
        start_place = self._add_start_place(model) # synthetic start place

        # connect final transitions based on completion block
        if model.completion:
            self._add_completion(model.completion, final_place)

        # initial marking
        initial_marking = Marking()

        # final marking
        final_marking = Marking()

        logger.info("built {}: {} places, {} transitions, {} arcs",
                model.name, len(self.net.places), len(self.net.transitions), len(self.net.arcs))
        
        return self.net, initial_marking, final_marking
    
    def _identify_entry_place_names(self, model: TechniqueModel) -> set[str]:
        entry_names = set()
        seen_post = set()
        for event in model.events:
            for cond in event.preconditions:
                name = self._get_place_name(cond)
                if name not in seen_post:
                    entry_names.add(name)
            for cond in event.postconditions:
                seen_post.add(self._get_place_name(cond))
        return entry_names
        
    def _add_start_place(self, model: TechniqueModel) -> PetriNet.Place:
        entry_names = self._identify_entry_place_names(model)
        start_place = self._get_or_create_place("start")
        silent = self._get_or_create_transition("τ_start", label=None)
        self._add_arc(start_place, silent)

        for name in entry_names:
            place = self.places.get(name)
            if place is not None:
                self._add_arc(silent, place)
        return start_place
    
    def _add_arc(self, source, target) -> bool:
        key = (source.name, target.name)
        if key in self._arc_index:
            return False
        petri_utils.add_arc_from_to(source, target, self.net)
        self._arc_index.add(key)
        return True

    def _remove_arc(self, arc) -> None:
        self._arc_index.discard((arc.source.name, arc.target.name))
        petri_utils.remove_arc(self.net, arc)

    def _arc_exists(self, source, target) -> bool:
        return (source.name, target.name) in self._arc_index
    
    def _apply_repetition(self, event: Event, transition: PetriNet.Transition) -> PetriNet.Transition:
        """
        When an event's repetition frequency is specified by an integer bigger than  1, then
        the current transition gets cloned that many times, with the same label.
         
        Chain shape for frequency N:
            transition → P_empty_1 → T_rep_1 → P_empty_2 → ... → P_empty_{N-1} → T_rep_{N-1}

        Returns the tail transition
        """
        repetition = event.repetition
        if not repetition:
            return transition

        frequency = repetition.frequency
        if not isinstance(frequency, str):
            return transition
        try:
            frequency = int(frequency)
        except ValueError:
            return transition
        if frequency <= 1:
            return transition

        post_name = "_".join(sorted(self._get_place_name(p) for p in event.postconditions)) # get all postconditions' name into 1 place

        current = transition
        for i in range(1, frequency):
            between_place = self._get_or_create_place(f"{post_name}_{i}")
            clone = self._get_or_create_transition(
                name=f"{transition.name}_rep_{i}",
                label=transition.label,
            )
            self._add_arc(current, between_place)
            self._add_arc(between_place, clone)
            current = clone
        return current

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
        logger.debug("adding event {} (operator={})", event.id, event.precondition_operator)

        transition_name = f"{event.action.actor.name}_{event.action.action_verb}_{event.action.object.name}"
        for modifier in event.action.modifiers or []:
            transition_name = self._add_modifier_to_name(transition_name, modifier)
        
        transition = self._get_or_create_transition(name=transition_name+event.id,label=transition_name)

        if event.precondition_operator == LogicalOperatorType.OR :
            #OR - get all transitions that produce the precondition places
            previous_transitions = []
            for condition in event.preconditions:
                place_name = self._get_place_name(condition)
                place = self._get_or_create_place(place_name)
                self._add_arc(place, transition)
                
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
                        new_transition = self._get_or_create_transition(name=t.name+f"_{k}"+event.id,label=t.name+f"_{k}")
                        for out in t.out_arcs:
                            self._add_arc(new_transition, out.target)
                        perm_transitions.append(new_transition)
                else: 
                    perm_transitions = list(perm)
                all_transitions.append(perm_transitions)
                # create final OR place that connects all final OR transitions
                final_or_place = self._get_or_create_place(f"final_or_place_{event.id}")
            
            for k, perm in enumerate(all_transitions):
                for j, t in enumerate(perm):
                    # if first transition, find incoming arcs and add them to it
                    if j == 0:
                        if not t.in_arcs:
                            # find cloned transition and connect arcs
                            for trans in self.transitions.values():
                                if trans.in_arcs and trans.name == "_".join(t.name.split("_")[:-1]):
                                    for arc in trans.in_arcs:
                                        if "intermediate" not in arc.source.name.split("_"):
                                            self._add_arc(arc.source, t)

                    # if last transition, find outgoing arcs and add them to it
                    if j==len(perm)-1:
                        if not t.out_arcs:
                            # find original transition and connect outgoing arcs to this one
                            for trans in self.transitions.values():
                                if trans.out_arcs and trans.name == "_".join(t.name.split("_")[:-1]):
                                    for arc in trans.out_arcs:
                                        if "intermediate" not in arc.target.name.split("_"):
                                            self._add_arc(t, arc.target)

                        # add silent transition between found outgoing places and final OR place
                        for out_arc in t.out_arcs:
                            out_place = out_arc.target
                            silent = self._get_or_create_transition(f"τ_{out_place.name}", label=None)
                            self._add_arc(out_place, silent)
                            self._add_arc(silent, final_or_place)

                            # their old outgoing arcs get deleted and the or_final_place gets connected to outgoing transitions
                            arcs_to_be_deleted = []
                            for place_out_arc in out_place.out_arcs:
                                out_transition = place_out_arc.target
            
                                if out_transition.label is None:
                                    continue
                                self._add_arc(final_or_place, out_transition)
                                arcs_to_be_deleted.append(place_out_arc)
                            
                            for arc in arcs_to_be_deleted:
                                self._remove_arc(arc)

                    # if not at last transition of the permutation
                    else:
                        # create intermediate place and connect to final or place
                        inter_place = self._get_or_create_place(f"intermediate_place_{k}{j}")
                        self._add_arc(t, inter_place)
                        silent = self._get_or_create_transition(f"τ_{inter_place.name}", label=None)
                        self._add_arc(inter_place, silent)
                        self._add_arc(silent, final_or_place)
                        # add arc to next transition in the permutation
                        self._add_arc(inter_place, perm[j+1])
            
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
            self._add_arc(xor_place, transition)
            
            for condition in event.preconditions:
                place_name = self._get_place_name(condition)
                place = self._get_or_create_place(place_name)
                silent = self._get_or_create_transition(f"τ_{place_name}", label=None)
                
                self._add_arc(place, silent)
                self._add_arc(silent, xor_place)
        else:
            # AND — connect all places directly to transition
            for condition in event.preconditions:
                place_name = self._get_place_name(condition)
                place = self._get_or_create_place(place_name)
                self._add_arc(place, transition)

        tail = self._apply_repetition(event, transition)

        # postconditions
        post_places = []
        for condition in event.postconditions:
            place_name = self._get_place_name(condition)
            place = self._get_or_create_place(place_name)
            self._add_arc(tail, place)
            post_places.append(place)

        self.event_postcondition_places[event.id] = post_places

    def _add_completion(self, completion: Completion, final_place: PetriNet.Place) -> None:
        if completion.operator == LogicalOperatorType.XOR:
            # XOR — each postcondition place gets its own silent transition to final place
            for event_ref in completion.event_refs:
                post_places = self._get_postcondition_place(event_ref.id)
                for post_place in post_places:
                    silent = self._get_or_create_transition(f"τ_detect_{post_place.name}", label=None)
                    self._add_arc(post_place, silent)
                    self._add_arc(silent, final_place)
        else:
            # AND (or single event) — all postcondition places feed into one shared silent transition
            silent = self._get_or_create_transition("τ_detect_and", label=None)
            for event_ref in completion.event_refs:
                post_places = self._get_postcondition_place(event_ref.id)
                for post_place in post_places:
                    self._add_arc(post_place, silent)
            self._add_arc(silent, final_place)

    def _get_postcondition_place(self, event_id: str) -> list[PetriNet.Place]:
        places = self.event_postcondition_places.get(event_id, [])
        if not places:
            logger.warning("No postcondition places recorded for event {!r}", event_id)
        return places

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
            transition = PetriNet.Transition(name, label=label)
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