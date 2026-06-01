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
    : processType
    | fileType
    | registryType
    | endpointType
    | networkConnectionType
    | driverType
    | moduleType
    | deviceType
    | volumeType
    | accountType
    | sessionType
    | messageType
    | directoryType
    | handleType
    | otherType
    ;

processType:
    PROCESS AS assetName (WITH processField EQUALS propertyValue (COMMA processField EQUALS propertyValue)*)?
    ;

fileType:
    FILE AS assetName (WITH fileField EQUALS propertyValue (COMMA fileField EQUALS propertyValue)*)?
    ;

registryType:
    REGISTRY AS assetName (WITH registryField EQUALS propertyValue)?
    ;

endpointType:
    ENDPOINT AS assetName (WITH endpointField EQUALS propertyValue (COMMA endpointField EQUALS propertyValue)*)?
    ;

networkConnectionType:
    NETWORK_CONNECTION AS assetName (WITH networkConnectionField EQUALS propertyValue (COMMA networkConnectionField EQUALS propertyValue)*)?
    ;

driverType:
    DRIVER AS assetName (WITH driverField EQUALS propertyValue)?
    ;

moduleType:
    MODULE AS assetName (WITH moduleField EQUALS propertyValue (COMMA moduleField EQUALS propertyValue)*)?
    ;

deviceType:
    DEVICE AS assetName (WITH deviceField EQUALS propertyValue)?
    ;

volumeType:
    VOLUME AS assetName (WITH volumeField EQUALS propertyValue)?
    ;

accountType:
    ACCOUNT AS assetName (WITH accountField EQUALS propertyValue)?
    ;

sessionType:
    SESSION AS assetName (WITH sessionField EQUALS propertyValue)?
    ;

messageType:
    MESSAGE AS assetName (WITH messageField EQUALS propertyValue (COMMA messageField EQUALS propertyValue)*)?
    ;

directoryType:
    DIRECTORY AS assetName (WITH directoryField EQUALS propertyValue)?
    ;

handleType:
    HANDLE AS assetName (WITH handleField EQUALS propertyValue (COMMA handleField EQUALS propertyValue)*)?
    ;

otherType: 
    IDENTIFIER AS assetName (WITH otherField EQUALS propertyValue (COMMA otherField EQUALS propertyValue)*)?
    ;

processField: PARENT_PROCESS | SIGNED | COMMAND_LINE | PARENT_PROCESS ;
fileField: PATH | SIGNED ;
registryField: PATH ;
endpointField: PORT | PROTOCOL | IP_ADDRESS ;
networkConnectionField: DESTINATION_ENDPOINT | SOURCE_ENDPOINT | TRANSPORT_PROTOCOL ;
driverField: SIGNED ;
moduleField: PATH | SIGNED ;
deviceField: DEVICE_TYPE ;
volumeField: PATH ;
accountField: SCOPE ;
sessionField: ACCESS_LEVEL ;
messageField: DATA ; 
directoryField: PATH ;
handleField: HEXADECIMAL_NUMBER | TARGET;
otherField: IDENTIFIER ;


assetName: IDENTIFIER ;
propertyName: IDENTIFIER ;
propertyValue: STRING ;

tactics
    :  (TACTICS | TACTIC) COLON tactic (COMMA tactic)*
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
    : stateCondition
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
    | trigger
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
source : FROM assetName;
trigger: BY assetName;
timing: timePreposition timePeriod;

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
    : eventRef ((OR eventRef)* | (AND eventRef)* | (XOR eventRef)*)
    ;

// General Technique Keywords
TACTICS     : 'Tactics';
TACTIC      : 'Tactic';
TECHNIQUE   : 'Technique';

TACTIC_ID
    : 'TA' DIGIT DIGIT DIGIT DIGIT
    ;

TECHNIQUE_ID
    : 'T' DIGIT DIGIT DIGIT DIGIT ('.' DIGIT DIGIT DIGIT)*
    ;

// Event Keywords
EVENT       : 'Event';
GIVEN       : 'Given';
WHEN        : 'When';
THEN        : 'Then';
AND         : 'And';
OR          : 'Or';
XOR         : 'Xor';

// Main Clauses Keywords
BACKGROUND  : 'Background';
DETECTION   : 'Detection';
IS          : 'is';
AS          : 'as';

// Modifier Keywords
IN          : 'in';
TO          : 'to';
BY          : 'by';
FROM        : 'from';

// Time Window Keywords
DURING      : 'During';
OUTSIDE     : 'Outside';

// Repetition Keywords
REPEATED    : 'Repeated';
TIMES       : 'times';
WITHIN      : 'within';

// Time unit Keywords
MILLISECONDS: 'milliseconds' | 'ms';
SECONDS     : 'seconds' | 'sec';
MINUTES     : 'minutes' | 'min';
HOURS       : 'hours';
WITH        : 'with';
EQUALS      : '=';

// Asset type Keywords
PROCESS         : 'process';
FILE            : 'file';
REGISTRY        : 'registry';
ENDPOINT        : 'endpoint';
NETWORK_CONNECTION : 'network_connection';
DRIVER          : 'driver';
MODULE          : 'module';
DEVICE          : 'device';
VOLUME          : 'volume';
ACCOUNT         : 'account';
SESSION         : 'session';
MESSAGE         : 'message';
DIRECTORY       : 'directory';
HANDLE          : 'handle';

// Asset fields
PARENT_PROCESS  : 'parent_process';
SIGNED          : 'signed';
COMMAND_LINE    : 'command_line';
PATH            : 'path';
PORT            : 'port';
PROTOCOL        : 'protocol';
IP_ADDRESS      : 'ip_address';
DESTINATION_ENDPOINT    : 'destination';
SOURCE_ENDPOINT         : 'source';
TRANSPORT_PROTOCOL      : 'transport_protocol';
DEVICE_TYPE     : 'device_type';
ACCESS_LEVEL    : 'access_level';
SCOPE           : 'scope';
DATA            : 'data';
HEXADECIMAL_NUMBER: 'hexadecimal_number';
TARGET          : 'target';
HANDLES         : 'handles';

// Other Keywords
STRING     : ( '"' ( ~["\\\r\n] | '\\' . )* '"' ) | ( '\'' ( ~['\\\r\n] | '\\' . )* '\'' ) ;
IDENTIFIER : [A-Za-z][A-Za-z0-9_]* ;
COMMA       : ',';
COLON       : ':';

WS
    : [ \t\r\n]+ -> skip
    ;

DIGIT
    : [0-9]
    ;

