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

class TablaVariableNodo:
	def __init__(self, nombre, tipo, dire):
		self.nombre_variable = nombre
		self.tipo_dato = tipo
		self.direccion = dire

class TablaProcedimientoNodo:
	def __init__(self, nombre, tipo, dirb):
		self.nombre_funcion = nombre
		self.tipo_retorno = tipo
		self.dir_base = dirb
		self.var = []
		self.se_uso = False

tabla_pro = [ ]

def insert_procedimiento(nombre, tipo, dirb):
	global tabla_pro
	pro = TablaProcedimientoNodo(nombre, tipo, dirb)
	tabla_pro.append(pro)

def print_tables(currentProList):
	print "Tabla de procedimientos y variables"
	for currentPro in currentProList:
		if currentPro:
			print currentPro.nombre_funcion, " - ", currentPro.tipo_retorno, " - ", currentPro.dir_base
			for variable in currentPro.var:
				print variable.nombre_variable, " - ", variable.tipo_dato, " - ", variable.direccion
			print "\n"
		else:
			print "List is empty"
			

def insert_variable(nombre, tipo, dire, proc):
	global tabla_pro
	variable = TablaVariableNodo(nombre, tipo, dire)
	for n,pro in enumerate(tabla_pro):
		if pro.nombre_funcion == proc:
			tabla_pro[n].var.append(variable)

def existe_pro(nombre):
	global tabla_pro
	for pro in tabla_pro:
		if pro.nombre_funcion == nombre:
			sys.exit()

def existe_var(tabla_var, nombre):
	for var in tabla_var:
		if var.nombre_variable == nombre:
			sys.exit()

def existe_var_asignar(tabla_var, nombre):
	if not existe_var(tabla_var, nombre):
		print "La variable " + nombre + " a la que quieres asignar un valor no existe"
		sys.exit()
