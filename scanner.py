#----------------------------------------------
# parser.py
# CACHACA - Scanner
# Analizador lexico
# Gerardo Chapa Quiroga 800249
# Tomas Castro Lopez 1033534
# Adolfo Castro Rojas 225591
# CREADO: 05/03/2013
# EDITADO: 07/03/2013
#----------------------------------------------
import sys
sys.path.insert(0,'../..')

import ply.lex as lex

# Palabras reservadas
reserved = (
	'RES_DEF', 'RES_INT', 'RES_FLOAT', 'RES_STRING', 'RES_DOUBLE',
	'RES_BOOLEAN', 'RES_LIST', 'RES_ARRAY', 'RES_FUNC', 'RES_START', 'RES_SET',  'RES_IF',
	'RES_ELIF', 'RES_ELSE', 'RES_SWITCH', 'RES_CASE', 'RES_FOR', 'RES_PRINT', 'RES_READ', 
	'RES_END', 'RES_AND', 'RES_OR', 'RES_TRUE', 'RES_FALSE', 'RES_WHILE',
	)

# Tokens
tokens = reserved + (
	'ID','CTE_INT', 'CTE_FLOAT', 'CTE_DOUBLE', 'CTE_STRING', 
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'LPAREN', 
	'RPAREN', 'TAB', 'STRING', 'MAY', 'MAY_EQ', 'MIN', 
	'MIN_EQ', 'NOT', 'DIF', 'EQ_EQ', 'NEW_LINE', 'VAR', 'COMMA',
	'LBRACKET', 'RBRACKET', 'LCURLY', 'RCURLY', 'COL', 'COMMENT','FUNC',
	'brconsbr','conscommaa', 'llamadas', 'zexp',
	)

# Operadores
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MAY = r'>'
t_MAY_EQ = r'>='
t_MIN = r'<'
t_MIN_EQ = r'<='
t_NOT = r'!'
t_DIF = r'!='
t_EQ_EQ = r'=='
t_COMMA = r'\,'
t_COL = r'\:'

# Asignacion
t_EQUALS = r'='

# Comentarios
t_COMMENT = r'\$[^$]*\$'

# Parentesis
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LCURLY = r'\{'
t_RCURLY = r'\}'


# Palabras Reservadas---------
t_RES_DEF = r'define'
t_RES_INT = r'Integer'
t_RES_STRING = r'String'
t_RES_FLOAT = r'Float'
t_RES_DOUBLE = r'Double'
t_RES_BOOLEAN = r'Boolean'
t_RES_LIST = r'List'
t_RES_ARRAY = r'Array'
t_RES_FUNC = r'func'
t_RES_START = r'start'
t_RES_TRUE = r'true'
t_RES_FALSE = r'false'
t_RES_SET = r'set'
t_RES_AND = r'and'
t_RES_OR = r'or'
t_RES_IF = r'if'
t_RES_ELSE = r'else'
t_RES_ELIF = r'elif'
t_RES_SWITCH = r'switch'
t_RES_CASE = r'case'
t_RES_FOR = r'for'
t_RES_WHILE = r'while'
t_RES_PRINT = r'print'
t_RES_READ = r'read'
t_RES_END = r'end'
#----------------------------

reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

t_TAB = r'\t'

# Identificador de funciones
def t_ID(t):
    r'[A-Za-z_][\w_]*'
    t.type = reserved_map.get(t.value,"ID")
    return t

# Identificador de Variables
def t_VAR(t):
    r'[a-zA-Z_][\w_]*'
    t.type = reserved.get(t.value,'ID')
    return t

# Constantes enteras
def t_CTE_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t

# Constantes de punto flotante
def t_CTE_FLOAT(t):
	r'[0-9]+.[0-9]+'
	t.value = float(t.value)
	return t

# Constantes 
def t_CTE_DOUBLE(t):
	r'[0-9]+.[0-9]{0-,100}'
	t.value = Double(t.value)
	return t

# Constantes String
def t_CTE_STRING(t):
	r'\"[^\"]*\"'
	t.value = string(t.value)
	return t

# Salto de linea
def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count("\n")

# Error
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# Construye el lexer
lex.lex()