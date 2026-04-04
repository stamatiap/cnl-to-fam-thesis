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
    : asset AS assetName
    ;

asset: lineText;
assetName: lineText;

tactic
    : TACTIC COLON TACTIC_ID lineText 
    ;

technique
    : TECHNIQUE COLON TECHNIQUE_ID lineText 
    ;

eventBlock
    : EVENT DIGIT 
      eventStatement
    ;

eventStatement
    : givenClause
      whenClause?
      thenClause
      (REPEATED lineText)? (WITHIN lineText)?
    ;

givenClause
    : GIVEN givenItem ((AND givenItem)* | (OR givenItem)*)
    ;

givenItem
    : eventRef
    | lineText
    ;

eventRef
    : EVENT DIGIT
    ;


whenClause
    : WHEN lineText ((AND lineText)* | (OR lineText)*)
    ;


thenClause
    : THEN lineText ((AND lineText)* )
    ;

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

TACTIC_ID
    : 'TA' DIGIT DIGIT DIGIT DIGIT
    ;

TECHNIQUE_ID
    : 'T' DIGIT DIGIT DIGIT DIGIT ('.' DIGIT DIGIT DIGIT)*
    ;


WS
    : [ \t\r\n]+ -> skip
    ;

DIGIT
    : [0-9]+
    ;

