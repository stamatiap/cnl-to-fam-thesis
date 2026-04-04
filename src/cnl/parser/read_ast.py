from antlr4 import CommonTokenStream, FileStream
from antlr4.tree.Tree import TerminalNodeImpl
from pprint import pprint
import sys

from src.cnl.grammar.CNLLexer import CNLLexer
from src.cnl.grammar.CNLParser import CNLParser


def strip_quotes(text):
    if text is None:
        return None
    if len(text) >= 2 and text[0] == '"' and text[-1] == '"':
        return text[1:-1]
    return text


def get_line_text(ctx):
    if ctx is None:
        return None
    return strip_quotes(ctx.getText())


def parse_header(header_ctx):
    header_info = {}

    if header_ctx is None:
        return header_info

    tactic_ctx = header_ctx.tactic()
    technique_ctx = header_ctx.technique()

    if tactic_ctx:
        header_info["tactic_id"] = tactic_ctx.TACTIC_ID().getText()
        header_info["tactic_name"] = get_line_text(tactic_ctx.lineText())

    if technique_ctx:
        header_info["technique_id"] = technique_ctx.TECHNIQUE_ID().getText()
        header_info["technique_name"] = get_line_text(technique_ctx.lineText())

    return header_info


def parse_asset_definition(asset_def_ctx):
    if asset_def_ctx is None:
        return None

    return {
        "asset": get_line_text(asset_def_ctx.asset()),
        "name": get_line_text(asset_def_ctx.assetName())
    }


def parse_background(background_ctx):
    background_info = {"assets": []}

    if background_ctx is None:
        return background_info

    assets_ctx = background_ctx.assets()
    if assets_ctx is None:
        return background_info

    for asset_def_ctx in assets_ctx.assetDefinition():
        parsed = parse_asset_definition(asset_def_ctx)
        if parsed:
            background_info["assets"].append(parsed)

    return background_info


def parse_event_ref(event_ref_ctx):
    if event_ref_ctx is None:
        return None
    return f"Event {event_ref_ctx.DIGIT().getText()}"


def parse_given_item(given_item_ctx):
    if given_item_ctx is None:
        return None

    if given_item_ctx.eventRef() is not None:
        return {
            "type": "event_ref",
            "value": parse_event_ref(given_item_ctx.eventRef())
        }

    if given_item_ctx.lineText() is not None:
        return {
            "type": "text",
            "value": get_line_text(given_item_ctx.lineText())
        }

    return None


def parse_given_clause(given_ctx):
    result = []

    if given_ctx is None:
        return result

    items = given_ctx.givenItem()
    if not items:
        return result

    result.append({
        "connector": "Given",
        **parse_given_item(items[0])
    })

    follow_connector = None
    if given_ctx.AND():
        follow_connector = "And"
    elif given_ctx.OR():
        follow_connector = "Or"

    for item_ctx in items[1:]:
        result.append({
            "connector": follow_connector,
            **parse_given_item(item_ctx)
        })

    return result


def parse_when_clause(when_ctx):
    result = []

    if when_ctx is None:
        return result

    line_texts = when_ctx.lineText()
    if not line_texts:
        return result

    result.append({
        "connector": "When",
        "text": get_line_text(line_texts[0])
    })

    follow_connector = None
    if when_ctx.AND():
        follow_connector = "And"
    elif when_ctx.OR():
        follow_connector = "Or"

    for extra_line in line_texts[1:]:
        result.append({
            "connector": follow_connector,
            "text": get_line_text(extra_line)
        })

    return result


def parse_then_clause(then_ctx):
    result = []

    if then_ctx is None:
        return result

    line_texts = then_ctx.lineText()
    if not line_texts:
        return result

    result.append({
        "connector": "Then",
        "text": get_line_text(line_texts[0])
    })

    for extra_line in line_texts[1:]:
        result.append({
            "connector": "And",
            "text": get_line_text(extra_line)
        })

    return result


def count_given_text_items(given_ctx):
    if given_ctx is None:
        return 0

    count = 0
    for item_ctx in given_ctx.givenItem():
        if item_ctx.lineText() is not None:
            count += 1
    return count


def parse_event_statement(stmt_ctx):
    event_info = {
        "given": parse_given_clause(stmt_ctx.givenClause()),
        "when": parse_when_clause(stmt_ctx.whenClause()),
        "then": parse_then_clause(stmt_ctx.thenClause()),
        "repeated": None,
        "within": None,
    }

    # eventStatement.lineText() returns all descendant lineText nodes:
    # - text givenItems
    # - whenClause texts
    # - thenClause texts
    # - optional Repeated/Within texts
    all_line_texts = stmt_ctx.lineText()

    consumed = 0
    consumed += count_given_text_items(stmt_ctx.givenClause())

    if stmt_ctx.whenClause() is not None:
        consumed += len(stmt_ctx.whenClause().lineText())

    if stmt_ctx.thenClause() is not None:
        consumed += len(stmt_ctx.thenClause().lineText())

    extras = all_line_texts[consumed:]

    extra_index = 0
    if stmt_ctx.REPEATED():
        if len(extras) > extra_index:
            event_info["repeated"] = get_line_text(extras[extra_index])
        extra_index += 1

    if stmt_ctx.WITHIN():
        if len(extras) > extra_index:
            event_info["within"] = get_line_text(extras[extra_index])

    return event_info


def parse_event_block(event_ctx):
    if event_ctx is None:
        return {}

    event_number = event_ctx.DIGIT().getText()

    event_info = {
        "event": f"Event {event_number}"
    }
    event_info.update(parse_event_statement(event_ctx.eventStatement()))

    return event_info


def parse_detection_expr(detection_expr_ctx):
    result = []

    if detection_expr_ctx is None:
        return result

    pending_connector = "Detection"

    for child in detection_expr_ctx.getChildren():
        if isinstance(child, TerminalNodeImpl):
            token_text = child.getText()
            if token_text == "And":
                pending_connector = "And"
            elif token_text == "Or":
                pending_connector = "Or"
        elif isinstance(child, CNLParser.EventRefContext):
            result.append({
                "connector": pending_connector,
                "event_ref": parse_event_ref(child)
            })

    return result


def parse_detection_block(detection_ctx):
    if detection_ctx is None:
        return None

    return {
        "expression": parse_detection_expr(detection_ctx.detectionExpr())
    }


def create_attack_dict(tree):
    attack_info = {
        "header": parse_header(tree.header()),
        "background": parse_background(tree.background()),
        "events": {},
        "detection": parse_detection_block(tree.detectionBlock())
    }

    for event_ctx in tree.eventBlock():
        parsed_event = parse_event_block(event_ctx)
        attack_info["events"][parsed_event["event"]] = parsed_event

    return attack_info


def main():
    if len(sys.argv) < 2:
        print("Usage: python read_ast.py <input_file>")
        sys.exit(1)

    input_path = "data/cnl_examples/" + sys.argv[1]

    input_attack = FileStream(input_path, encoding="utf-8")

    lexer = CNLLexer(input_attack)
    stream = CommonTokenStream(lexer)
    parser = CNLParser(stream)

    tree = parser.attack()

    print(tree.toStringTree(recog=parser))

    attack_data = create_attack_dict(tree)
    pprint(attack_data, sort_dicts=False, width=100)


if __name__ == "__main__":
    main()