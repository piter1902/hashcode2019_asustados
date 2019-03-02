

class Pic:
	def __init__(self, orien: str, id: int, tags: set):
		self.__id = id
		self.__orien = orien
		self._tags = tags

	def __init__(id: int, resto: list):
		self.__id = id
		self.__orien = resto[0] #orientacion es el primer elto de la lista
		#resto[1] es el nº de tags que nos da igual
		self.__tags = set(resto[2:]) 

	def tags(self):
		return set(self.__tags)

	def id(self) -> int:
		return self.__id
