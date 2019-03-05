import sys # solo para tener stderr
import random
import numpy as np
import math
from typing import re

from slide import *

PORCENTAJE_BATCH = 1 # proporcion del vector usada en cada batch


# devuelve el indice en <batch> con mayor valor (<maximo>) para <elto>
# de la forma (id, maximo)
def buscarMaxElto(elto: Slide, batch: list) -> (int, int):
    maximo = 0
    id = 0
    for i, element in enumerate(batch):
        valor = element.min(elto)
        if valor > maximo:
            maximo = valor
            # sys.stderr.write('\n-----------\nMAXIMO = ' + str(maximo) + '\n-----------\n')
            id = i
    
    # sys.stderr.write('\n-----------\nMAXIMO = ' + str(maximo) + '\n-----------\n')
                 
    return id, maximo



class slideshow:
    def __init__(self, vector: list = list()):
        self.__m = 0    # para match_barato
        self.__num = len(vector) # nº de slides en vector
        # np.random.shuffle(vector) #lo reordenamos una vez y prau # o 0 veces
        self.__v = []
        self.__v.append(vector.pop(random.randint(0,self.__num))) # empezamos con un elto aleatorio de momento?
        for i in range(self.__num-1):
            self.anyadirDeBatch(vector)

            # if len(self.__v) < 50:

                # sys.stderr.write('----------- ' + str(len(self.__v)) + ' -----------\n')
                # #print("-----")
                # for el in self.__v:
                #     sys.stderr.write(str(el) + '\n')

    def anyadirDeBatch(self, vector: list):
        tamagno = math.ceil(len(vector) * PORCENTAJE_BATCH)
        batch = vector[:tamagno] # los primeros eltos del tamagno que sea
        primeroMayor, i = self.buscarMaxs(batch)        
        if primeroMayor: # ha devuelto true, es el primero
            self.__v.insert(0, vector.pop(i))
        else: # false, pal final
            self.__v.append(vector.pop(i))

    # devuelve (primeroMayor, id), donde id es el indice en batch del elto con mayor valor 
    # con el principio o el final del vector de self. Devuelve true en primeroMayor sii el
    # maximo era el principio de la lista (false si es al final)
    def buscarMaxs(self, batch: list) -> (bool, int):
        primerElto = self.__v[0]
        ultimoElto = self.__v[-1] # ultimo ????? 
        valor1 = valor2 = 0
        id1, valor1 = buscarMaxElto(primerElto, batch)
        id2, valor2 = buscarMaxElto(ultimoElto, batch)
        if valor1 > valor2:
            # sys.stderr.write(
            #     '\n\n\n\n\n\n valor1(' + str(id1) + ', ' + str(valor1) \
            #     + ') > valor2('+ str(id2) + ', ' + str(valor2) + ') \n\n\n\n\n\n\n')
            primeroMayor = True
            id = id1
        else:
            # sys.stderr.write('\n\n\n\n\n\n valor1(' + str(id1) + ', ' + str(valor1) \
            #     + ') <= valor2('+ str(id2) + ', ' + str(valor2) + ') \n\n\n\n\n\n\n')
            primeroMayor = False
            id = id2
        return primeroMayor, id



    # def unirverticales(self):
    #   for el in self.__v:
    #       pi = el.pics()
    #       pi1 = pi.pop()
    #       if pi1.orientation() == 'V':
    #           self.__v.remove(el)
    #           self.__verticales.append(pi1)
    #   #Juntamos verticales de forma aleatoria
    #   #random.shuffle(self.__verticales)
    #   self.maximizar_verticales()
    #   #for i in range(0, len(self.__verticales)-1):
    #   #   self.__v.append(Slide(self.__verticales[i], self.__verticales[i+1]))
    #   #   i+=1

    # def maximizar_verticales(self):
    #   for i in range(0, len(self.__verticales) - 2):
    #       max_el = i + 1
    #       max_intersec = len(self.__verticales[i].tags() & self.__verticales[i+1].tags())
    #       for j in range(i+1, len(self.__verticales) - 1):
    #           cand = len(self.__verticales[i].tags() & self.__verticales[j].tags())
    #           # La interseccion del elemento actual con el j-esimo es mayor que la que teniamos
    #           if cand > max_intersec:
    #               max_intersec = cand
    #               max_el = j
    #       el1 = Slide(self.__verticales[i], self.__verticales[max_el])
    #       self.__v.append(el1)
    #       self.__verticales.remove(self.__verticales[i])
    #       self.__verticales.remove(self.__verticales[max_el])


    # def ordenarMax(self):
    #   maxi = self
    #   maximo = 0
    #   for i in range(0, len(self.__v) - 1):
    #       # print(i)
    #       maximo = maxi.match(i,i+1)
    #       sys.stderr.write('max (' + str(i) + ') = ' + str(maximo)+'\n')
            
    #       maxj = i + 1
    #       for j in range(0, i + 1):
    #           s = maxi.moverelem(i+1, j)
    #           k = s.match(i,i+1)
    #           if k > maximo:
    #               maxj = j
    #               maximo = k
    #       if i+1 != maxj:
    #           maxi = maxi.moverelem(i+1, maxj)
    #   return maxi

    # def muestra(self, n: int = 30000) -> list:
    #   if n > len(self.__v):
    #       n = len(self.__v)//2
    #   return random.sample(self.__v, n)

    # def obtenermax(self, ult: int, v: list) -> Slide:
    #   self.__m, sl = self.match_barato(ult, v)
    #   return sl

    # def ordenarEstadisticamente(self):
    #   maxi = slideshow()
    #   el = random.choice(self.__v)
    #   self.__v.remove(el)
    #   maxi.__v.append(el)
    #   for i in range(1, len(self.__v)-1):
    #       sys.stderr.write(str(i))
    #       opciones = self.muestra()
    #       m = self.obtenermax(i-1, opciones)
    #       maxi.__v.append(m)
    #       self.__v.remove(m)
    #   return maxi


    # def moverelem(self, elem: int, pos: int):
    #   #s = self
    #   #aux = s.__v[elem]
    #   #inf = pos
    #   #sup = elem
    #   #if pos > elem:
    #   #   inf = elem
    #   #   sup = pos
    #   #for i in range(sup, inf, -1):
    #   #   s.__v[i] = s.__v[i-1]
    #   #s.__v[pos] = aux
    #   #return s
    #   s = self
    #   el = s.__v.pop(elem)
    #   s.__v.insert(pos, el)
    #   return s

    # # Para calcular la suma de maximos desde 0 hasta el elemento señalado
    # def match(self, hasta: int):
    #   suma = 0
    #   for i in range(0, hasta):
    #       # La suma es en parejas, es decir: (0,1), (1,2), (2,3), (3,4) ... (hasta-1,hasta)
    #       suma += self.__v[i].min(self.__v[i+1])
    #       sys.stderr.write('suma en for = ' + str(suma)+'\n')
    #   sys.stderr.write('suma = ' + str(suma)+'\n')
    #   return suma

    # #suponemos que entre distintos matches solo cambia el elemento final
    # # devuelve el match maximo del conjunto de elementos y el slide con el que se consigue
    # def match_barato(self, ultimo: int, elementos: list) -> (int, Slide):
    #   ma = self.__m
    #   sl = None
    #   for el in elementos:
    #       candidato = self.__m + self.__v[ultimo].min(el)
    #       if candidato >= ma:
    #           sl = el
    #           ma = candidato
    #   return ma, sl


    # # Para calcular la suma de maximos desde 0 hasta el elemento señalado
    # def match(self, indice: int, hasta: int):
    #   suma = 0
    #   for i in range(0, hasta):
    #       # La suma es en parejas, es decir: (0,1), (1,2), (2,3), (3,4) ... (hasta-1,hasta)
    #       suma += self.__v[i].min(self.__v[i+1])
    #       sys.stderr.write('suma en for = ' + str(suma)+'\n')
    #   sys.stderr.write('suma = ' + str(suma)+'\n')
    #   return suma


    def escribir(self):
      #print("Longitud:")
      print(len(self.__v))
      #print("-----")
      for el in self.__v:
          print(str(el))
