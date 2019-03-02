

class Pic:
	def __init__(self, orien: str, id: int, tags: set):
		self.__id = id
		self.__orien = orien
		self._tags = tags

	def tags(self):
		return set(self.__tags)

	def id(self) -> int:
		return self.__id
