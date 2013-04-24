from tvariables import *
from tconstantes import *

class Tempo:
	def __init__(self, dire, val):
		self.direccion = dire
		self.valor = val

tabla_tempo=[]

def get_value_temp(dirb):
	global tabla_tempo
	for temp in tabla_tempo:
		if temp.direccion == dirb:
			return temp.valor

def lee_cuadruplos(currentCuadList):
	for currentCuad in currentCuadList:
		if currentCuad:
			if currentCuad.op == "=":
				if currentCuad.o1 >=11000 and currentCuad.o1 <=15999:
					val=get_value_temp(currentCuad.o1)
				elif currentCuad.o1 >= 16000 and currentCuad.o1 <=20999:
					val=get_value_cons(currentCuad.o1)	
				elif currentCuad.o1 >= 0 and currentCuad.o1 <=9999:
					val=get_value_var(currentCuad.o1,"Main")

				cambia_valor(currentCuad.res,"Main",val)

			elif currentCuad.op == "+":
				if currentCuad.o1 >=11000 and currentCuad.o1 <=15999:
					op1 = get_value_temp(currentCuad.o1)
				elif currentCuad.o1 >= 16000 and currentCuad.o1 <=20999:
					op1 = get_value_cons(currentCuad.o1)
				elif currentCuad.o1 >= 0 and currentCuad.o1 <=9999:
					op1 = get_value_var(currentCuad.o1,"Main")

				if currentCuad.o2 >=11000 and currentCuad.o2 <=15999:
					op2 = get_value_temp(currentCuad.o2)
				elif currentCuad.o2 >= 16000 and currentCuad.o2 <=20999:
					op2 = get_value_cons(currentCuad.o2)
				elif currentCuad.o2 >= 0 and currentCuad.o2 <=9999:
					op2 = get_value_var(currentCuad.o2,"Main")

				result = op1 + op2
				newtempo = Tempo(currentCuad.res,result)
				tabla_tempo.append(newtempo)

			elif currentCuad.op == "-":
				if currentCuad.o1 >=11000 and currentCuad.o1 <=15999:
					op1 = get_value_temp(currentCuad.o1)
				elif currentCuad.o1 >= 16000 and currentCuad.o1 <=20999:
					op1 = get_value_cons(currentCuad.o1)
				elif currentCuad.o1 >= 0 and currentCuad.o1 <=9999:
					op1 = get_value_var(currentCuad.o1,"Main")

				if currentCuad.o2 >=11000 and currentCuad.o2 <=15999:
					op2 = get_value_temp(currentCuad.o2)
				elif currentCuad.o2 >= 16000 and currentCuad.o2 <=20999:
					op2 = get_value_cons(currentCuad.o2)
				elif currentCuad.o2 >= 0 and currentCuad.o2 <=9999:
					op2 = get_value_var(currentCuad.o2,"Main")

				result = op1 - op2
				newtempo = Tempo(currentCuad.res,result)
				tabla_tempo.append(newtempo)

			elif currentCuad.op == "*":
				if currentCuad.o1 >=11000 and currentCuad.o1 <=15999:
					op1 = get_value_temp(currentCuad.o1)
				elif currentCuad.o1 >= 16000 and currentCuad.o1 <=20999:
					op1 = get_value_cons(currentCuad.o1)
				elif currentCuad.o1 >= 0 and currentCuad.o1 <=9999:
					op1 = get_value_var(currentCuad.o1,"Main")

				if currentCuad.o2 >=11000 and currentCuad.o2 <=15999:
					op2 = get_value_temp(currentCuad.o2)
				elif currentCuad.o2 >= 16000 and currentCuad.o2 <=20999:
					op2 = get_value_cons(currentCuad.o2)
				elif currentCuad.o2 >= 0 and currentCuad.o2 <=9999:
					op2 = get_value_var(currentCuad.o2,"Main")

				result = op1 * op2
				newtempo = Tempo(currentCuad.res,result)
				tabla_tempo.append(newtempo)

			elif currentCuad.op == "/":
				if currentCuad.o1 >=11000 and currentCuad.o1 <=15999:
					op1 = get_value_temp(currentCuad.o1)
				elif currentCuad.o1 >= 16000 and currentCuad.o1 <=20999:
					op1 = get_value_cons(currentCuad.o1)
				elif currentCuad.o1 >= 0 and currentCuad.o1 <=9999:
					op1 = get_value_var(currentCuad.o1,"Main")

				if currentCuad.o2 >=11000 and currentCuad.o2 <=15999:
					op2 = get_value_temp(currentCuad.o2)
				elif currentCuad.o2 >= 16000 and currentCuad.o2 <=20999:
					op2 = get_value_cons(currentCuad.o2)
				elif currentCuad.o2 >= 0 and currentCuad.o2 <=9999:
					op2 = get_value_var(currentCuad.o2,"Main")

				result = op1 / op2
				newtempo = Tempo(currentCuad.res,result)
				tabla_tempo.append(newtempo)
	pass

#impresion de los temporales para revisar que existan
def print_temporales(currentProList):
	print "tabla temporales"
	for currentPro in currentProList:
		if currentPro:
			print currentPro.direccion, currentPro.valor
		else:
			print "List is empty"
