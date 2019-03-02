from pic import Pic


class Slide:
	# def __init__(self, pic: Pic):
	# 	self.__pic1 = pic
	# 	self.__pic2 = None
	# 	self.__tags = self.__pic1.tags()

	def __init__(self, pic1: Pic, pic2: Pic = None):
		self.__pic1 = pic1
		self.__pic2 = pic2
		if (pic2 != None):	
			self.__tags = self.__pic1.tags() | self.__pic2.tags()
		else:
			self.__tags = self.__pic1.tags()

	def tags(self):
		return self.__tags

	def min(self, s):
		a1 = s.tags() & self.tags()
		a2 = s.tags() - self.tags()
		a3 = self.tags() - s.tags()
		return min(len(a1), len(a2), len(a3))

	def __str__(self):
		s = str(self.__pic1.id())
		if self.__pic2 is not None:
			s += " " + str(self.__pic2.id())
		return s
