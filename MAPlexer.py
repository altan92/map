import ply.lex as lex
#http://flex.sourceforge.net/manual/Patterns.html
tokens = (
	'NUMERIC', #1
	'SINGLEQUOTE', #2
	'DOUBLEQUOTE', #2.1
	'TEXT',	   #3
	'BOOLEAN', #4
	'TIME',    #5	
	'NULL',    #6
	'DIREDGE', #7.1
	'UNDIREDGE', #7.2
	'NODE',    #8
	'PATH',    #9
	'GRAPH',   #10	
	'PLUS',    #11
	'MINUS',   #12
	'TIMES',   #13
	'DIVIDE',  #14
	'LPAREN',  #15
	'RPAREN',  #16
	'MODULUS', #16.1
	'SEMICOLON', # 16.2
	'COLON', # 16.3
	'LESSTHAN', #17
	'GREATERTHAN', #18
	'EQUALS', 
	'LESSTHANOREQUALTO', #19
	'GREATERTHANOREQUALTO', #20
	'EQUALSEQUALS', #21
	'DOESNOTEQUAL', #22	
	'LOGICALAND', #24
	'LOGICALOR',  #25
	'COMMENT',    #26
	'COMMENTFRONT', #27
	'COMMENTBACK',   #28
	'PRINT',         #29
	#Graphing functions
	'GADD',          #30
	'GDELETE',       #31
	'GADJACENT',     #32
	'GPATH',         #33
	'GGETEDGE',      #34
	'GADDEDGE',      #35
	'GDELETEEDGE',   #35
	'GFINDSHORTESTPATH',#36
	'COMMA', #37
	'NEWLINE',#38
	'READ', #39
	'WRITE',#40
	'GEQUALS', # 49
	#keywords
	'FUNC',#39
	'LBR', # 40
	'RBR', # 41
	'IF', #42
	'FOR', #43
	'BREAK', #44
	'ELIF', # 45
	'FOREACH', # 46
	'CONTINUE', # 47
	'RETURN', # 48
	'ELSE', #50
	'LSB', 
	'RSB',
	'PERIOD',
	'EXCLAMATION',
	'IN',
	)

#primitive data types
t_NUMERIC=r'(\d+\.?\d+ | \.\d+)'   #1
t_SINGLEQUOTE=r'(\')' #2
t_DOUBLEQUOTE=r'(\")' #2.1
t_TEXT=r'[a-zA-Z]'+r'[a-zA-Z0-9]+'#3
t_SEMICOLON = r';' 
t_COLON = r'\:'
t_PERIOD = r'\.'
t_EXCLAMATION = r'\!'

def t_IN(t):
	r'in\s'
	return t 

def t_FUNC(t):
	r'^func '
	return t 

def t_ELSE(t):
	r'^else\s'
	return t 

def t_RETURN(t):
	r'^return '
	return t

def t_CONTINUE(t):
	r'^continue\s'
	return t

def t_FOREACH(t):
	r'^foreach\($'
	return t 

def t_IF(t):
	r'^if$'
	return t # 42

def t_FOR(t):
	r'^for$'
	return t # 43

def t_BREAK(t):
	r'^break$'
	return t

def t_ELIF(t): 
	r'^elif$'
	return t 

def t_BOOLEAN(t): #4
	r'(True | False | true | false)'
	t.value= 'rue' in t.value
	return t

def t_TIME(t):
	r'Time\s'
	return t #5

def t_NULL(t):
	r'NULL$' 
	t.value=None
	return t #6

def t_DIREDGE(t):
	r'Diredge$' 
	return t #7.1

def t_UNDIREDGE(t):
	r'Undiredge$'
	return t #7.2

def t_NODE(t):
	r'Node$' 
	return t #8

def t_PATH(t):
	r'Path$' 
	return t #9

def t_GRAPH(t):
	r'Graph$' 
	return t  #10

#aritmetic operators
t_MODULUS = r'\%' #16.1
t_PLUS    = r'\+' #11
t_MINUS   = r'-'  #12
t_TIMES   = r'\*' #13
t_DIVIDE  = r'/'  #14
t_LPAREN  = r'\(' #15
t_RPAREN  = r'\)' #16
t_LESSTHAN=r'\<'  #17
t_GREATERTHAN=r'\>' #18
t_LESSTHANOREQUALTO=r'<\=' #19
t_GREATERTHANOREQUALTO=r'>\='#20
t_EQUALS = r'\='
t_EQUALSEQUALS=r'\=\='#21
t_DOESNOTEQUAL=r'!='#22
t_LOGICALAND=r'&'  #24
t_LOGICALOR=r'\|'  #25

#commenting
t_COMMENT=r'//' #26
t_COMMENTBACK=r'(\*/)' #27
t_COMMENTFRONT=r'(/\*)'#28
t_LSB = '\['
t_RSB = '\]'
t_LBR = '\{'
t_RBR = '\}'

#standard library operators
def t_PRINT(t):
	r'^Print\('         
	return t #29

t_GADD=r'\.add'          		#30
t_GDELETE=r'\.delete'       	#31
t_GADJACENT=r'\.adjacent'     	#32
t_GPATH=r'\.path'         		#33
t_GGETEDGE=r'\.getEdge'      	#34
t_GADDEDGE=r'\.addEdge'      	#35
t_GDELETEEDGE=r'\.deleteEdge'   #35
t_GFINDSHORTESTPATH=r'\.findShortestPath'   #36
t_GEQUALS = r'\.equals' # 49

t_COMMA=r'\,' #37

t_NEWLINE=r'\n'#38
def t_READ(t):
	r'read\(' 
	return t  #39

def t_WRITE(t):
	r'write\(' 
	return t  #40	

t_ignore  = ' \t'

def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)
