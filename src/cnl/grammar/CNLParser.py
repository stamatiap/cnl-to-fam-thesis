# Generated from CNL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,53,242,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,1,0,1,0,4,
        0,68,8,0,11,0,12,0,69,1,0,3,0,73,8,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,5,3,87,8,3,10,3,12,3,90,9,3,1,4,1,4,1,4,1,4,
        1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,10,3,10,119,8,10,1,10,1,10,3,10,123,
        8,10,1,11,1,11,1,11,1,11,5,11,129,8,11,10,11,12,11,132,9,11,1,11,
        1,11,5,11,136,8,11,10,11,12,11,139,9,11,3,11,141,8,11,1,12,1,12,
        3,12,145,8,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,5,14,154,8,14,10,
        14,12,14,157,9,14,1,15,1,15,1,15,3,15,162,8,15,1,15,1,15,5,15,166,
        8,15,10,15,12,15,169,9,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,
        1,20,1,20,1,20,3,20,182,8,20,1,21,1,21,1,21,1,21,5,21,188,8,21,10,
        21,12,21,191,9,21,1,22,1,22,1,22,5,22,196,8,22,10,22,12,22,199,9,
        22,1,23,1,23,1,24,1,24,1,24,1,24,1,24,5,24,208,8,24,10,24,12,24,
        211,9,24,3,24,213,8,24,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,
        28,1,28,1,28,1,28,3,28,227,8,28,1,29,1,29,1,29,1,30,1,30,1,30,5,
        30,235,8,30,10,30,12,30,238,9,30,1,31,1,31,1,31,0,0,32,0,2,4,6,8,
        10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,
        54,56,58,60,62,0,3,1,0,23,35,1,0,36,48,1,0,10,11,229,0,64,1,0,0,
        0,2,76,1,0,0,0,4,79,1,0,0,0,6,83,1,0,0,0,8,91,1,0,0,0,10,95,1,0,
        0,0,12,97,1,0,0,0,14,99,1,0,0,0,16,104,1,0,0,0,18,109,1,0,0,0,20,
        113,1,0,0,0,22,124,1,0,0,0,24,144,1,0,0,0,26,146,1,0,0,0,28,149,
        1,0,0,0,30,158,1,0,0,0,32,170,1,0,0,0,34,172,1,0,0,0,36,174,1,0,
        0,0,38,176,1,0,0,0,40,181,1,0,0,0,42,183,1,0,0,0,44,192,1,0,0,0,
        46,200,1,0,0,0,48,212,1,0,0,0,50,214,1,0,0,0,52,216,1,0,0,0,54,219,
        1,0,0,0,56,226,1,0,0,0,58,228,1,0,0,0,60,231,1,0,0,0,62,239,1,0,
        0,0,64,65,3,2,1,0,65,67,3,4,2,0,66,68,3,18,9,0,67,66,1,0,0,0,68,
        69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,71,73,3,58,
        29,0,72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,75,5,0,0,1,75,
        1,1,0,0,0,76,77,3,14,7,0,77,78,3,16,8,0,78,3,1,0,0,0,79,80,5,16,
        0,0,80,81,5,6,0,0,81,82,3,6,3,0,82,5,1,0,0,0,83,88,3,8,4,0,84,85,
        5,10,0,0,85,87,3,8,4,0,86,84,1,0,0,0,87,90,1,0,0,0,88,86,1,0,0,0,
        88,89,1,0,0,0,89,7,1,0,0,0,90,88,1,0,0,0,91,92,3,10,5,0,92,93,5,
        15,0,0,93,94,3,12,6,0,94,9,1,0,0,0,95,96,5,51,0,0,96,11,1,0,0,0,
        97,98,5,51,0,0,98,13,1,0,0,0,99,100,5,3,0,0,100,101,5,12,0,0,101,
        102,5,49,0,0,102,103,5,51,0,0,103,15,1,0,0,0,104,105,5,4,0,0,105,
        106,5,12,0,0,106,107,5,50,0,0,107,108,5,51,0,0,108,17,1,0,0,0,109,
        110,5,5,0,0,110,111,5,53,0,0,111,112,3,20,10,0,112,19,1,0,0,0,113,
        114,3,22,11,0,114,115,3,28,14,0,115,118,3,42,21,0,116,117,5,13,0,
        0,117,119,3,62,31,0,118,116,1,0,0,0,118,119,1,0,0,0,119,122,1,0,
        0,0,120,121,5,14,0,0,121,123,3,62,31,0,122,120,1,0,0,0,122,123,1,
        0,0,0,123,21,1,0,0,0,124,125,5,6,0,0,125,140,3,24,12,0,126,127,5,
        10,0,0,127,129,3,24,12,0,128,126,1,0,0,0,129,132,1,0,0,0,130,128,
        1,0,0,0,130,131,1,0,0,0,131,141,1,0,0,0,132,130,1,0,0,0,133,134,
        5,11,0,0,134,136,3,24,12,0,135,133,1,0,0,0,136,139,1,0,0,0,137,135,
        1,0,0,0,137,138,1,0,0,0,138,141,1,0,0,0,139,137,1,0,0,0,140,130,
        1,0,0,0,140,137,1,0,0,0,141,23,1,0,0,0,142,145,3,26,13,0,143,145,
        3,44,22,0,144,142,1,0,0,0,144,143,1,0,0,0,145,25,1,0,0,0,146,147,
        5,5,0,0,147,148,5,53,0,0,148,27,1,0,0,0,149,150,5,7,0,0,150,155,
        3,30,15,0,151,152,5,10,0,0,152,154,3,30,15,0,153,151,1,0,0,0,154,
        157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,29,1,0,0,0,157,155,
        1,0,0,0,158,159,3,32,16,0,159,161,3,38,19,0,160,162,3,34,17,0,161,
        160,1,0,0,0,161,162,1,0,0,0,162,163,1,0,0,0,163,167,3,36,18,0,164,
        166,3,40,20,0,165,164,1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,
        168,1,0,0,0,168,31,1,0,0,0,169,167,1,0,0,0,170,171,3,12,6,0,171,
        33,1,0,0,0,172,173,5,51,0,0,173,35,1,0,0,0,174,175,5,51,0,0,175,
        37,1,0,0,0,176,177,7,0,0,0,177,39,1,0,0,0,178,182,3,52,26,0,179,
        182,3,54,27,0,180,182,3,56,28,0,181,178,1,0,0,0,181,179,1,0,0,0,
        181,180,1,0,0,0,182,41,1,0,0,0,183,184,5,8,0,0,184,189,3,44,22,0,
        185,186,5,10,0,0,186,188,3,44,22,0,187,185,1,0,0,0,188,191,1,0,0,
        0,189,187,1,0,0,0,189,190,1,0,0,0,190,43,1,0,0,0,191,189,1,0,0,0,
        192,193,3,46,23,0,193,197,3,48,24,0,194,196,3,40,20,0,195,194,1,
        0,0,0,196,199,1,0,0,0,197,195,1,0,0,0,197,198,1,0,0,0,198,45,1,0,
        0,0,199,197,1,0,0,0,200,201,5,51,0,0,201,47,1,0,0,0,202,203,5,18,
        0,0,203,213,5,51,0,0,204,205,5,18,0,0,205,209,3,50,25,0,206,208,
        3,40,20,0,207,206,1,0,0,0,208,211,1,0,0,0,209,207,1,0,0,0,209,210,
        1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,212,202,1,0,0,0,212,204,
        1,0,0,0,213,49,1,0,0,0,214,215,7,1,0,0,215,51,1,0,0,0,216,217,5,
        19,0,0,217,218,3,12,6,0,218,53,1,0,0,0,219,220,5,20,0,0,220,221,
        3,12,6,0,221,55,1,0,0,0,222,223,5,21,0,0,223,227,3,12,6,0,224,225,
        5,22,0,0,225,227,3,12,6,0,226,222,1,0,0,0,226,224,1,0,0,0,227,57,
        1,0,0,0,228,229,5,17,0,0,229,230,3,60,30,0,230,59,1,0,0,0,231,236,
        3,26,13,0,232,233,7,2,0,0,233,235,3,26,13,0,234,232,1,0,0,0,235,
        238,1,0,0,0,236,234,1,0,0,0,236,237,1,0,0,0,237,61,1,0,0,0,238,236,
        1,0,0,0,239,240,5,1,0,0,240,63,1,0,0,0,19,69,72,88,118,122,130,137,
        140,144,155,161,167,181,189,197,209,212,226,236
    ]

class CNLParser ( Parser ):

    grammarFileName = "CNL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'Tactic'", 
                     "'Technique'", "'Event'", "'Given'", "'When'", "'Then'", 
                     "'If'", "'And'", "'Or'", "':'", "'Repeated'", "'Within'", 
                     "'as'", "'Background'", "'Detection'", "'is'", "'in'", 
                     "'to'", "'by'", "'from'", "'spawns'", "'creates'", 
                     "'executes'", "'loads'", "'requests'", "'receives'", 
                     "'sends'", "'mounts'", "'modifies'", "'records'", "'raises'", 
                     "'performs'", "'recognizes'", "'spawned'", "'created'", 
                     "'executed'", "'loaded'", "'requested'", "'received'", 
                     "'sent'", "'mounted'", "'modified'", "'recorded'", 
                     "'raised'", "'performed'", "'recognized'" ]

    symbolicNames = [ "<INVALID>", "STRING", "ESC", "TACTIC", "TECHNIQUE", 
                      "EVENT", "GIVEN", "WHEN", "THEN", "IF", "AND", "OR", 
                      "COLON", "REPEATED", "WITHIN", "AS", "BACKGROUND", 
                      "DETECTION", "IS", "IN", "TO", "BY", "FROM", "SPAWNS", 
                      "CREATES", "EXECUTES", "LOADS", "REQUESTS", "RECEIVES", 
                      "SENDS", "MOUNTS", "MODIFIES", "RECORDS", "RAISES", 
                      "PERFORMS", "RECOGNIZES", "SPAWNED", "CREATED", "EXECUTED", 
                      "LOADED", "REQUESTED", "RECEIVED", "SENT", "MOUNTED", 
                      "MODIFIED", "RECORDED", "RAISED", "PERFORMED", "RECOGNIZED", 
                      "TACTIC_ID", "TECHNIQUE_ID", "IDENTIFIER", "WS", "DIGIT" ]

    RULE_attack = 0
    RULE_header = 1
    RULE_background = 2
    RULE_assets = 3
    RULE_assetDefinition = 4
    RULE_assetType = 5
    RULE_assetName = 6
    RULE_tactic = 7
    RULE_technique = 8
    RULE_eventBlock = 9
    RULE_eventStatement = 10
    RULE_givenClause = 11
    RULE_givenItem = 12
    RULE_eventRef = 13
    RULE_whenClause = 14
    RULE_action = 15
    RULE_actor = 16
    RULE_adjective = 17
    RULE_actionObject = 18
    RULE_actionVerb = 19
    RULE_modifier = 20
    RULE_thenClause = 21
    RULE_stateCondition = 22
    RULE_conditionObject = 23
    RULE_stateVerb = 24
    RULE_pastParticiple = 25
    RULE_location = 26
    RULE_destination = 27
    RULE_source = 28
    RULE_detectionBlock = 29
    RULE_detectionExpr = 30
    RULE_lineText = 31

    ruleNames =  [ "attack", "header", "background", "assets", "assetDefinition", 
                   "assetType", "assetName", "tactic", "technique", "eventBlock", 
                   "eventStatement", "givenClause", "givenItem", "eventRef", 
                   "whenClause", "action", "actor", "adjective", "actionObject", 
                   "actionVerb", "modifier", "thenClause", "stateCondition", 
                   "conditionObject", "stateVerb", "pastParticiple", "location", 
                   "destination", "source", "detectionBlock", "detectionExpr", 
                   "lineText" ]

    EOF = Token.EOF
    STRING=1
    ESC=2
    TACTIC=3
    TECHNIQUE=4
    EVENT=5
    GIVEN=6
    WHEN=7
    THEN=8
    IF=9
    AND=10
    OR=11
    COLON=12
    REPEATED=13
    WITHIN=14
    AS=15
    BACKGROUND=16
    DETECTION=17
    IS=18
    IN=19
    TO=20
    BY=21
    FROM=22
    SPAWNS=23
    CREATES=24
    EXECUTES=25
    LOADS=26
    REQUESTS=27
    RECEIVES=28
    SENDS=29
    MOUNTS=30
    MODIFIES=31
    RECORDS=32
    RAISES=33
    PERFORMS=34
    RECOGNIZES=35
    SPAWNED=36
    CREATED=37
    EXECUTED=38
    LOADED=39
    REQUESTED=40
    RECEIVED=41
    SENT=42
    MOUNTED=43
    MODIFIED=44
    RECORDED=45
    RAISED=46
    PERFORMED=47
    RECOGNIZED=48
    TACTIC_ID=49
    TECHNIQUE_ID=50
    IDENTIFIER=51
    WS=52
    DIGIT=53

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AttackContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def header(self):
            return self.getTypedRuleContext(CNLParser.HeaderContext,0)


        def background(self):
            return self.getTypedRuleContext(CNLParser.BackgroundContext,0)


        def EOF(self):
            return self.getToken(CNLParser.EOF, 0)

        def eventBlock(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.EventBlockContext)
            else:
                return self.getTypedRuleContext(CNLParser.EventBlockContext,i)


        def detectionBlock(self):
            return self.getTypedRuleContext(CNLParser.DetectionBlockContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_attack

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttack" ):
                listener.enterAttack(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttack" ):
                listener.exitAttack(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttack" ):
                return visitor.visitAttack(self)
            else:
                return visitor.visitChildren(self)




    def attack(self):

        localctx = CNLParser.AttackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_attack)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.header()
            self.state = 65
            self.background()
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.eventBlock()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 71
                self.detectionBlock()


            self.state = 74
            self.match(CNLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class HeaderContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tactic(self):
            return self.getTypedRuleContext(CNLParser.TacticContext,0)


        def technique(self):
            return self.getTypedRuleContext(CNLParser.TechniqueContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_header

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHeader" ):
                listener.enterHeader(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHeader" ):
                listener.exitHeader(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHeader" ):
                return visitor.visitHeader(self)
            else:
                return visitor.visitChildren(self)




    def header(self):

        localctx = CNLParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.tactic()
            self.state = 77
            self.technique()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BackgroundContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BACKGROUND(self):
            return self.getToken(CNLParser.BACKGROUND, 0)

        def GIVEN(self):
            return self.getToken(CNLParser.GIVEN, 0)

        def assets(self):
            return self.getTypedRuleContext(CNLParser.AssetsContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_background

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBackground" ):
                listener.enterBackground(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBackground" ):
                listener.exitBackground(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBackground" ):
                return visitor.visitBackground(self)
            else:
                return visitor.visitChildren(self)




    def background(self):

        localctx = CNLParser.BackgroundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_background)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(CNLParser.BACKGROUND)
            self.state = 80
            self.match(CNLParser.GIVEN)
            self.state = 81
            self.assets()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssetsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assetDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.AssetDefinitionContext)
            else:
                return self.getTypedRuleContext(CNLParser.AssetDefinitionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.AND)
            else:
                return self.getToken(CNLParser.AND, i)

        def getRuleIndex(self):
            return CNLParser.RULE_assets

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssets" ):
                listener.enterAssets(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssets" ):
                listener.exitAssets(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssets" ):
                return visitor.visitAssets(self)
            else:
                return visitor.visitChildren(self)




    def assets(self):

        localctx = CNLParser.AssetsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assets)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.assetDefinition()
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 84
                self.match(CNLParser.AND)
                self.state = 85
                self.assetDefinition()
                self.state = 90
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssetDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assetType(self):
            return self.getTypedRuleContext(CNLParser.AssetTypeContext,0)


        def AS(self):
            return self.getToken(CNLParser.AS, 0)

        def assetName(self):
            return self.getTypedRuleContext(CNLParser.AssetNameContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_assetDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssetDefinition" ):
                listener.enterAssetDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssetDefinition" ):
                listener.exitAssetDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssetDefinition" ):
                return visitor.visitAssetDefinition(self)
            else:
                return visitor.visitChildren(self)




    def assetDefinition(self):

        localctx = CNLParser.AssetDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assetDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.assetType()
            self.state = 92
            self.match(CNLParser.AS)
            self.state = 93
            self.assetName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssetTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_assetType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssetType" ):
                listener.enterAssetType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssetType" ):
                listener.exitAssetType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssetType" ):
                return visitor.visitAssetType(self)
            else:
                return visitor.visitChildren(self)




    def assetType(self):

        localctx = CNLParser.AssetTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assetType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(CNLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssetNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_assetName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssetName" ):
                listener.enterAssetName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssetName" ):
                listener.exitAssetName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssetName" ):
                return visitor.visitAssetName(self)
            else:
                return visitor.visitChildren(self)




    def assetName(self):

        localctx = CNLParser.AssetNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assetName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(CNLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TacticContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TACTIC(self):
            return self.getToken(CNLParser.TACTIC, 0)

        def COLON(self):
            return self.getToken(CNLParser.COLON, 0)

        def TACTIC_ID(self):
            return self.getToken(CNLParser.TACTIC_ID, 0)

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_tactic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTactic" ):
                listener.enterTactic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTactic" ):
                listener.exitTactic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTactic" ):
                return visitor.visitTactic(self)
            else:
                return visitor.visitChildren(self)




    def tactic(self):

        localctx = CNLParser.TacticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tactic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(CNLParser.TACTIC)
            self.state = 100
            self.match(CNLParser.COLON)
            self.state = 101
            self.match(CNLParser.TACTIC_ID)
            self.state = 102
            self.match(CNLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TechniqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TECHNIQUE(self):
            return self.getToken(CNLParser.TECHNIQUE, 0)

        def COLON(self):
            return self.getToken(CNLParser.COLON, 0)

        def TECHNIQUE_ID(self):
            return self.getToken(CNLParser.TECHNIQUE_ID, 0)

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_technique

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTechnique" ):
                listener.enterTechnique(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTechnique" ):
                listener.exitTechnique(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTechnique" ):
                return visitor.visitTechnique(self)
            else:
                return visitor.visitChildren(self)




    def technique(self):

        localctx = CNLParser.TechniqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_technique)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(CNLParser.TECHNIQUE)
            self.state = 105
            self.match(CNLParser.COLON)
            self.state = 106
            self.match(CNLParser.TECHNIQUE_ID)
            self.state = 107
            self.match(CNLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVENT(self):
            return self.getToken(CNLParser.EVENT, 0)

        def DIGIT(self):
            return self.getToken(CNLParser.DIGIT, 0)

        def eventStatement(self):
            return self.getTypedRuleContext(CNLParser.EventStatementContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_eventBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventBlock" ):
                listener.enterEventBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventBlock" ):
                listener.exitEventBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventBlock" ):
                return visitor.visitEventBlock(self)
            else:
                return visitor.visitChildren(self)




    def eventBlock(self):

        localctx = CNLParser.EventBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_eventBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(CNLParser.EVENT)
            self.state = 110
            self.match(CNLParser.DIGIT)
            self.state = 111
            self.eventStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def givenClause(self):
            return self.getTypedRuleContext(CNLParser.GivenClauseContext,0)


        def whenClause(self):
            return self.getTypedRuleContext(CNLParser.WhenClauseContext,0)


        def thenClause(self):
            return self.getTypedRuleContext(CNLParser.ThenClauseContext,0)


        def REPEATED(self):
            return self.getToken(CNLParser.REPEATED, 0)

        def lineText(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.LineTextContext)
            else:
                return self.getTypedRuleContext(CNLParser.LineTextContext,i)


        def WITHIN(self):
            return self.getToken(CNLParser.WITHIN, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_eventStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventStatement" ):
                listener.enterEventStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventStatement" ):
                listener.exitEventStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventStatement" ):
                return visitor.visitEventStatement(self)
            else:
                return visitor.visitChildren(self)




    def eventStatement(self):

        localctx = CNLParser.EventStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_eventStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.givenClause()
            self.state = 114
            self.whenClause()
            self.state = 115
            self.thenClause()
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 116
                self.match(CNLParser.REPEATED)
                self.state = 117
                self.lineText()


            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 120
                self.match(CNLParser.WITHIN)
                self.state = 121
                self.lineText()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GivenClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GIVEN(self):
            return self.getToken(CNLParser.GIVEN, 0)

        def givenItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.GivenItemContext)
            else:
                return self.getTypedRuleContext(CNLParser.GivenItemContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.AND)
            else:
                return self.getToken(CNLParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.OR)
            else:
                return self.getToken(CNLParser.OR, i)

        def getRuleIndex(self):
            return CNLParser.RULE_givenClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGivenClause" ):
                listener.enterGivenClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGivenClause" ):
                listener.exitGivenClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGivenClause" ):
                return visitor.visitGivenClause(self)
            else:
                return visitor.visitChildren(self)




    def givenClause(self):

        localctx = CNLParser.GivenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_givenClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(CNLParser.GIVEN)
            self.state = 125
            self.givenItem()
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==10:
                    self.state = 126
                    self.match(CNLParser.AND)
                    self.state = 127
                    self.givenItem()
                    self.state = 132
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 137
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==11:
                    self.state = 133
                    self.match(CNLParser.OR)
                    self.state = 134
                    self.givenItem()
                    self.state = 139
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GivenItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eventRef(self):
            return self.getTypedRuleContext(CNLParser.EventRefContext,0)


        def stateCondition(self):
            return self.getTypedRuleContext(CNLParser.StateConditionContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_givenItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGivenItem" ):
                listener.enterGivenItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGivenItem" ):
                listener.exitGivenItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGivenItem" ):
                return visitor.visitGivenItem(self)
            else:
                return visitor.visitChildren(self)




    def givenItem(self):

        localctx = CNLParser.GivenItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_givenItem)
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.eventRef()
                pass
            elif token in [51]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
                self.stateCondition()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EventRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EVENT(self):
            return self.getToken(CNLParser.EVENT, 0)

        def DIGIT(self):
            return self.getToken(CNLParser.DIGIT, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_eventRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventRef" ):
                listener.enterEventRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventRef" ):
                listener.exitEventRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEventRef" ):
                return visitor.visitEventRef(self)
            else:
                return visitor.visitChildren(self)




    def eventRef(self):

        localctx = CNLParser.EventRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_eventRef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(CNLParser.EVENT)
            self.state = 147
            self.match(CNLParser.DIGIT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhenClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(CNLParser.WHEN, 0)

        def action(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.ActionContext)
            else:
                return self.getTypedRuleContext(CNLParser.ActionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.AND)
            else:
                return self.getToken(CNLParser.AND, i)

        def getRuleIndex(self):
            return CNLParser.RULE_whenClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhenClause" ):
                listener.enterWhenClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhenClause" ):
                listener.exitWhenClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhenClause" ):
                return visitor.visitWhenClause(self)
            else:
                return visitor.visitChildren(self)




    def whenClause(self):

        localctx = CNLParser.WhenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_whenClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(CNLParser.WHEN)
            self.state = 150
            self.action()

            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 151
                self.match(CNLParser.AND)
                self.state = 152
                self.action()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def actor(self):
            return self.getTypedRuleContext(CNLParser.ActorContext,0)


        def actionVerb(self):
            return self.getTypedRuleContext(CNLParser.ActionVerbContext,0)


        def actionObject(self):
            return self.getTypedRuleContext(CNLParser.ActionObjectContext,0)


        def adjective(self):
            return self.getTypedRuleContext(CNLParser.AdjectiveContext,0)


        def modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.ModifierContext)
            else:
                return self.getTypedRuleContext(CNLParser.ModifierContext,i)


        def getRuleIndex(self):
            return CNLParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAction" ):
                return visitor.visitAction(self)
            else:
                return visitor.visitChildren(self)




    def action(self):

        localctx = CNLParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.actor()
            self.state = 159
            self.actionVerb()
            self.state = 161
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 160
                self.adjective()


            self.state = 163
            self.actionObject()
            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0):
                self.state = 164
                self.modifier()
                self.state = 169
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assetName(self):
            return self.getTypedRuleContext(CNLParser.AssetNameContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_actor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActor" ):
                listener.enterActor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActor" ):
                listener.exitActor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActor" ):
                return visitor.visitActor(self)
            else:
                return visitor.visitChildren(self)




    def actor(self):

        localctx = CNLParser.ActorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_actor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.assetName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdjectiveContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_adjective

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdjective" ):
                listener.enterAdjective(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdjective" ):
                listener.exitAdjective(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdjective" ):
                return visitor.visitAdjective(self)
            else:
                return visitor.visitChildren(self)




    def adjective(self):

        localctx = CNLParser.AdjectiveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_adjective)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(CNLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_actionObject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionObject" ):
                listener.enterActionObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionObject" ):
                listener.exitActionObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionObject" ):
                return visitor.visitActionObject(self)
            else:
                return visitor.visitChildren(self)




    def actionObject(self):

        localctx = CNLParser.ActionObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_actionObject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(CNLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionVerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPAWNS(self):
            return self.getToken(CNLParser.SPAWNS, 0)

        def CREATES(self):
            return self.getToken(CNLParser.CREATES, 0)

        def EXECUTES(self):
            return self.getToken(CNLParser.EXECUTES, 0)

        def LOADS(self):
            return self.getToken(CNLParser.LOADS, 0)

        def REQUESTS(self):
            return self.getToken(CNLParser.REQUESTS, 0)

        def RECEIVES(self):
            return self.getToken(CNLParser.RECEIVES, 0)

        def SENDS(self):
            return self.getToken(CNLParser.SENDS, 0)

        def MOUNTS(self):
            return self.getToken(CNLParser.MOUNTS, 0)

        def MODIFIES(self):
            return self.getToken(CNLParser.MODIFIES, 0)

        def RECORDS(self):
            return self.getToken(CNLParser.RECORDS, 0)

        def RAISES(self):
            return self.getToken(CNLParser.RAISES, 0)

        def PERFORMS(self):
            return self.getToken(CNLParser.PERFORMS, 0)

        def RECOGNIZES(self):
            return self.getToken(CNLParser.RECOGNIZES, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_actionVerb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionVerb" ):
                listener.enterActionVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionVerb" ):
                listener.exitActionVerb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActionVerb" ):
                return visitor.visitActionVerb(self)
            else:
                return visitor.visitChildren(self)




    def actionVerb(self):

        localctx = CNLParser.ActionVerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_actionVerb)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 68711088128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def location(self):
            return self.getTypedRuleContext(CNLParser.LocationContext,0)


        def destination(self):
            return self.getTypedRuleContext(CNLParser.DestinationContext,0)


        def source(self):
            return self.getTypedRuleContext(CNLParser.SourceContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifier" ):
                listener.enterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifier" ):
                listener.exitModifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifier" ):
                return visitor.visitModifier(self)
            else:
                return visitor.visitChildren(self)




    def modifier(self):

        localctx = CNLParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_modifier)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                self.location()
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 179
                self.destination()
                pass
            elif token in [21, 22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 180
                self.source()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThenClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THEN(self):
            return self.getToken(CNLParser.THEN, 0)

        def stateCondition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.StateConditionContext)
            else:
                return self.getTypedRuleContext(CNLParser.StateConditionContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.AND)
            else:
                return self.getToken(CNLParser.AND, i)

        def getRuleIndex(self):
            return CNLParser.RULE_thenClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThenClause" ):
                listener.enterThenClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThenClause" ):
                listener.exitThenClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThenClause" ):
                return visitor.visitThenClause(self)
            else:
                return visitor.visitChildren(self)




    def thenClause(self):

        localctx = CNLParser.ThenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_thenClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(CNLParser.THEN)
            self.state = 184
            self.stateCondition()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10:
                self.state = 185
                self.match(CNLParser.AND)
                self.state = 186
                self.stateCondition()
                self.state = 191
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionObject(self):
            return self.getTypedRuleContext(CNLParser.ConditionObjectContext,0)


        def stateVerb(self):
            return self.getTypedRuleContext(CNLParser.StateVerbContext,0)


        def modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.ModifierContext)
            else:
                return self.getTypedRuleContext(CNLParser.ModifierContext,i)


        def getRuleIndex(self):
            return CNLParser.RULE_stateCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateCondition" ):
                listener.enterStateCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateCondition" ):
                listener.exitStateCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateCondition" ):
                return visitor.visitStateCondition(self)
            else:
                return visitor.visitChildren(self)




    def stateCondition(self):

        localctx = CNLParser.StateConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stateCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.conditionObject()
            self.state = 193
            self.stateVerb()
            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0):
                self.state = 194
                self.modifier()
                self.state = 199
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_conditionObject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionObject" ):
                listener.enterConditionObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionObject" ):
                listener.exitConditionObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionObject" ):
                return visitor.visitConditionObject(self)
            else:
                return visitor.visitChildren(self)




    def conditionObject(self):

        localctx = CNLParser.ConditionObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_conditionObject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.match(CNLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StateVerbContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IS(self):
            return self.getToken(CNLParser.IS, 0)

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def pastParticiple(self):
            return self.getTypedRuleContext(CNLParser.PastParticipleContext,0)


        def modifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.ModifierContext)
            else:
                return self.getTypedRuleContext(CNLParser.ModifierContext,i)


        def getRuleIndex(self):
            return CNLParser.RULE_stateVerb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateVerb" ):
                listener.enterStateVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateVerb" ):
                listener.exitStateVerb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStateVerb" ):
                return visitor.visitStateVerb(self)
            else:
                return visitor.visitChildren(self)




    def stateVerb(self):

        localctx = CNLParser.StateVerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stateVerb)
        try:
            self.state = 212
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.match(CNLParser.IS)
                self.state = 203
                self.match(CNLParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(CNLParser.IS)
                self.state = 205
                self.pastParticiple()
                self.state = 209
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 206
                        self.modifier() 
                    self.state = 211
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PastParticipleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SPAWNED(self):
            return self.getToken(CNLParser.SPAWNED, 0)

        def CREATED(self):
            return self.getToken(CNLParser.CREATED, 0)

        def EXECUTED(self):
            return self.getToken(CNLParser.EXECUTED, 0)

        def LOADED(self):
            return self.getToken(CNLParser.LOADED, 0)

        def REQUESTED(self):
            return self.getToken(CNLParser.REQUESTED, 0)

        def RECEIVED(self):
            return self.getToken(CNLParser.RECEIVED, 0)

        def SENT(self):
            return self.getToken(CNLParser.SENT, 0)

        def MOUNTED(self):
            return self.getToken(CNLParser.MOUNTED, 0)

        def MODIFIED(self):
            return self.getToken(CNLParser.MODIFIED, 0)

        def RECORDED(self):
            return self.getToken(CNLParser.RECORDED, 0)

        def RAISED(self):
            return self.getToken(CNLParser.RAISED, 0)

        def PERFORMED(self):
            return self.getToken(CNLParser.PERFORMED, 0)

        def RECOGNIZED(self):
            return self.getToken(CNLParser.RECOGNIZED, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_pastParticiple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPastParticiple" ):
                listener.enterPastParticiple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPastParticiple" ):
                listener.exitPastParticiple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPastParticiple" ):
                return visitor.visitPastParticiple(self)
            else:
                return visitor.visitChildren(self)




    def pastParticiple(self):

        localctx = CNLParser.PastParticipleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_pastParticiple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 562881233944576) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IN(self):
            return self.getToken(CNLParser.IN, 0)

        def assetName(self):
            return self.getTypedRuleContext(CNLParser.AssetNameContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLocation" ):
                listener.enterLocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLocation" ):
                listener.exitLocation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLocation" ):
                return visitor.visitLocation(self)
            else:
                return visitor.visitChildren(self)




    def location(self):

        localctx = CNLParser.LocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(CNLParser.IN)
            self.state = 217
            self.assetName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DestinationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TO(self):
            return self.getToken(CNLParser.TO, 0)

        def assetName(self):
            return self.getTypedRuleContext(CNLParser.AssetNameContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_destination

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDestination" ):
                listener.enterDestination(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDestination" ):
                listener.exitDestination(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDestination" ):
                return visitor.visitDestination(self)
            else:
                return visitor.visitChildren(self)




    def destination(self):

        localctx = CNLParser.DestinationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_destination)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(CNLParser.TO)
            self.state = 220
            self.assetName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(CNLParser.BY, 0)

        def assetName(self):
            return self.getTypedRuleContext(CNLParser.AssetNameContext,0)


        def FROM(self):
            return self.getToken(CNLParser.FROM, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_source

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSource" ):
                listener.enterSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSource" ):
                listener.exitSource(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSource" ):
                return visitor.visitSource(self)
            else:
                return visitor.visitChildren(self)




    def source(self):

        localctx = CNLParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_source)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(CNLParser.BY)
                self.state = 223
                self.assetName()
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(CNLParser.FROM)
                self.state = 225
                self.assetName()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DetectionBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DETECTION(self):
            return self.getToken(CNLParser.DETECTION, 0)

        def detectionExpr(self):
            return self.getTypedRuleContext(CNLParser.DetectionExprContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_detectionBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetectionBlock" ):
                listener.enterDetectionBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetectionBlock" ):
                listener.exitDetectionBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetectionBlock" ):
                return visitor.visitDetectionBlock(self)
            else:
                return visitor.visitChildren(self)




    def detectionBlock(self):

        localctx = CNLParser.DetectionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_detectionBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(CNLParser.DETECTION)
            self.state = 229
            self.detectionExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DetectionExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eventRef(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.EventRefContext)
            else:
                return self.getTypedRuleContext(CNLParser.EventRefContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.AND)
            else:
                return self.getToken(CNLParser.AND, i)

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.OR)
            else:
                return self.getToken(CNLParser.OR, i)

        def getRuleIndex(self):
            return CNLParser.RULE_detectionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetectionExpr" ):
                listener.enterDetectionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetectionExpr" ):
                listener.exitDetectionExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDetectionExpr" ):
                return visitor.visitDetectionExpr(self)
            else:
                return visitor.visitChildren(self)




    def detectionExpr(self):

        localctx = CNLParser.DetectionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_detectionExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.eventRef()
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==10 or _la==11:
                self.state = 232
                _la = self._input.LA(1)
                if not(_la==10 or _la==11):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 233
                self.eventRef()
                self.state = 238
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineTextContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CNLParser.STRING, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_lineText

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLineText" ):
                listener.enterLineText(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLineText" ):
                listener.exitLineText(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLineText" ):
                return visitor.visitLineText(self)
            else:
                return visitor.visitChildren(self)




    def lineText(self):

        localctx = CNLParser.LineTextContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_lineText)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.match(CNLParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





