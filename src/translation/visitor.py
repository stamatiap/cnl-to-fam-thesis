from src.cnl.grammar.CNLVisitor import CNLVisitor
from src.cnl.grammar.CNLParser import CNLParser
from src.monitoring import logger

class Visitor(CNLVisitor): 

    def visitAssetDefinition(self, ctx: CNLParser.AssetDefinitionContext):
        if ctx.processType():
            asset_type = "process"
            asset_name, properties = self._extract_process(ctx.processType())
        elif ctx.fileType():
            asset_type = "file"
            asset_name, properties = self._extract_file(ctx.fileType())
        elif ctx.registryType():
            asset_type = "registry"
            asset_name, properties = self._extract_registry(ctx.registryType())
        elif ctx.endpointType():
            asset_type = "endpoint"
            asset_name, properties = self._extract_endpoint(ctx.endpointType())
        elif ctx.networkConnectionType():
            asset_type = "network_connection"
            asset_name, properties = self._extract_network_connection(ctx.networkConnectionType())
        elif ctx.driverType():
            asset_type = "driver"
            asset_name, properties = self._extract_driver(ctx.driverType())
        elif ctx.moduleType():
            asset_type = "module"
            asset_name, properties = self._extract_module(ctx.moduleType())
        elif ctx.deviceType():
            asset_type = "device"
            asset_name, properties = self._extract_device(ctx.deviceType())
        elif ctx.volumeType():
            asset_type = "volume"
            asset_name, properties = self._extract_volume(ctx.volumeType())
        elif ctx.accountType():
            asset_type = "account"
            asset_name, properties = self._extract_account(ctx.accountType())
        elif ctx.sessionType():
            asset_type = "session"
            asset_name, properties = self._extract_session(ctx.sessionType())
        elif ctx.messageType():
            asset_type = "message"
            asset_name, properties = self._extract_message(ctx.messageType())
        elif ctx.directoryType():
            asset_type = "directory"
            asset_name, properties = self._extract_directory(ctx.directoryType())
        elif ctx.handleType():
            asset_type = "handle"
            asset_name, properties = self._extract_handle(ctx.handleType())
        elif ctx.otherType():
            asset_type = ctx.otherType().IDENTIFIER().getText()
            asset_name, properties = self._extract_other(ctx.otherType())
        
        return asset_type, asset_name, properties
    
    def _collect_properties(self, asset_name, field_ctxs, value_ctxs):
        if not value_ctxs:
            return None
        properties = {}
        for f, v in zip(field_ctxs, value_ctxs):
            name = f.getText()
            if name in properties:
                logger.warning("Field {!r} declared more than once for asset {!r}. Using {!r}.", name, asset_name, v.getText())
            properties[name] = v.getText()
        return properties

    def _extract_process(self, ctx: CNLParser.ProcessTypeContext):
        """processType: PROCESS AS assetName (WITH processField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.processField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_file(self, ctx: CNLParser.FileTypeContext):
        """fileType: FILE AS assetName (WITH fileField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.fileField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_registry(self, ctx: CNLParser.RegistryTypeContext):
        """registryType: REGISTRY AS assetName (WITH registryField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.registryField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_endpoint(self, ctx: CNLParser.EndpointTypeContext):
        """endpointType: ENDPOINT AS assetName (WITH endpointField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.endpointField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_network_connection(self, ctx: CNLParser.NetworkConnectionTypeContext):
        """networkConnectionType: NETWORK_CONNECTION AS assetName (WITH networkConnectionField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.networkConnectionField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_driver(self, ctx: CNLParser.DriverTypeContext):
        """driverType: DRIVER AS assetName (WITH driverField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.driverField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_module(self, ctx: CNLParser.ModuleTypeContext):
        """moduleType: MODULE AS assetName (WITH moduleField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.moduleField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_device(self, ctx: CNLParser.DeviceTypeContext):
        """deviceType: DEVICE AS assetName (WITH deviceField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.deviceField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_volume(self, ctx: CNLParser.VolumeTypeContext):
        """volumeType: VOLUME AS assetName (WITH volumeField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.volumeField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_account(self, ctx: CNLParser.AccountTypeContext):
        """accountType: ACCOUNT AS assetName (WITH accountField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.accountField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_session(self, ctx: CNLParser.SessionTypeContext):
        """sessionType: SESSION AS assetName (WITH sessionField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.sessionField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_message(self, ctx: CNLParser.MessageTypeContext):
        """messageType: MESSAGE AS assetName (WITH messageField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.messageField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_directory(self, ctx: CNLParser.DirectoryTypeContext):
        """directoryType: DIRECTORY AS assetName (WITH directoryField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.directoryField(), ctx.propertyValue()
        )
        return asset_name, properties
    
    def _extract_handle(self, ctx: CNLParser.HandleTypeContext):
        """handleType: HANDLE AS assetName (WITH handleField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.handleField(), ctx.propertyValue()
        )
        return asset_name, properties
 
    def _extract_other(self, ctx: CNLParser.OtherTypeContext):
        """otherType: IDENTIFIER AS assetName (WITH otherField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = self._collect_properties(
            asset_name, ctx.otherField(), ctx.propertyValue()
        )
        return asset_name, properties

    def visitAssets(self, ctx: CNLParser.AssetsContext):
        result ={}
        for asset_def in ctx.assetDefinition():
            asset_type, asset_name, properties = self.visitAssetDefinition(asset_def)
            result[asset_name] = {"asset_type": asset_type, "properties": properties}
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
            return ("source", ctx.source().assetName().getText())
        elif ctx.trigger():
            return ("trigger", ctx.trigger().assetName().getText())

    def visitTiming(self, ctx: CNLParser.TimingContext):
        if ctx is None:
            return None
        return (ctx.timePreposition().getText(), ctx.timePeriod().getText())
    
    def visitRepeat(self, ctx: CNLParser.RepeatContext):
        if ctx is None:
            return None
        if ctx.DIGIT():
            return "".join(d.getText() for d in ctx.DIGIT())
        else:
            return ctx.IDENTIFIER().getText()
        
    def visitTimeWindow(self, ctx: CNLParser.TimeWindowContext):
        if ctx is None:
            return None
        return "".join(d.getText() for d in ctx.DIGIT()), ctx.time().getText()

    def visitRepetition(self, ctx: CNLParser.RepetitionContext):
        if ctx is None:
            return None
        
        repeats = self.visitRepeat(ctx.repeat())
        x, time_unit = self.visitTimeWindow(ctx.timeWindow())
        return (repeats, x, time_unit)
        

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
            return "is_" + ctx.IDENTIFIER().getText()
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
        items = ctx.givenItem()
        operator = None
        
        # get the operator between given items
        if len(items) > 1:
            if ctx.AND():
                operator = "AND"
            elif ctx.OR():
                operator = "OR"
            elif ctx.XOR():
                operator = "XOR"
        
        given_items = [self.visitGivenItem(item) for item in items]
        
        return {
            "preconditions": given_items,
            "operator": operator
        }
    
    def visitThenClause(self, ctx: CNLParser.ThenClauseContext):
        then_items = [self.visitStateCondition(item) for item in ctx.stateCondition()]
        operator = "AND" # then clause supports only AND
    
        return {
            "postconditions": then_items,
            "operator": operator
        }
        
    def visitEventBlock(self, ctx: CNLParser.EventBlockContext):
        event_number = "".join(d.getText() for d in ctx.DIGIT())
        statement = self.visitEventStatement(ctx.eventStatement())
        timing = self.visitTiming(ctx.timing())
        repetition = self.visitRepetition(ctx.repetition())
        return {
            "event_number": event_number,
            **statement,
            "repetition": repetition,
            "time_period": timing
        }

    def visitEventStatement(self, ctx: CNLParser.EventStatementContext):
        when = self.visitWhenClause(ctx.whenClause())
        given = self.visitGivenClause(ctx.givenClause())
        then = self.visitThenClause(ctx.thenClause())
        return {"when": when,
                "given": given,
                "then": then}
    
    def visitCompletionBlock(self, ctx: CNLParser.CompletionBlockContext):
        if ctx is None:
            return None
        return self.visitCompletionExpr(ctx.completionExpr())

    def visitCompletionExpr(self, ctx: CNLParser.CompletionExprContext):
        event_refs = [self.visitEventRef(e) for e in ctx.eventRef()]
        
        # figure out the operator between them
        operator =None

        if len(event_refs) > 1:
            if ctx.AND():
                operator = "AND"
            elif ctx.OR():
                operator = "OR"
            elif ctx.XOR():
                operator = "XOR"
            
        return {
            "events": event_refs,
            "operator": operator
        }

    def visitEventRef(self, ctx: CNLParser.EventRefContext):
        return "".join(d.getText() for d in ctx.DIGIT())
    
    def visitHeader(self, ctx: CNLParser.HeaderContext):
        tactics = self.visitTactics(ctx.tactics())
        technique = self.visitTechnique(ctx.technique())
        return {**tactics, **technique}

    def visitTactics(self, ctx: CNLParser.TacticsContext):
        entries = [self.visitTactic(e) for e in ctx.tactic()]
        return {"tactics": entries}

    def visitTactic(self, ctx: CNLParser.TacticContext):
        return {
            "tactic_id": ctx.TACTIC_ID().getText(),
            "tactic_name": ctx.IDENTIFIER().getText()
        }

    def visitTechnique(self, ctx: CNLParser.TechniqueContext):
        return {
            "technique_id": ctx.TECHNIQUE_ID().getText(),
            "technique_name": ctx.IDENTIFIER().getText()
        }

    def visitAttack(self, ctx:CNLParser.AttackContext):
        header = self.visitHeader(ctx.header())
        background = self.visitBackground(ctx.background())
        events = [self.visitEventBlock(e) for e in ctx.eventBlock()]
        completion = self.visitCompletionBlock(ctx.completionBlock()) if ctx.completionBlock() else None
        attack =  {
            **header,
            **background,
            "events": events,
            "completion": completion
        }
        return attack