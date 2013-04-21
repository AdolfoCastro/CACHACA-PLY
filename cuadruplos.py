#----------------------------------------------
# cuadruplos.py
# Cuadruplos
# Gerardo Chapa Quiroga 800249
# Tomas Castro Lopez 1033534
# Adolfo Castro Rojas 225591
# CREADO: 18/03/2013
# EDITADO: 19/03/2013
#----------------------------------------------
from clases import Stack
from cubo_semantico import cubo_semantico
import os, sys
from memory import *

cont_saltos = 0

class Cuadruplo:

  def __init__(self, operacion, operando1, operando2, mem):
		self.op = operacion
		self.o1 = operando1
		self.o2 = operando2
		self.res = mem


def insert_cuadruplo(cuad):
	global tabla_cuadruplos
	global cont_saltos
	global exp_for
	global tabla_aux
	if exp_for:
		tabla_aux.append(cuad)
	else:
		tabla_cuadruplos.append(cuad)
		cont_saltos += 1
	#print cont_saltos

# Pilas para las acciones de la validacion semantica
pila_o = Stack()
p_tipos = Stack()
p_oper = Stack()
p_saltos = Stack()
tabla_cuadruplos = []
tabla_aux = []
exp_for = False
rescase  = None
resswitch  = None

p_oper.push(None)

# Acciones de Generacion de codigo para Expresiones usando 
# cuadruplos incluyendo algunas acciones para verificacion semantica
def exp_1(var, tipo):
	global p_tipos
	global pila_o
	pila_o.push(var)
	p_tipos.push(tipo)

def exp_2(oper):
	global p_oper
	if oper:
		p_oper.push(oper)

def exp_3(oper):
	global p_oper
	if oper:
		p_oper.push(oper)

def exp_4():
	global contEntTmp
	global contFlotTmp
	global contDoubleTmp
	global contStrTmp
	global contBoolTmp
	global p_oper
	global p_tipos
	global pila_o
	if p_oper.head() == "+" or p_oper.head() == "-":
		tipo_res = cubo_semantico[p_tipos.head()][p_tipos.neck()][p_oper.head()]
		if tipo_res != "Error":
			if tipo_res == "Integer":
				memoria  = contEntTmp
				contEntTmp+=1
			elif tipo_res == "Float":
				memoria = contFlotTmp
				contFlotTmp+=1
			elif tipo_res == "Double":
				memoria = contDoubleTmp
				contDoubleTmp+=1
			elif tipo_res == "String":
				memoria = contStrTmp
				contStrTmp+=1

			p_tipos.pop()
			p_tipos.pop()

			cuadruplo = Cuadruplo(p_oper.pop(), pila_o.pop(), pila_o.pop(), memoria)
			insert_cuadruplo(cuadruplo)

			#Libera la memoria
			#if cuadruplo.o1 >= 11000 or cuadruplo.o1 <= 15999:
			#	pila_o.pop()
			#if  cuadruplo.o2 >= 11000 or cuadruplo.o2 <= 15999:
			#	pila_o.pop()

			pila_o.push(cuadruplo.res)
			p_tipos.push(tipo_res)
		else:
			print "Error semantico tipos incompatibles"

def exp_5():
	global contEntTmp
	global contFlotTmp
	global contDoubleTmp
	global contStrTmp
	global contBoolTmp
	global p_oper
	global p_tipos
	global pila_o
	if p_oper.head() == "*" or p_oper.head() == "/":
		tipo_res = cubo_semantico[p_tipos.head()][p_tipos.neck()][p_oper.head()]
		if tipo_res != "Error":
			if tipo_res == "Integer":
				memoria  = contEntTmp
				contEntTmp+=1
			elif tipo_res == "Float":
				memoria = contFlotTmp
				contFlotTmp+=1
			elif tipo_res == "Double":
				memoria = contDoubleTmp
				contDoubleTmp+=1
			elif tipo_res == "String":
				memoria = contStrTmp
				contStrTmp+=1

			p_tipos.pop()
			p_tipos.pop()

			cuadruplo = Cuadruplo(p_oper.pop(), pila_o.pop(), pila_o.pop(), memoria)
			insert_cuadruplo(cuadruplo)

			#Libera la memoria
			#if cuadruplo.o1 >= 11000 or cuadruplo.o1 <= 15999:
			#	pila_o.pop()
			#if  cuadruplo.o2 >= 11000 or cuadruplo.o2 <= 15999:
			#	pila_o.pop()

			pila_o.push(cuadruplo.res)
			p_tipos.push(tipo_res)
		else:
			print "Sorry - incomaptible types"

def exp_6():
	global p_oper
	p_oper.push("{")

def exp_7():
	global p_oper
	#if p_oper.head() == "{":
	p_oper.pop()

def exp_8(oper):
	p_oper.push(oper)

def exp_9():
	global contEntTmp
	global contFlotTmp
	global contDoubleTmp
	global contStrTmp
	global contBoolTmp
	global p_oper
	global p_tipos
	global pila_o
	if p_oper.head() == ">" or p_oper.head() == ">=" or	p_oper.head() == "<" or p_oper.head() == "<=" or p_oper.head() == "==" or p_oper.head() == "!=" or p_oper.head() == "=":
		tipo_res = cubo_semantico[p_tipos.head()][p_tipos.neck()][p_oper.head()]
		if tipo_res != "Error":
			if tipo_res == "Integer":
				memoria  = contEntTmp
				contEntTmp+=1
			elif tipo_res == "Float":
				memoria = contFlotTmp
				contFlotTmp+=1
			elif tipo_res == "Double":
				memoria = contDoubleTmp
				contDoubleTmp+=1
			elif tipo_res == "String":
				memoria = contStrTmp
				contStrTmp+=1
			elif tipo_res == "Boolean":
				memoria = contBoolTmp
				contBoolTmp+=1

			p_tipos.pop()
			p_tipos.pop()

			if p_oper.head() == "=":
				res = pila_o.pop()
				op = pila_o.pop()
				cuadruplo = Cuadruplo(p_oper.pop(), op, None, res)
			else:
				cuadruplo = Cuadruplo(p_oper.pop(), pila_o.pop(), pila_o.pop(), memoria)
				pila_o.push(cuadruplo.res)
				p_tipos.push(tipo_res)

			insert_cuadruplo(cuadruplo)

			#Libera la memoria
			#if cuadruplo.o1 >= 11000 or cuadruplo.o1 <= 15999:
			#	pila_o.pop()
			#if  cuadruplo.o2 >= 11000 or cuadruplo.o2 <= 15999:
			#	pila_o.pop()

		else:
			print "Sorry - incomaptible types"
			sys.exit()

# Acciones de Generacion de codigo para estatutos condicionales if 
def est_if_1():
	aux = p_tipos.pop()
	if aux != "Boolean":
		print "Sorry - if statement must return a Boolean value"
	else:
		res = pila_o.pop()
		cuadruplo = Cuadruplo("GOTOFALSE", res, "", "")
		insert_cuadruplo(cuadruplo)
		p_saltos.push(cont_saltos-1)

def est_if_2():
	fin = p_saltos.pop()
	tabla_cuadruplos[fin].res = cont_saltos

def est_if_else_1():
	aux = p_tipos.pop()
	if aux != "Boolean":
		print "Sorry - if statement must return a Boolean value"
	else:
		res = pila_o.pop()
		cuadruplo = Cuadruplo("GOTOFALSE", res, "", "")
		insert_cuadruplo(cuadruplo)
		p_saltos.push(cont_saltos)

def est_if_else_2():
	cuadruplo = Cuadruplo("GOTO", "", "", "")
	insert_cuadruplo(cuadruplo)
	falso = p_saltos.pop()
	tabla_cuadruplos[falso].res = cont_saltos
	p_saltos.push(cont_saltos-1)

def est_if_else_3():
	falso = p_saltos.pop()
	tabla_cuadruplos[falso].res = cont_saltos

# Acciones de Generacion de codigo para estatutos condicionales while
def est_while_1():
	global cont_saltos
	p_saltos.push(cont_saltos)

def est_while_2():
	aux = p_tipos.pop()
	if aux != "Boolean":
		print "Sorry - While expressions must return Boolean values"
		sys.exit()
	else:
		res = pila_o.pop()
		cuadruplo = Cuadruplo("GOTOFALSE", res, "", "")
		insert_cuadruplo(cuadruplo)
		p_saltos.push(cont_saltos-1)

def est_while_3():
	falso = p_saltos.pop()
	retorno = p_saltos.pop()
	cuadruplo = Cuadruplo("GOTO", "", "", retorno)
	insert_cuadruplo(cuadruplo)
	tabla_cuadruplos[falso].res = cont_saltos

def est_print():
	res = pila_o.pop()
	cuadruplo = Cuadruplo("PRINT", res, "", "")
	insert_cuadruplo(cuadruplo)


# Acciones de Generacion de codigo para estatutos condicionales for
def exp_for_(boool):
	global exp_for
	exp_for=boool
	print "Entra a exp_for = %r" %exp_for

def est_for_1():
	p_saltos.push(cont_saltos)

def est_for_2():
	res = tabla_cuadruplos[-1].res
	cuadruplo = Cuadruplo("GOTOFALSE", res, "", "")
	insert_cuadruplo(cuadruplo)
	p_saltos.push(cont_saltos)
	pass

def est_for_3():
	global tabla_aux
	global tabla_cuadruplos
	for cuad in tabla_aux:
		insert_cuadruplo(cuad)
	falso = p_saltos.pop()
	asign = p_saltos.pop()
	tabla_cuadruplos[falso-1].res = cont_saltos
	cuadruplo = Cuadruplo("GOTO", "", "", asign)
	insert_cuadruplo(cuadruplo)
	pass

# def est_for_4():
# 	# id_ = pila_o.pop()
# 	# id_ = pila_o.head()
# 	# retorno = p_saltos.pop()
# 	# cuadruplo2 = Cuadruplo("GOTO", "", "",retorno)
# 	# cuadruplo3.res = retorno + 1
# 	pass


# Acciones de Generacion de codigo para estatutos condicionales switch
def est_case_1(res):
	global resswitch
	resswitch = res
	print resswitch
	pass

def est_case_2(res):
	global rescase
	global resswitch
	global contBoolTmp
	rescase  = res
	cuadruplo = Cuadruplo('==',resswitch,rescase,contBoolTmp)
	insert_cuadruplo(cuadruplo)
	p_tipos.push('Boolean')
	pila_o.push(contBoolTmp)
	contBoolTmp+=1
	print rescase
	pass

def est_case_3():
	aux = p_tipos.pop()
	if aux != "Boolean":
		print "Sorry - if statement must return a Boolean value"
	else:
		res = pila_o.pop()
		cuadruplo = Cuadruplo("GOTOFALSE", res, "", "")
		insert_cuadruplo(cuadruplo)
		p_saltos.push(cont_saltos-1)

def est_case_4():
	falso = p_saltos.pop()
	tabla_cuadruplos[falso].res = cont_saltos
	pass

def print_pilas():
	print "Pilas"
	global pila_o
	global p_tipos
	global p_oper
	global p_saltos

	print "\n"
	print "--Opernando--"
	pila_o.show()
	#print 'cabeza pila o', pila_o.head()
	print "\n"
	print "--Tipos--"
	p_tipos.show()
	print "\n"
	print "--Operador--" 
	p_oper.show()
	print "\n"
	print "--Saltos--"
	p_saltos.show()

def print_cuadruplos(currentCuadList):
	print "Tabla Cuadruplos"
	for currentCuad in currentCuadList:
		if currentCuad:
			print currentCuad.op, " , ", currentCuad.o1, " , ", currentCuad.o2," , ",currentCuad.res
		else:
			print "List is empty"
	pass

