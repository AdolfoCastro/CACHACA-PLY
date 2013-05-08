from tvariables import *
from tconstantes import *

class Memoria:
	def __init__(self, dire, val):
		self.direccion = dire
		self.valor = val

class Parametro:
	def __init__(self,dire,poin,val):
		self.direccion = dire
		self.pointer = poin
		self.valor = val

class Returnes:
	def __init__(self,direccion,valor):
		self.direccion = direccion
		self.valor = valor

tabla_tempo=[]
tabla_const=[]
tabla_varia=[]
tabla_varia_globales=[]
tabla_parametros = []
tabla_retrun = []
contcuad = 0
pila_brincos = []
tabla_varia_aux = []
#Carga en memoria la tabla de globales del programa.
def carga_globales():
	global tabla_pro
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == "Global":
			for variable in pro.var:
				mem = Memoria(variable.direccion,variable.valor)
				tabla_varia_globales.append(mem)
	pass
#Carga en memoria las constantes que se vana utilizar durante la ejecucion del programa.
def carga_const():
	for cons in tabla_cons:
			mem = Memoria(cons.dirb,cons.cons)
			tabla_const.append(mem)
#Primeramente carga el scope de main para la ejecucion del programa, posteriormetne
#por cada llamada que se realice a una funcion carga las variables de esta hasta el 
#momento en que se termina la ejecucion de la funcion y esta memoria es eliminada.
def carga_scope_local(proc):
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			for variable in pro.var:
				mem = Memoria(variable.direccion,variable.valor)
				tabla_varia.append(mem)
	pass
#Funcion que va leyendo linea por linea lo que en va apareciendo en los cuadruplos
# para posteriormente son utilizados en la maquina_virtual() para generar la ejecucion
# del programa
def lee_cuadruplos():
	global contcuad
	currentCuadList = tabla_cuadruplos
	for currentCuad in currentCuadList:
		contcuad += 1
# Funcion utilizada para extraer los valores de las direcciones que aparecen en los cuadruplos
# las cuales seran utilizadas para funciones aritmeticas y comparaciones
def dame_o1_o2(i):
	global op1
	global op2
	if tabla_cuadruplos[i].o1 >=11000 and tabla_cuadruplos[i].o1 <=15999:
		op1 = get_value_temp(tabla_cuadruplos[i].o1)
	elif tabla_cuadruplos[i].o1 >= 16000 and tabla_cuadruplos[i].o1 <=20999:
		op1 = get_value_const(tabla_cuadruplos[i].o1)
	elif tabla_cuadruplos[i].o1 >= 0 and tabla_cuadruplos[i].o1 <=9999:
		op1 = get_value_var(tabla_cuadruplos[i].o1)

	if tabla_cuadruplos[i].o2 >=11000 and tabla_cuadruplos[i].o2 <=15999:
		op2 =  get_value_temp(tabla_cuadruplos[i].o2)
	elif tabla_cuadruplos[i].o2 >= 16000 and tabla_cuadruplos[i].o2 <=20999:
		op2 =  get_value_const(tabla_cuadruplos[i].o2)
	elif tabla_cuadruplos[i].o2 >= 0 and tabla_cuadruplos[i].o2 <=9999:
		op2 =  get_value_var(tabla_cuadruplos[i].o2)
# Funcion que toma una direccion temporal y regresa su valor que esta alojado en la memoria.
def get_value_temp(dirb):
	global tabla_tempo
	for temp in tabla_tempo:
		if temp.direccion == dirb:
			return temp.valor
	return False
	pass
# Funcion que toma una direccion temporal y cambia su valor que esta alojado en la memoria.
def set_value_tmp(dirb,newvalue):
	global tabla_tempo
	for temp in tabla_tempo:
		if temp.direccion == dirb:
			temp.valor = newvalue
			break
# Funcion que toma una direccion constante y regresa su valor que esta alojado en la memoria.
def get_value_const(dirb):
	global tabla_const
	for constante in tabla_const:
		if constante.direccion == dirb:
			return constante.valor
	pass
# Las siguente dos funciones son utilizadas para buscar los valores de las variables de cada 
# funcion, dado que la memoria se maneja como una anidacion de listas para realizar las llamadas
# de funciones, todas las funciones que necesiten obtener o modificar un valor de la memoria de 
# variables de las funciones, necesitaran tener una funcion auxiliar que les ayuda a entrar hasta
# la seccion de memoria donde se esta realizando la funcion (la lista mas profunda).
# Esta funcion regresa el valor que se tiene actualmente en la variable buscada.
def get_value_var(dirb):
	global tabla_varia
	global tabla_varia_globales
	if tabla_varia:
		if isinstance(tabla_varia[-1],list):
			return get_value_var_aux(dirb,tabla_varia[-1])
		else:
			for variable in tabla_varia:
				if variable.direccion == dirb:
					return variable.valor
	if tabla_varia_globales:
		for variable in tabla_varia_globales:
			if variable.direccion == dirb:
				return variable.valor

def get_value_var_aux(dirb,lista):
	global tabla_varia_globales
	if lista:
		if isinstance(lista[-1],list):
			return get_value_var_aux(dirb,lista[-1])
		else:
			for variable in lista:
				if variable.direccion == dirb:
					return variable.valor
	if tabla_varia_globales:
		for variable in tabla_varia_globales:
			if variable.direccion == dirb:
				return variable.valor
# Funcion que vusca el valor de los parametros con los que se hizo la llamada, para poder realizar
# la funcion que se corre.(utiliza aux)
def get_value_param(dirb):
	global tabla_varia
	global tabla_varia_globales
	entra = "entra"
	if isinstance(tabla_varia[-1][-1],list):
		return get_value_param_aux(dirb,tabla_varia[-1])
	else:
		for variable in tabla_varia:
			if variable.direccion == dirb:
				return variable.valor
	if tabla_varia_globales:
		for variable in tabla_varia_globales:
			if variable.direccion == dirb:
				return variable.valor

def get_value_param_aux(dirb,lista):
	global tabla_varia_globales
	if isinstance(lista[-1][-1],list):
		return get_value_param_aux(dirb,lista[-1])
	else:
		for variable in lista:
			if variable.direccion == dirb:
				return variable.valor
	if tabla_varia_globales:
		for variable in tabla_varia_globales:
			if variable.direccion == dirb:
				return variable.valor
# Funcion que cambia los valores de las variabes en la memoria del procedimiento en que se
# esta corriendo.
def cambia_valor(dirb,val):
	global tabla_varia
	global tabla_varia_globales
	if tabla_varia:
		if isinstance(tabla_varia[-1],list):
			cambia_valor_aux(dirb,val,tabla_varia[-1])
		else:
			for variable in tabla_varia:
				if variable.direccion == dirb:
					variable.valor = val
					break
	if tabla_varia_globales:
		for variable in tabla_varia_globales:
			if variable.direccion == dirb:
				variable.valor = val

def cambia_valor_aux(dirb,val,lista):
	global tabla_varia_globales
	if lista:
		if isinstance(lista[-1],list):
			cambia_valor_aux(dirb,val,lista[-1])
		else:
			for variable in lista:
				if variable.direccion == dirb:
					variable.valor = val
					break
	if tabla_varia_globales:
		for variable in tabla_varia_globales:
			if variable.direccion == dirb:
				variable.valor = val
	pass
# Funcion que busca en las tablas procedentes de la compilacion, y genera el espacio en la memoria
# suficientes para realizar el procedimiento llamado, el cual sera alojado en la memoria de variables
# de la funcion actual
def crea_espacio(proc):
	global tabla_pro
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			auxlist  = []
			for variable in pro.var:
				mem = Memoria(variable.direccion,variable.valor)
				auxlist.append(mem)
			for variable in pro.param:
				mem = Memoria(variable.direccion,variable.valor)
				auxlist.append(mem)
	return auxlist
# Ya generado el espacio de la memoria esta es introducida dentro de la memoria de variables para la
# funcion.
def genera_memoria_proc(proc,lista):
	if lista:
		if isinstance(lista[-1],list):
			if lista[-1]:
				genera_memoria_proc(proc,lista[-1])
			else:
				mem = crea_espacio(proc)
				lista.append(mem)
		else:
			aux = crea_espacio(proc)
			lista.append(aux)
	pass
#Borrado de la memoria del procedimiento al terminar la ejecucion de este
def borra_memoria(proc):
	if isinstance(proc[-1],list):
		if proc[-1]:
			if isinstance(proc[-1][-1],list):
				borra_memoria(proc[-1])
			else:
				del proc[-1]	
#Procedimientos utilizados para cargar los valores de los parametros de las funciones llamadas a la 
# memoria de las funciones antes de que comience su ejecucion
def carga_params(param):
	global tabla_varia
	if not isinstance(tabla_varia[-1],list):
		tabla_varia.append(param)
	else:
		carga_params_aux(param,tabla_varia[-1])

def carga_params_aux(param,lista):
	if lista:
		if not isinstance(lista[-1],list):
			lista.append(param)
		else:
			carga_params_aux(lista[-1])
#Las proximas tres funciones son utilizadas para mandar parametros por referencia al procedimiento
# las cuales solo fueron creadas para pruebas pero no estan funcionando, dado que solo se tienen la sitnaxis
# y las semantica para las llamadas con parametros pro referencia, sin embargo fueron probadas y funciona.
def asigna_valores_parametros(lista):
	global tabla_parametros
	if lista:
		if isinstance(lista[-1],list):
			asigna_valores_parametros(lista[-1])
		else:
			for variable in lista:
				for param in tabla_parametros:
					if variable.direccion == param.direccion:	
						param.valor = variable.valor

def cambia_valores_parametros(lista):
	global tabla_parametros
	if lista:
		if isinstance(lista[-1],list):
			asigna_valores_parametros(lista[-1])
		else:
			for variable in lista:
				for param in tabla_parametros:
					if tabla_parametros:
						if variable.direccion == param.pointer:
							variable.valor = param.valor
							del param
						
def intercambio_de_parametros():
	for param in tabla_parametros:
		for pointer in tabla_parametros:
			if param.direccion == pointer.pointer:
				param.valor = pointer.valor
				del pointer
#Funcion que guarda el return en una memoria externa para ser enviado a la funcion que fue llamada
#donde se le realizara la asignacion del valor del return a una variable local de la funcion o una 
#variable global del programa
def carga_return(lista):
	if lista:
		if isinstance(lista[-1],list):
			carga_return(lista[-1])
		else:
			for resultado in tabla_retrun:
				lista.append(resultado)
				del resultado
#Funcion principal que realiza las llamadas a todos las funciones necesarias pra realizar las operaciones
#que el lenguaje permite, ademas de hacer validaciones para revizar que los valores esten alojados donde
#deberian o que no tengan valores nulos que el compilador no puede operar
def maquina_virtual():
	carga_globales()
	carga_const()
	carga_scope_local("Main")
	lee_cuadruplos()
	global tabla_parametros
	global pila_brincos
	global op1
	global op2
	global contcuad
	global tabla_pro
	i  = 0
	while i < contcuad:
		if tabla_cuadruplos[i].op == "=":
			if tabla_cuadruplos[i].o1 >=11000 and tabla_cuadruplos[i].o1 <=15999:
				val= get_value_temp(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 16000 and tabla_cuadruplos[i].o1 <=20999:
				val= get_value_const(tabla_cuadruplos[i].o1)	
			elif tabla_cuadruplos[i].o1 >= 0 and tabla_cuadruplos[i].o1 <=9999:
				val= get_value_var(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 == 'RETURN':
				if tabla_retrun:
					val = tabla_retrun[-1].valor
					del tabla_retrun[-1]
				else:
					i+=1
					break

			cambia_valor(tabla_cuadruplos[i].res,val)
			i+=1

		elif tabla_cuadruplos[i].op == "+":
			dame_o1_o2(i)
			if (op1  is None or op2  is None):
				print "Sorry - None value"
				sys.exit()
			result = op1 + op2
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			#limpia tabla de retorno
			if tabla_retrun:
					val = tabla_retrun[-1].valor
					del tabla_retrun[-1]
			#-----------------------------------------------------
			i+=1

		elif tabla_cuadruplos[i].op == "-":
			dame_o1_o2(i)
			if (op1  is None or op2  is None):
				print "Sorry - None value"
				sys.exit()
			result = op1 - op2
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "*":
			dame_o1_o2(i)
			if (op1  is None or op2  is None):
				print "Sorry - None value"
				sys.exit()
			result = op1 * op2
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "/":
			dame_o1_o2(i)
			if (op1  is None or op2  is None):
				print "Sorry - None value"
				sys.exit()
			result = op1 / op2
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "==":
			dame_o1_o2(i)
			if (op1  is None or op2  is None):
				print "Sorry - None value"
				sys.exit()
			if op1 == op2:
				result = "true"
			else:
				result = "false"
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "!=":
			dame_o1_o2(i)
			if (op1  is None or op2  is None):
				print "Sorry - None value"
				sys.exit()
			if op1 != op2:
				result = "true"
			else:
				result = "false"
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "<=":
			dame_o1_o2(i)
			if (op1  is None or op2  is None):
				print "Sorry - None value"
				sys.exit()
			if op1 <= op2:
				result = "true"
			else:
				result = "false"
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == ">=":
			dame_o1_o2(i)
			if (op1  is None or op2  is None):
				print "Sorry - None value"
				sys.exit()
			if op1 >= op2:
				result = "true"
			else:
				result = "false"
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == ">":
			dame_o1_o2(i)
			if (op1  is None or op2  is None):
				print "Sorry - None value"
				sys.exit()
			if op1 > op2:
				result = "true"
			else:
				result = "false"
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "<":
			dame_o1_o2(i)
			if (op1  is None or op2  is None):
				print "Sorry - None value"
				sys.exit()
			if op1 < op2:
				result = "true"
			else:
				result = "false"
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "GOTO":
			i = tabla_cuadruplos[i].res
			
		elif tabla_cuadruplos[i].op == "GOTOFALSE":
			if get_value_temp(tabla_cuadruplos[i].o1) == "false":
				i = tabla_cuadruplos[i].res
			else:
				i+=1

		elif tabla_cuadruplos[i].op == "PRINT":
			if tabla_cuadruplos[i].o1 >=11000 and tabla_cuadruplos[i].o1 <=15999:
				op1 = get_value_temp(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 16000 and tabla_cuadruplos[i].o1 <=20999:
				op1 = get_value_const(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 0 and tabla_cuadruplos[i].o1 <=9999:
				op1 = get_value_var(tabla_cuadruplos[i].o1)

			print op1
			i+=1 

		elif tabla_cuadruplos[i].op ==  "ERA":
			genera_memoria_proc(tabla_cuadruplos[i].o1,tabla_varia)
			proc_actual = tabla_cuadruplos[i].o1
			i+=1

		elif tabla_cuadruplos[i].op ==  "PARAM":
			valor = get_value_param(tabla_cuadruplos[i].o1)
			for n,pro in enumerate(tabla_pro):
				if pro.nombre_funcion == proc_actual:
					for variable in pro.param:
						if variable.nombre_variable == tabla_cuadruplos[i].res:
							# newparam = Parametro(variable.direccion,tabla_cuadruplos[i].o1,None)
							# tabla_parametros.append(newparam)
							cambia_valor(variable.direccion,valor)
			
			#parametro = Memoria(tabla_cuadruplos[i].o1,valor)
			#carga_params(parametro)
			i+=1
			pass

		elif tabla_cuadruplos[i].op ==  "GOSUB":
			pila_brincos.append(i+1)
			for pro in tabla_pro:
				if pro.nombre_funcion == tabla_cuadruplos[i].o1:
					i = pro.dir_base
			pass

		elif tabla_cuadruplos[i].op ==  "ENDPROC":
			i = pila_brincos[-1]
			del pila_brincos[-1]
			# asigna_valores_parametros(tabla_varia)
			borra_memoria(tabla_varia)
			carga_return(tabla_varia)
			# intercambio_de_parametros()
			# cambia_valores_parametros(tabla_varia)
			pass

		elif tabla_cuadruplos[i].op ==  "END":
			# print
			# for para in tabla_parametros:
			# 	print para.direccion,para.pointer,para.valor
			sys.exit()

			pass

		elif tabla_cuadruplos[i].op ==  "VER":
			if tabla_cuadruplos[i].o1 >=11000 and tabla_cuadruplos[i].o1 <=15999:
				dim = get_value_temp(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 16000 and tabla_cuadruplos[i].o1 <=20999:
				dim = get_value_const(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 0 and tabla_cuadruplos[i].o1 <=9999:
				dim = get_value_var(tabla_cuadruplos[i].o1)

			if dim >= tabla_cuadruplos[i].o2 and dim <= tabla_cuadruplos[i].res:
				i+=1
			else:
				print "Sorry - array out of bounds"
				sys.exit()
			pass

		elif tabla_cuadruplos[i].op ==  "MULTM":
			if tabla_cuadruplos[i].o1 >=11000 and tabla_cuadruplos[i].o1 <=15999:
				val_direc = get_value_temp(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 16000 and tabla_cuadruplos[i].o1 <=20999:
				val_direc = get_value_const(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 0 and tabla_cuadruplos[i].o1 <=9999:
				val_direc = get_value_var(tabla_cuadruplos[i].o1)

			result = val_direc * tabla_cuadruplos[i].o2
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1
			pass

		elif tabla_cuadruplos[i].op ==  "SUMM":
			if tabla_cuadruplos[i].o1 >=11000 and tabla_cuadruplos[i].o1 <=15999:
				val_direc = get_value_temp(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 16000 and tabla_cuadruplos[i].o1 <=20999:
				val_direc = get_value_const(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 0 and tabla_cuadruplos[i].o1 <=9999:
				val_direc = get_value_var(tabla_cuadruplos[i].o1)

			result = val_direc + tabla_cuadruplos[i].o2
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1
			pass

		elif tabla_cuadruplos[i].op ==  "SUMB":
			if tabla_cuadruplos[i].o2 >=11000 and tabla_cuadruplos[i].o2 <=15999:
				val_direc = get_value_temp(tabla_cuadruplos[i].o2)
			elif tabla_cuadruplos[i].o2 >= 16000 and tabla_cuadruplos[i].o2 <=20999:
				val_direc = get_value_const(tabla_cuadruplos[i].o2)
			elif tabla_cuadruplos[i].o2 >= 0 and tabla_cuadruplos[i].o2 <=9999:
				val_direc = get_value_var(tabla_cuadruplos[i].o2)

			result = tabla_cuadruplos[i].o1 + val_direc
			if get_value_temp(tabla_cuadruplos[i].res):
				set_value_tmp(tabla_cuadruplos[i].res,result)
			else:
				newtempo = Memoria(tabla_cuadruplos[i].res,result)
				tabla_tempo.append(newtempo)
			i+=1
			pass

		elif tabla_cuadruplos[i].op ==  "RETURN":
			if tabla_cuadruplos[i].o1 >=11000 and tabla_cuadruplos[i].o1 <=15999:
				valor = get_value_temp(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 16000 and tabla_cuadruplos[i].o1 <=20999:
				valor = get_value_const(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 0 and tabla_cuadruplos[i].o1 <=9999:
				valor = get_value_var(tabla_cuadruplos[i].o1)

			regreso = Returnes(tabla_cuadruplos[i].o1,valor)
			tabla_retrun.append(regreso)
			# for dato in tabla_retrun:
			# 	print dato.direccion,dato.valor
			i+=1
# impresion de la memoira (solo para testing)
def print_memoria():
	global tabla_tempo
	global tabla_const
	global tabla_varia
	global tabla_varia_globales
	global contcuad

	print "memoria temporal"
	for campo in tabla_tempo:
		print campo.direccion, campo.valor
	
	print "memoria global"
	for campo in tabla_varia_globales:
		print campo.direccion, campo.valor

	print "memoria local"
	for campo in tabla_varia:
		if not isinstance(campo, list):
			print campo.direccion, campo.valor
		else:
			print '*******************'
			for campo in tabla_varia[-1]:
				print campo.direccion, campo.valor
			print '*******************'




