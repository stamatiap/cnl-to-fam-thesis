grammar CNL;

attack
    : header background eventBlock+ detectionBlock? EOF
    ;

header
    : tactics technique
    ;

background
    : BACKGROUND GIVEN assets
    ;

assets
    : assetDefinition (AND assetDefinition)*
    ;

assetDefinition
    : assetType AS assetName
    ;

assetType: IDENTIFIER ;
assetName: IDENTIFIER ;

tactics
    :  TACTICS COLON tactic (COMMA tactic)*
    ;

tactic
    : TACTIC_ID IDENTIFIER  
    ;

technique
    : TECHNIQUE COLON TECHNIQUE_ID IDENTIFIER  
    ;

eventBlock
    : EVENT DIGIT+
      eventStatement repetition? timing?
    ;

eventStatement
    : givenClause
      whenClause
      thenClause
    ;

givenClause
    : GIVEN givenItem ((AND givenItem)* | (OR givenItem)* | (XOR givenItem)* )
    ;

givenItem
    : eventRef
    | stateCondition
    ;

eventRef
    : EVENT DIGIT+
    ;

whenClause
    : WHEN action
    ;

action
    : actor actionVerb actionObject modifier*
    ;

actor : assetName ;
actionObject: assetName ;

actionVerb
    : IDENTIFIER
    ;

modifier
    : location
    | destination
    | source
    | geolocation
    ;

thenClause
    : THEN stateCondition (AND stateCondition)*
    ;

stateCondition
    : conditionObject stateVerb modifier*
    ;

conditionObject : assetName ;

stateVerb
    : IS IDENTIFIER
    | IDENTIFIER
    ;


location : IN assetName;
destination : TO assetName;
source : BY assetName | FROM assetName;
timing: timePreposition timePeriod;
geolocation: LOCATED_AT geo_location;

timePreposition: 
    DURING | OUTSIDE
    ;

repetition:
    repeat timeWindow?
    ;

repeat:
    REPEATED (DIGIT+ | IDENTIFIER) TIMES
    ;

timePeriod:
    IDENTIFIER
    ;

timeWindow:
    WITHIN DIGIT+ time
    ;

time:
    MILLISECONDS | SECONDS | MINUTES | HOURS
    ;

geo_location
    : IDENTIFIER
    ;

detectionBlock
    : DETECTION detectionExpr
    ;

detectionExpr
    : eventRef ((AND | OR | XOR) eventRef)*
    ;

// Keywords
TACTICS     : 'Tactics';
TECHNIQUE   : 'Technique';
EVENT       : 'Event';
GIVEN       : 'Given';
WHEN        : 'When';
THEN        : 'Then';
AND         : 'And';
OR          : 'Or';
XOR         : 'Xor';
COLON       : ':';
AS          : 'as';
BACKGROUND  : 'Background';
DETECTION   : 'Detection';
IS          : 'is';
IN          : 'in';
TO          : 'to';
BY          : 'by';
FROM        : 'from';
LOCATED_AT  : 'located_at';
DURING      : 'During';
COMMA       : ',';
OUTSIDE     : 'Outside';
REPEATED    : 'Repeated';
TIMES       : 'times';
WITHIN      : 'within';
MILLISECONDS: 'milliseconds' | 'ms';
SECONDS     : 'seconds' | 'sec';
MINUTES     : 'minutes' | 'min';
HOURS       : 'hours';


TACTIC_ID
    : 'TA' DIGIT DIGIT DIGIT DIGIT
    ;

TECHNIQUE_ID
    : 'T' DIGIT DIGIT DIGIT DIGIT ('.' DIGIT DIGIT DIGIT)*
    ;

IDENTIFIER : [A-Za-z][A-Za-z0-9_]* ;

WS
    : [ \t\r\n]+ -> skip
    ;

DIGIT
    : [0-9]
    ;

