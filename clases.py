#----------------------------------------------
# clases.py
# Diversas clases necesarias para el proyecto
# Gerardo Chapa Quiroga 800249
# Tomas Castro Lopez 1033534
# Adolfo Castro Rojas 225591
# CREADO: 13/03/2013
# EDITADO: 14/03/2013
#----------------------------------------------


#Clase de Stack
class Stack(object):
	def __init__(self): 
		# Initialize the stack
		self.stack = [ ] 
	def push(self,object):
		self.stack.append(object) 
	def pop(self):
		return self.stack.pop()
	def neck(self):
		return self.stack[-2]
	def head(self):
		return self.stack[-1]
	def length(self):
		return len(self.stack)
	def show(self):
		for node in self.stack:
			print node

class Memoria(object):
	def __init__(self):
		self.int = [ ]
		self.dbl = [ ]
		self.flt = [ ]
		self.str = [ ]
		self.boo = [ ]

	def siguiente(tipo):
		if tipo == "Integer":
			return self.int
		elif tipo == "Double":
			return self.dbl
		elif tipo == "Float":
			return self.flt
		elif tipo == "String":
			return self.str
		elif tipo == "Boolean":
			return self.boo
