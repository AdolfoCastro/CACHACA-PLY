#----------------------------------------------
# parser.py
# CACHACA - Parser
# Analizador sintactico
# Gerardo Chapa Quiroga 800249
# Tomas Castro Lopez 1033534
# Adolfo Castro Rojas 225591
# CREADO: 05/03/2013
# EDITADO: 07/03/2013
#----------------------------------------------
import sys
import scanner
import clases
import ply.yacc as yacc
import fileinput
from tvariables import *

# Consigue el mapa de tokens
tokens = scanner.tokens
start = 'programa'

nombre_pro_act = None
tipo_pro = None
tipo_pro_actual  = None

def p_programa(t):
	'''programa : programa1 programa2 programa3 main programa3
	            | empty'''
	pass

def p_programa1(t):
	'''programa1 : RES_PROTO prototipos seen_prototipo programa1_1
				 '''
	pass

def p_seen_prototipo(t):
	'seen_prototipo : '
	global nombre_pro_act
	global tipo_pro_actual
	insert_procedimiento(nombre_pro_act,tipo_pro_actual,1)
	insert_variable(nombre_pro_act,tipo_pro_actual,2)
	pass

def p_programa1_1(t):
	'''programa1_1 : programa1
				   | empty
				   '''
	pass

def p_programa2(t):
	'''programa2 : programa2 vars
				 | empty
				 '''
	pass

def p_programa3(t):
	'''programa3 : programa3 modulos
				 | empty
				 '''
	pass

def p_prototipos(t):
	'''prototipos : RES_FUNC dato seen_dato ID LPAREN prototipos_1 RPAREN'''
	global nombre_pro_act 
	nombre_pro_act = t[4]
	pass

def p_seen_dato(t):
	'seen_dato :'
	global tipo_pro_actual
	tipo_pro_actual  = tipo_pro

def p_prototipos_1(t):
	''' prototipos_1 : tipo ID prototipos_2'''
	pass

def p_prototipos_2(t):
	'''prototipos_2  : COMMA prototipos_1
					 | empty
					 '''

def p_dato(t):
	'''dato : RES_INT
			| RES_FLOAT
			| RES_BOOLEAN
			| RES_STRING 
			'''
	global tipo_pro 
	tipo_pro = t[1]
	pass

def p_tipo(t):
	'''tipo : dato
			| estructura
			'''
	pass

def p_estructura(t):
	'''estructura : list
				  | array
				  '''
	pass

def p_vars(t):
	'vars : RES_DEF vars1 '
	pass

def p_vars1(t):
	'''vars1 : estructura
			| estructura vars1
			| dato ID vars2 vars1_1
			'''
	pass

def p_vars1_1(t):
	''' vars1_1 : vars1
				| empty
				'''
	pass

def p_vars2(t):
	'''vars2 : EQUALS cons
			| vars3
			'''
	pass

def p_vars3(t):
	'''vars3 : COMMA ID vars3
			| empty
			'''
	pass

def p_list(t):
	'list : RES_LIST dato ID list1 '
	pass

def p_list1(t):
	'''list1 : LCURLY cons_loop RCURLY
			 | empty
			 '''
	pass

def p_cons_loop(t):
	'''cons_loop : cons cons_loop_1
				 '''
	pass

def p_cons_loop_1(t):
	'''cons_loop_1 : COMMA cons_loop
				   | empty'''	

def p_array(t):
	'array : RES_ARRAY dato ID LBRACKET CTE_INT RBRACKET array1 '
	pass

def p_array1(t):
	'''array1 : COL LBRACKET array2 RBRACKET
				| empty 
				'''
	pass

def p_array2(t):
	'''array2 : cons
				| cons COMMA array2
				'''
	pass

def p_modulos(t):
	'''modulos : prototipos COL  bloque'''
	pass

def p_bloque(t):
	'''bloque : estatutos bloque 
			  | empty
			  '''
	pass

def p_estatutos(t):
	'''estatutos : condicion E_END
				 | ciclo E_END
				 | lectura 
				 | escritura 
				 | asignacion 
				 | llamada 
				 | vars
				 '''
	pass

def p_ciclo(t):
	'''ciclo : while
			 | for
			 '''
	pass

def p_condicion(t):
	'''condicion : if
				 | switch
				 '''
	pass

def p_llamada(t):
	'llamada : ID LPAREN llamada1 RPAREN '
	pass

def p_llamada1(t):
	'''llamada1 : expresion
				| empty
				'''
	pass

def p_lectura(t):
	'lectura : RES_READ LPAREN tipo RPAREN '
	pass

def p_escritura(t):
	'escritura : RES_PRINT LPAREN escritura1 RPAREN '
	pass

def p_escritura1(t):
	'''escritura1 : expresion
				  | CTE_STRING 
				  '''
	pass 


def p_asignacion(t):
	'asignacion : ID EQUALS asignacion1 '
	pass

def p_asignacion1(t):
	'''asignacion1 : expresion
					| asignlist
					| asignarray
					'''
	pass

def p_asignlist(t):
	'asignlist : LCURLY asignlist1 RCURLY'
	pass

def p_asignlist1(t):
	'''asignlist1 : cons
				  | cons COMMA asignlist1
				  '''
	pass

def p_asignarray(t):
	'asignarray : LBRACKET asignarray1 RBRACKET'
	pass

def p_asignarray1(t):
	'''asignarray1 : cons
				| cons COMMA asignarray1
				'''
	pass

def p_while(t):
	'while : RES_WHILE LPAREN expresion RPAREN COL  bloque'
	pass

def p_for(t):
	'for : RES_FOR LPAREN forexp RPAREN COL  bloque'
	pass

def p_forexp(t):
	'''forexp : ID EQUALS cons COL expresion COL ID EQUALS expresion
			   '''
	pass
"""
def p_comparacion(t):
	'''comparacion : MAY
					| MAY_EQ
					| MIN
					| MIN_EQ
					| DIF
					'''
	pass
"""

def p_if(t):
	'''if : RES_IF LPAREN expresion RPAREN COL  bloque ifelse
		  '''
	pass

def p_ifelse(t):
	''' ifelse : RES_ELSE COL  bloque
			   | empty
			   '''
	pass

def p_switch(t):
	'switch : RES_SWITCH COL  switch2'
	pass

def p_switch2(t):
	'''switch2 : RES_CASE expresion COL  bloque switch2 
			   | empty
			   '''
	pass

def p_expresion(t):
	'''expresion : exp expresion_1
				  '''
	pass
def p_expresion_1(t):
	'''expresion_1 : MIN exp
				   | MIN_EQ exp
			 	   | MAY exp
				   | MAY_EQ exp
				   | DIF exp
				   | empty
				   '''

def p_exp(t):
	'''exp : termino exp1
		   '''
	pass

def p_exp1(t):
	'''exp1 : PLUS exp
			| MINUS exp
			| empty
			'''
	pass

def p_termino(t):
	'''termino : factor termino1
			   '''
	pass

def p_termino1(t):
	'''termino1 : TIMES termino
				| DIVIDE termino
				| empty
				'''
	pass

def p_factor(t):
	'''factor : LPAREN expresion RPAREN
			| cons
			| PLUS cons
			| MINUS cons
			'''
	pass

def p_cons(t):
	'''cons : ID
			| CTE_INT
			| CTE_FLOAT
			| consarray
			| conslist
			'''
	pass

def p_main(t):
	'''main : RES_START COL  bloque RES_END '''

	pass

def p_consarray(t):
	'consarray : ID LBRACKET CTE_INT RBRACKET EQUALS cons '
	pass

def p_conslist(t):
	'conslist : ID EQUALS LCURLY conslist1 RCURLY '
	pass

def p_conslist1(t):
	'''conslist1 : cons 
				| cons COMMA conslist1
				'''
	pass

def p_empty(t):
	'empty : '
	pass

def p_error(t):
	print "error sintactico"
	print "Syntax error at token", t.value ,">>", t.type
	# Just discard the token and tell the parser it's okay.
	yacc.restart()



import profile

yacc.yacc(method = 'LALR')
#yacc.parse(debug = 1)


program = []
for line in fileinput.input():
	program.append(line)
yacc.parse(' '.join(program))

print_tables(tabla_pro)