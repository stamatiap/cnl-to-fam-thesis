from src.cnl.grammar.CNLVisitor import CNLVisitor
from src.cnl.grammar.CNLParser import CNLParser


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
        elif ctx.otherType():
            asset_type = ctx.otherType().IDENTIFIER().getText()
            asset_name, properties = self._extract_other(ctx.otherType())
        
        return asset_type, asset_name, properties
 
    def _extract_process(self, ctx):
        """processType: PROCESS AS assetName (WITH processField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.processField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_file(self, ctx):
        """fileType: FILE AS assetName (WITH fileField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.fileField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_registry(self, ctx):
        """registryType: REGISTRY AS assetName (WITH registryField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.registryField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_endpoint(self, ctx):
        """endpointType: ENDPOINT AS assetName (WITH endpointField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.endpointField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_network_connection(self, ctx):
        """networkConnectionType: NETWORK_CONNECTION AS assetName (WITH networkConnectionField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.networkConnectionField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_driver(self, ctx):
        """driverType: DRIVER AS assetName (WITH driverField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.driverField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_module(self, ctx):
        """moduleType: MODULE AS assetName (WITH moduleField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.moduleField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_device(self, ctx):
        """deviceType: DEVICE AS assetName (WITH deviceField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.deviceField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_volume(self, ctx):
        """volumeType: VOLUME AS assetName (WITH volumeField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.volumeField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_account(self, ctx):
        """accountType: ACCOUNT AS assetName (WITH accountField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.accountField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_session(self, ctx):
        """sessionType: SESSION AS assetName (WITH sessionField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.sessionField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_message(self, ctx):
        """messageType: MESSAGE AS assetName (WITH messageField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.messageField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_directory(self, ctx):
        """directoryType: DIRECTORY AS assetName (WITH directoryField EQUALS propertyValue)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_name = ctx.directoryField().getText()
            prop_value = ctx.propertyValue().getText()
            properties[field_name] = prop_value
        
        return asset_name, properties
 
    def _extract_other(self, ctx):
        """otherType: IDENTIFIER AS assetName (WITH otherField EQUALS propertyValue (COMMA ...)*)?"""
        asset_name = ctx.assetName().getText()
        properties = None
        
        if ctx.propertyValue():
            properties = {}
            field_names = [f.getText() for f in ctx.otherField()]
            property_values = [p.getText() for p in ctx.propertyValue()]
            for field_name, prop_value in zip(field_names, property_values):
                properties[field_name] = prop_value
        
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
        elif ctx.geolocation():
            return ("geolocation", ctx.geolocation().geo_location().getText())

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
    
    def visitDetectionBlock(self, ctx: CNLParser.DetectionBlockContext):
        if ctx is None:
            return None
        return self.visitDetectionExpr(ctx.detectionExpr())

    def visitDetectionExpr(self, ctx: CNLParser.DetectionExprContext):
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
        detection = self.visitDetectionBlock(ctx.detectionBlock()) if ctx.detectionBlock() else None
        attack =  {
            **header,
            **background,
            "events": events,
            "detection": detection
        }
        return attack