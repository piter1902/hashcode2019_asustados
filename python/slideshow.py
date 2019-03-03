import sys # solo para tener stderr
import random
from typing import re

from slide import *

class slideshow:
	def __init__(self, vector: list = list()):
		self.__v = vector
		self.__verticales = list()
		if len(vector) > 0:
			self.unirverticales()

	def unirverticales(self):
		for el in self.__v:
			self.__v.remove(el)
			pi = el.pics()
			pi1 = pi.pop()
			if pi1.orientation() == 'V':
				self.__verticales.append(pi1)
		#Juntamos verticales de forma aleatoria
		random.shuffle(self.__verticales)
		for i in range(0, len(self.__verticales)-1):
			self.__v.append(Slide(self.__verticales[i], self.__verticales[i+1]))
			i+=1


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

	def muestra(self, n: int = 30000) -> list:
		li = list()
		i = 0
		while i < n:
			index = random.randint(0, len(self.__v)-1)
			if self.__v[index] not in li:
				li.append(self.__v[index])
				i += 1
		return li

	def obtenermax(self, v: list) -> Slide:
		maximo = 0
		indiceMax = 0
		for i in range(0, len(v)):
			self.__v.append(v[i]) # Para comprobar el maximo
			op = self.match()
			if i == 0:
				indiceMax = 0
				maximo = op
			elif maximo < op:
				indiceMax = i
				maximo = op
			self.__v.remove(v[i])
		return v[indiceMax]


	def ordenarEstadisticamente(self):
		maxi = slideshow()
		el = random.choice(self.__v)
		self.__v.remove(el)
		maxi.__v.append(el)
		for i in range(1, len(self.__v)):
			opciones = self.muestra()
			m = self.obtenermax(opciones)
			maxi.__v.append(m)
			self.__v.remove(m)
		return maxi


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
