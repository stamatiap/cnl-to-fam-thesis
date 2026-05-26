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


    # Visit a parse tree produced by CNLParser#processType.
    def visitProcessType(self, ctx:CNLParser.ProcessTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#fileType.
    def visitFileType(self, ctx:CNLParser.FileTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#registryType.
    def visitRegistryType(self, ctx:CNLParser.RegistryTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#endpointType.
    def visitEndpointType(self, ctx:CNLParser.EndpointTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#networkConnectionType.
    def visitNetworkConnectionType(self, ctx:CNLParser.NetworkConnectionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#driverType.
    def visitDriverType(self, ctx:CNLParser.DriverTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#moduleType.
    def visitModuleType(self, ctx:CNLParser.ModuleTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#deviceType.
    def visitDeviceType(self, ctx:CNLParser.DeviceTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#volumeType.
    def visitVolumeType(self, ctx:CNLParser.VolumeTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#accountType.
    def visitAccountType(self, ctx:CNLParser.AccountTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#sessionType.
    def visitSessionType(self, ctx:CNLParser.SessionTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#messageType.
    def visitMessageType(self, ctx:CNLParser.MessageTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#directoryType.
    def visitDirectoryType(self, ctx:CNLParser.DirectoryTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#otherType.
    def visitOtherType(self, ctx:CNLParser.OtherTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#processField.
    def visitProcessField(self, ctx:CNLParser.ProcessFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#fileField.
    def visitFileField(self, ctx:CNLParser.FileFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#registryField.
    def visitRegistryField(self, ctx:CNLParser.RegistryFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#endpointField.
    def visitEndpointField(self, ctx:CNLParser.EndpointFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#networkConnectionField.
    def visitNetworkConnectionField(self, ctx:CNLParser.NetworkConnectionFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#driverField.
    def visitDriverField(self, ctx:CNLParser.DriverFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#moduleField.
    def visitModuleField(self, ctx:CNLParser.ModuleFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#deviceField.
    def visitDeviceField(self, ctx:CNLParser.DeviceFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#volumeField.
    def visitVolumeField(self, ctx:CNLParser.VolumeFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#accountField.
    def visitAccountField(self, ctx:CNLParser.AccountFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#sessionField.
    def visitSessionField(self, ctx:CNLParser.SessionFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#messageField.
    def visitMessageField(self, ctx:CNLParser.MessageFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#directoryField.
    def visitDirectoryField(self, ctx:CNLParser.DirectoryFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#otherField.
    def visitOtherField(self, ctx:CNLParser.OtherFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#assetName.
    def visitAssetName(self, ctx:CNLParser.AssetNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#propertyName.
    def visitPropertyName(self, ctx:CNLParser.PropertyNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#propertyValue.
    def visitPropertyValue(self, ctx:CNLParser.PropertyValueContext):
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


    # Visit a parse tree produced by CNLParser#timePreposition.
    def visitTimePreposition(self, ctx:CNLParser.TimePrepositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#repetition.
    def visitRepetition(self, ctx:CNLParser.RepetitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#repeat.
    def visitRepeat(self, ctx:CNLParser.RepeatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#timePeriod.
    def visitTimePeriod(self, ctx:CNLParser.TimePeriodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#timeWindow.
    def visitTimeWindow(self, ctx:CNLParser.TimeWindowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CNLParser#time.
    def visitTime(self, ctx:CNLParser.TimeContext):
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