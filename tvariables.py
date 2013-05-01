#----------------------------------------------
# tvariables.py
# Tablas de Variables y de Procedimientos
# Gerardo Chapa Quiroga 800249
# Tomas Castro Lopez 1033534
# Adolfo Castro Rojas 225591
# CREADO: 13/03/2013
# EDITADO: 14/03/2013
#----------------------------------------------

import sys
from cuadruplos import * 

class TablaVariableNodo:
	def __init__(self, nombre, tipo, dire):
		self.nombre_variable = nombre
		self.tipo_dato = tipo
		self.direccion = dire
		self.valor = None
		self.dim = []

	# def __init__(self, nombre, tipo, dire):
	# 	self.nombre_variable = nombre
	# 	self.tipo_dato = tipo
	# 	self.direccion = dire
	# 	self.dim = []

class Dimension:
	def __init__(self, ls, m):
		self.ls = ls
		self.m = m
		
class TablaProcedimientoNodo:
	def __init__(self, nombre, tipo, dirb):
		self.nombre_funcion = nombre
		self.tipo_retorno = tipo
		self.dir_base = dirb
		self.var = []
		self.param = []
		self.se_uso = False

tabla_pro = [ ]

def def_proc_1(nombre, tipo, dirb):
	global tabla_pro
	if existe_pro(nombre):
		print "Sorry - the prototype %s already exist" %nombre
		sys.exit()
	pro = TablaProcedimientoNodo(nombre, tipo, dirb)
	tabla_pro.append(pro)

def def_proc_2(nombre, tipo, dire, proc):
	global tabla_pro
	existe_param(nombre,proc)
	param = TablaVariableNodo(nombre, tipo, dire)
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			tabla_pro[n].param.append(param)

def def_proc_3(n, cont_saltos):
	global tabla_pro
	tabla_pro[n].dir_base = cont_saltos
	pass

def def_proc_4():
	global tabla_pro
	cuadruplo = Cuadruplo("ENDPROC", "", "", "")
	insert_cuadruplo(cuadruplo)
	pass


def print_tables(currentProList):
	print "Tabla de procedimientos y variables"
	for currentPro in currentProList:
		if currentPro:
			print currentPro.nombre_funcion, " - ", currentPro.tipo_retorno, " - ", currentPro.dir_base
			print "Vars"
			for variable in currentPro.var:
				print variable.nombre_variable, " - ", variable.tipo_dato, " - ", variable.direccion
			print "Params"
			for param in currentPro.param:
				print param.nombre_variable, " - ", param.tipo_dato, " - ", param.direccion
			print "\n"
		else:
			print "List is empty"
			

def insert_variable(nombre, tipo, dire, proc):
	global tabla_pro

	if existe_var(nombre,proc):
		print "Sorry - the variable %s already exist"%nombre
		sys.exit()
	else:
		for n,pro in enumerate(tabla_pro):
			if pro.nombre_funcion == proc:
				variable = TablaVariableNodo(nombre, tipo, dire)
				tabla_pro[n].var.append(variable)
				break

def insert_dim_arr(nom, proc, ls):
	global tabla_pro
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			for m,var in enumerate(tabla_pro[n].var):
				if var.nombre_variable == nom:
					dim = Dimension(ls, "m")
					tabla_pro[n].var[m].dim.append(dim)
					break

def genera_m_arr(nom, proc):
	global tabla_pro
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			for m,var in enumerate(tabla_pro[n].var):
				if var.nombre_variable == nom:
					lss = [d.ls for d in tabla_pro[n].var[m].dim]
					mx = reduce(lambda x, y: (x+1)*(y+1), lss)
					m_aux = 1
					for dim in tabla_pro[n].var[m].dim:
						if not dim == tabla_pro[n].var[m].dim[-1]:
							d_n=dim.ls+1
							dim.m = ((mx/m_aux)/d_n)
							m_aux *= d_n
						else:
							dim.m = 0
					break

def verifica_tope(proc, nom, pos, dimn):
	global tabla_pro
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			for m,var in enumerate(tabla_pro[n].var):
				if var.nombre_variable == nom:
					if var.dim:
						if not (0 <= pos <= var.dim[dimn].ls):
							print "Sorry, array %s out of bounds" %nom
							sys.exit()


def existe_pro(nombre):
	global tabla_pro
	for pro in tabla_pro:
		if pro.nombre_funcion == nombre:
			return True
	return False

def existe_var(nombre,proc):
	global tabla_pro
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			for variable in pro.var:
				if variable.nombre_variable == nombre:
					return True
	return False

def existe_param(nombre,proc):
	global tabla_pro
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			for param in pro.param:
				if param.nombre_variable == nombre:
					print "Sorry - the parameter %s already exist"%nombre
					sys.exit()
	pass

def busca_tipo(nombre,proc):
	global tabla_pro
	esta = False
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			for variable in pro.var:
				if variable.nombre_variable == nombre:
					tipo_var  = variable.tipo_dato
					esta = True
					return tipo_var
 	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == "Global":
			for variable in pro.var:
				if variable.nombre_variable == nombre:
					tipo_var  = variable.tipo_dato
					esta = True
					return tipo_var
	if not esta:
		print "Sorry - the variable  %s was not declared"%nombre
 		sys.exit()

	pass

def get_address(nombre,proc):
	global tabla_pro
	esta = False
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			for variable in pro.var:
				if variable.nombre_variable == nombre:
					address_var  = variable.direccion
					esta = True
					return address_var
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == "Global":
			for variable in pro.var:
				if variable.nombre_variable == nombre:
					address_var  = variable.direccion
					esta = True
					return address_var
	if not esta:
		print "Sorry - the variable  %s was not declared"%nombre
 		sys.exit()
	pass

#cambia el valor de la variable
def cambia_valor(dire,val):
	global tabla_pro
	esta = False
	for n,pro in enumerate(tabla_pro):
			for variable in pro.var:
				if variable.direccion == dire:
					variable.valor  = val
					esta = True

	for n,pro in enumerate(tabla_pro):
			for variable in pro.var:
				if variable.direccion == dire:
					variable.valor  = val
					esta = True
	if not esta:
		print "Sorry - the variable  %s was not declared"%nombre
 		sys.exit()

	pass


def existe_var_asignar(tabla_var, nombre):
	if not existe_var(tabla_var, nombre):
		print "Sorry - Var " + nombre + " does not exist."
		sys.exit()


def get_value_var(dirb):
	global tabla_pro
	esta = False
	for n,pro in enumerate(tabla_pro):
			for variable in pro.var:
				if variable.direccion == dirb:
					esta = True
					return variable.valor
	pass


#tabla para ver que los valores si esten cambiando con forme se leen los cuadruplos
def print_tables_alfinal(currentProList):
	print "Tabla de procedimientos y variables"
	for currentPro in currentProList:
		if currentPro:
			print currentPro.nombre_funcion, " - ", currentPro.tipo_retorno, " - ", currentPro.dir_base
			print "Vars"
			for variable in currentPro.var:
				print variable.nombre_variable, " - ", variable.tipo_dato, " - ", variable.direccion
				for dim in variable.dim:
					print dim.ls, "-", dim.m
			print "Params"
			for param in currentPro.param:
				print param.nombre_variable, " - ", param.tipo_dato, " - ", param.direccion
			print "\n"
		else:
			print "List is empty"
