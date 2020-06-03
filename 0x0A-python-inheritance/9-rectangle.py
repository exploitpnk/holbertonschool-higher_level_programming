#!/usr/bin/python3
""" Class Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class Rectangle """
    def __init__(self, width, height):
        """ init method """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ return area """
        return self.__width * self.__height

    def __str__(self):
        """ __str__ method """
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
