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


def carga_globales():
	global tabla_pro
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == "Global":
			for variable in pro.var:
				mem = Memoria(variable.direccion,variable.valor)
				tabla_varia_globales.append(mem)
	pass

def carga_const():
	for cons in tabla_cons:
			mem = Memoria(cons.dirb,cons.cons)
			tabla_const.append(mem)

def carga_scope_local(proc):
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			for variable in pro.var:
				mem = Memoria(variable.direccion,variable.valor)
				tabla_varia.append(mem)
	pass

def lee_cuadruplos():
	global contcuad
	currentCuadList = tabla_cuadruplos
	for currentCuad in currentCuadList:
		contcuad += 1

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

def get_value_temp(dirb):
	global tabla_tempo
	for temp in tabla_tempo:
		if temp.direccion == dirb:
			return temp.valor
	return False
	pass

def set_value_tmp(dirb,newvalue):
	global tabla_tempo
	for temp in tabla_tempo:
		if temp.direccion == dirb:
			temp.valor = newvalue
			break

def get_value_const(dirb):
	global tabla_const
	for constante in tabla_const:
		if constante.direccion == dirb:
			return constante.valor
	pass

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

def borra_memoria(proc):
	if isinstance(proc[-1],list):
		if proc[-1]:
			if isinstance(proc[-1][-1],list):
				borra_memoria(proc[-1])
			else:
				del proc[-1]	

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

def carga_return(lista):
	if lista:
		if isinstance(lista[-1],list):
			carga_return(lista[-1])
		else:
			for resultado in tabla_retrun:
				lista.append(resultado)
				del resultado

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

		elif tabla_cuadruplos[i].op ==  "RETURN":
			print 
			if tabla_cuadruplos[i].o1 >=11000 and tabla_cuadruplos[i].o1 <=15999:
				valor = get_value_temp(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 16000 and tabla_cuadruplos[i].o1 <=20999:
				valor = get_value_const(tabla_cuadruplos[i].o1)
			elif tabla_cuadruplos[i].o1 >= 0 and tabla_cuadruplos[i].o1 <=9999:
				valor = get_value_var(tabla_cuadruplos[i].o1)

			regreso = Returnes(tabla_cuadruplos[i].o1,valor)
			tabla_retrun.append(regreso)
			for dato in tabla_retrun:
				print dato.direccion,dato.valor
			i+=1

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




