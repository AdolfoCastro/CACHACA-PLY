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
import tvariables
import ply.yacc as yacc
import fileinput

# Consigue el mapa de tokens
tokens = scanner.tokens
start = 'programa'

def p_programa(t):
	'''programa : programa1 programa2 programa3 main programa3
	            | empty'''
	pass

def p_programa1(t):
	'''programa1 : RES_PROTO prototipos empty_lines_almost_one programa1 NEW_LINE
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
	'''prototipos : RES_FUNC dato ID LPAREN prototipos_1 RPAREN'''
	pass

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
	'vars : RES_DEF vars1 empty_lines_almost_one'
	pass

def p_vars1(t):
	'''vars1 : estructura
			| estructura vars1
			| dato VAR vars2 vars1_1
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
	'''vars3 : COMMA VAR vars3
			| empty
			'''
	pass

def p_list(t):
	'list : RES_LIST dato ID list1 empty_lines_almost_one'
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
	'array : RES_ARRAY dato VAR LBRACKET CTE_INT RBRACKET array1 empty_lines_almost_one'
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
	'''modulos : prototipos COL empty_lines_almost_one bloque'''
	pass

def p_bloque(t):
	'''bloque : bloque NEW_LINE
	 		  | estatutos
			  | empty
			  '''
	pass

def p_estatutos(t):
	'''estatutos : condicion
				 | ciclo
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
				 | ifelse
				 | switch
				 '''
	pass

def p_llamada(t):
	'llamada : VAR LPAREN llamada1 RPAREN empty_lines_almost_one'
	pass

def p_llamada1(t):
	'''llamada1 : expresion
				| expresion COMMA llamada1
				'''
	pass

def p_lectura(t):
	'lectura : RES_READ LPAREN tipo RPAREN empty_lines_almost_one'
	pass

def p_escritura(t):
	'escritura : RES_PRINT LPAREN escritura1 RPAREN empty_lines_almost_one'
	pass

def p_escritura1(t):
	'''escritura1 : expresion COMMA escritura1
				| CTE_STRING  COMMA escritura1
				| expresion
				| CTE_STRING
				'''
	pass 

def p_asignacion(t):
	'asignacion : VAR EQUALS asignacion1 empty_lines_almost_one'
	pass

def p_asignacion1(t):
	'''asignacion1 : cons
					| VAR
					| expresion
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
	'while : RES_WHILE LPAREN expresion RPAREN COL empty_lines_almost_one bloque'
	pass

def p_for(t):
	'for : RES_FOR LPAREN forexp RPAREN COL empty_lines_almost_one bloque'
	pass

def p_forexp(t):
	'''forexp : ID EQUALS cons COL ID comparacion ID COL ID EQUALS expresion
			   | ID EQUALS cons COL ID comparacion cons COL ID EQUALS expresion
			   '''
	pass

def p_comparacion(t):
	'''comparacion : MAY
					| MAY_EQ
					| MIN
					| MIN_EQ
					| DIF
					'''
	pass

def p_if(t):
	'''if : RES_IF LPAREN expresion RPAREN COL empty_lines_almost_one bloque
		  '''
	pass

def p_ifelse(t):
	''' ifelse : RES_IF LPAREN expresion RPAREN COL empty_lines_almost_one bloque RES_ELSE COL empty_lines_almost_one bloque
			   '''
	pass

def p_switch(t):
	'switch : RES_SWITCH COL empty_lines_almost_one switch2'
	pass

def p_switch2(t):
	'''switch2 : RES_CASE expresion COL empty_lines_almost_one bloque
	           | switch2 NEW_LINE
			   | empty
			   '''
	pass

def p_expresion(t):
	'''expresion : exp
				 | exp MIN exp
				 | exp MIN_EQ exp
			 	 | exp MAY exp
				 | exp MAY_EQ exp
				 | exp DIF exp
				  '''
	pass

def p_exp(t):
	'''exp : termino exp1
		   | termino
		   '''
	pass

def p_exp1(t):
	'''exp1 : PLUS exp
			| MINUS exp
			'''
	pass

def p_termino(t):
	'''termino : factor termino1
			   | factor
			   '''
	pass

def p_termino1(t):
	'''termino1 : TIMES termino
				| DIVIDE termino
				'''
	pass

def p_factor(t):
	'''factor : LPAREN expresion RPAREN
			| PLUS cons
			| MINUS cons
			'''
	pass

def p_cons(t):
	'''cons : ID
			| CTE_INT
			| CTE_FLOAT
			| CTE_STRING
			| consarray
			| conslist
			'''
	pass

def p_main(t):
	'''main : RES_START COL NEW_LINE bloque RES_END empty_lines'''

	pass

def p_consarray(t):
	'consarray : ID LBRACKET CTE_INT RBRACKET EQUALS cons empty_lines_almost_one'
	pass

def p_conslist(t):
	'conslist : ID EQUALS LCURLY conslist1 RCURLY empty_lines_almost_one'
	pass

def p_conslist1(t):
	'''conslist1 : cons 
				| cons COMMA conslist1
				'''
	pass

def p_empty_lines(t):
	'''empty_lines : empty_lines NEW_LINE 
				   | empty
				   '''
	pass

def p_empty_lines_almost_one(t):
	'''empty_lines_almost_one : NEW_LINE empty_lines'''
	pass

def p_empty(t):
	'empty : '
	pass

def p_error(t):
	print "Syntax error at token", t.value ,">>", t.type
	# Just discard the token and tell the parser it's okay.
	yacc.errok()



import profile

yacc.yacc(method = 'LALR')
#yacc.parse(debug = 1)


program = []
for line in fileinput.input():
	program.append(line)
yacc.parse(' '.join(program))