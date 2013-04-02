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
		nombre_variable = nombre
		tipo_dato = tipo
		direccion = dire

class TablaProcedimientoNodo:
	def __init__(self, nombre, tipo, dirb, var):
		nombre_funcion = nombre
		tipo_retorno = tipo
		dir_base = dirb
		var = var

tabla_var = [ ]
tabla_pro = [ ]

def insert_procedimiento(nombre, tipo, dirb):
	pro = TablaProcedimientoNodo(nombre, tipo, dirb)
	tabla_pro.append(pro)

def print_tables(currentProList):
	print "Tabla de procedimientos y variables"
	for currentPro in currentProList:
		var = currentPro.var

		if currentPro:
			print "List is empty"
		else:
			print currentPro.nombre_funcion + " - " + currentPro.tipo_retorno + " - " + currentPro.dir_base + " - " + currentPro.var.first
			for variable in currentPro.var : 
				print currentPro.var.first.nombre_variable + " - " + currentPro.var.first.tipo_dato + " - " + currentPro.var.first.direccion
			print "\n"

def insert_variable(nombre, tipo, dire):
	var = TablaVariableNodo(nombre, tipo, dire)
	tabla_var.append(var)

def existe_pro(tabla_pro, nombre):
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