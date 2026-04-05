grammar CNL;

attack
    : header background eventBlock+ detectionBlock? EOF
    ;

header
    : tactic technique
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

tactic
    : TACTIC COLON TACTIC_ID IDENTIFIER  
    ;

technique
    : TECHNIQUE COLON TECHNIQUE_ID IDENTIFIER  
    ;

eventBlock
    : EVENT DIGIT 
      eventStatement
    ;

eventStatement
    : givenClause
      whenClause
      thenClause
      (REPEATED lineText)? (WITHIN lineText)?
    ;

givenClause
    : GIVEN givenItem ((AND givenItem)* | (OR givenItem)*)
    ;

givenItem
    : eventRef
    | stateCondition
    ;

eventRef
    : EVENT DIGIT
    ;

whenClause
    : WHEN action ((AND action)* )
    ;

action
    : actor actionVerb adjective? actionObject modifier*
    ;

actor : assetName ;
adjective   : IDENTIFIER ;
actionObject: IDENTIFIER ;

actionVerb
    : SPAWNS | CREATES | EXECUTES | LOADS | REQUESTS | RECEIVES
    | SENDS | MOUNTS | MODIFIES | RECORDS | RAISES | PERFORMS
    | RECOGNIZES
    ;

modifier
    : location
    | destination
    | source
    ;

thenClause
    : THEN stateCondition (AND stateCondition)*
    ;

stateCondition
    : conditionObject stateVerb modifier*
    ;

conditionObject
    : IDENTIFIER
    ;

stateVerb
    : IS IDENTIFIER
    | IS pastParticiple modifier*
    ;

pastParticiple
    : SPAWNED | CREATED | EXECUTED | LOADED | REQUESTED | RECEIVED
    | SENT | MOUNTED | MODIFIED | RECORDED | RAISED | PERFORMED
    | RECOGNIZED
    ;

location : IN assetName;
destination : TO assetName;
source : BY assetName | FROM assetName;


detectionBlock
    : DETECTION detectionExpr
    ;

detectionExpr
    : eventRef ((AND | OR) eventRef)*
    ;

lineText
    : STRING
    ;

STRING
    : '"' (ESC | '.' | ~["\\])* '"'
    ;

ESC
    : '\\' ["\\/bfnrt] ;

// Keywords
TACTIC      : 'Tactic';
TECHNIQUE   : 'Technique';
EVENT       : 'Event';
GIVEN       : 'Given';
WHEN        : 'When';
THEN        : 'Then';
IF          : 'If';
AND         : 'And';
OR          : 'Or';
COLON       : ':';
REPEATED    : 'Repeated';
WITHIN      : 'Within';
AS          : 'as';
BACKGROUND  : 'Background';
DETECTION   : 'Detection';
IS          : 'is';
IN          : 'in';
TO          : 'to';
BY          : 'by';
FROM        : 'from';

// Action Verbs
SPAWNS      : 'spawns' ;
CREATES     : 'creates' ;
EXECUTES    : 'executes' ;
LOADS       : 'loads' ;
REQUESTS    : 'requests' ;
RECEIVES    : 'receives' ;
SENDS       : 'sends' ;
MOUNTS      : 'mounts' ;
MODIFIES    : 'modifies' ;
RECORDS     : 'records' ;
RAISES      : 'raises' ;
PERFORMS    : 'performs' ;
RECOGNIZES  : 'recognizes' ;

// Past participles for state verbs
SPAWNED     : 'spawned' ;
CREATED     : 'created' ;
EXECUTED    : 'executed' ;
LOADED      : 'loaded' ;
REQUESTED   : 'requested' ;
RECEIVED    : 'received' ;
SENT        : 'sent' ;
MOUNTED     : 'mounted' ;
MODIFIED    : 'modified' ;
RECORDED    : 'recorded' ;
RAISED      : 'raised' ;
PERFORMED   : 'performed' ;
RECOGNIZED  : 'recognized' ;

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
    : [0-9]+
    ;

