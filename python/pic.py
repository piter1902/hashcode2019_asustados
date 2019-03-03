

class Pic:
	# def __init__(self, orien: str, id: int, tags: set):
	# 	self.__id = id
	# 	self.__orien = orien
	# 	self._tags = tags
######### este constructor de arriba era como si no estuviera, ##########
######### se redefinía con el de debajo						   ##########
	def __init__(self, id: int, resto: list):
		self.__id = id
		self.__orien = resto[0] #orientacion es el primer elto de la lista
		#resto[1] es el nº de tags que nos da igual
		self.__tags = set(resto[2:]) # Asi se deberia convertir la lista en set

	def tags(self):
		return set(self.__tags)

	def id(self) -> int:
		return self.__id

	def orientation(self) -> str:
		return self.__orien
