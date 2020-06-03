#!/usr/bin/python3
""" class Square inherits from Rectangle """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square inherits from Rectangle """
    def __init__(self, size):
        """ init method """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ return area """
        return super().area()
