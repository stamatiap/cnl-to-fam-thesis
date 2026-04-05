# Generated from CNL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CNLParser import CNLParser
else:
    from CNLParser import CNLParser

# This class defines a complete listener for a parse tree produced by CNLParser.
class CNLListener(ParseTreeListener):

    # Enter a parse tree produced by CNLParser#attack.
    def enterAttack(self, ctx:CNLParser.AttackContext):
        pass

    # Exit a parse tree produced by CNLParser#attack.
    def exitAttack(self, ctx:CNLParser.AttackContext):
        pass


    # Enter a parse tree produced by CNLParser#header.
    def enterHeader(self, ctx:CNLParser.HeaderContext):
        pass

    # Exit a parse tree produced by CNLParser#header.
    def exitHeader(self, ctx:CNLParser.HeaderContext):
        pass


    # Enter a parse tree produced by CNLParser#background.
    def enterBackground(self, ctx:CNLParser.BackgroundContext):
        pass

    # Exit a parse tree produced by CNLParser#background.
    def exitBackground(self, ctx:CNLParser.BackgroundContext):
        pass


    # Enter a parse tree produced by CNLParser#assets.
    def enterAssets(self, ctx:CNLParser.AssetsContext):
        pass

    # Exit a parse tree produced by CNLParser#assets.
    def exitAssets(self, ctx:CNLParser.AssetsContext):
        pass


    # Enter a parse tree produced by CNLParser#assetDefinition.
    def enterAssetDefinition(self, ctx:CNLParser.AssetDefinitionContext):
        pass

    # Exit a parse tree produced by CNLParser#assetDefinition.
    def exitAssetDefinition(self, ctx:CNLParser.AssetDefinitionContext):
        pass


    # Enter a parse tree produced by CNLParser#assetType.
    def enterAssetType(self, ctx:CNLParser.AssetTypeContext):
        pass

    # Exit a parse tree produced by CNLParser#assetType.
    def exitAssetType(self, ctx:CNLParser.AssetTypeContext):
        pass


    # Enter a parse tree produced by CNLParser#assetName.
    def enterAssetName(self, ctx:CNLParser.AssetNameContext):
        pass

    # Exit a parse tree produced by CNLParser#assetName.
    def exitAssetName(self, ctx:CNLParser.AssetNameContext):
        pass


    # Enter a parse tree produced by CNLParser#tactic.
    def enterTactic(self, ctx:CNLParser.TacticContext):
        pass

    # Exit a parse tree produced by CNLParser#tactic.
    def exitTactic(self, ctx:CNLParser.TacticContext):
        pass


    # Enter a parse tree produced by CNLParser#technique.
    def enterTechnique(self, ctx:CNLParser.TechniqueContext):
        pass

    # Exit a parse tree produced by CNLParser#technique.
    def exitTechnique(self, ctx:CNLParser.TechniqueContext):
        pass


    # Enter a parse tree produced by CNLParser#eventBlock.
    def enterEventBlock(self, ctx:CNLParser.EventBlockContext):
        pass

    # Exit a parse tree produced by CNLParser#eventBlock.
    def exitEventBlock(self, ctx:CNLParser.EventBlockContext):
        pass


    # Enter a parse tree produced by CNLParser#eventStatement.
    def enterEventStatement(self, ctx:CNLParser.EventStatementContext):
        pass

    # Exit a parse tree produced by CNLParser#eventStatement.
    def exitEventStatement(self, ctx:CNLParser.EventStatementContext):
        pass


    # Enter a parse tree produced by CNLParser#givenClause.
    def enterGivenClause(self, ctx:CNLParser.GivenClauseContext):
        pass

    # Exit a parse tree produced by CNLParser#givenClause.
    def exitGivenClause(self, ctx:CNLParser.GivenClauseContext):
        pass


    # Enter a parse tree produced by CNLParser#givenItem.
    def enterGivenItem(self, ctx:CNLParser.GivenItemContext):
        pass

    # Exit a parse tree produced by CNLParser#givenItem.
    def exitGivenItem(self, ctx:CNLParser.GivenItemContext):
        pass


    # Enter a parse tree produced by CNLParser#eventRef.
    def enterEventRef(self, ctx:CNLParser.EventRefContext):
        pass

    # Exit a parse tree produced by CNLParser#eventRef.
    def exitEventRef(self, ctx:CNLParser.EventRefContext):
        pass


    # Enter a parse tree produced by CNLParser#whenClause.
    def enterWhenClause(self, ctx:CNLParser.WhenClauseContext):
        pass

    # Exit a parse tree produced by CNLParser#whenClause.
    def exitWhenClause(self, ctx:CNLParser.WhenClauseContext):
        pass


    # Enter a parse tree produced by CNLParser#action.
    def enterAction(self, ctx:CNLParser.ActionContext):
        pass

    # Exit a parse tree produced by CNLParser#action.
    def exitAction(self, ctx:CNLParser.ActionContext):
        pass


    # Enter a parse tree produced by CNLParser#actor.
    def enterActor(self, ctx:CNLParser.ActorContext):
        pass

    # Exit a parse tree produced by CNLParser#actor.
    def exitActor(self, ctx:CNLParser.ActorContext):
        pass


    # Enter a parse tree produced by CNLParser#adjective.
    def enterAdjective(self, ctx:CNLParser.AdjectiveContext):
        pass

    # Exit a parse tree produced by CNLParser#adjective.
    def exitAdjective(self, ctx:CNLParser.AdjectiveContext):
        pass


    # Enter a parse tree produced by CNLParser#actionObject.
    def enterActionObject(self, ctx:CNLParser.ActionObjectContext):
        pass

    # Exit a parse tree produced by CNLParser#actionObject.
    def exitActionObject(self, ctx:CNLParser.ActionObjectContext):
        pass


    # Enter a parse tree produced by CNLParser#actionVerb.
    def enterActionVerb(self, ctx:CNLParser.ActionVerbContext):
        pass

    # Exit a parse tree produced by CNLParser#actionVerb.
    def exitActionVerb(self, ctx:CNLParser.ActionVerbContext):
        pass


    # Enter a parse tree produced by CNLParser#modifier.
    def enterModifier(self, ctx:CNLParser.ModifierContext):
        pass

    # Exit a parse tree produced by CNLParser#modifier.
    def exitModifier(self, ctx:CNLParser.ModifierContext):
        pass


    # Enter a parse tree produced by CNLParser#thenClause.
    def enterThenClause(self, ctx:CNLParser.ThenClauseContext):
        pass

    # Exit a parse tree produced by CNLParser#thenClause.
    def exitThenClause(self, ctx:CNLParser.ThenClauseContext):
        pass


    # Enter a parse tree produced by CNLParser#stateCondition.
    def enterStateCondition(self, ctx:CNLParser.StateConditionContext):
        pass

    # Exit a parse tree produced by CNLParser#stateCondition.
    def exitStateCondition(self, ctx:CNLParser.StateConditionContext):
        pass


    # Enter a parse tree produced by CNLParser#conditionObject.
    def enterConditionObject(self, ctx:CNLParser.ConditionObjectContext):
        pass

    # Exit a parse tree produced by CNLParser#conditionObject.
    def exitConditionObject(self, ctx:CNLParser.ConditionObjectContext):
        pass


    # Enter a parse tree produced by CNLParser#stateVerb.
    def enterStateVerb(self, ctx:CNLParser.StateVerbContext):
        pass

    # Exit a parse tree produced by CNLParser#stateVerb.
    def exitStateVerb(self, ctx:CNLParser.StateVerbContext):
        pass


    # Enter a parse tree produced by CNLParser#pastParticiple.
    def enterPastParticiple(self, ctx:CNLParser.PastParticipleContext):
        pass

    # Exit a parse tree produced by CNLParser#pastParticiple.
    def exitPastParticiple(self, ctx:CNLParser.PastParticipleContext):
        pass


    # Enter a parse tree produced by CNLParser#location.
    def enterLocation(self, ctx:CNLParser.LocationContext):
        pass

    # Exit a parse tree produced by CNLParser#location.
    def exitLocation(self, ctx:CNLParser.LocationContext):
        pass


    # Enter a parse tree produced by CNLParser#destination.
    def enterDestination(self, ctx:CNLParser.DestinationContext):
        pass

    # Exit a parse tree produced by CNLParser#destination.
    def exitDestination(self, ctx:CNLParser.DestinationContext):
        pass


    # Enter a parse tree produced by CNLParser#source.
    def enterSource(self, ctx:CNLParser.SourceContext):
        pass

    # Exit a parse tree produced by CNLParser#source.
    def exitSource(self, ctx:CNLParser.SourceContext):
        pass


    # Enter a parse tree produced by CNLParser#detectionBlock.
    def enterDetectionBlock(self, ctx:CNLParser.DetectionBlockContext):
        pass

    # Exit a parse tree produced by CNLParser#detectionBlock.
    def exitDetectionBlock(self, ctx:CNLParser.DetectionBlockContext):
        pass


    # Enter a parse tree produced by CNLParser#detectionExpr.
    def enterDetectionExpr(self, ctx:CNLParser.DetectionExprContext):
        pass

    # Exit a parse tree produced by CNLParser#detectionExpr.
    def exitDetectionExpr(self, ctx:CNLParser.DetectionExprContext):
        pass


    # Enter a parse tree produced by CNLParser#lineText.
    def enterLineText(self, ctx:CNLParser.LineTextContext):
        pass

    # Exit a parse tree produced by CNLParser#lineText.
    def exitLineText(self, ctx:CNLParser.LineTextContext):
        pass



del CNLParser