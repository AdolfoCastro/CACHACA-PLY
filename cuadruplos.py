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

class Cuadruplo:

  def __init__(self, operacion, operando1, operando2, mem):
		self.op = operacion
		self.o1 = operando1
		self.o2 = operando2
		self.res = mem

# Pilas para las acciones de la validacion semantica
pila_o = Stack()
p_tipos = Stack()
p_oper = Stack()
p_saltos = Stack()

# Acciones de Generacion de codigo para Expresiones usando 
# cuadruplos incluyendo algunas acciones para verificacion semantica
def exp_1(var, tipo):
	pila_o.push(var)
	p_tipos.push(tipo)

def exp_2(oper):
	if oper:
		p_oper.push(oper)

def exp_3(oper):
	if oper:
		p_oper.push(oper)

def exp_4(memoria):
	if p_oper.head() == "+" or p_oper.head() == "-":
		tipo_res = cubo_semantico[p_tipos.head()][p_tipos.neck()][p_oper.head()]
		if tipo_res != "Error":
			p_tipos.pop()
			p_tipos.pop()
			cuadruplo = Cuadruplo(p_oper.pop(), pila_o.pop(), pila_o.pop(), memoria.siguiente())
			#Libera la memoria
			if cuadruplo.o1.contains("MEM"):
				memoria.liberar(cuadruplo.o1)
			if  cuadruplo.o2.contains("MEM"):
				memoria.liberar(cuadruplo.o2)

			pila_o.push(cuadruplo.res)
			p_tipos.push(tipo_res)
		else:
			print "Error semantico tipos incompatibles"

def exp_5():
	if p_oper.head() == "*" or p_oper.head() == "/":
		tipo_res = cubo_semantico[p_tipos.head()][p_tipos.neck()][p_oper.head()]
		if tipo_res != "Error":
			p_tipos.pop()
			p_tipos.pop()
			cuadruplo = Cuadruplo(p_oper.pop(), pila_o.pop(), pila_o.pop(), memoria.siguiente())
			#Libera la memoria
			if cuadruplo.o1.contains("MEM"):
				memoria.liberar(cuadruplo.o1)
			if  cuadruplo.o2.contains("MEM"):
				memoria.liberar(cuadruplo.o2)

			pila_o.push(cuadruplo.res)
			p_tipos.push(tipo_res)
		else:
			print "Error semantico tipos incompatibles"

def exp_6():
	p_oper.push("{")

def exp_7():
	if p_oper.head() == "{":
		p_oper.pop()

def exp_8(oper):
	p_oper.push(oper)

def exp_9():
	if p_oper.head() == "&&" or p_oper.head() == "||":
		tipo_res = cubo_semantico[p_tipos.head()][p_tipos.neck()][p_oper.head()]
		if tipo_res != "Error":
			p_tipos.pop()
			p_tipos.pop()
			cuadruplo = Cuadruplo(p_oper.pop(), pila_o.pop(), pila_o.pop(), memoria.siguiente())
			#Libera la memoria
			if cuadruplo.o1.contains("MEM"):
				memoria.liberar(cuadruplo.o1)
			if  cuadruplo.o2.contains("MEM"):
				memoria.liberar(cuadruplo.o2)

			pila_o.push(cuadruplo.res)
			p_tipos.push(tipo_res)
		else:
			print "Error semantico tipos incompatibles"

# Acciones de Generacion de codigo para estatutos condicionales if 
def est_if_1():
	aux = p_tipos.pop()
	if aux != "Boolean":
		print "Error Semantico"
	else:
		pila_o.pop()
		cuadruplo = Cuadruplo("GOTOFALSO", res, "", "")
		p_saltos.push(cont-1)

def est_if_2(cuadruplo):
	p_saltos.pop()
	cuadruplo.res = memoria.siguiente()

def est_if_else_1():
	aux = p_tipos.pop()
	if aux != "Boolean":
		print "Error semantico"
	else:
		pila_o.pop()
		cuadruplo = Cuadruplo("GOTOFALSO", res, "", "")
		p_saltos.push(cont)

def est_if_else_2():
	cuadruplo = Cuadruplo("GOTO", "", "", "")
	p_saltos.pop()
	cuadruplo.res = memoria.siguiente()
	p_saltos.push(cont-1)

def est_if_else_3():
	p_saltos.pop()
	cuadruplo.res = cont

# Acciones de Generacion de codigo para estatutos condicionales while
def est_while_1():
	p_saltos.push(cont)
	cuadruplo.res = memoria.siguiente()

def est_while_2():
	p_tipos.pop(aux)
	if aux != "Boolean":
		print "Error Semantico"
	else:
		pila_o.pop()
		cuadruplo = Cuadruplo("GOTOFALSO", res, "", "")
		p_saltos.pop(cont-1)

def est_while_3():
	p_saltos().pop(falso)
	p_saltos().pop(retorno)
	cuadruplo = Cuadruplo("GOTO", retorno, "", "")
	cuadruplo.res = cont

# Acciones de Generacion de codigo para estatutos condicionales switch
def est_case_1(exp):
	if exp == "Integer" or exp == "Float" or exp == "Boolean" or exp == "Double":
		p_saltos.push("(")

def est_case_2():
	#Verificar que la expresion ordinal
	cte = pila_o.pop()
	exp = pila_o.pop()
	cuadruplo1 = Cuadruplo("=", exp, cte, tk)
	cuadruplo2 = Cuadruplo("GOTOVERDADERO", tk, "", "")
	pila_o.pop(tk)
	pila_o.push(exp)
	p_saltos(cont-1)

def est_case_3():
	#Verificar que la expresion ordinal...
	cte = pila_o.pop()
	exp = pila_o.pop()
	cuadruplo = Cuadruplo("=", exp, cte, tk)

def est_case_4():
	pass
def est_case_5():
	pass
def est_case_6():
	pass
def est_case_7():
	pass

# Acciones de Generacion de codigo para estatutos condicionales for
def est_for_1(dir):
	pila_o.push(dir)

def est_for_2():
	exp1 = pila_o.pop()
	id_ = pila_o.head()
	cuadruplo = Cuadruplo("=", exp1, "", id_)

def est_for_3():
	tmpf = Temporal()
	exp2 = pila_o.pop()
	tmpx = Temporal()
	cuadruplo1 = Cuadruplo("=", exp2, "", tmpf)
	cuadruplo2 = Cuadruplo("<=", id_, tmpf, tmpx)
	cuadruplo3 = Cuadruplo("GOTOFALSO", tmpx, "")
	tmpf.free()
	p_saltos.push(cont-2)

def est_for_4():
	id_ = pila_o.pop()
	cuadruplo1 = Cuadruplo("+", id_, 1, id_)
	retorno = p_saltos.pop()
	cuadruplo2 = Cuadruplo("GOTO", "", "",retorno)
	cuadruplo3.res = retorno + 1
	tmpf.free()

def print_cuadruplos():
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
