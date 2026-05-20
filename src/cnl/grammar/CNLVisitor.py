# Generated from CNL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CNLParser import CNLParser
else:
    from CNLParser import CNLParser

# This class defines a complete generic visitor for a parse tree produced by CNLParser.

class CNLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CNLParser#attack.
    def visitAttack(self, ctx:CNLParser.AttackContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#header.
    def visitHeader(self, ctx:CNLParser.HeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#background.
    def visitBackground(self, ctx:CNLParser.BackgroundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#assets.
    def visitAssets(self, ctx:CNLParser.AssetsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#assetDefinition.
    def visitAssetDefinition(self, ctx:CNLParser.AssetDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#assetType.
    def visitAssetType(self, ctx:CNLParser.AssetTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#assetName.
    def visitAssetName(self, ctx:CNLParser.AssetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#tactics.
    def visitTactics(self, ctx:CNLParser.TacticsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#tactic.
    def visitTactic(self, ctx:CNLParser.TacticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#technique.
    def visitTechnique(self, ctx:CNLParser.TechniqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#eventBlock.
    def visitEventBlock(self, ctx:CNLParser.EventBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#eventStatement.
    def visitEventStatement(self, ctx:CNLParser.EventStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#givenClause.
    def visitGivenClause(self, ctx:CNLParser.GivenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#givenItem.
    def visitGivenItem(self, ctx:CNLParser.GivenItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#eventRef.
    def visitEventRef(self, ctx:CNLParser.EventRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#whenClause.
    def visitWhenClause(self, ctx:CNLParser.WhenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#action.
    def visitAction(self, ctx:CNLParser.ActionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#actor.
    def visitActor(self, ctx:CNLParser.ActorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#actionObject.
    def visitActionObject(self, ctx:CNLParser.ActionObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#actionVerb.
    def visitActionVerb(self, ctx:CNLParser.ActionVerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#modifier.
    def visitModifier(self, ctx:CNLParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#thenClause.
    def visitThenClause(self, ctx:CNLParser.ThenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#stateCondition.
    def visitStateCondition(self, ctx:CNLParser.StateConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#conditionObject.
    def visitConditionObject(self, ctx:CNLParser.ConditionObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#stateVerb.
    def visitStateVerb(self, ctx:CNLParser.StateVerbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#location.
    def visitLocation(self, ctx:CNLParser.LocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#destination.
    def visitDestination(self, ctx:CNLParser.DestinationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#source.
    def visitSource(self, ctx:CNLParser.SourceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#timing.
    def visitTiming(self, ctx:CNLParser.TimingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#geolocation.
    def visitGeolocation(self, ctx:CNLParser.GeolocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#timeWindow.
    def visitTimeWindow(self, ctx:CNLParser.TimeWindowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#geo_location.
    def visitGeo_location(self, ctx:CNLParser.Geo_locationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#detectionBlock.
    def visitDetectionBlock(self, ctx:CNLParser.DetectionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#detectionExpr.
    def visitDetectionExpr(self, ctx:CNLParser.DetectionExprContext):
        return self.visitChildren(ctx)



del CNLParser