#!/usr/bin/python3
""" class Rectangle that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ class Rectangle that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init method """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter """
        if isinstance(value, int):
            if value < 0 or value == 0:
                raise ValueError("width must be > 0")
            self.__width = value
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """ getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter """
        if isinstance(value, int):
            if value < 0 or value == 0:
                raise ValueError("height must be > 0")
            self.__height = value
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """ getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ setter for x """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """ getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter for y """
        if isinstance(value, int):
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value
        else:
            raise TypeError("y must be an integer")

    def area(self):
        """ return the area value """
        return self.width * self.height

    def display(self):
        """ display in stdout the Rectangle """
        for i in range(self.y):
            print("")
        for j in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def __str__(self):
        """ __str__ method update """
        frmt = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        frmt = frmt.format(self.id, self.x, self.y, self.width, self.height)
        return frmt

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """

        attrbts = ["id", "width", "height", "x", "y"]

        if args is not None:
            for i, value in enumerate(args):
                setattr(self, attrbts[i], value)
        if kwargs is not None:
            for key, value in kwargs.items():
                setattr(self, key, value)
