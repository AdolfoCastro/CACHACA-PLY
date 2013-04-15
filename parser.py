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
from clases import *
import ply.yacc as yacc
import fileinput
from tvariables import *
from memory import *
from cuadruplos import *
from tconstantes import *

# Consigue el mapa de tokens
tokens = scanner.tokens
start = 'programa'

nombre_pro_act = None
tipo_pro = None
tipo_pro_actual  = None
nombre_var_actual = None
tipo_var = None
memoria = None
esta_global = False
nombre_var_asignacion = None

def p_programa(t):
	'''programa : programa1 valida_entra_global generaglo programa2 valida_salir_gobal programa3 main programa3
	            | empty'''
	pass

def p_prueba(t):
	'prueba : '
	global nombre_pro_act
	print nombre_pro_act
	print nombre_pro_act
	print nombre_pro_act
	print nombre_pro_act
	print nombre_pro_act
	pass

def p_generaglo(t):
	'generaglo : '
	global nombre_pro_act
	insert_procedimiento('Global',' ',0)
	tabla_pro[-1].se_uso = True
	nombre_pro_act = "Global"
	pass

def p_programa1(t):
	'''programa1 : RES_PROTO prototipos seen_prototipo programa1
				 | empty'''
	pass

def p_seen_prototipo(t):
	'seen_prototipo : '
	global nombre_pro_act
	global tipo_pro_actual
	insert_procedimiento(nombre_pro_act,tipo_pro_actual,1)
	pass

def p_programa2(t):
	'''programa2 : vars programa2 
				 | empty
				 '''
	pass

def p_valida_entra_global(t):
	'valida_entra_global : '
	global esta_global
	esta_global = True

def p_valida_salir_gobal(t):
	'valida_salir_gobal : '
	global esta_global
	esta_global = False


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
			| RES_DOUBLE
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
	'vars : RES_DEF COL vars1 '
	global memoria
	insert_variable(nombre_var_actual,tipo_pro_actual,memoria, nombre_pro_act)
	pass

def p_vars1(t):
	'''vars1 : estructura vars1
			| dato ID vars2 vars1_1
			'''
	global tipo_pro_actual

	global contEntLoc
	global contFlotLoc
	global contStrLoc
	global contDoubleLoc

	global contEntGlo
	global contFlotGlo
	global coutDoubleGlo
	global contStrGlo

	global memoria
	global esta_global
	tipo_pro_actual = tipo_pro
	if esta_global:
		if tipo_pro_actual == "Integer":
			memoria = contEntGlo
			contEntGlo += 1
		if tipo_pro_actual == "Float":
			memoria = contFlotGlo
			contFlotGlo += 1
		if tipo_pro_actual == "Double":
			memoria = coutDoubleGlo
			coutDoubleGlo += 1
		if tipo_pro_actual == "String":
			memoria = contStrGlo
			contStrGlo += 1
	else:
		if tipo_pro_actual == "Integer":
			memoria = contEntLoc
			contEntLoc += 1
		if tipo_pro_actual == "Float":
			memoria = contFlotLoc
			contFlotLoc += 1
		if tipo_pro_actual == "Double":
			memoria = contDoubleLoc
			contDoubleLoc += 1
		if tipo_pro_actual == "String":
			memoria = contStrLoc
			contStrLoc += 1
	global nombre_var_actual
	nombre_var_actual = t[2]
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
	'''modulos : prototipos se_uso COL  bloque '''
	pass

def p_se_uso(t):
	'se_uso : '
	global nombre_pro_act
	global tabla_pro
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == nombre_pro_act and not pro.se_uso:
			tabla_pro[n].se_uso = True
			break
		elif pro.nombre_funcion == nombre_pro_act and pro.se_uso:
			print "Sorry - function %s already exists" %nombre_pro_act
			sys.exit()
		elif n+1 == len(tabla_pro):
			print "Sorry - prototype %s doesn't exist" % nombre_pro_act
			sys.exit()
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
	'asignacion : seen_id_asignacion EQUALS asignacion1 insert_asignacion'
	pass

def p_seen_id_asignacion(t):
	'seen_id_asignacion : ID '
	global nombre_var_asignacion
	nombre_var_asignacion = t[1]

def p_insert_asignacion(t):
	'insert_asignacion : '
	global nombre_var_asignacion
	global tipo_var
	direccion_var_actual = get_address(nombre_var_asignacion,nombre_pro_act)
	tipo_var = busca_tipo(nombre_var_asignacion,nombre_pro_act)
	exp_1(direccion_var_actual,tipo_var)
	pass


def p_asignacion1(t):
	'''asignacion1 : exp
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
				   | EQ_EQ exp
				   | empty
				   '''

def p_exp(t):
	'''exp : termino exp1
		   '''
	pass

def p_cuadruplo_exp_4(t):
	'cuadruplo_exp_4 : '



def p_exp1(t):
	'''exp1 : PLUS exp cuadruplo_exp_4
			| MINUS exp cuadruplo_exp_4
			| empty
			'''
	signo = t[1]
	exp_2(signo)
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
	signo = t[1]
	exp_3(signo)
	pass

def p_factor(t):
	'''factor : LPAREN exp RPAREN
			  | cons
			  | PLUS cons
			  | MINUS cons
			  '''
	pass

def p_cons(t):
	'''cons : seen_id_cons exp_1
			| seen_int_cons exp_cons_int
			| seen_float_cons exp_cons_float
			| CTE_DOUBLE
			| CTE_STRING
			| RES_TRUE
			| RES_FALSE
			| consarray
			| conslist
			'''

	pass
def p_seen_id_cons(t):
	'''seen_id_cons : ID'''
	global nombre_var_actual 
	nombre_var_actual = t[1]
	pass


def p_seen_float_cons(t):
	'''seen_float_cons : CTE_FLOAT'''
	global nombre_var_actual 
	global tipo_var
	tipo_var = "Float"
	nombre_var_actual = t[1]
	pass

def p_seen_int_cons(t):
	'''seen_int_cons : CTE_INT'''
	global nombre_var_actual 
	global tipo_var
	tipo_var = "Integer"
	nombre_var_actual = t[1]
	pass

def p_exp_1(t):
	'exp_1 : '
	global nombre_var_actual
	global tipo_var
	direccion_var_actual = get_address(nombre_var_actual,nombre_pro_act)
	tipo_var = busca_tipo(nombre_var_actual,nombre_pro_act)
	exp_1(direccion_var_actual,tipo_var)

def p_exp_cons_int(t):
	'exp_cons_int : '
	global nombre_var_actual
	global tipo_var
	global contEntGlo
	global contEntLoc
	if nombre_var_actual == 'Global':
		insert_constante(nombre_var_actual,tipo_var,contEntGlo)
		contEntGlo+=1
	else:
		insert_constante(nombre_var_actual,tipo_var,contEntLoc)
		contEntLoc+=1


def p_exp_cons_float(t):
	'exp_cons_float : '
	global nombre_var_actual
	global tipo_var
	global contFlotGlo
	global contFlotLoc
	if nombre_var_actual == 'Global':
		insert_constante(nombre_var_actual,tipo_var,contFlotGlo)
		contEntGlo+=1
	else:
		insert_constante(nombre_var_actual,tipo_var,contFlotLoc)
		contFlotLoc+=1
	pass
def p_main(t):
	'''main : RES_START comienza_main COL bloque RES_END '''
	pass 

def p_comienza_main(t):
	'comienza_main : '
	insert_procedimiento("Main"," ",1)
	tabla_pro[-1].se_uso = True
	global nombre_pro_act
	nombre_pro_act = 'Main'
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
print_pilas()
print_constantes(tabla_cons)
print_cuadruplos(tabla_cuadruplos)
