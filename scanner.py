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
reserved = {
	'Prototype'	:'RES_PROTO',
	'Define'	:'RES_DEF',
	'Integer'	:'RES_INT',
	'String'	:'RES_STRING',
	'Float'		:'RES_FLOAT',
	'Double'	:'RES_DOUBLE',
	'Boolean'	:'RES_BOOLEAN',
	'List'		:'RES_LIST',
	'Array'		:'RES_ARRAY',
	'func'		:'RES_FUNC',
	'Start'		:'RES_START',
	'true'		:'RES_TRUE',
	'false'		:'RES_FALSE',
	'set'		:'RES_SET',
	'if'		:'RES_IF',
	'else'		:'RES_ELSE',
	'elif'		:'RES_ELIF',
	'switch'	:'RES_SWITCH',
	'case'		:'RES_CASE',
	'for'		:'RES_FOR',
	'while'		:'RES_WHILE',
	'print'		:'RES_PRINT',
	'read'		:'RES_READ',
	'End'		:'RES_END',
	'end'		:'E_END',
	'endi'		:'ENDI'
	}

# Tokens
tokens = [ 	'ID','CTE_INT', 'CTE_FLOAT', 'CTE_DOUBLE', 'CTE_STRING', 'VAR',
		   	'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS', 'LPAREN', 
		   	'RPAREN', 'TAB', 'MAY', 'MAY_EQ', 'MIN','MIN_EQ',
			'DIF', 'EQ_EQ', 'NEW_LINE', 'COMMA', 'LBRACKET', 
			'RBRACKET', 'LCURLY', 'RCURLY', 'COL',
			'AND', 'OR'] + list(reserved.values())

# Operadores
t_PLUS 		= r'\+'
t_MINUS 	= r'-'
t_TIMES 	= r'\*'
t_DIVIDE 	= r'/'
t_MAY_EQ 	= r'>='
t_MIN_EQ 	= r'<='
t_EQ_EQ 	= r'=='
t_COMMA 	= r'\,'
t_COL 		= r'\:'
t_AND 		= r'&&'
t_OR 		= r'\|\|'

# Asignacion
t_EQUALS 	= r'='
t_MAY 		= r'>'
t_MIN 		= r'<'
t_DIF 		= r'!='

# Comentarios
t_ignore_COMMENT = r'\$[^$]*\$|\#.*'


# Parentesis, Corchetes, Llaves
t_LPAREN 	= r'\('
t_RPAREN 	= r'\)'
t_LBRACKET 	= r'\['
t_RBRACKET 	= r'\]'
t_LCURLY 	= r'\{'
t_RCURLY 	= r'\}'

#new line, tab
t_TAB = r'\t'


# Palabras Reservadas---------

#----------------------------

reserved_map = { }
for r in reserved:
    reserved_map[r.lower()] = r

t_ignore = ' \t \n'

# Identificador de funciones
def t_ID(t):
    r'[a-zA-Z_][\w_]*'
    t.type = reserved.get(t.value,'ID')
    return t

# Identificador de Variables
"""
def t_VAR(t):
    r'[a-z]|[A-Z_][\w_]*'
    t.type = reserved.get(t.value,'VAR')
    return t
"""

#Constantes de punto flotante
def t_CTE_FLOAT(t):
	r'[0-9]+.[0-9]+'
	t.value = float(t.value)
	return t

# Constantes enteras
def t_CTE_INT(t):
	r'[0-9]+'
	print"pasa",t
	t.value = int(t.value)
	return t

# Constantes 
def t_CTE_DOUBLE(t):
	r'[0-9]+.[0-9]'
	t.value = Double(t.value)
	return t

# Constantes String
def t_CTE_STRING(t):
	r'\"[^\"]*\"'
	t.value = t.value
	return t

# Salto de linea
def t_NEW_LINE(t):
	r'\n'
	t.lexer.lineno += t.value.count("\n")

# Error
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# Construye el lexer
lex.lex()
