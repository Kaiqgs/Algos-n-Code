/******************************************************
 * A multi-line Javadoc-like comment about my grammar *
 * ****************************************************
 */
grammar Papete;


prog: (line EOL)* EOF;

line: assg;
assg: 
    decl EQ expr
    | VAR EQ expr
    ;
decl: type_ VAR;
expr:
	fact			
	| expr PLUS fact	
	| expr MINUS fact	
	| expr TIMES fact	
	| expr DIV fact	
	| expr MOD fact	
    ;
funcsign:
    type_ VAR PAROPEN (decl)* PARCLOSE stmt;

stmt: BROPEN (line EOL)* EOF;

fact:
	VAR				
	| NUM
    | STRING
    | TRUE
    | FALSE		
	| PAROPEN expr PARCLOSE
    ; 
type_:
	INT_TYPE
	| FLOAT_TYPE
	| STRING_TYPE
	| BOOL_TYPE
    ;

TRUE: 'true';
FALSE: 'false';
INT_TYPE: 'int';
FLOAT_TYPE: 'double';
STRING_TYPE: 'string';
BOOL_TYPE: 'bool';

PAROPEN : '(';
PARCLOSE : ')';
BROPEN: '{';
BRCLOSE: '}';
EQ = '=';
GT = '>';
GE = '>=';
LT = '<';
LE = '<=';
PLUS = '+';
MINUS = '-';
TIMES = '*';
DIV = '/';
MOD = '%';

EOL: ';';
STRING: '"'(~["\\\r\n])*'"';
VAR: [a-zA-Z][a-zA-Z0-9_]*;
NUM: [+-]?DIGIT+('.'DIGIT+)?;
DIGIT: [0-9];
WS : [ \t\r\n]+ -> skip;
