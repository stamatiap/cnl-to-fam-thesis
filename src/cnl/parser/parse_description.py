from antlr4 import CommonTokenStream, FileStream
from pprint import pprint
import sys
import json
import os

from src.cnl.grammar.CNLLexer import CNLLexer
from src.cnl.grammar.CNLParser import CNLParser


def get_text(ctx):
    if ctx is None:
        return None
    return ctx.getText()


# Header
def parse_tactic(ctx):
    if ctx is None:
        return {}
    return {
        "tactic_id":   get_text(ctx.TACTIC_ID()),
        "tactic_name": get_text(ctx.IDENTIFIER())
    }


def parse_technique(ctx):
    if ctx is None:
        return {}
    return {
        "technique_id":   get_text(ctx.TECHNIQUE_ID()),
        "technique_name": get_text(ctx.IDENTIFIER())
    }


def parse_header(ctx):
    if ctx is None:
        return {}
    result = {}
    result.update(parse_tactic(ctx.tactic()))
    result.update(parse_technique(ctx.technique()))
    return result


# Background
def parse_asset_definition(ctx):
    if ctx is None:
        return None
    return {
        "type": get_text(ctx.assetType()),
        "name": get_text(ctx.assetName())
    }


def parse_background(ctx):
    if ctx is None:
        return {"assets": []}
    return {
        "assets": [
            parse_asset_definition(a)
            for a in ctx.assets().assetDefinition()
        ]
    }


# Modifiers
def parse_modifier(ctx):
    if ctx is None:
        return None
    if ctx.location():
        return {
            "type":  "location",
            "value": get_text(ctx.location().assetName())
        }
    if ctx.destination():
        return {
            "type":  "destination",
            "value": get_text(ctx.destination().assetName())
        }
    if ctx.source():
        source = ctx.source()
        return {
            "type":    "source",
            "keyword": "by" if source.BY() else "from",
            "value":   get_text(source.assetName())
        }
    return None


# State condition
def parse_state_verb(ctx):
    if ctx is None:
        return None

    # IS pastParticiple e.g "is created", "is spawned"
    if ctx.pastParticiple():
        return get_text(ctx.pastParticiple())

    # IS IDENTIFIER  e.g. "is active", "is running"
    identifier = ctx.IDENTIFIER()
    if identifier:
        return get_text(identifier)

    return None


def parse_state_condition(ctx):
    if ctx is None:
        return None
    return {
        "subject":   get_text(ctx.conditionObject()),
        "verb":      parse_state_verb(ctx.stateVerb()),
        "modifiers": [parse_modifier(m) for m in ctx.modifier()]
    }


# Given Clause
def parse_event_ref(ctx):
    if ctx is None:
        return None
    return {
        "type":     "event_ref",
        "event_id": get_text(ctx.DIGIT())
    }


def parse_given_item(ctx):
    if ctx is None:
        return None
    if ctx.eventRef():
        return parse_event_ref(ctx.eventRef())
    if ctx.stateCondition():
        parsed = parse_state_condition(ctx.stateCondition())
        if parsed:
            parsed["type"] = "state_condition"
        return parsed
    return None


def parse_given_clause(ctx):
    if ctx is None:
        return []

    items      = ctx.givenItem()

    # we enforce either Or or And for the entire clause, so we first check if any OR exists
    # and if not we default to And for all items following
    has_or     = bool(ctx.OR())
    connectors = ["Given"] + ["Or" if has_or else "And"] * (len(items) - 1)

    result = []
    for connector, item_ctx in zip(connectors, items):
        parsed = parse_given_item(item_ctx)
        if parsed:
            parsed["connector"] = connector
            result.append(parsed)

    return result


# When Clause
def parse_action(ctx):
    if ctx is None:
        return None
    return {
        "actor_adjective": get_text(ctx.actorAdjective()) if ctx.actorAdjective() else None,
        "actor":           get_text(ctx.actor()),
        "verb":            get_text(ctx.actionVerb()),
        "adjective":       get_text(ctx.adjective()) if ctx.adjective() else None,
        "object":          get_text(ctx.actionObject()),
        "modifiers":       [parse_modifier(m) for m in ctx.modifier()]
    }

def parse_when_clause(ctx):
    if ctx is None:
        return []
    return [parse_action(a) for a in ctx.action()]


# Then Clause
def parse_then_clause(ctx):
    if ctx is None:
        return []
    return [parse_state_condition(sc) for sc in ctx.stateCondition()]


# Event Statement
def parse_event_statement(ctx):
    if ctx is None:
        return {}
    return {
        "given": parse_given_clause(ctx.givenClause()),
        "when":  parse_when_clause(ctx.whenClause()),
        "then":  parse_then_clause(ctx.thenClause())
    }


def parse_event_block(ctx):
    if ctx is None:
        return {}
    return {
        "event_id":  get_text(ctx.DIGIT()),
        "statement": parse_event_statement(ctx.eventStatement())
    }


# Detection
def parse_detection_expr(ctx):
    if ctx is None:
        return None

    event_ids = [get_text(e.DIGIT()) for e in ctx.eventRef()]
    operators = [
        child.getText()
        for child in ctx.children
        if hasattr(child, 'getText') and child.getText() in ("And", "Or")
    ]

    if not operators:
        return {"operator": None, "event_ids": event_ids}

    unique_ops = set(operators)
    return {
        "operator":  operators[0] if len(unique_ops) == 1 else "mixed",
        "event_ids": event_ids,
        **({"operators": operators} if len(unique_ops) > 1 else {})
    }


def parse_detection_block(ctx):
    if ctx is None:
        return None
    return parse_detection_expr(ctx.detectionExpr())


def create_attack_dict(tree):
    return {
        "header":     parse_header(tree.header()),
        "background": parse_background(tree.background()),
        "events":     [parse_event_block(e) for e in tree.eventBlock()],
        "detection":  parse_detection_block(tree.detectionBlock())
    }

def save_attack_data(attack_data, input_filename):
    output_dir = "data/parsed_descriptions"
    os.makedirs(output_dir, exist_ok=True)

    input_stem = os.path.splitext(os.path.basename(input_filename))[0]
    output_path = os.path.join(output_dir, f"{input_stem}.json")

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(attack_data, f, indent=2, ensure_ascii=False)

    print(f"Saved JSON to: {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_description.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    input_path = "data/example_descriptions/" + input_file

    input_attack = FileStream(input_path, encoding="utf-8")
    lexer        = CNLLexer(input_attack)
    stream       = CommonTokenStream(lexer)
    parser       = CNLParser(stream)
    tree         = parser.attack()

    print(tree.toStringTree(recog=parser))

    attack_data = create_attack_dict(tree)
    pprint(attack_data, sort_dicts=False, width=100)
    save_attack_data(attack_data, input_path)


if __name__ == "__main__":
    main()