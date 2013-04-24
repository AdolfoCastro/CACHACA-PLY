class TConstantes:

  def __init__(self, constante,tipo,dirb):
		self.cons = constante
		self.tipo = tipo
		self.dirb = dirb

tabla_cons = [ ]
def insert_constante(nombre, tipo, dirb):
	global tabla_cons
	cons = TConstantes(nombre, tipo, dirb)
	tabla_cons.append(cons)

def print_constantes(currentProList):
	print "Tabla de constantes"
	for currentPro in currentProList:
		if currentPro:
			print currentPro.cons, currentPro.tipo, currentPro.dirb
		else:
			print "List is empty"

def get_value_cons(dirb):
	global tabla_cons
	for cons in tabla_cons:
		if cons.dirb == dirb:
			return cons.cons

			
