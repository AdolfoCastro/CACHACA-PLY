#globales
contEntGlo = 0
contFlotGlo = 1000
coutDoubleGlo = 4000
contStrGlo = 2000
contBoolGlo = 3000
#contSaltosGlo=4000

#locales
contEntLoc=5000
contFlotLoc=6000
contDoubleLoc=7000
contStrLoc=8000
contBoolLoc=9000
#contSaltosLoc=9000

#Temporales
contEntTmp=11000
contFlotTmp=12000
contDoubleTmp=13000 
contStrTmp=14000
contBoolTmp=15000
#contSaltosTmp=14000

#Constates
contEntCons=16000
contFlotCons=17000
contDoubleCons=18000 
contStrCons=19000
contBoolCons=20000
#contSaltosCons=19000

class Memoria(object):
  def __init__(self):
		self.globales = Memoria_sub()
		self.locales = Memoria_sub()
		self.temporales = Memoria_sub()
		self.constantes = Memoria_sub()
		
class Memoria_sub(object):
	def __init__(self):
		self.int = [ ]
		self.dbl = [ ]
		self.flt = [ ]
		self.str = [ ]
		self.boo = [ ]

	def new_int(self, celda):
		self.int.append(celda)

	def new_dbl(self, celda):
		self.dbl.append(celda)

	def new_flt(self, celda):
		self.flt.append(celda)

	def new_str(self, celda):
		self.str.append(celda)

	def new_boo(self, celda):
		self.boo.append(celda)

class Memoria_celda(object):
	def __init__(self, _dir, value):
		if _dir>=0:
			self.direccion = _dir
			self.valor = value
		else:
			print "Error - direccion de memoria inexistente"
			sys.exit()
