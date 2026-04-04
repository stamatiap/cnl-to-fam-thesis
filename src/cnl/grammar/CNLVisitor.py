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


    # Visit a parse tree produced by CNLParser#asset.
    def visitAsset(self, ctx:CNLParser.AssetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#assetName.
    def visitAssetName(self, ctx:CNLParser.AssetNameContext):
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


    # Visit a parse tree produced by CNLParser#thenClause.
    def visitThenClause(self, ctx:CNLParser.ThenClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#detectionBlock.
    def visitDetectionBlock(self, ctx:CNLParser.DetectionBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#detectionExpr.
    def visitDetectionExpr(self, ctx:CNLParser.DetectionExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#lineText.
    def visitLineText(self, ctx:CNLParser.LineTextContext):
        return self.visitChildren(ctx)



del CNLParser