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

# Consigue el mapa de tokens
tokens = scanner.tokens
start = 'programa'
'''
/*******************globales********************/
int contEntGlo=0;
int contFlotGlo=1000;
int contStrGlo=2000;
int contBoolGlo=3000;
//int contSaltosGlo=4000;
/*******************Locales********************/
int contEntLoc=5000;
int contFlotLoc=6000;
int contStrLoc=7000;
int contBoolLoc=8000;
//int contSaltosLoc=9000;
/*******************Temporales*****************/
int contEntTmp=10000;
int contFlotTmp=11000;
int contStrTmp=12000;
int contBoolTmp=13000;
//int contSaltosTmp=14000;
/*******************Constantes*****************/
int contEntCons=15000;
int contFlotCons=16000;
int contStrCons=17000;
int contBoolCons=18000;
//int contSaltosCons=19000;
'''

nombre_pro_act = None
tipo_pro = None
tipo_pro_actual  = None
nombre_var_actual = None

def p_programa(t):
	'''programa : programa1 generaglo programa2 programa3 main programa3
	            | empty'''
	pass

def p_generaglo(t):
	'generaglo : '
	global nombre_pro_act
	insert_procedimiento('Global',' ',0)
	nombre_pro_act = "Global"
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
			| RES_DOUBLE
			| RES_BOOLEAN
			| RES_DOUBLE
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
	insert_variable(nombre_var_actual,tipo_pro_actual,1, nombre_pro_act)
	pass

def p_vars1(t):
	'''vars1 : estructura vars1
			| dato ID vars2 vars1_1
			'''
	global tipo_pro_actual
	tipo_pro_actual = tipo_pro
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
	'''modulos : prototipos se_uso COL  bloque'''
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
	'asignacion : ID EQUALS asignacion1 '
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
	'''cons : ID exp_1
			| CTE_INT
			| CTE_FLOAT
			| CTE_DOUBLE
			| CTE_STRING
			| RES_TRUE
			| RES_FALSE
			| consarray
			| conslist
			'''
	pass

#no se que hace esta funcion, me produce errores "Adolfo"
def p_exp_1(t):
	'exp_1 : '
	#global tabla_pro
	#global nombre_pro_act
	#tabla_pro[subindice_tabla_pro_pro_actual(nombre_pro_act)].var
	#exp_1(t[1], tipo)
	

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
