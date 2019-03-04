from pic import Pic

import sys


class Slide:
	# def __init__(self, pic: Pic):
	# 	self.__pic1 = pic
	# 	self.__pic2 = None
	# 	self.__tags = self.__pic1.tags()

	def __init__(self, pic1: Pic, pic2: Pic = None):
		self.__pic1 = pic1
		self.__pic2 = pic2
		if pic2 is not None:	
			self.__tags = self.__pic1.tags() | self.__pic2.tags()
		else:
			self.__tags = self.__pic1.tags()

	def tags(self):
		return self.__tags

	def min(self, s):
		a1 = s.tags() & self.tags()
		# sys.stderr.write('a1 = ' + str(len(a1))+'\n')
		a2 = s.tags() - self.tags()
		# sys.stderr.write('a2 = ' + str((len(a2)))+'\n')
		a3 = self.tags() - s.tags()
		# sys.stderr.write('a3 = ' + str((len(a3)))+'\n')
		return min(len(a1), len(a2), len(a3))

	def __str__(self):
		s = str(self.__pic1.id())
		if self.__pic2 is not None:
			s += " " + str(self.__pic2.id())
		return s

	def pics(self) -> list:
		li = list()
		li.append(self.__pic1)
		if self.__pic2 is not None:
			li.append(self.__pic2)
		return li
