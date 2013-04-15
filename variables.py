class Variable():
  dataType = None

	def __init__(self, dataType):
		self.dataType = dataType

class VariableInt(Variable):
	valor = None

	def __init__(self):
		super(VariableInt, self).__init__("Integer")

	def __init__(self, valor):
		super(VariableInt, self).__init__("Integer")
		self.valor = valor

class VariableFloat(Variable):
	valor = None

	def __init__(self):
		super(VariableFloat, self).__init__("Float")

	def __init__(self, valor):
		super(VariableFloat, self).__init__("Float")
		self.valor = valor

class VariableDouble(Variable):
	valor = None

	def __init__(self):
		super(VariableDouble, self).__init__("Double")

	def __init__(self, valor):
		super(VariableDouble, self).__init__("Double")
		self.valor = valor

class VariableStr(Variable):
	valor = None

	def __init__(self):
		super(VariableString, self).__init__("String")

	def __init__(self, valor):
		super(VariableString, self).__init__("String")
		self.valor = valor

class VariableBool(Variable):
	valor = None

	def __init__(self):
		super(VariableBool, self).__init__("Boolean")

	def __init__(self, valor):
		super(VariableBool, self).__init__("Boolean")
		self.valor = valor

class VariableList(Variable):
	valor = None

	def __init__(self):
		super(VariableList, self).__init__("List")

	def __init__(self, valor):
		super(VariableList, self).__init__("List")
		self.valor = valor

class VariableArray(Variable):
	valor = None

	def __init__(self):
		super(VariableArray, self).__init__("Array")

	def __init__(self, valor):
		super(VariableArray, self).__init__("Array")
		self.valor = valor
