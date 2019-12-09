/******************************************************
 * A multi-line Javadoc-like comment about my grammar *
 * ****************************************************
 */
grammar Papete;


prog: (line EOL | func)+ EOF
	| IMPORT '<' VAR '.' GRAMATICA '>' ';' prog;
line:
	atr			# AtrLine
	| print_	# PrintLine
	| init_		# InitLine
	| callfunc	# CallFuncLine;
func:
	type_ VAR '(' (((type_ VAR) ';'?)+ | '0') ')' OBR (cmd)+ retr CBR
	| VOID VAR '(' (((type_ VAR) ';'?)+ | '0') ')' OBR (cmd)+ CBR
	| (INT | VOID) MAIN '(' '0' ')' OBR (cmd)+ RET '0' EOL CBR;
cmd:
	atr EOL			# AtrCmd
	| init_ EOL		# InitCmd
	| print_ EOL	# PrintCmd
	| read EOL		# ReadCmd
	| ifstmt		# IfCmd
	| while_		# WhileCmd
	| for_			# ForCmd
	| callfunc EOL	# FuncCmd;
callfunc:
	VAR '(' ((VAR | NUMINT | NUMDOUBLE) ','?)+ ')'
	| VAR '(' ')';
while_: WHILE '(' cond ')' OBR (cmd)+ CBR;
for_: FOR '(' (atr | init_) ';' cond ';' atr ')' OBR (cmd)+ CBR;
ifstmt:
	IF '(' cond ')' OBR (cmd)+ CBR							# NormalIfStmt
	| IF '(' (VAR | '!' VAR) ')' OBR (cmd)+ CBR				# NegIfStmt
	| IF '(' cond ')' OBR (cmd)+ CBR ELSE OBR (cmd)+ CBR	# IfElseIfStmt;
cond: cond OR cdand # OrCond | cdand # CdandCond;
cdand: cdand AND cndts # AndCdand | cndts # CndtsCdand;
cndts: expr relop expr # RelopCndts | '(' cond ')' # CondCndts;
relop: GRT | LESS | GRTEQ | LESSEQ | EQ | NEQ;
read: READ VAR | READ type_ VAR;
print_:
	PRINT '(' ('+'? STRVALUE '+'? VAR?)+ ')'	# ConcatPrint
	| PRINT '(' VAR ')'							# VarPrint;
init_: type_ VAR;
retr: RET VAR EOL # VarRetr | RET expr EOL # ExprRetr;
atr:
	INT VAR '=' (expr | callfunc)			# IntAtr
	| DOUBLE VAR '=' (expr | callfunc)		# DoubleAtr
	| STRING VAR '=' (STRVALUE | callfunc)	# StringAtr
	| BOOL VAR '=' (TRUE | FALSE)			# BoolAtr
	| VAR '=' (expr | callfunc)				# VarExprFuncAtr
	| VAR '=' (STRVALUE)					# VarStrAtr
	| VAR '=' (TRUE | FALSE)				# VarBoolAtr;
expr:
	term			# TermExpr
	| expr '+' term	# SumExpr
	| expr '-' term	# MinusExpr;
term:
	fact			# FactTerm
	| term '*' fact	# MultTerm
	| term '/' fact	# DivTerm
	| term '%' fact	# RestTerm;
fact:
	VAR					# varFact
	| NUMDOUBLE			# NumDoubleFact
	| (NUMINT | '0')	# NumIntFact
	| '(' expr ')'		# exprFact;
type_:
	INT			# intType
	| DOUBLE	# doubleType
	| FLOAT		# floatType
	| STRING	# stringType
	| BOOL		# boolType;
GRAMATICA: 'gramaticaextensao';
IMPORT: 'import';
TRUE: 'true';
FALSE: 'false';
FOR: 'for';
WHILE: 'while';
GRT: '>';
LESS: '<';
GRTEQ: '>=';
LESSEQ: '<=';
EQ: '==';
NEQ: '!=';
OR: '||';
IF: 'if';
AND: '&&';
ELSE: 'else';
PRINT: 'print';
MAIN: 'main';
INT: 'int';
FLOAT: 'float';
DOUBLE: 'double';
STRING: 'string';
VOID: 'void';
BOOL: 'boolean';
READ: 'read';
RET: 'return';
OBR: '{';
CBR: '}';
EOL: ';';
GLOBAL: 'global';
STRVALUE: '"' [a-zA-Z0-9 ]? [ a-zA-Z0-9_.:]* '"';
VAR: [a-zA-Z][a-zA-Z0-9_]*;
PRINTCONC: (
		('+'? '"' [a-zA-Z0-9 ]? [ a-zA-Z0-9_:.]* '"')+ ('+' VAR)?
	)+;
NUMDOUBLE: [-]? [0-9]+ ('.' [0-9]+);
NUMINT: [-]? [0-9]+;
COMMENT: '/*' .*? '*/' -> skip;
LINE_COMMENT: '//' ~[\r\n]* -> skip;
WS: [ \t\r\n]+ -> skip;
COM: '//' (~[\r\n])* '\r'? '\n' -> skip;