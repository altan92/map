'''ERROR: yacc.py:71: Symbol 'IN' used, but not defined as a token or a rule
ERROR: yacc.py:83: Symbol 'ASSIGN' used, but not defined as a token or a rule
ERROR: yacc.py:118: Symbol 'multiplicative-exression' used, but not defined as a token or a rule
ERROR: yacc.py:129: Symbol 'DIVIDES' used, but not defined as a token or a rule
ERROR: yacc.py:133: Symbol 'constant' used, but not defined as a token or a rule
ERROR: yacc.py:134: Symbol 'string' used, but not defined as a token or a rule
ERROR: yacc.py:135: Symbol 'node' used, but not defined as a token or a rule
ERROR: yacc.py:136: Symbol 'edge' used, but not defined as a token or a rule
ERROR: yacc.py:141: Symbol 'DOT' used, but not defined as a token or a rule
ERROR: yacc.py:144: Symbol 'print' used, but not defined as a token or a rule
ERROR: yacc.py:145: Symbol 'read' used, but not defined as a token or a rule
ERROR: yacc.py:146: Symbol 'write' used, but not defined as a token or a rule
'''


import ply.yacc as yacc
from MAPlexer import * 
#parsing rules

# Parsing rules

'''def p_tu_ed(t):
	'translation-unit : external-declaration'
	t[0] = t[1]

def p_tu_ed2(t):
	'translation-unit : translation-unit external-declaration'
	t[0] = t[1] + ' ' + t[2]

def p_ed1(t):
	'external-declaration : function-definition'
	t[0] = t[1]

def p_ed2(t):
	'external-declaration : statement'
	t[0] = t[1]
'''
def p_fd(t):
	'function-definition : FUNC identifier LPAREN parameter-list RPAREN' # compound-statement'
	print "funtion-definition : {1} {2}{3}{4}{5}".format(t[0],t[1],t[2],t[3],t[4],t[5])
	t[0] = t[1] + t[2] + t[3] + t[4] + t[5]

def p_id(t):
	'identifier : TEXT'
	print "identifier : {1}".format(t[0],t[1])
	t[0] = t[1]

def p_listE(t):
	'parameter-list : '

def p_plist(t):
	'parameter-list : identifier'
	t[0] = t[1]

def p_plist2(t):
	'parameter-list : parameter-list COMMA identifier'
	t[0] = t[1] + t[2] + t[3]

def p_cs(t):
	'compound-statement : LBR statement-list RBR'

def p_slist(t):
	'statement-list : statement'
	t[0] = t[1]

def p_slist2(t):
	'statement-list : statement-list statement'

def p_slist3(t):
	'statement-list : '
	t[0] = ""
def p_s(t):
	'''statement : expression
	| compound-statement
	| selection-statement
	| iteration-statement'''
	t[0] = t[1]

def p_sels(t):
	'selection-statement : IF LPAREN expression RPAREN statement'

def p_sels2(t):
	'selection-statement : IF LPAREN expression RPAREN statement ELSE statement'

def p_iters(t):
	'iteration-statement : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement'

def p_ters2(t):
	'iteration-statement : FOREACH LPAREN identifier IN identifier RPAREN statement'

def p_expr(t):
	'expression : assignment-expression'

def p_expr2(t):
	'expression : expression COMMA assignment-expression'

def p_aexpr(t):
	'assignment-expression : conditional-expression'

def p_aexpr2(t):
	'assignment-expression : primary-expression EQUALS assignment-expression'

def p_condexpr(t):
	'''conditional-expression : logical-OR-expression
	| logical-AND-expression'''

def p_logorexpr(t):
	'logical-OR-expression : logical-AND-expression'

def p_logorexpr2(t):	
	'logical-OR-expression : logical-OR-expression LOGICALOR logical-AND-expression'

def p_logandexpr(t):
	'logical-AND-expression : equality-expression'

def p_logandexpr2(t):
	'logical-AND-expression : logical-AND-expression LOGICALAND equality-expression'

def p_eqexpr(t):
	'equality-expression : relational-expression'

def p_eqexpr2(t):
	'''equality-expression : equality-expression EQUALSEQUALS relational-expression
	| equality-expression DOESNOTEQUAL relational-expression'''

def p_relexpr(t):
	'relational-expression : additive-expression'

def p_relexpr2(t):
	'''relational-expression : relational-expression GREATERTHAN additive-expression
	| relational-expression LESSTHAN additive-expression
	| relational-expression LESSTHANOREQUALTO additive-expression
	| relational-expression GREATERTHANOREQUALTO additive-expression'''

def p_addexpr(t):
	'additive-expression : multiplicative-expression'

def p_addexpr2(t):
	'''additive-expression : additive-expression PLUS multiplicative-expression
	| additive-expression MINUS multiplicative-expression'''

def p_multexpr(t):
	'multiplicative-expression : primary-expression'

def p_multexpr2(t):
	'''multiplicative-expression : multiplicative-expression TIMES primary-expression
	| multiplicative-expression DIVIDE primary-expression'''

def p_primexp(t):
	'''primary-expression : identifier
	| TEXT
	| NODE
	| LPAREN expression RPAREN'''
	#| function-call'''
'''
def p_funcall(t):
	'function-call : identifier DOT function-name LPAREN parameter-list RPAREN'
'''
def p_funcall2(t):
	'''function-call : PRINT LPAREN identifier RPAREN
	| READ LPAREN identifier RPAREN
	| WRITE LPAREN identifier COMMA identifier RPAREN'''

def p_funcname(t):
	'''function-name : ADD
	| DELETEFUNC
	| ADJACENTFUNC
	| PATHFUNC
	| GETEDGEFUNC
	| ADDEDGEFUNC
	| DELETEEDGEFUNC
	| FINDSHORTESTFUNC
	| EQUALSFUNC'''
def p_error(t):
	print("Syntax error at '%s'" % t.value)

yacc.yacc()


print yacc.parse("func main(hi, bye) ")
		# {\n\tText t = \"Hello, world\";\n\tprint(t);\n}")


