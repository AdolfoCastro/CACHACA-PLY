from tvariables import *
from tconstantes import *

class Memoria:
	def __init__(self, dire, val):
		self.direccion = dire
		self.valor = val

tabla_tempo=[]
tabla_const=[]
tabla_varia=[]
tabla_varia_globales=[]
contcuad=0
global op1
global op2

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

def get_value_temp(dirb):
	global tabla_tempo
	for temp in tabla_tempo:
		if temp.direccion == dirb:
			return temp.valor
	pass

def get_value_const(dirb):
	global tabla_const
	for constante in tabla_const:
		if constante.direccion == dirb:
			return constante.valor
	pass

def get_value_var(dirb):
	global tabla_varia
	for variable in tabla_varia:
		if variable.direccion == dirb:
			return variable.valor
	pass

def lee_cuadruplos():
	global contcuad
	currentCuadList = tabla_cuadruplos
	for currentCuad in currentCuadList:
		contcuad += 1

def cambia_valor(dire,val):
	global tabla_varia
	global tabla_varia_globales
	esta = False
	for variable in tabla_varia:
		if variable.direccion == dire:
			variable.valor  = val
			esta = True
	if esta:
		for variable in tabla_varia_globales:
			if variable.direccion == dire:
				variable.valor  = val
				esta = True

	if not esta:
		print "Sorry - the variable  %s was not declared"%nombre
 		sys.exit()

	pass

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
	
def maquina_virtual():
	carga_globales()
	carga_const()
	carga_scope_local("Main")
	lee_cuadruplos()
	global op1
	global op2

	global contcuad
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
			result = op1 + op2
			newtempo = Memoria(tabla_cuadruplos[i].res,result)
			tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "-":
			dame_o1_o2(i)
			result = op1 - op2
			newtempo = Memoria(tabla_cuadruplos[i].res,result)
			tabla_tempo.append(newtempo)
			i+=1


		elif tabla_cuadruplos[i].op == "*":
			dame_o1_o2(i)
			result = op1 * op2
			newtempo = Memoria(tabla_cuadruplos[i].res,result)
			tabla_tempo.append(newtempo)
			i+=1


		elif tabla_cuadruplos[i].op == "/":
			dame_o1_o2(i)
			result = op1 / op2
			newtempo = Memoria(tabla_cuadruplos[i].res,result)
			tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "==":
			dame_o1_o2(i)
			if op1 == op2:
				result = "true"
			else:
				result = "false"
			newtempo = Memoria(tabla_cuadruplos[i].res,result)
			tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "<=":
			dame_o1_o2(i)
			if op1 <= op2:
				result = "true"
			else:
				result = "false"
			newtempo = Memoria(tabla_cuadruplos[i].res,result)
			tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == ">=":
			dame_o1_o2(i)
			if op1 >= op2:
				result = "true"
			else:
				result = "false"
			newtempo = Memoria(tabla_cuadruplos[i].res,result)
			tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == ">":
			dame_o1_o2(i)
			if op1 > op2:
				result = "true"
			else:
				result = "false"
			newtempo = Memoria(tabla_cuadruplos[i].res,result)
			tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "<":
			dame_o1_o2(i)
			if op1 < op2:
				result = "true"
			else:
				result = "false"
			newtempo = Memoria(tabla_cuadruplos[i].res,result)
			tabla_tempo.append(newtempo)
			i+=1

		elif tabla_cuadruplos[i].op == "!=":
			dame_o1_o2(i)
			if op1 != op2:
				result = "true"
			else:
				result = "false"
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

def print_memoria():
	global tabla_tempo
	global tabla_const
	global tabla_varia
	global tabla_varia_globales
	global contcuad

	print "memoria temporal"
	for campo in tabla_tempo:
		print campo.direccion, campo.valor
	print "memoria local"
	for campo in tabla_varia:
		print campo.direccion, campo.valor
	print "memoria global"
	for campo in tabla_varia_globales:
		print campo.direccion, campo.valor
