#!/usr/bin/python3
"""defines a square"""


class Square:
    """"""
    def __init__(self, size=0):
        """initializes a claass
        size: size of square
        if size is not int raises typeerror
        if size < 0 raises valu error
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
