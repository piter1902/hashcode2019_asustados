

class slideshow:
	def __init__(self, vector: list):
		self.__v = vector

	def ordenarMax(self):
		maxi = self
		maximo = self.match()
		for i in range(0, len(self.__v) - 1):
			maxj = i + 1
			for j in range(0, i + 1):
				s = maxi.moverelem(i+1, j)
				k = s.match()
				if k > maximo:
					maxj = j
					maximo = k
			if i+1 != maxj:
				maxi = maxi.moverelem(i+1, maxj)
		return maxi

	def moverelem(self, elem: int, pos: int):
		s = self
		aux = s.__v[elem]
		inf = pos
		sup = elem
		if pos > elem:
			inf = elem
			sup = pos
		for i in range(sup, inf, -1):
			s.__v[i] = s.__v[i-1]
		s.__v[pos] = aux
		return s

	def match(self):
		suma = 0
		for i in range(len(self.__v)-1):
			suma += self.__v[i].min(self.__v[i+1])
		return suma

	def escribir(self):
		#print("Longitud:")
		print(len(self.__v))
		#print("-----")
		for el in self.__v:
			print(str(el))
