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
from mprueba import *

# Consigue el mapa de tokens
tokens = scanner.tokens
start = 'programa'

nombre_pro_act = None
tipo_pro = None
tipo_pro_actual  = None
nombre_var_actual = None
tipo_var = None
memoria = 0
esta_global = False
nombre_var_asignacion = None
oper = None
nombre_var_for = None
param = None
dim_int = 0
cont_dim = 0
pila_dim = Stack()
arr = None
params = []


def p_programa(t):
	'''programa : ins_gt_main programa1 valida_entra_global generaglo programa2 valida_salir_gobal programa3 dir_gt_main main programa3
	            | empty'''
	pass

def p_ins_gt_main(t):
	'ins_gt_main : '
	goto_main()
	pass

def p_dir_gt_main(t):
	'dir_gt_main : '
	dir_main()
	pass

def p_generaglo(t):
	'generaglo : '
	global nombre_pro_act
	def_proc_1('Global',' ',0)
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
	def_proc_1(nombre_pro_act,tipo_pro_actual,cont_saltos)
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
	pass

def p_valida_salir_gobal(t):
	'valida_salir_gobal : '
	global esta_global
	esta_global = False
	pass

def p_programa3(t):
	'''programa3 : programa3 modulos
				 | empty
				 '''
	pass

def p_prototipos(t):
	'''prototipos : RES_FUNC dato seen_dato seen_nom_func  LPAREN prototipos_1 RPAREN'''
	pass

def p_seen_nom_func(t):
	'seen_nom_func : ID '
	global nombre_pro_act
	nombre_pro_act = t[1]
	pass


def p_seen_dato(t):
	'seen_dato :'
	global tipo_pro_actual
	tipo_pro_actual  = tipo_pro
	pass

# def p_prototipos_0(t):
# 	'prototipos_0 : prototipos_1'
# 	global param
# 	global tipo_var
	
# 	pass

def p_prototipos_1(t):
	''' prototipos_1 : tipo seen_id_proto prototipos_2
					| empty
					'''
	pass

def p_seen_id_proto(t):
	'seen_id_proto : ID'
	global param
	global tipo_pro
	global nombre_pro_act
	global memoria
	global contEntLoc
	global contFlotLoc
	global contDoubleLoc
	global contStrLoc
	global contBoolLoc
	param = t[1]
	if tipo_pro == "Integer":
		memoria = contEntLoc
		contEntLoc += 1
	elif tipo_pro == "Float":
		memoria = contFlotLoc
		contFlotLoc += 1
	elif tipo_pro == "Double":
		memoria = contDoubleLoc
		contDoubleLoc += 1
	elif tipo_pro == "String":
		memoria = contStrLoc
		contStrLoc += 1
	elif tipo_pro == "Boolean":
		memoria = contBoolLoc 
		contBoolLoc+=1
	def_proc_2(param, tipo_pro, memoria, nombre_pro_act)
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
	'vars : RES_DEF COL vars1'
	pass

def p_vars_1(t):
	'vars_1 : dato ID vars2 vars1_1 '
	global tipo_pro_actual

	global contEntLoc
	global contFlotLoc
	global contStrLoc
	global contDoubleLoc
	global contBoolLoc

	global contEntGlo
	global contFlotGlo
	global coutDoubleGlo
	global contStrGlo
	global contBoolGlo

	global memoria
	global esta_global
	tipo_pro_actual = tipo_pro
	if esta_global:
		if tipo_pro_actual == "Integer":
			memoria = contEntGlo
			contEntGlo += 1
		elif tipo_pro_actual == "Float":
			memoria = contFlotGlo
			contFlotGlo += 1
		elif tipo_pro_actual == "Double":
			memoria = coutDoubleGlo
			coutDoubleGlo += 1
		elif tipo_pro_actual == "String":
			memoria = contStrGlo
			contStrGlo += 1
		elif tipo_pro_actual == "Boolean":
			memoria = contBoolGlo 
			contBoolGlo+=1
	else:
		if tipo_pro_actual == "Integer":
			memoria = contEntLoc
			contEntLoc += 1
		elif tipo_pro_actual == "Float":
			memoria = contFlotLoc
			contFlotLoc += 1
		elif tipo_pro_actual == "Double":
			memoria = contDoubleLoc
			contDoubleLoc += 1
		elif tipo_pro_actual == "String":
			memoria = contStrLoc
			contStrLoc += 1
		elif tipo_pro_actual == "Boolean":
			memoria = contBoolLoc 
			contBoolLoc+=1

	global nombre_var_actual
	nombre_var_actual = t[2]
	insert_variable(nombre_var_actual,tipo_pro_actual,memoria, nombre_pro_act)
	pass

def p_vars1(t):
	'''vars1 : estructura empty
			| vars_1
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
	pass

def p_array(t):
	'array : RES_ARRAY dato crea_arr LBRACKET dim RBRACKET genera_ms array1 '
	global tipo_pro
	global nombre_pro_act
	global nombre_var_actual
	global contEntLoc
	global contFlotLoc
	global contStrLoc
	global contDoubleLoc
	global contBoolLoc
	global contEntGlo
	global contFlotGlo
	global coutDoubleGlo
	global contStrGlo
	global contBoolGlo
	global memoria
	global esta_global
	mem = arr_mem(nombre_pro_act, nombre_var_actual)
	if esta_global:
		if tipo_pro.replace("arr", "") == "Integer":
			memoria = contEntGlo
			contEntGlo += mem
		elif tipo_pro.replace("arr", "") == "Float":
			memoria = contFlotGlo
			contFlotGlo += mem
		elif tipo_pro.replace("arr", "") == "Double":
			memoria = coutDoubleGlo
			coutDoubleGlo += mem
		elif tipo_pro.replace("arr", "") == "String":
			memoria = contStrGlo
			contStrGlo += mem
		elif tipo_pro.replace("arr", "") == "Boolean":
			memoria = contBoolGlo 
			contBoolGlo+= mem
	else:
		if tipo_pro.replace("arr", "") == "Integer":
			memoria = contEntLoc
			contEntLoc += mem
		elif tipo_pro.replace("arr", "") == "Float":
			memoria = contFlotLoc
			contFlotLoc += mem
		elif tipo_pro.replace("arr", "") == "Double":
			memoria = contDoubleLoc
			contDoubleLoc += mem
		elif tipo_pro.replace("arr", "") == "String":
			memoria = contStrLoc
			contStrLoc += mem
		elif tipo_pro.replace("arr", "") == "Boolean":
			memoria = contBoolLoc 
			contBoolLoc+=mem
	pass

def p_genera_ms(t):
	'genera_ms : '
	global nombre_var_actual
	global nombre_pro_act
	genera_m_arr(nombre_var_actual, nombre_pro_act)
	pass

def p_crea_arr(t):
	'crea_arr : ID '
	global tipo_pro
	global nombre_pro_act
	global nombre_var_actual
	global contEntLoc
	global contFlotLoc
	global contStrLoc
	global contDoubleLoc
	global contBoolLoc

	global contEntGlo
	global contFlotGlo
	global coutDoubleGlo
	global contStrGlo
	global contBoolGlo

	global memoria
	global esta_global
	tipo_pro_actual = tipo_pro
	if esta_global:
		if tipo_pro_actual == "Integer":
			memoria = contEntGlo
			contEntGlo += 1
		elif tipo_pro_actual == "Float":
			memoria = contFlotGlo
			contFlotGlo += 1
		elif tipo_pro_actual == "Double":
			memoria = coutDoubleGlo
			coutDoubleGlo += 1
		elif tipo_pro_actual == "String":
			memoria = contStrGlo
			contStrGlo += 1
		elif tipo_pro_actual == "Boolean":
			memoria = contBoolGlo 
			contBoolGlo+=1
	else:
		if tipo_pro_actual == "Integer":
			memoria = contEntLoc
			contEntLoc += 1
		elif tipo_pro_actual == "Float":
			memoria = contFlotLoc
			contFlotLoc += 1
		elif tipo_pro_actual == "Double":
			memoria = contDoubleLoc
			contDoubleLoc += 1
		elif tipo_pro_actual == "String":
			memoria = contStrLoc
			contStrLoc += 1
		elif tipo_pro_actual == "Boolean":
			memoria = contBoolLoc 
			contBoolLoc+=1
	nombre_var_actual = t[1]
	p_tipos.push(tipo_pro)
	insert_variable(nombre_var_actual, tipo_pro, memoria, nombre_pro_act)
	pass

def p_dim(t):
	'''dim : dim_cte dim_struct dim2'''
	pass

def p_dim_cte(t):
	'dim_cte : CTE_INT'
	global dim_int
	dim_int = t[1]
	pass

def p_dim_struct(t):
	'dim_struct : '
	global nombre_var_actual
	global nombre_pro_act
	global dim_int
	insert_dim_arr(nombre_var_actual, nombre_pro_act, dim_int)
	pass

def p_dim2(t):
	'''dim2 : COMMA dim
			| empty
			'''
	pass

def p_array1(t):
	'''array1 : COL LBRACKET array2 RBRACKET array1
				| empty 
				'''
	pass

def p_array2(t):
	'''array2 : cons array3'''
	pass

def p_array3(t):
	'''array3 : COMMA array2
				| empty
				'''

def p_modulos(t):
	'''modulos : prototipos se_uso COL bloque cuad_def_proc_4 '''
	pass

def p_cuad_def_proc_4(t):
	'cuad_def_proc_4 : '
	def_proc_4()
	pass

def p_se_uso(t):
	'se_uso : '
	global nombre_pro_act
	global tabla_pro
	global cont_saltos
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == nombre_pro_act and not pro.se_uso:
			tabla_pro[n].se_uso = True
			def_proc_3(n, get_cont_saltos())
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
			  | return bloque
			  | empty
			  '''
	pass

def p_return(t):
	'return : RES_RETURN exp'
	global nombre_pro_act
	global tabla_pro
	genera_return(nombre_pro_act, tabla_pro)
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
	'llamada : seen_id_call LPAREN call_proc_2 llamada1 RPAREN call_proc_4 '
	pass

def p_call_proc_4(t):
	'call_proc_4 : '
	global func_actual
	global dirb_actual
	global params
	
	params.reverse()
	arg =[]
	tipo = []
	for param in params:
		arg.append(pila_o.pop())
		tipo.append(p_tipos.pop())

	arg.reverse()
	tipo.reverse()
	for n,param in enumerate(params):
		call_proc_3(param, arg[n], tipo[n])

	call_proc_4(func_actual, dirb_actual)
	pass

def p_seen_id_call(t):
	'seen_id_call : ID'
	global tabla_pro
	global func_actual
	global param_actual
	global dirb_actual
	func_actual = t[1]
	existe = existe_pro(func_actual)
	call_proc_1(existe, func_actual)
	for proc in tabla_pro:
		if proc.nombre_funcion == func_actual:
			param_actual = [param for param in proc.param]
			dirb_actual = proc.dir_base
	pass

def p_call_proc_2(t):
	'call_proc_2 : '
	global func_actual
	call_proc_2(func_actual)
	pass

def p_llamada1(t):
	'''llamada1 : exp call_proc_3 param
				| empty
				'''
	pass

def p_call_proc_3(t):
	'call_proc_3 : '
	global param_actual
	global params
	if param_actual:
		params.append(param_actual.pop())
	pass

def p_param(t):
	'''param : COMMA exp call_proc_3 param
			| empty'''
	pass

def p_lectura(t):
	'lectura : RES_READ LPAREN tipo RPAREN '
	pass

def p_escritura(t):
	'escritura : RES_PRINT LPAREN cons RPAREN cuadruplo_est_prnt'
	pass

def p_cuadruplo_est_prnt(t):
	'cuadruplo_est_prnt : '
	est_print()
	pass

#def p_escritura1(t):
#	'''escritura1 : exp
#				  | CTE_STRING 
#				  '''
#	pass 


def p_asignacion(t):
	'''asignacion : seen_id_asignacion consarray EQUALS cuadruplo_exp_8_asignacion asignacion1 insert_asignacion cuadruplo_exp_9_asignacion'''
	global arr
	arr = None
	pass

def p_cuadruplo_exp_8_asignacion(t):
	'cuadruplo_exp_8_asignacion : '
	exp_8("=")
	pass

def p_cuadruplo_exp_9_asignacion(t):
	'cuadruplo_exp_9_asignacion : '
	global arr
	global nombre_pro_act
	global nombre_var_actual
	if es_dim(nombre_pro_act,nombre_var_actual):
		asign_arr(get_address(arr, nombre_pro_act))
		arr = None
	else:
		exp_9()
	pass 

# def p_asigna_arr(t):
# 	'asigna_arr : '
# 	asign_arr()
# 	pass


def p_seen_id_asignacion(t):
	'seen_id_asignacion : ID '
	global nombre_var_asignacion
	global nombre_var_actual
	nombre_var_asignacion = t[1]
	nombre_var_actual = t[1]

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
				   | llamada
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
	'while : RES_WHILE cuadruplo_est_while_1 LPAREN expresion RPAREN cuadruplo_est_while_2 COL  bloque cuadruplo_est_while_3'
	pass

def p_cuadruplo_est_while_1(t):
	'cuadruplo_est_while_1 : '
	est_while_1()
	pass

def p_cuadruplo_est_while_2(t):
	'cuadruplo_est_while_2 : '
	est_while_2()
	pass

def p_cuadruplo_est_while_3(t):
	'cuadruplo_est_while_3 : '
	est_while_3()
	pass

def p_for(t):
	'for : RES_FOR LPAREN forexp RPAREN sale_update COL bloque cuadruplo_est_for_3 '
	pass

def p_sale_update(t):
	'sale_update : '
	exp_for_(False)
	pass

def p_forexp(t):
	'''forexp : asignacion cuadruplo_est_for_1 COL expresion cuadruplo_est_for_2 COL entra_update asignacion
			   '''
	pass

def p_entra_update(t):
	'entra_update : '
	exp_for_(True)
	pass

# def p_seen_id_for(t):
# 	'seen_id_for : ID'
# 	global nombre_var_for
# 	nombre_var_for = t[1]
# 	pass

def p_cuadruplo_est_for_1(t):
	'cuadruplo_est_for_1 : '
	est_for_1()
	pass

def p_cuadruplo_est_for_2(t):
	'cuadruplo_est_for_2 : '
	est_for_2()
	pass

def p_cuadruplo_est_for_3(t):
	'cuadruplo_est_for_3 : '
	est_for_3()
	pass

# def p_cuadruplo_est_for_4(t):
# 	'cuadruplo_est_for_4 : '
# 	est_for_4()
# 	pass

#def p_comparacion(t):
#	'''comparacion : MAY
#					| MAY_EQ
#					| MIN
#					| MIN_EQ
#					| DIF
#					'''
#	pass


def p_if(t):
	'''if : RES_IF LPAREN expresion RPAREN cuadruplo_est_if_1 COL  bloque ifelse
		  '''
	pass

def p_cuadruplo_est_if_1(t):
	'cuadruplo_est_if_1 : '
	est_if_1()
	pass

def p_ifelse(t):
	''' ifelse : cuadruplo_est_if_else_2 RES_ELSE COL  bloque cuadruplo_est_if_else_3
			   | empty cuadruplo_est_if_2
			   '''
	pass

def p_cuadruplo_est_if_2(t):
	'cuadruplo_est_if_2 : '
	est_if_2()
	pass

def p_cuadruplo_est_if_else_2(t):
	'cuadruplo_est_if_else_2 : '
	est_if_else_2()
	pass

def p_cuadruplo_est_if_else_3(t):
	'cuadruplo_est_if_else_3 : '
	est_if_else_3()
	pass

def p_switch(t):
	'switch : RES_SWITCH LPAREN seen_exp_switch RPAREN COL  switch2'
	pass

def p_seen_exp_switch(t):
	'seen_exp_switch : exp'
	est_case_1()

def p_switch2(t):
	'''switch2 : RES_CASE seen_exp_case COL seen_case_3  bloque  seen_case_4 switch2 
			   | empty
			   '''
	pass

def p_seen_case_3(t):
	'seen_case_3 : '
	est_case_3()
	pass

def p_seen_case_4(t):
	'seen_case_4 : '
	est_case_4()
	pass

def p_seen_exp_case(t):
	'seen_exp_case : exp '
	est_case_2()
	pass

def p_expresion(t):
	'''expresion : exp expresion_1 cuadruplo_exp_9
				  '''
	pass
def p_expresion_1(t):
	'''expresion_1 : see_rel cuadruplo_exp_8 exp
				   | empty
				   '''
	pass

def p_see_rel(t):
	'''see_rel : MIN
				| MIN_EQ
				| MAY
				| MAY_EQ
				| DIF
				| EQ_EQ
				'''
	global oper
	oper = t[1]
	pass

def p_cuadruplos_exp_8(t):
	'cuadruplo_exp_8 : '
	global oper
	exp_8(oper)
	pass

def p_cuadruplos_exp_9(t):
	'cuadruplo_exp_9 : '
	exp_9()
	pass

def p_exp(t):
	'''exp : termino cuadruplo_exp_4 exp1
		   '''
	pass

def p_exp1(t):
	'''exp1 : see_operador_e cuadruplos_exp_2 exp
			| empty
			'''
	pass

def p_see_operador_e(t):
	'''see_operador_e : PLUS
					  | MINUS
				'''
	global oper
	oper = t[1]
	pass

def p_cuadruplos_exp_2(t):
	'''cuadruplos_exp_2 : '''
	global oper
	exp_2(oper)
	pass

def p_termino(t):
	'''termino : factor cuadruplo_exp_5 termino1
			   '''
	pass
 
def p_termino1(t):
	'''termino1 : see_operador_f cuadruplos_exp_3 termino
				| empty
				'''
	pass

def p_see_operador_f(t):
	'''see_operador_f : TIMES
					| DIVIDE
				'''
	global oper
	oper = t[1]
	pass

def p_cuadruplos_exp_3(t):
	'''cuadruplos_exp_3 : '''
	global oper
	exp_3(oper)
	pass

def p_cuadruplo_exp_4(t):
	'cuadruplo_exp_4 : '
	exp_4()
	pass

def p_cuadruplo_exp_5(t):
	'cuadruplo_exp_5 : '
	exp_5()
	pass

def p_factor(t):
	'''factor : LPAREN cuadruplo_exp_6 exp RPAREN cuadruplo_exp_7
			  | cons
			  | PLUS cons
			  | MINUS cons
			  '''
	pass

def p_cuadruplo_exp_6(t):
	'cuadruplo_exp_6 : '
	exp_6()
	pass

def p_cuadruplo_exp_7(t):
	'cuadruplo_exp_7 : '
	exp_7()
	pass

def p_cons(t):
	'''cons : seen_id_cons consarray exp_1
			| seen_int_cons exp_cons_int
			| seen_float_cons exp_cons_float
			| seen_double_cons exp_cons_double
			| seen_string_cons exp_cons_string
			| seen_bool
			| conslist
			'''
	pass

def p_seen_bool(t):
	'''seen_bool : RES_TRUE
				| RES_FALSE'''
	global nombre_var_actual
	global tipo_var
	global contBoolCons
	tipo_var = "Boolean"
	insert_constante(t[1], tipo_var, contBoolCons)
	pila_o.push(contBoolCons)
	p_tipos.push("Boolean")
	contBoolCons+=1
	pass

def p_seen_id_cons(t):
	'''seen_id_cons : ID'''
	global nombre_var_actual 
	global _arr
	global nombre_pro_act
	_arr = None
	nombre_var_actual = t[1]
	if es_dim(nombre_pro_act, nombre_var_actual):
		_arr = nombre_var_actual
	pass


def p_seen_float_cons(t):
	'''seen_float_cons : CTE_FLOAT'''
	global nombre_var_actual 
	global tipo_var
	tipo_var = "Float"
	nombre_var_actual = t[1]
	pass

def p_seen_double_cons(t):
	'''seen_double_cons : CTE_DOUBLE'''
	global nombre_var_actual 
	global tipo_var
	tipo_var = "Double"
	nombre_var_actual = t[1]
	pass

def p_seen_string_cons(t):
	'''seen_string_cons : CTE_STRING'''
	global nombre_var_actual 
	global tipo_var
	tipo_var = "String"
	nombre_var_actual = t[1]
	pass

def p_seen_int_cons(t):
	'''seen_int_cons : CTE_INT'''
	global nombre_var_actual 
	global tipo_var
	tipo_var = "Integer"
	nombre_var_actual = t[1]
	print nombre_var_actual
	pass

def p_exp_1(t):
	'exp_1 : '
	global nombre_var_actual
	global nombre_pro_act
	global tipo_var
	global _arr
	if _arr:
		tipo_var = busca_tipo(arr,nombre_pro_act)
		suma_base()
		direccion_var_actual = pila_o.pop()
		_arr = None
	else:
		tipo_var = busca_tipo(nombre_var_actual,nombre_pro_act)
		direccion_var_actual = get_address(nombre_var_actual,nombre_pro_act)
	exp_1(direccion_var_actual,tipo_var)

def p_exp_cons_int(t):
	'exp_cons_int : '
	global nombre_var_actual
	global tipo_var
	global contEntCons
	insert_constante(nombre_var_actual, tipo_var, contEntCons)
	pila_o.push(contEntCons)
	p_tipos.push("Integer")
	contEntCons+=1

def p_exp_cons_float(t):
	'exp_cons_float : '
	global nombre_var_actual
	global tipo_var
	global contFlotCons
	insert_constante(nombre_var_actual, tipo_var, contFlotCons)
	pila_o.push(contFlotCons)
	p_tipos.push("Float")
	contFlotCons+=1

def p_exp_cons_double(t):
	'exp_cons_double : '
	global nombre_var_actual
	global tipo_var
	global contDoubleCons
	insert_constante(nombre_var_actual, tipo_var, contDoubleCons)
	pila_o.push(contDoubleCons)
	p_tipos.push("Double")
	contDoubleCons+=1

def p_exp_cons_string(t):
	'exp_cons_string : '
	global nombre_var_actual
	global tipo_var
	global contStrCons
	insert_constante(nombre_var_actual, tipo_var, contStrCons)
	pila_o.push(contStrCons)
	p_tipos.push("String")
	contStrCons+=1

def p_main(t):
	'''main : RES_START comienza_main COL bloque RES_END '''
	crea_end()
	pass 

def p_comienza_main(t):
	'comienza_main : '
	def_proc_1("Main"," ",1)
	tabla_pro[-1].se_uso = True
	global nombre_pro_act
	nombre_pro_act = 'Main'
	pass

def p_consarray(t):
	'''consarray : is_dim LBRACKET dim_pos RBRACKET
				| empty'''
	pass

def p_is_dim(t):
	'is_dim : '
	global nombre_var_actual
	global nombre_pro_act
	global arr
	global cont_dim
	arr = None
	if not es_dim(nombre_pro_act, nombre_var_actual):
		print "Sorry, variable %s is neither a list nor an array" % nombre_var_actual
		sys.exit()
	else:
		cont_dim = 0
		pila_dim.push(nombre_var_actual)
		pila_dim.push(cont_dim)
		arr = nombre_var_actual
	pass

def p_dim_pos(t):
	'dim_pos : seen_int_pos dim_pos_2'
	pass

def p_seen_int_pos(t):
	'''seen_int_pos : exp'''
	global nombre_pro_act
	global nombre_var_actual
	global pila_dim
	global cont_dim
	global arr
	ls = get_ls(nombre_pro_act, arr, cont_dim)
	m = get_m(nombre_pro_act, arr, cont_dim)
	ln = arr_size(nombre_pro_act, arr)
	verifica_tope_arr(ls, m, cont_dim, ln)
	cont_dim+=1
	pass

def p_dim_pos_2(t):
	'''dim_pos_2 : COMMA dim_pos
				| empty'''

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
	print "Sorry, what did you mean by %s, at line %d?"%(t.value,t.lexer.lineno)
	print "Sorry - Syntax error at token", t.value ,">>", t.type
	sys.exit()
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
# lee_cuadruplos(tabla_cuadruplos)
# print_tables_alfinal(tabla_pro)
# print_temporales(tabla_tempo)

#print "Num Saltos: %d" %cont_saltos
