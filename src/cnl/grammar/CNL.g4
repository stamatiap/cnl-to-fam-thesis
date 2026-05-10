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
    : GIVEN givenItem ((AND givenItem)* | (OR givenItem)* | (XOR givenItem)* )
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

pastParticiple
    : IDENTIFIER
    ;

location : IN assetName;
destination : TO assetName;
source : BY assetName | FROM assetName;


detectionBlock
    : DETECTION detectionExpr
    ;

detectionExpr
    : eventRef ((AND | OR | XOR) eventRef)*
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

