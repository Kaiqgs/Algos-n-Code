
grammar Papete;



import_: IMPORTOK*;

prog: 
    import_
    | (line EOL)* EOF //Implemented
    ;

line: assg #LineAssg //Implemented
    | decl #LineDecl //Implemented
    | call #LineCall //Implemented
    | cond #LineCond //Implemented
    | loop #LineLoop //Implemented
    ;

paramblock: PAROPEN decl* PARCLOSE //Implemented
          ;

argsblock: PAROPEN (expr (COMMA expr)*)? PARCLOSE //Implemented
         ;

exprblock: PAROPEN expr PARCLOSE //Implemented
        ; 

loop: WHILEFUNC exprblock stmt;

cond: IFTOK exprblock stmt (ELSETOK  stmt)? //Implemented
    ; 

call: VAR argsblock # CallFunc //Implemented
    | READFUNC argsblock # CallRead //Implemented
    | PRINTFUNC argsblock # CallPrint //Implemented
    | RETURNTOK expr #CallReturnTok //Implemented
    ;

args: VAR (COMMA VAR)* //Implemented
    ; 

assg: 
    decl EQ expr # AssgDeclVar //Implemented
    | VAR EQ expr # AssgVar //Implemented
    ;
decl: 
    type_ VAR (COMMA type_ VAR)* #DeclMultTypeVar //Implemented
    | type_ args #DeclTypeMultVar //Implemented
    | FUNCTOK VAR paramblock stmt #DeclFunc //Implemented
    ;

expr:
	fact #ExprFact //Implemented
	| expr operation fact # ExprOperationFact //Implemented
    ;


stmt: BROPEN (line EOL)* BRCLOSE //Implemented
    ; 

fact:
	VAR #FactVar //Implemented
	| NUM #FactNum //Implemented
    | STRING #FactString //Implemented
    | CHAR #FactChar //Implemented
    | TRUE #FactTrue //Implemented
    | FALSE #FactFalse //Implemented
    | call #FactCall //Implemented 
    | exprblock # FactExprBlock
    ; 


operation:
    PLUS #OperationPlus //Implemented
    | MINUS #OperationMinus //Implemented
    | TIMES #OperationTimes //Implemented
    | DIV #OperationDiv //Implemented
    | MOD #OperationMod //Implemented
    | EE #OperationEe //Implemented
    | NE #OperationNe //Implemented
    | GT #OperationGt //Implemented
    | GE #OperationGe //Implemented
    | LT #OperationLt //Implemented
    | LE #OperationLe //Implemented
    | AND #OperationAnd //Implemented
    | OR #OperationOr //Implemented
    ;

type_:
	INT_TYPE #TypeInt //Implemented
	| DOUBLE_TYPE #TypeDouble //Implemented
	| STRING_TYPE #TypeString //Implemented
	| BOOL_TYPE #TypeBool //Implemented
    | VOID_TYPE #TypeVoid //Implemented
    | CHAR_TYPE #TypeChar //Implemented
    ;


TRUE: 'true';
FALSE: 'false';
INT_TYPE: 'int';
DOUBLE_TYPE: 'double';
STRING_TYPE: 'string';
CHAR_TYPE: 'char';
BOOL_TYPE: 'bool';
VOID_TYPE: 'void';

PRINTFUNC: 'print';
READFUNC: 'read';
FUNCTOK: 'func';

COMMA: ',';
PAROPEN : '(';
PARCLOSE : ')';
BROPEN: '{';
BRCLOSE: '}';
EQ: '=';
EE: '==';
NE: '!=';
GT: '>';
GE: '>=';
LT: '<';
LE: '<=';
AND: 'and';
OR: 'or';
NOT: 'not';
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
MOD: '%';
COMMENT:'!' ~[\r\n]* -> skip;

MINUSVAL: '_';

IFTOK: 'if';
ELSETOK: 'else';

WHILEFUNC: 'while';
EOL: ';';
IMPORTOK: 'import' (' ') STRING;
RETURNTOK: 'return';



STRING: '"'(~["\\\r\n])*'"';
CHAR: '\''(~["\\\r\n])?'\'';
VAR: [a-zA-Z][a-zA-Z0-9_]*;
NUM: MINUSVAL? DIGIT+('.'DIGIT+)?;
DIGIT: [0-9];
WS : [ \t\r\n]+ -> skip;