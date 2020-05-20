#!/usr/bin/python3
""" Class Square that defines a square """


class Square:
    """ Class Square """
    def __init__(self, size=0):
        """ __init__ method """
        self.__size = size
        try:
            int(self.__size)
            if self.__size >= 0:
                pass
            else:
                raise ValueError("size must be >= 0")
        except TypeError:
            print("size must be an integer")
