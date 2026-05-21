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
        4,1,34,292,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,1,0,1,0,1,
        0,4,0,82,8,0,11,0,12,0,83,1,0,3,0,87,8,0,1,0,1,0,1,1,1,1,1,1,1,2,
        1,2,1,2,1,2,1,3,1,3,1,3,5,3,101,8,3,10,3,12,3,104,9,3,1,4,1,4,1,
        4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,7,1,7,1,7,5,7,119,8,7,10,7,12,7,
        122,9,7,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,10,1,10,4,10,134,8,10,
        11,10,12,10,135,1,10,1,10,3,10,140,8,10,1,10,3,10,143,8,10,1,11,
        1,11,1,11,1,11,1,12,1,12,1,12,1,12,5,12,153,8,12,10,12,12,12,156,
        9,12,1,12,1,12,5,12,160,8,12,10,12,12,12,163,9,12,1,12,1,12,5,12,
        167,8,12,10,12,12,12,170,9,12,3,12,172,8,12,1,13,1,13,3,13,176,8,
        13,1,14,1,14,4,14,180,8,14,11,14,12,14,181,1,15,1,15,1,15,1,16,1,
        16,1,16,1,16,5,16,191,8,16,10,16,12,16,194,9,16,1,17,1,17,1,18,1,
        18,1,19,1,19,1,20,1,20,1,20,1,20,3,20,206,8,20,1,21,1,21,1,21,1,
        21,5,21,212,8,21,10,21,12,21,215,9,21,1,22,1,22,1,22,5,22,220,8,
        22,10,22,12,22,223,9,22,1,23,1,23,1,24,1,24,1,24,3,24,230,8,24,1,
        25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,3,27,242,8,27,1,
        28,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,31,1,31,3,31,254,8,31,1,
        32,1,32,4,32,258,8,32,11,32,12,32,259,1,32,3,32,263,8,32,1,32,1,
        32,1,33,1,33,1,34,1,34,4,34,271,8,34,11,34,12,34,272,1,34,1,34,1,
        35,1,35,1,36,1,36,1,37,1,37,1,37,1,38,1,38,1,38,5,38,287,8,38,10,
        38,12,38,290,9,38,1,38,0,0,39,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        70,72,74,76,0,3,2,0,20,20,22,22,1,0,26,29,1,0,7,9,279,0,78,1,0,0,
        0,2,90,1,0,0,0,4,93,1,0,0,0,6,97,1,0,0,0,8,105,1,0,0,0,10,109,1,
        0,0,0,12,111,1,0,0,0,14,113,1,0,0,0,16,123,1,0,0,0,18,126,1,0,0,
        0,20,131,1,0,0,0,22,144,1,0,0,0,24,148,1,0,0,0,26,175,1,0,0,0,28,
        177,1,0,0,0,30,183,1,0,0,0,32,186,1,0,0,0,34,195,1,0,0,0,36,197,
        1,0,0,0,38,199,1,0,0,0,40,205,1,0,0,0,42,207,1,0,0,0,44,216,1,0,
        0,0,46,224,1,0,0,0,48,229,1,0,0,0,50,231,1,0,0,0,52,234,1,0,0,0,
        54,241,1,0,0,0,56,243,1,0,0,0,58,246,1,0,0,0,60,249,1,0,0,0,62,251,
        1,0,0,0,64,255,1,0,0,0,66,266,1,0,0,0,68,268,1,0,0,0,70,276,1,0,
        0,0,72,278,1,0,0,0,74,280,1,0,0,0,76,283,1,0,0,0,78,79,3,2,1,0,79,
        81,3,4,2,0,80,82,3,20,10,0,81,80,1,0,0,0,82,83,1,0,0,0,83,81,1,0,
        0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,87,3,74,37,0,86,85,1,0,0,0,86,
        87,1,0,0,0,87,88,1,0,0,0,88,89,5,0,0,1,89,1,1,0,0,0,90,91,3,14,7,
        0,91,92,3,18,9,0,92,3,1,0,0,0,93,94,5,12,0,0,94,95,5,4,0,0,95,96,
        3,6,3,0,96,5,1,0,0,0,97,102,3,8,4,0,98,99,5,7,0,0,99,101,3,8,4,0,
        100,98,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,0,0,0,103,
        7,1,0,0,0,104,102,1,0,0,0,105,106,3,10,5,0,106,107,5,11,0,0,107,
        108,3,12,6,0,108,9,1,0,0,0,109,110,5,32,0,0,110,11,1,0,0,0,111,112,
        5,32,0,0,112,13,1,0,0,0,113,114,5,1,0,0,114,115,5,10,0,0,115,120,
        3,16,8,0,116,117,5,21,0,0,117,119,3,16,8,0,118,116,1,0,0,0,119,122,
        1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,15,1,0,0,0,122,120,1,
        0,0,0,123,124,5,30,0,0,124,125,5,32,0,0,125,17,1,0,0,0,126,127,5,
        2,0,0,127,128,5,10,0,0,128,129,5,31,0,0,129,130,5,32,0,0,130,19,
        1,0,0,0,131,133,5,3,0,0,132,134,5,34,0,0,133,132,1,0,0,0,134,135,
        1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,139,
        3,22,11,0,138,140,3,62,31,0,139,138,1,0,0,0,139,140,1,0,0,0,140,
        142,1,0,0,0,141,143,3,56,28,0,142,141,1,0,0,0,142,143,1,0,0,0,143,
        21,1,0,0,0,144,145,3,24,12,0,145,146,3,30,15,0,146,147,3,42,21,0,
        147,23,1,0,0,0,148,149,5,4,0,0,149,171,3,26,13,0,150,151,5,7,0,0,
        151,153,3,26,13,0,152,150,1,0,0,0,153,156,1,0,0,0,154,152,1,0,0,
        0,154,155,1,0,0,0,155,172,1,0,0,0,156,154,1,0,0,0,157,158,5,8,0,
        0,158,160,3,26,13,0,159,157,1,0,0,0,160,163,1,0,0,0,161,159,1,0,
        0,0,161,162,1,0,0,0,162,172,1,0,0,0,163,161,1,0,0,0,164,165,5,9,
        0,0,165,167,3,26,13,0,166,164,1,0,0,0,167,170,1,0,0,0,168,166,1,
        0,0,0,168,169,1,0,0,0,169,172,1,0,0,0,170,168,1,0,0,0,171,154,1,
        0,0,0,171,161,1,0,0,0,171,168,1,0,0,0,172,25,1,0,0,0,173,176,3,28,
        14,0,174,176,3,44,22,0,175,173,1,0,0,0,175,174,1,0,0,0,176,27,1,
        0,0,0,177,179,5,3,0,0,178,180,5,34,0,0,179,178,1,0,0,0,180,181,1,
        0,0,0,181,179,1,0,0,0,181,182,1,0,0,0,182,29,1,0,0,0,183,184,5,5,
        0,0,184,185,3,32,16,0,185,31,1,0,0,0,186,187,3,34,17,0,187,188,3,
        38,19,0,188,192,3,36,18,0,189,191,3,40,20,0,190,189,1,0,0,0,191,
        194,1,0,0,0,192,190,1,0,0,0,192,193,1,0,0,0,193,33,1,0,0,0,194,192,
        1,0,0,0,195,196,3,12,6,0,196,35,1,0,0,0,197,198,3,12,6,0,198,37,
        1,0,0,0,199,200,5,32,0,0,200,39,1,0,0,0,201,206,3,50,25,0,202,206,
        3,52,26,0,203,206,3,54,27,0,204,206,3,58,29,0,205,201,1,0,0,0,205,
        202,1,0,0,0,205,203,1,0,0,0,205,204,1,0,0,0,206,41,1,0,0,0,207,208,
        5,6,0,0,208,213,3,44,22,0,209,210,5,7,0,0,210,212,3,44,22,0,211,
        209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,
        43,1,0,0,0,215,213,1,0,0,0,216,217,3,46,23,0,217,221,3,48,24,0,218,
        220,3,40,20,0,219,218,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,221,
        222,1,0,0,0,222,45,1,0,0,0,223,221,1,0,0,0,224,225,3,12,6,0,225,
        47,1,0,0,0,226,227,5,14,0,0,227,230,5,32,0,0,228,230,5,32,0,0,229,
        226,1,0,0,0,229,228,1,0,0,0,230,49,1,0,0,0,231,232,5,15,0,0,232,
        233,3,12,6,0,233,51,1,0,0,0,234,235,5,16,0,0,235,236,3,12,6,0,236,
        53,1,0,0,0,237,238,5,17,0,0,238,242,3,12,6,0,239,240,5,18,0,0,240,
        242,3,12,6,0,241,237,1,0,0,0,241,239,1,0,0,0,242,55,1,0,0,0,243,
        244,3,60,30,0,244,245,3,66,33,0,245,57,1,0,0,0,246,247,5,19,0,0,
        247,248,3,72,36,0,248,59,1,0,0,0,249,250,7,0,0,0,250,61,1,0,0,0,
        251,253,3,64,32,0,252,254,3,68,34,0,253,252,1,0,0,0,253,254,1,0,
        0,0,254,63,1,0,0,0,255,262,5,23,0,0,256,258,5,34,0,0,257,256,1,0,
        0,0,258,259,1,0,0,0,259,257,1,0,0,0,259,260,1,0,0,0,260,263,1,0,
        0,0,261,263,5,32,0,0,262,257,1,0,0,0,262,261,1,0,0,0,263,264,1,0,
        0,0,264,265,5,24,0,0,265,65,1,0,0,0,266,267,5,32,0,0,267,67,1,0,
        0,0,268,270,5,25,0,0,269,271,5,34,0,0,270,269,1,0,0,0,271,272,1,
        0,0,0,272,270,1,0,0,0,272,273,1,0,0,0,273,274,1,0,0,0,274,275,3,
        70,35,0,275,69,1,0,0,0,276,277,7,1,0,0,277,71,1,0,0,0,278,279,5,
        32,0,0,279,73,1,0,0,0,280,281,5,13,0,0,281,282,3,76,38,0,282,75,
        1,0,0,0,283,288,3,28,14,0,284,285,7,2,0,0,285,287,3,28,14,0,286,
        284,1,0,0,0,287,290,1,0,0,0,288,286,1,0,0,0,288,289,1,0,0,0,289,
        77,1,0,0,0,290,288,1,0,0,0,24,83,86,102,120,135,139,142,154,161,
        168,171,175,181,192,205,213,221,229,241,253,259,262,272,288
    ]

class CNLParser ( Parser ):

    grammarFileName = "CNL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Tactics'", "'Technique'", "'Event'", 
                     "'Given'", "'When'", "'Then'", "'And'", "'Or'", "'Xor'", 
                     "':'", "'as'", "'Background'", "'Detection'", "'is'", 
                     "'in'", "'to'", "'by'", "'from'", "'located_at'", "'During'", 
                     "','", "'Outside'", "'Repeated'", "'times'", "'within'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'hours'" ]

    symbolicNames = [ "<INVALID>", "TACTICS", "TECHNIQUE", "EVENT", "GIVEN", 
                      "WHEN", "THEN", "AND", "OR", "XOR", "COLON", "AS", 
                      "BACKGROUND", "DETECTION", "IS", "IN", "TO", "BY", 
                      "FROM", "LOCATED_AT", "DURING", "COMMA", "OUTSIDE", 
                      "REPEATED", "TIMES", "WITHIN", "MILLISECONDS", "SECONDS", 
                      "MINUTES", "HOURS", "TACTIC_ID", "TECHNIQUE_ID", "IDENTIFIER", 
                      "WS", "DIGIT" ]

    RULE_attack = 0
    RULE_header = 1
    RULE_background = 2
    RULE_assets = 3
    RULE_assetDefinition = 4
    RULE_assetType = 5
    RULE_assetName = 6
    RULE_tactics = 7
    RULE_tactic = 8
    RULE_technique = 9
    RULE_eventBlock = 10
    RULE_eventStatement = 11
    RULE_givenClause = 12
    RULE_givenItem = 13
    RULE_eventRef = 14
    RULE_whenClause = 15
    RULE_action = 16
    RULE_actor = 17
    RULE_actionObject = 18
    RULE_actionVerb = 19
    RULE_modifier = 20
    RULE_thenClause = 21
    RULE_stateCondition = 22
    RULE_conditionObject = 23
    RULE_stateVerb = 24
    RULE_location = 25
    RULE_destination = 26
    RULE_source = 27
    RULE_timing = 28
    RULE_geolocation = 29
    RULE_timePreposition = 30
    RULE_repetition = 31
    RULE_repeat = 32
    RULE_timePeriod = 33
    RULE_timeWindow = 34
    RULE_time = 35
    RULE_geo_location = 36
    RULE_detectionBlock = 37
    RULE_detectionExpr = 38

    ruleNames =  [ "attack", "header", "background", "assets", "assetDefinition", 
                   "assetType", "assetName", "tactics", "tactic", "technique", 
                   "eventBlock", "eventStatement", "givenClause", "givenItem", 
                   "eventRef", "whenClause", "action", "actor", "actionObject", 
                   "actionVerb", "modifier", "thenClause", "stateCondition", 
                   "conditionObject", "stateVerb", "location", "destination", 
                   "source", "timing", "geolocation", "timePreposition", 
                   "repetition", "repeat", "timePeriod", "timeWindow", "time", 
                   "geo_location", "detectionBlock", "detectionExpr" ]

    EOF = Token.EOF
    TACTICS=1
    TECHNIQUE=2
    EVENT=3
    GIVEN=4
    WHEN=5
    THEN=6
    AND=7
    OR=8
    XOR=9
    COLON=10
    AS=11
    BACKGROUND=12
    DETECTION=13
    IS=14
    IN=15
    TO=16
    BY=17
    FROM=18
    LOCATED_AT=19
    DURING=20
    COMMA=21
    OUTSIDE=22
    REPEATED=23
    TIMES=24
    WITHIN=25
    MILLISECONDS=26
    SECONDS=27
    MINUTES=28
    HOURS=29
    TACTIC_ID=30
    TECHNIQUE_ID=31
    IDENTIFIER=32
    WS=33
    DIGIT=34

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




    def attack(self):

        localctx = CNLParser.AttackContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_attack)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.header()
            self.state = 79
            self.background()
            self.state = 81 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 80
                self.eventBlock()
                self.state = 83 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==3):
                    break

            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 85
                self.detectionBlock()


            self.state = 88
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

        def tactics(self):
            return self.getTypedRuleContext(CNLParser.TacticsContext,0)


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




    def header(self):

        localctx = CNLParser.HeaderContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_header)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.tactics()
            self.state = 91
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




    def background(self):

        localctx = CNLParser.BackgroundContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_background)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(CNLParser.BACKGROUND)
            self.state = 94
            self.match(CNLParser.GIVEN)
            self.state = 95
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




    def assets(self):

        localctx = CNLParser.AssetsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assets)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.assetDefinition()
            self.state = 102
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 98
                self.match(CNLParser.AND)
                self.state = 99
                self.assetDefinition()
                self.state = 104
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




    def assetDefinition(self):

        localctx = CNLParser.AssetDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assetDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.assetType()
            self.state = 106
            self.match(CNLParser.AS)
            self.state = 107
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




    def assetType(self):

        localctx = CNLParser.AssetTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assetType)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
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




    def assetName(self):

        localctx = CNLParser.AssetNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_assetName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(CNLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TacticsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TACTICS(self):
            return self.getToken(CNLParser.TACTICS, 0)

        def COLON(self):
            return self.getToken(CNLParser.COLON, 0)

        def tactic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CNLParser.TacticContext)
            else:
                return self.getTypedRuleContext(CNLParser.TacticContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.COMMA)
            else:
                return self.getToken(CNLParser.COMMA, i)

        def getRuleIndex(self):
            return CNLParser.RULE_tactics

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTactics" ):
                listener.enterTactics(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTactics" ):
                listener.exitTactics(self)




    def tactics(self):

        localctx = CNLParser.TacticsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tactics)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(CNLParser.TACTICS)
            self.state = 114
            self.match(CNLParser.COLON)
            self.state = 115
            self.tactic()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21:
                self.state = 116
                self.match(CNLParser.COMMA)
                self.state = 117
                self.tactic()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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




    def tactic(self):

        localctx = CNLParser.TacticContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tactic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(CNLParser.TACTIC_ID)
            self.state = 124
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




    def technique(self):

        localctx = CNLParser.TechniqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_technique)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(CNLParser.TECHNIQUE)
            self.state = 127
            self.match(CNLParser.COLON)
            self.state = 128
            self.match(CNLParser.TECHNIQUE_ID)
            self.state = 129
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

        def eventStatement(self):
            return self.getTypedRuleContext(CNLParser.EventStatementContext,0)


        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.DIGIT)
            else:
                return self.getToken(CNLParser.DIGIT, i)

        def repetition(self):
            return self.getTypedRuleContext(CNLParser.RepetitionContext,0)


        def timing(self):
            return self.getTypedRuleContext(CNLParser.TimingContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_eventBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventBlock" ):
                listener.enterEventBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventBlock" ):
                listener.exitEventBlock(self)




    def eventBlock(self):

        localctx = CNLParser.EventBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_eventBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(CNLParser.EVENT)
            self.state = 133 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 132
                self.match(CNLParser.DIGIT)
                self.state = 135 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
                    break

            self.state = 137
            self.eventStatement()
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==23:
                self.state = 138
                self.repetition()


            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20 or _la==22:
                self.state = 141
                self.timing()


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


        def getRuleIndex(self):
            return CNLParser.RULE_eventStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventStatement" ):
                listener.enterEventStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventStatement" ):
                listener.exitEventStatement(self)




    def eventStatement(self):

        localctx = CNLParser.EventStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_eventStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.givenClause()
            self.state = 145
            self.whenClause()
            self.state = 146
            self.thenClause()
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

        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.XOR)
            else:
                return self.getToken(CNLParser.XOR, i)

        def getRuleIndex(self):
            return CNLParser.RULE_givenClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGivenClause" ):
                listener.enterGivenClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGivenClause" ):
                listener.exitGivenClause(self)




    def givenClause(self):

        localctx = CNLParser.GivenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_givenClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.match(CNLParser.GIVEN)
            self.state = 149
            self.givenItem()
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==7:
                    self.state = 150
                    self.match(CNLParser.AND)
                    self.state = 151
                    self.givenItem()
                    self.state = 156
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 2:
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==8:
                    self.state = 157
                    self.match(CNLParser.OR)
                    self.state = 158
                    self.givenItem()
                    self.state = 163
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass

            elif la_ == 3:
                self.state = 168
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==9:
                    self.state = 164
                    self.match(CNLParser.XOR)
                    self.state = 165
                    self.givenItem()
                    self.state = 170
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




    def givenItem(self):

        localctx = CNLParser.GivenItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_givenItem)
        try:
            self.state = 175
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self.eventRef()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 174
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

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.DIGIT)
            else:
                return self.getToken(CNLParser.DIGIT, i)

        def getRuleIndex(self):
            return CNLParser.RULE_eventRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEventRef" ):
                listener.enterEventRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEventRef" ):
                listener.exitEventRef(self)




    def eventRef(self):

        localctx = CNLParser.EventRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_eventRef)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(CNLParser.EVENT)
            self.state = 179 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 178
                self.match(CNLParser.DIGIT)
                self.state = 181 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
                    break

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

        def action(self):
            return self.getTypedRuleContext(CNLParser.ActionContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_whenClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhenClause" ):
                listener.enterWhenClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhenClause" ):
                listener.exitWhenClause(self)




    def whenClause(self):

        localctx = CNLParser.WhenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_whenClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(CNLParser.WHEN)
            self.state = 184
            self.action()
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




    def action(self):

        localctx = CNLParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.actor()
            self.state = 187
            self.actionVerb()
            self.state = 188
            self.actionObject()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0):
                self.state = 189
                self.modifier()
                self.state = 194
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




    def actor(self):

        localctx = CNLParser.ActorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_actor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.assetName()
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

        def assetName(self):
            return self.getTypedRuleContext(CNLParser.AssetNameContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_actionObject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionObject" ):
                listener.enterActionObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionObject" ):
                listener.exitActionObject(self)




    def actionObject(self):

        localctx = CNLParser.ActionObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_actionObject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.assetName()
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

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_actionVerb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActionVerb" ):
                listener.enterActionVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActionVerb" ):
                listener.exitActionVerb(self)




    def actionVerb(self):

        localctx = CNLParser.ActionVerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_actionVerb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(CNLParser.IDENTIFIER)
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


        def geolocation(self):
            return self.getTypedRuleContext(CNLParser.GeolocationContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifier" ):
                listener.enterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifier" ):
                listener.exitModifier(self)




    def modifier(self):

        localctx = CNLParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_modifier)
        try:
            self.state = 205
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.location()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.destination()
                pass
            elif token in [17, 18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.source()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.geolocation()
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




    def thenClause(self):

        localctx = CNLParser.ThenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_thenClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(CNLParser.THEN)
            self.state = 208
            self.stateCondition()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 209
                self.match(CNLParser.AND)
                self.state = 210
                self.stateCondition()
                self.state = 215
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




    def stateCondition(self):

        localctx = CNLParser.StateConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_stateCondition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.conditionObject()
            self.state = 217
            self.stateVerb()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0):
                self.state = 218
                self.modifier()
                self.state = 223
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

        def assetName(self):
            return self.getTypedRuleContext(CNLParser.AssetNameContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_conditionObject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionObject" ):
                listener.enterConditionObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionObject" ):
                listener.exitConditionObject(self)




    def conditionObject(self):

        localctx = CNLParser.ConditionObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_conditionObject)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.assetName()
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

        def getRuleIndex(self):
            return CNLParser.RULE_stateVerb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStateVerb" ):
                listener.enterStateVerb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStateVerb" ):
                listener.exitStateVerb(self)




    def stateVerb(self):

        localctx = CNLParser.StateVerbContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_stateVerb)
        try:
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(CNLParser.IS)
                self.state = 227
                self.match(CNLParser.IDENTIFIER)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.match(CNLParser.IDENTIFIER)
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




    def location(self):

        localctx = CNLParser.LocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(CNLParser.IN)
            self.state = 232
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




    def destination(self):

        localctx = CNLParser.DestinationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_destination)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(CNLParser.TO)
            self.state = 235
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




    def source(self):

        localctx = CNLParser.SourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_source)
        try:
            self.state = 241
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17]:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.match(CNLParser.BY)
                self.state = 238
                self.assetName()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 2)
                self.state = 239
                self.match(CNLParser.FROM)
                self.state = 240
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


    class TimingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def timePreposition(self):
            return self.getTypedRuleContext(CNLParser.TimePrepositionContext,0)


        def timePeriod(self):
            return self.getTypedRuleContext(CNLParser.TimePeriodContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_timing

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTiming" ):
                listener.enterTiming(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTiming" ):
                listener.exitTiming(self)




    def timing(self):

        localctx = CNLParser.TimingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_timing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.timePreposition()
            self.state = 244
            self.timePeriod()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GeolocationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LOCATED_AT(self):
            return self.getToken(CNLParser.LOCATED_AT, 0)

        def geo_location(self):
            return self.getTypedRuleContext(CNLParser.Geo_locationContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_geolocation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeolocation" ):
                listener.enterGeolocation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeolocation" ):
                listener.exitGeolocation(self)




    def geolocation(self):

        localctx = CNLParser.GeolocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_geolocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
            self.match(CNLParser.LOCATED_AT)
            self.state = 247
            self.geo_location()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimePrepositionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DURING(self):
            return self.getToken(CNLParser.DURING, 0)

        def OUTSIDE(self):
            return self.getToken(CNLParser.OUTSIDE, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_timePreposition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimePreposition" ):
                listener.enterTimePreposition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimePreposition" ):
                listener.exitTimePreposition(self)




    def timePreposition(self):

        localctx = CNLParser.TimePrepositionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_timePreposition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            _la = self._input.LA(1)
            if not(_la==20 or _la==22):
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


    class RepetitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def repeat(self):
            return self.getTypedRuleContext(CNLParser.RepeatContext,0)


        def timeWindow(self):
            return self.getTypedRuleContext(CNLParser.TimeWindowContext,0)


        def getRuleIndex(self):
            return CNLParser.RULE_repetition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetition" ):
                listener.enterRepetition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetition" ):
                listener.exitRepetition(self)




    def repetition(self):

        localctx = CNLParser.RepetitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_repetition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.repeat()
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==25:
                self.state = 252
                self.timeWindow()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepeatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REPEATED(self):
            return self.getToken(CNLParser.REPEATED, 0)

        def TIMES(self):
            return self.getToken(CNLParser.TIMES, 0)

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.DIGIT)
            else:
                return self.getToken(CNLParser.DIGIT, i)

        def getRuleIndex(self):
            return CNLParser.RULE_repeat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepeat" ):
                listener.enterRepeat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepeat" ):
                listener.exitRepeat(self)




    def repeat(self):

        localctx = CNLParser.RepeatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_repeat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255
            self.match(CNLParser.REPEATED)
            self.state = 262
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.state = 257 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 256
                    self.match(CNLParser.DIGIT)
                    self.state = 259 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==34):
                        break

                pass
            elif token in [32]:
                self.state = 261
                self.match(CNLParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 264
            self.match(CNLParser.TIMES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimePeriodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_timePeriod

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimePeriod" ):
                listener.enterTimePeriod(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimePeriod" ):
                listener.exitTimePeriod(self)




    def timePeriod(self):

        localctx = CNLParser.TimePeriodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_timePeriod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(CNLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeWindowContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITHIN(self):
            return self.getToken(CNLParser.WITHIN, 0)

        def time(self):
            return self.getTypedRuleContext(CNLParser.TimeContext,0)


        def DIGIT(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.DIGIT)
            else:
                return self.getToken(CNLParser.DIGIT, i)

        def getRuleIndex(self):
            return CNLParser.RULE_timeWindow

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTimeWindow" ):
                listener.enterTimeWindow(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTimeWindow" ):
                listener.exitTimeWindow(self)




    def timeWindow(self):

        localctx = CNLParser.TimeWindowContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_timeWindow)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.match(CNLParser.WITHIN)
            self.state = 270 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 269
                self.match(CNLParser.DIGIT)
                self.state = 272 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==34):
                    break

            self.state = 274
            self.time()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MILLISECONDS(self):
            return self.getToken(CNLParser.MILLISECONDS, 0)

        def SECONDS(self):
            return self.getToken(CNLParser.SECONDS, 0)

        def MINUTES(self):
            return self.getToken(CNLParser.MINUTES, 0)

        def HOURS(self):
            return self.getToken(CNLParser.HOURS, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_time

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTime" ):
                listener.enterTime(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTime" ):
                listener.exitTime(self)




    def time(self):

        localctx = CNLParser.TimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_time)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
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


    class Geo_locationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CNLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return CNLParser.RULE_geo_location

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGeo_location" ):
                listener.enterGeo_location(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGeo_location" ):
                listener.exitGeo_location(self)




    def geo_location(self):

        localctx = CNLParser.Geo_locationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_geo_location)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 278
            self.match(CNLParser.IDENTIFIER)
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




    def detectionBlock(self):

        localctx = CNLParser.DetectionBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_detectionBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 280
            self.match(CNLParser.DETECTION)
            self.state = 281
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

        def XOR(self, i:int=None):
            if i is None:
                return self.getTokens(CNLParser.XOR)
            else:
                return self.getToken(CNLParser.XOR, i)

        def getRuleIndex(self):
            return CNLParser.RULE_detectionExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDetectionExpr" ):
                listener.enterDetectionExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDetectionExpr" ):
                listener.exitDetectionExpr(self)




    def detectionExpr(self):

        localctx = CNLParser.DetectionExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_detectionExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self.eventRef()
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0):
                self.state = 284
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 285
                self.eventRef()
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





