#!/usr/bin/python3
"""
more class base
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square class
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ size init"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Returns the area of a square"""
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
