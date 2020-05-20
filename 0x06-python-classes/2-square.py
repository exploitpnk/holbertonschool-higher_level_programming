#!/usr/bin/python3

class Square:
	def __init__(self, size=0):
		self.__size = size
		try:
			int(self.__size)
			if self.__size >= 0:
				pass
			else:
				raise ValueError("size must be >= 0") 
		except TypeError:
			print("size must be an integer")
