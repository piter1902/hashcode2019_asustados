import sys # solo para tener stderr
import random

class slideshow:
	def __init__(self, vector: list):
		self.__v = vector

	def ordenarMax(self):
		maxi = self
		maximo = 0
		for i in range(0, len(self.__v) - 1):
			# print(i)
			maximo = maxi.match(i,i+1)
			sys.stderr.write('max (' + str(i) + ') = ' + str(maximo)+'\n')
			
			maxj = i + 1
			for j in range(0, i + 1):
				s = maxi.moverelem(i+1, j)
				k = s.match(i,i+1)
				if k > maximo:
					maxj = j
					maximo = k
			if i+1 != maxj:
				maxi = maxi.moverelem(i+1, maxj)
		return maxi

	def ordenarEstadisticamente(self):
		maxi = self
		v = self.__v
		for i in range(0, len(self.__v)):
			

	def moverelem(self, elem: int, pos: int):
		#s = self
		#aux = s.__v[elem]
		#inf = pos
		#sup = elem
		#if pos > elem:
		#	inf = elem
		#	sup = pos
		#for i in range(sup, inf, -1):
		#	s.__v[i] = s.__v[i-1]
		#s.__v[pos] = aux
		#return s
		s = self
		el = s.__v.pop(elem)
		s.__v.insert(pos, el)
		return s

	# Para calcular la suma de maximos desde 0 hasta el elemento señalado
	def match(self, hasta: int):
		suma = 0
		for i in range(0, hasta):
			# La suma es en parejas, es decir: (0,1), (1,2), (2,3), (3,4) ... (hasta-1,hasta)
			suma += self.__v[i].min(self.__v[i+1])
			sys.stderr.write('suma en for = ' + str(suma)+'\n')
		sys.stderr.write('suma = ' + str(suma)+'\n')
		return suma

	# Para calcular la suma de maximos desde 0 hasta el elemento señalado
	def match(self, indice: int, hasta: int):
		suma = 0
		for i in range(0, hasta):
			# La suma es en parejas, es decir: (0,1), (1,2), (2,3), (3,4) ... (hasta-1,hasta)
			suma += self.__v[indice].min(self.__v[i+1])
			sys.stderr.write('suma en for = ' + str(suma)+'\n')
		sys.stderr.write('suma = ' + str(suma)+'\n')
		return suma


	def escribir(self):
		#print("Longitud:")
		print(len(self.__v))
		#print("-----")
		for el in self.__v:
			print(str(el))
