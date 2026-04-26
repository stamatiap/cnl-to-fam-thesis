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
    : WHEN action
    ;

action
    : actorAdjective? actor actionVerb adjective? actionObject modifier*
    ;

actorAdjective: IDENTIFIER ;
actor : assetName ;
adjective   : IDENTIFIER ;
actionObject: assetName ;

actionVerb
    : SPAWNS | CREATES | EXECUTES | LOADS | REQUESTS | RECEIVES
    | SENDS | MOUNTS | MODIFIES | RECORDS | RAISES | PERFORMS
    | RECOGNIZES | ACCEPTS | REJECTS | LOCATES
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

conditionObject : assetName ;

stateVerb
    : IS IDENTIFIER
    | IS pastParticiple
    ;

pastParticiple
    : SPAWNED | CREATED | EXECUTED | LOADED | REQUESTED | RECEIVED
    | SENT | MOUNTED | MODIFIED | RECORDED | RAISED | PERFORMED
    | RECOGNIZED | ACCEPTED | REJECTED | LOCATED
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

ESC
    : '\\' ["\\/bfnrt] ;

// Keywords
TACTIC      : 'Tactic';
TECHNIQUE   : 'Technique';
EVENT       : 'Event';
GIVEN       : 'Given';
WHEN        : 'When';
THEN        : 'Then';
AND         : 'And';
OR          : 'Or';
COLON       : ':';
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
ACCEPTS     : 'accepts' ;
REJECTS     : 'rejects' ;
LOCATES     : 'locates' ;

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
ACCEPTED    : 'accepted' ;
REJECTED    : 'rejected' ;
LOCATED     : 'located' ;

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

