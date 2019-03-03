import sys # solo para tener stderr
import random
from typing import re

from slide import *

class slideshow:
	def __init__(self, vector: list = list()):
		self.__m = 0	# para match_barato
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
		return random.sample(self.__v, n)

	def obtenermax(self, ult: int, v: list) -> Slide:
		self.__m, sl = self.match_barato(ult, v)
		return sl


	def ordenarEstadisticamente(self):
		maxi = slideshow()
		el = random.choice(self.__v)
		self.__v.remove(el)
		maxi.__v.append(el)
		for i in range(1, len(self.__v)):
			sys.stderr.write(str(i))
			opciones = self.muestra()
			m = self.obtenermax(i-1, opciones)
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

	#suponemos que entre distintos matches solo cambia el elemento final
	# devuelve el match maximo del conjunto de elementos y el slide con el que se consigue
	def match_barato(self, ultimo: int, elementos: list) -> (int, Slide):
		ma = self.__m
		sl = None
		for el in elementos:
			candidato = self.__m + self.__v[ultimo].min(el)
			if candidato >= ma:
				sl = el
				ma = candidato
		return ma, sl


	# Para calcular la suma de maximos desde 0 hasta el elemento señalado
	def match(self, indice: int, hasta: int):
		suma = 0
		for i in range(0, hasta):
			# La suma es en parejas, es decir: (0,1), (1,2), (2,3), (3,4) ... (hasta-1,hasta)
			suma += self.__v[i].min(self.__v[i+1])
			sys.stderr.write('suma en for = ' + str(suma)+'\n')
		sys.stderr.write('suma = ' + str(suma)+'\n')
		return suma


	def escribir(self):
		#print("Longitud:")
		print(len(self.__v))
		#print("-----")
		for el in self.__v:
			print(str(el))
