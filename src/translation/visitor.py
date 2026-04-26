from src.cnl.grammar.CNLVisitor import CNLVisitor
from src.cnl.grammar.CNLParser import CNLParser


class Visitor(CNLVisitor):
    def visitAssetDefinition(self, ctx: CNLParser.AssetDefinitionContext):
        asset_type = ctx.assetType().getText()
        asset_name = ctx.assetName().getText()
        return asset_type, asset_name

    def visitAssets(self, ctx: CNLParser.AssetsContext):
        result ={}
        for asset_def in ctx.assetDefinition():
            asset_type, asset_name = self.visitAssetDefinition(asset_def)
            result[asset_name] = asset_type
        return result
    
    def visitActionObject(self, ctx:CNLParser.ActionObjectContext):
        return ctx.getText()
    
    def visitModifier(self, ctx:CNLParser.ModifierContext):
        if ctx is None:
            return None
        if ctx.location():
            return ("location", ctx.location().assetName().getText())
        elif ctx.destination():
            return ("destination", ctx.destination().assetName().getText())
        elif ctx.source():
            source = ctx.source()
            if source.BY():
                return ("source_by", source.assetName().getText())
            elif source.FROM():
                return ("source_from", source.assetName().getText())

    def visitAction(self, ctx: CNLParser.ActionContext):
        action_verb = ctx.actionVerb().getText()
        actor = ctx.actor().getText()
        object = self.visitActionObject(ctx.actionObject())
        modifiers = [self.visitModifier(m) for m in ctx.modifier()]
        action_dict = {
            "actor": actor,
            "action_verb": action_verb,
            "object": object,
            "modifiers": modifiers
        }
        return action_dict
    
    def visitWhenClause(self, ctx:CNLParser.WhenClauseContext):
        return self.visitAction(ctx.action())
    
    def visitBackground(self, ctx: CNLParser.BackgroundContext):
        assets = self.visitAssets(ctx.assets())
        return {"assets": assets}
    
    def visitStateVerb(self, ctx: CNLParser.StateVerbContext):
        if ctx.IS():
            return ctx.IDENTIFIER().getText()
        return ctx.IDENTIFIER().getText()
    
    def visitStateCondition(self, ctx: CNLParser.StateConditionContext):
        condition_object = ctx.conditionObject().getText()
        state_verb = self.visitStateVerb(ctx.stateVerb())
        modifiers = [self.visitModifier(m) for m in ctx.modifier()]
        condition = {
            "object":condition_object,
            "verb": state_verb,
            "modifiers": modifiers
        }
        return condition
    
    def visitGivenItem(self, ctx: CNLParser.GivenItemContext):
        return self.visitStateCondition(ctx.stateCondition())

    def visitGivenClause(self, ctx: CNLParser.GivenClauseContext):
        given_items = [self.visitGivenItem(item) for item in ctx.givenItem()]
        return given_items
    
    def visitThenClause(self, ctx: CNLParser.ThenClauseContext):
        then_items = [self.visitStateCondition(item) for item in ctx.stateCondition()]
        return then_items
    
    def visitEventBlock(self, ctx: CNLParser.EventBlockContext):
        event_number = ctx.DIGIT().getText()
        statement = self.visitEventStatement(ctx.eventStatement())
        return {
            "event_number": event_number,
            **statement
        }

    def visitEventStatement(self, ctx: CNLParser.EventStatementContext):
        when = self.visitWhenClause(ctx.whenClause())
        given = self.visitGivenClause(ctx.givenClause())
        then = self.visitThenClause(ctx.thenClause())
        return {"when": when,
                "given": given,
                "then": then}
    
    def visitDetectionBlock(self, ctx: CNLParser.DetectionBlockContext):
        if ctx is None:
            return None
        return self.visitDetectionExpr(ctx.detectionExpr())

    def visitDetectionExpr(self, ctx: CNLParser.DetectionExprContext):
        event_refs = [self.visitEventRef(e) for e in ctx.eventRef()]
        
        # figure out the operator between them
        if ctx.AND():
            operator = "AND"
        elif ctx.OR():
            operator = "OR"
        else:
            operator = None
        
        return {
            "operator": operator,
            "events": event_refs
        }

    def visitEventRef(self, ctx: CNLParser.EventRefContext):
        return ctx.DIGIT().getText()

    def visitAttack(self, ctx:CNLParser.AttackContext):
        background = self.visitBackground(ctx.background())
        events = [self.visitEventBlock(e) for e in ctx.eventBlock()]
        detection = self.visitDetectionBlock(ctx.detectionBlock()) if ctx.detectionBlock() else None
        attack =  {
            "background": background,
            "events": events,
            "detection": detection
        }
        return attack